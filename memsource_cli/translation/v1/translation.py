#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import memsource_cli
from memsource_cli.lib import utils

from cliff.show import ShowOne
import json
import datetime


class PreTranslate(ShowOne):
    """
    Pre-translate job
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(PreTranslate, self).get_parser(prog_name)

        all_params = {
            'project_id': 'project_uid',
            'callback_url': 'callbackUrl'
        }
        all_params_bool_true = {
            'no_translation_memory': 'useTranslationMemory',
            'no_machine_translation': 'useMachineTranslation'
        }
        all_params_bool_false = {
            'insert_machine_translation_into_target': 'insertMachineTranslationIntoTarget',
            'pre_translate_non_translatables': 'preTranslateNonTranslatables',
            'confirm100_non_translatable_matches': 'confirm100NonTranslatableMatches',
            'confirm100_translation_memory_matches': 'confirm100TranslationMemoryMatches',
            'confirm101_translation_memory_matches': 'confirm101TranslationMemoryMatches',
            'lock100_non_translatable_matches': 'lock100NonTranslatableMatches',
            'lock100_translation_memory_matches': 'lock100TranslationMemoryMatches',
            'lock101_translation_memory_matches': 'lock101TranslationMemoryMatches',
            'overwrite': 'overwrite',
            'use_project_pre_translate_settings': 'useProjectPreTranslateSettings',
        }
        all_params_int = {
            'translation_memory_treshold': 'translationMemoryTreshold'
        }
        all_params_list = {
            'job_ids': 'jobs',
            'segment_filters': 'segmentFilters'
        }

        for k, v in all_params_bool_false.items():
            parser.add_argument(
                '--' + k.replace('_', '-'),
                help=v,
                dest=v,
                action="store_true"
            )
        for k, v in all_params_bool_true.items():
            parser.add_argument(
                '--' + k.replace('_', '-'),
                help="Not " + v,
                dest=v,
                action="store_false"
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
                default=0.7,
                dest=v,
                type=float
            )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.TranslationApi(self.app.client)

        _job_ids = []
        for i in parsed_args.jobs:
            _job_ids.append({'uid': i})
        parsed_args.jobs = _job_ids

        response = api.pre_translate(
            project_uid=parsed_args.project_uid, body=vars(parsed_args),
            token=self.app.client.configuration.token)

        column_headers = ['id', 'created_by', 'date_created',
                          'action', 'async_response', 'parent', 'project']
        data = []

        output = response.to_dict()

        content = output['async_request']
        for k, v in content.items():
            if isinstance(v, datetime.datetime):
                v = json.dumps(v, default=str).replace('"', '')
            if isinstance(v, dict):
                v = json.dumps(v)
            data += [(v)]

        return((column_headers), (data))
