#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

from cliff.show import ShowOne
from cliff import command
from cliff.lister import Lister

import json
import datetime
import memsource_cli


class CreateAnalysis(ShowOne):
    """
    Create analysis
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(CreateAnalysis, self).get_parser(prog_name)

        all_params = {
            'type': 'type',
            'name': 'name',
            'net_rate_scheme': 'netRateScheme',
            'callback_url': 'callbackUrl',
            'linguist': 'IdReference'
        }
        all_params_bool = {
            'include_fuzzy_repetitions': 'includeFuzzyRepetitions',
            'include_confirmed_segments': 'includeConfirmedSegments',
            'include_numbers': 'includeNumbers',
            'include_locked_segments': 'includeLockedSegments',
            'count_source_units': 'countSourceUnits',
            'include_trans_memory': 'includeTransMemory',
            'include_non_translatables': 'includeNonTranslatables',
            'include_machine_translation_matches': 'includeMachineTranslationMatches',  # noqa E501
            'trans_memory_post_editing': 'transMemoryPostEditing',
            'non_translatable_post_editing': 'nonTranslatablePostEditing',
            'machine_translate_post_editing': 'machineTranslatePostEditing',
            'use_project_analysis_settings': 'useProjectAnalysisSettings',
        }
        all_params_int = {
            'compare_workflow_level': 'compareWorkflowLevel',
        }
        all_params_list = {
            'jobs': 'jobs',
        }
        for k, v in all_params_bool.items():
            parser.add_argument(
                '--' + k.replace('_', '-'),
                help=v,
                dest=v,
                default=False,
                action="store_true"
            )
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
        api = memsource_cli.AnalysisApi(self.app.client)
        args = {}

        for k, v in vars(parsed_args).items():
            if v is not None:
                args[k] = v

        _job_ids = []
        for i in parsed_args.jobs:
            _job_ids.append({'uid': i})
        args['jobs'] = _job_ids

        response = api.create_analyse_async(
            token=self.app.client.configuration.token,
            body=args)

        column_headers = ['analyse', 'id', 'created_by', 'date_created',
                          'action', 'async_response', 'parent', 'project']
        data = []

        output = response.to_dict()
        data += [(json.dumps(output['analyse']))]

        content = output['async_request']
        for k, v in content.items():
            if isinstance(v, datetime.datetime):
                v = json.dumps(v, default=str).replace('"', '')
            if isinstance(v, dict):
                v = json.dumps(v)
            data += [(v)]

        return((column_headers), (data))


class CreateAnalysisByLanguages(Lister):
    """
    Create analyses by languages
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(CreateAnalysisByLanguages, self).get_parser(prog_name)

        all_params = {
            'type': 'type',
            'name': 'name',
            'net_rate_scheme': 'netRateScheme',
            'callback_url': 'callbackUrl',
            'linguist': 'IdReference'
        }
        all_params_bool = {
            'include_fuzzy_repetitions': 'includeFuzzyRepetitions',
            'include_confirmed_segments': 'includeConfirmedSegments',
            'include_numbers': 'includeNumbers',
            'include_locked_segments': 'includeLockedSegments',
            'count_source_units': 'countSourceUnits',
            'include_trans_memory': 'includeTransMemory',
            'include_non_translatables': 'includeNonTranslatables',
            'include_machine_translation_matches': 'includeMachineTranslationMatches',  # noqa E501
            'trans_memory_post_editing': 'transMemoryPostEditing',
            'non_translatable_post_editing': 'nonTranslatablePostEditing',
            'machine_translate_post_editing': 'machineTranslatePostEditing',
            'use_project_analysis_settings': 'useProjectAnalysisSettings',
        }
        all_params_int = {
            'compare_workflow_level': 'compareWorkflowLevel',
        }
        all_params_list = {
            'jobs': 'jobs',
        }
        for k, v in all_params_bool.items():
            parser.add_argument(
                '--' + k.replace('_', '-'),
                help=v,
                dest=v,
                default=False,
                action="store_true"
            )
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
        api = memsource_cli.AnalysisApi(self.app.client)
        args = {}

        for k, v in vars(parsed_args).items():
            if v is not None:
                args[k] = v

        _job_ids = []
        for i in parsed_args.jobs:
            _job_ids.append({'uid': i})
        args['jobs'] = _job_ids

        response = api.create_analyses_for_langs(
            token=self.app.client.configuration.token,
            body=args)

        output = response.to_dict()

        return(('id',
                'analyse_id',
                'action',
                'date_created',
                'project_uid',
                'project_name',
                'created_by'
                ), (
            (output['analyses'][i]['async_request']['id'],
             output['analyses'][i]['analyse']['id'],
             output['analyses'][i]['async_request']['action'],
             json.dumps(output['analyses'][i]['async_request']
                        ['date_created'], default=str).replace('"', ''),
             output['analyses'][i]['async_request']['project']['uid'],
             output['analyses'][i]['async_request']['project']['name'],
             json.dumps(output['analyses'][i]['async_request']['created_by']))
            for i in range(0, len(output['analyses']))
        ))


class DeleteAnalysis(command.Command):
    """
    Delete analysis
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(DeleteAnalysis, self).get_parser(prog_name)
        parser.add_argument(
            '--analyse-id',
            action='store',
            dest='analyse_id',
            help='analyse_id'
        )
        parser.add_argument(
            '--purge',
            action='store_true',
            dest='purge',
            help='purge'
        )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.AnalysisApi(self.app.client)
        api.delete(token=self.app.client.configuration.token,
                   analyse_id=parsed_args.analyse_id,
                   purge=parsed_args.purge)
