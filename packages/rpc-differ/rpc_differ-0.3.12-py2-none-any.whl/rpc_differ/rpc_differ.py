#!/usr/bin/env python
# Copyright 2016, Major Hayden
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Analyzes the differences between two OpenStack-Ansible commits."""
import argparse
import json
import logging
import os
import re
import sys


from git import Repo

import jinja2

from osa_differ import exceptions, osa_differ

import requests

import yaml


# Configure logging
log = logging.getLogger()
log.setLevel(logging.ERROR)
stdout_handler = logging.StreamHandler(sys.stdout)
log.addHandler(stdout_handler)

# Additional constants
ROLE_REQ_FILE = 'ansible-role-requirements.yml'


class SHANotFound(Exception):
    """Exception handler for situations where the specified SHA is missing."""

    pass


def create_parser():
    """Setup argument Parsing."""
    description = """RPC Release Diff Generator
--------------------------

Finds changes in OpenStack-Ansible, OpenStack-Ansible roles, and OpenStack
projects between two RPC-OpenStack revisions.

"""

    parser = argparse.ArgumentParser(
        usage='%(prog)s',
        description=description,
        epilog='Licensed "Apache 2.0"',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'old_commit',
        action='store',
        nargs=1,
        help="Git SHA of the older commit",
    )
    parser.add_argument(
        'new_commit',
        action='store',
        nargs=1,
        help="Git SHA of the newer commit",
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        default=False,
        help="Enable debug output",
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        default=False,
        help="Enable verbose output",
    )
    parser.add_argument(
        '-d', '--directory',
        action='store',
        default="~/.osa-differ",
        help="Git repo storage directory (default: ~/.osa-differ)",
    )
    parser.add_argument(
        '-rroc', '--role-requirements-old-commit',
        action='store',
        default=None,
        help=(
            "Name of the Ansible role requirements file to read from the old "
            "commit, defaults to value of `--role-requirements`."
        ),
    )
    parser.add_argument(
        '-rr', '--role-requirements',
        action='store',
        default=ROLE_REQ_FILE,
        help="Name of the ansible role requirements file to read",
    )
    parser.add_argument(
        '-r', '--rpc-repo-url',
        action='store',
        default="https://github.com/rcbops/rpc-openstack",
        help="Github repository for the rpc-openstack project"
    )
    parser.add_argument(
        '--osa-repo-url',
        action='store',
        default="https://git.openstack.org/openstack/openstack-ansible",
        help="URL of the openstack-ansible git repo"
    )
    parser.add_argument(
        '-rpoc', '--rpc-product-old-commit',
        action='store',
        default=None,
        help=(
            "Set the RPC product version for the old commit, defaults to "
            "value of `--rpc-product`."
        )
    )
    parser.add_argument(
        '-rp', '--rpc-product',
        action='store',
        default="master",
        help="Set the RPC product version"
    )
    parser.add_argument(
        '-u', '--update',
        action='store_true',
        default=False,
        help="Fetch latest changes to repo",
    )
    parser.add_argument(
        '--version-mappings',
        action=osa_differ.VersionMappingsAction,
        help=(
            "Map dependency versions in cases where the old version no longer "
            "exists. The argument should be of the form "
            "'repo-name;old-version1:new-version1;old-version2:new-version2'."
        ),
    )

    display_opts = parser.add_argument_group("Limit scope")
    display_opts.add_argument(
        "--skip-projects",
        action="store_true",
        help="Skip checking for changes in OpenStack projects"
    )
    display_opts.add_argument(
        "--skip-roles",
        action="store_true",
        help="Skip checking for changes in OpenStack-Ansible roles"
    )
    output_desc = ("Output is printed to stdout by default.")
    output_opts = parser.add_argument_group('Output options', output_desc)
    output_opts.add_argument(
        '--quiet',
        action='store_true',
        default=False,
        help="Do not output to stdout",
    )
    output_opts.add_argument(
        '--gist',
        action='store_true',
        default=False,
        help="Output into a GitHub Gist",
    )
    output_opts.add_argument(
        '--file',
        metavar="FILENAME",
        action='store',
        help="Output to a file",
    )
    return parser


def get_osa_commit(repo, ref, rpc_product=None):
    """Get the OSA sha referenced by an RPCO Repo."""
    osa_differ.checkout(repo, ref)

    functions_path = os.path.join(repo.working_tree_dir,
                                  'scripts/functions.sh')
    release_path = os.path.join(repo.working_tree_dir,
                                'playbooks/vars/rpc-release.yml')

    if os.path.exists(release_path):
        with open(release_path) as f:
            rpc_release_data = yaml.safe_load(f.read())

        rpc_product_releases = rpc_release_data['rpc_product_releases']
        release_data = rpc_product_releases[rpc_product]

        return release_data['osa_release']

    elif repo.submodules['openstack-ansible']:
        return repo.submodules['openstack-ansible'].hexsha

    elif os.path.exists(functions_path):
        # This branch doesn't use a submodule for OSA
        # Pull the SHA out of functions.sh
        quoted_re = re.compile('OSA_RELEASE:-?"?([^"}]+)["}]')
        with open(functions_path, "r") as funcs:
            for line in funcs.readlines():
                match = quoted_re.search(line)
                if match:
                    return match.groups()[0]
            else:
                raise SHANotFound(
                    ("Cannot find OSA SHA in submodule or "
                     "script: {}".format(functions_path)))

    else:
        raise SHANotFound('No OSA SHA was able to be derived.')


def validate_rpc_sha(repo_dir, commit):
    """Validate/update a SHA given for the rpc-openstack repo."""

    # Is the commit valid? Just in case the commit is a
    # PR ref, we try both the ref given and the ref prepended
    # with the remote 'origin'.
    try:
        osa_differ.validate_commits(repo_dir, [commit])
    except exceptions.InvalidCommitException:
        log.debug("The reference {c} cannot be found. Prepending "
                  "origin remote and retrying.".format(c=commit))
        commit = 'origin/' + commit
        osa_differ.validate_commits(repo_dir, [commit])

    return commit


def make_rpc_report(repo_dir, old_commit, new_commit,
                    args):
    """Create initial RST report header for OpenStack-Ansible."""

    # Do we have a valid commit range?
    # NOTE:
    # An exception is thrown by osa_differ if these two commits
    # are the the same, but it is sometimes necessary to compare
    # two RPC tags that have the same OSA SHA. For example,
    # comparing two tags that only have differences between the
    # two RPCO commit, but no differences between the OSA SHAs
    # that correspond to those two commits.
    # To handle this case, the exception will be caught and flow
    # of execution will continue normally.
    try:
        osa_differ.validate_commit_range(repo_dir, old_commit, new_commit)
    except exceptions.InvalidCommitRangeException:
        pass

    # Get the commits in the range
    commits = osa_differ.get_commits(repo_dir, old_commit, new_commit)

    # Start off our report with a header and our OpenStack-Ansible commits.
    template_vars = {
        'args': args,
        'repo': 'rpc-openstack',
        'commits': commits,
        'commit_base_url': osa_differ.get_commit_url(args.rpc_repo_url),
        'old_sha': old_commit,
        'new_sha': new_commit
    }
    return render_template('offline-header.j2', template_vars)


def parse_arguments():
    """Parse arguments."""
    parser = create_parser()
    args = parser.parse_args()
    if not args.role_requirements_old_commit:
        args.role_requirements_old_commit = args.role_requirements
    if not args.rpc_product_old_commit:
        args.rpc_product_old_commit = args.rpc_product
    return args


def post_gist(report_data, old_sha, new_sha):
    """Post the report to a GitHub Gist and return the URL of the gist."""
    payload = {
        "description": ("Changes in RPC-OpenStack between "
                        "{0} and {1}".format(old_sha, new_sha)),
        "public": True,
        "files": {
            "rpc-diff-{0}-{1}.rst".format(old_sha, new_sha): {
                "content": report_data
            }
        }
    }
    url = "https://api.github.com/gists"
    r = requests.post(url, data=json.dumps(payload))
    response = r.json()
    return response['html_url']


def publish_report(report, args, old_commit, new_commit):
    """Publish the RST report based on the user request."""
    # Print the report to stdout unless the user specified --quiet.
    output = ""

    if not args.quiet and not args.gist and not args.file:
        return report

    if args.gist:
        gist_url = post_gist(report, old_commit, new_commit)
        output += "\nReport posted to GitHub Gist: {0}".format(gist_url)

    if args.file is not None:
        with open(args.file, 'w') as f:
            f.write(report.encode('utf-8'))
        output += "\nReport written to file: {0}".format(args.file)

    return output


def render_template(template_file, template_vars):
    """Render a jinja template."""
    # Load our Jinja templates
    template_dir = "{0}/templates".format(
        os.path.dirname(os.path.abspath(__file__))
    )
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dir),
        trim_blocks=True
    )
    rendered = jinja_env.get_template(template_file).render(template_vars)

    return rendered


def run_rpc_differ():
    """The script starts here."""
    args = parse_arguments()

    # Set up DEBUG logging if needed
    if args.debug:
        log.setLevel(logging.DEBUG)
    elif args.verbose:
        log.setLevel(logging.INFO)

    # Create the storage directory if it doesn't exist already.
    try:
        storage_directory = osa_differ.prepare_storage_dir(args.directory)
    except OSError:
        print("ERROR: Couldn't create the storage directory {0}. "
              "Please create it manually.".format(args.directory))
        sys.exit(1)

    # Prepare the rpc-openstack repository.
    rpc_repo_url = args.rpc_repo_url
    rpc_repo_dir = "{0}/rpc-openstack".format(storage_directory)
    osa_differ.update_repo(rpc_repo_dir, rpc_repo_url, args.update)

    # Validate/update the commits.
    rpc_old_commit = validate_rpc_sha(rpc_repo_dir, args.old_commit[0])
    rpc_new_commit = validate_rpc_sha(rpc_repo_dir, args.new_commit[0])

    # Generate RPC report header.
    report_rst = make_rpc_report(rpc_repo_dir,
                                 rpc_old_commit,
                                 rpc_new_commit,
                                 args)

    # Get the list of RPC roles from the newer and older commits.
    try:
        role_yaml = osa_differ.get_roles(
            rpc_repo_dir,
            rpc_old_commit,
            args.role_requirements_old_commit
        )
    except IOError:
        role_yaml = osa_differ.get_roles(
            rpc_repo_dir,
            rpc_old_commit,
            ROLE_REQ_FILE
        )

    try:
        role_yaml_latest = osa_differ.get_roles(
            rpc_repo_dir,
            rpc_new_commit,
            args.role_requirements
        )
    except IOError:
        role_yaml_latest = osa_differ.get_roles(
            rpc_repo_dir,
            rpc_new_commit,
            ROLE_REQ_FILE
        )

    # Generate the role report.
    report_rst += ("\nRPC-OpenStack Roles\n"
                   "-------------------")
    report_rst += osa_differ.make_report(storage_directory,
                                         role_yaml,
                                         role_yaml_latest,
                                         args.update,
                                         args.version_mappings)

    report_rst += "\n"

    # Generate OpenStack-Ansible report.
    repo = Repo(rpc_repo_dir)
    osa_old_commit = get_osa_commit(repo,
                                    rpc_old_commit,
                                    rpc_product=args.rpc_product_old_commit)
    osa_new_commit = get_osa_commit(repo,
                                    rpc_new_commit,
                                    rpc_product=args.rpc_product)
    log.debug("OSA Commits old:{old} new:{new}".format(old=osa_old_commit,
                                                       new=osa_new_commit))

    osa_repo_dir = "{0}/openstack-ansible".format(storage_directory)
    # NOTE:
    # An exception is thrown by osa_differ if these two commits
    # are the the same, but it is sometimes necessary to compare
    # two RPC tags that have the same OSA SHA. For example,
    # comparing two tags that only have differences between the
    # two RPCO commit, but no differences between the OSA SHAs
    # that correspond to those two commits.
    # To handle this case, the exception will be caught and flow
    # of execution will continue normally.
    try:
        report_rst += osa_differ.make_osa_report(osa_repo_dir,
                                                 osa_old_commit,
                                                 osa_new_commit,
                                                 args)
    except exceptions.InvalidCommitRangeException:
        pass

    # Get the list of OpenStack-Ansible roles from the newer and older commits.
    try:
        role_yaml = osa_differ.get_roles(osa_repo_dir,
                                         osa_old_commit,
                                         args.role_requirements_old_commit)
    except IOError:
        role_yaml = osa_differ.get_roles(osa_repo_dir,
                                         osa_old_commit,
                                         ROLE_REQ_FILE)
    try:
        role_yaml_latest = osa_differ.get_roles(osa_repo_dir,
                                                osa_new_commit,
                                                args.role_requirements)
    except IOError:
        role_yaml_latest = osa_differ.get_roles(osa_repo_dir,
                                                osa_new_commit,
                                                ROLE_REQ_FILE)

    # Generate the role report.
    report_rst += ("\nOpenStack-Ansible Roles\n"
                   "-----------------------")
    report_rst += osa_differ.make_report(storage_directory,
                                         role_yaml,
                                         role_yaml_latest,
                                         args.update,
                                         args.version_mappings)

    project_yaml = osa_differ.get_projects(osa_repo_dir,
                                           osa_old_commit)
    project_yaml_latest = osa_differ.get_projects(osa_repo_dir,
                                                  osa_new_commit)

    # Generate the project report.
    report_rst += ("OpenStack-Ansible Projects\n"
                   "--------------------------")
    report_rst += osa_differ.make_report(storage_directory,
                                         project_yaml,
                                         project_yaml_latest,
                                         args.update,
                                         args.version_mappings)

    # Publish report according to the user's request.
    output = publish_report(report_rst,
                            args,
                            rpc_old_commit,
                            rpc_new_commit)
    print(output)

if __name__ == "__main__":
    run_rpc_differ()
