#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

from cliff.lister import Lister

import memsource_cli
import json


class ListAnalysisByProject(Lister):
    """
    List analyses by project
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(ListAnalysisByProject, self).get_parser(prog_name)
        parser.add_argument(
            '--project-id',
            action='store',
            dest='project_uid',
            help='project_uid'
        )
        parser.add_argument(
            '--page-size',
            action='store',
            default=50,
            help='page_size'
        )
        parser.add_argument(
            '--page-number',
            action='store',
            default=0,
            help='page_number'
        )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.AnalysisApi(self.app.client)

        response = api.list_by_project_v2(token=self.app.client.configuration.token,
                                          project_uid=parsed_args.project_uid,
                                          page_size=parsed_args.page_size,
                                          page_number=parsed_args.page_number)

        response = response.to_dict()
        return(('id',
                'name',
                'jobs',
                'provider',
                'type',
                'date_created',
                'source_lang',
                'target_lang'
                ), (
            (response['content'][i]['id'],
             response['content'][i]['name'],
             json.dumps(response['content'][i]['analyse_language_parts']
                        [j]['jobs']),
             response['content'][i]['provider'],
             response['content'][i]['type'],
             json.dumps(response['content'][i]['date_created'],
                        default=str).replace('"', ''),
             response['content'][i]['analyse_language_parts']
             [j]['source_lang'],
             response['content'][i]['analyse_language_parts']
             [j]['target_lang']
             )
            for i in range(0, len(response['content']))
            for j in range(0, len(response['content'][i]
                                  ['analyse_language_parts'])))
        )


class ShowAnalysis(Lister):
    """
    Get Analysis
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(ShowAnalysis, self).get_parser(prog_name)
        parser.add_argument(
            '--analyse-id',
            action='store',
            dest='analyse_id',
            help='analyse_id'
        )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.AnalysisApi(self.app.client)
        response = api.get_analyse_v2(token=self.app.client.configuration.token,
                                      analyse_id=parsed_args.analyse_id)
        column_headers = ['jobs', 'netrate', 'all', 'source_lang',
                          'target_lang']
        data = []
        output = response.to_dict()
        content = output['analyse_language_parts']

        for j in range(0, len(content)):
            if content[j]['discounted_data'] is not None:
                discounted_data = content[j]['discounted_data']['all']['words']
            else:
                discounted_data = None
            data += [(json.dumps(content[j]['jobs']),
                      discounted_data,
                      content[j]['data']['all']['words'],
                      content[j]['source_lang'],
                      content[j]['target_lang'])]

        return((column_headers), (data))
