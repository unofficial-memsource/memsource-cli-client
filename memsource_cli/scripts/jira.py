
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import requests
import argparse
from requests_kerberos import HTTPKerberosAuth
import sys
import json


def parse_args():
    parser = argparse.ArgumentParser(prefix_chars='--',
                                     description="Create task in JIRA via REST API")
    parser.add_argument("--jira-url",
                        dest='jira_url',
                        help="JIRA REST API URL")
    parser.add_argument("--auth-url",
                        dest='auth_url',
                        required=True,
                        help="JIRA REST API AUTH URL")
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
        self.kerberos_auth = HTTPKerberosAuth(
            force_preemptive=True, mutual_authentication=False)


if __name__ == '__main__':
    jira = Jira()

    _components = []
    for i in jira.args.components:
        _components.append({'name': i})

    _fixversions = []
    for i in jira.args.fix_versions:
        _fixversions.append({'name': i})

    _versions = []
    for i in jira.args.affects_versions:
        _versions.append({'name': i})

    s = requests.Session()
    response = s.get(
        jira.args.auth_url, auth=jira.kerberos_auth, verify=False)
    cookies = response.cookies
    response = s.post(
        jira.args.jira_url + '/rest/api/2/issue', cookies=cookies, verify=False,
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
    response = s.put(
        jira.args.jira_url + '/rest/api/2/issue/' + issue, cookies=cookies, verify=False,
        json={
            "fields": {
                "fixVersions": _fixversions,
                "versions": _versions,
            }},
        headers={
            "Content-Type": "application/json"
        })
    response = s.post(
        jira.args.jira_url + '/rest/agile/1.0/epic/' +
        jira.args.epic + '/issue', cookies=cookies, verify=False,
        json={
            "issues": [
                issue
            ]
        },
        headers={
            "Content-Type": "application/json"
        })
    response = s.post(
        jira.args.jira_url + '/rest/agile/1.0/sprint/' +
        jira.args.sprint + '/issue', cookies=cookies, verify=False,
        json={
            "issues": [
                issue
            ]
        },
        headers={
            "Content-Type": "application/json"
        })
