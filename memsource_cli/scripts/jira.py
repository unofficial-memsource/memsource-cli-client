
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import requests
import argparse
import sys
import json
import os


def env(*vars, **kwargs):
    """Search for the first defined of possibly many env vars
    Returns the first environment variable defined in vars, or
    returns the default defined in kwargs.
    """
    for v in vars:
        value = os.environ.get(v, None)
        if value:
            return value
    return kwargs.get('default', '')


def parse_args():
    parser = argparse.ArgumentParser(prefix_chars='--',
                                     description="Create task in JIRA via REST API")
    parser.add_argument("--jira-url",
                        dest='jira_url',
                        help="JIRA REST API URL",
                        required=True)
    parser.add_argument("--auth-url",
                        dest='auth_url',
                        help="JIRA REST API Kerberos URL")
    parser.add_argument("--basic",
                        dest='basic',
                        action='store_true',
                        help="JIRA basic authentication")
    parser.add_argument("--no-ssl",
                        dest='ssl',
                        action='store_false',
                        help="JIRA turn off SSL verification")
    parser.add_argument("--user-name",
                        dest='username',
                        default=env('JIRA_USERNAME'),
                        help="JIRA username")
    parser.add_argument("--password",
                        dest='password',
                        default=env('JIRA_PASSWORD'),
                        help="JIRA password")
    parser.add_argument("--project",
                        dest='project',
                        required=True,
                        help="JIRA project ID")
    parser.add_argument("--summary",
                        dest='summary',
                        required=True,
                        help="JIRA summary")
    parser.add_argument("--description",
                        dest='description',
                        required=True,
                        help="JIRA description")
    parser.add_argument("--issue-type",
                        dest='issue_type',
                        required=True,
                        help="JIRA issue type")
    parser.add_argument("--labels",
                        help='JIRA labels',
                        nargs='+',
                        default=[])
    parser.add_argument("--components",
                        nargs='+',
                        default=[],
                        help="JIRA components")
    parser.add_argument("--fix-versions",
                        nargs='+',
                        default=[],
                        help="JIRA Fix version/s")
    parser.add_argument("--epic",
                        dest='epic',
                        help="JIRA epic")
    parser.add_argument("--sprint",
                        dest='sprint',
                        help="JIRA Sprint ID")
    parser.add_argument("--affects-versions",
                        nargs='+',
                        default=[],
                        help="JIRA Affects version/s")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


class Jira:
    def __init__(self):
        self.args = parse_args()


if __name__ == '__main__':
    jira = Jira()

    s = requests.Session()

    if jira.args.auth_url:
        print('Using GSSAPI Authentication')
        from requests_kerberos import HTTPKerberosAuth
        kerberos_auth = HTTPKerberosAuth(
            force_preemptive=True, mutual_authentication=False)
        response = s.get(
            jira.args.auth_url, auth=kerberos_auth, verify=jira.args.ssl)

    elif jira.args.basic and not jira.args.username and not jira.args.password:
        print('Using Basic Authentication')
        print('With \'--basic\'. You must specify \'--user-name\' and \'---password\'.')
        sys.exit(1)

    elif jira.args.basic and jira.args.username and jira.args.password:
        print('Using Basic Authentication')
        basic_auth = requests.auth.HTTPBasicAuth(
            jira.args.username, jira.args.password)
        response = s.get(
            jira.args.jira_url, auth=basic_auth, verify=jira.args.ssl)

    cookies = response.cookies

    _components = []
    for i in jira.args.components:
        _components.append({'name': i})

    response = s.post(
        jira.args.jira_url + '/rest/api/2/issue', cookies=cookies, verify=jira.args.ssl,
        json={
            "fields": {
                "project":
                {
                    "key": jira.args.project
                },
                "summary": jira.args.summary,
                "description": jira.args.description,
                "labels": jira.args.labels,
                "components": _components,
                "issuetype": {
                    "name": jira.args.issue_type
                }
            }},
        headers={
            "Content-Type": "application/json"
        })

    issue = json.loads(response.content).get("key")
    print(jira.args.jira_url + '/browse/' + issue)

    if jira.args.fix_versions and jira.args.affects_versions:

        _fixversions = []
        for i in jira.args.fix_versions:
            _fixversions.append({'name': i})

        _versions = []
        for i in jira.args.affects_versions:
            _versions.append({'name': i})

        response = s.put(
            jira.args.jira_url + '/rest/api/2/issue/' + issue, cookies=cookies,
            verify=jira.args.ssl,
            json={
                "fields": {
                    "fixVersions": _fixversions,
                    "versions": _versions,
                }},
            headers={
                "Content-Type": "application/json"
            })

    if jira.args.epic:
        response = s.post(
            jira.args.jira_url + '/rest/agile/1.0/epic/' +
            jira.args.epic + '/issue', cookies=cookies, verify=jira.args.ssl,
            json={
                "issues": [
                    issue
                ]
            },
            headers={
                "Content-Type": "application/json"
            })
    if jira.args.sprint:
        response = s.post(
            jira.args.jira_url + '/rest/agile/1.0/sprint/' +
            jira.args.sprint + '/issue', cookies=cookies, verify=jira.args.ssl,
            json={
                "issues": [
                    issue
                ]
            },
            headers={
                "Content-Type": "application/json"
            })
