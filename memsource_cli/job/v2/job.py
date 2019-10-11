#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

from cliff.lister import Lister

import json
import memsource_cli


class ListJobs(Lister):
    """
    List jobs in project
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(ListJobs, self).get_parser(prog_name)

        all_params = {
            'project_id': 'project_uid',
            'filename': 'filename',
            'target_lang': 'target_lang',
        }
        all_params_int = {
            'page_number': 'page_number',
            'page_size': 'page_size',
            'assigned_user': 'assigned_user',
            'assigned_vendor': 'assigned_vendor',
            'due_in_hours': 'due_in_hours',
            'workflow_level': 'workflow_level'
        }
        all_params_list = {
            'status': 'status',
        }

        for k, v in all_params.items():
            parser.add_argument(
                '--' + k.replace('_', '-'),
                help=v,
                dest=v
            )
        for k, v in all_params_list.items():
            parser.add_argument(
                '--' + k.replace('_', '-'),
                help=v,
                dest=v,
                nargs='+',
                default=[]
            )
        for k, v in all_params_int.items():
            parser.add_argument(
                '--' + k.replace('_', '-'),
                help=v,
                dest=v,
                type=int
            )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.JobApi(self.app.client)
        query_params = vars(parsed_args)
        args = {}
        all_params = ['project_uid', 'page_number', 'page_size',
                      'count', 'workflow_level', 'status', 'assigned_user',
                      'due_in_hours', 'filename', 'target_lang', 'assigned_vendor']  # noqa: E501

        for k, v in query_params.items():
            if k in all_params and v is not None:
                args[k] = v

        response = api.list_parts_v2(token=self.app.client.configuration.token,
                                     **args)

        column_headers = ['uid', 'status', 'providers',
                          'target_lang', 'workflow_step', 'filename',
                          'date_due', 'date_created', 'imported', 'continuous']

        data = []

        output = response.to_dict()
        content = output['content']

        for i in range(0, len(content)):
            for j in column_headers:
                if isinstance(content[i][j], dict):
                    content[i][j] = json.dumps(content[i][j])
            data += [(content[i]['uid'],
                      content[i]['status'],
                      content[i]['providers'],
                      content[i]['target_lang'],
                      content[i]['workflow_step'],
                      content[i]['filename'],
                      json.dumps(content[i]['date_due'],
                                 default=str).replace('"', ''),
                      json.dumps(content[i]['date_created'],
                                 default=str).replace('"', ''),
                      content[i]['imported'],
                      content[i]['continuous'])]

        return((column_headers), (data))
