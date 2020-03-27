#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

from cliff import command
from cliff.lister import Lister
from cliff.show import ShowOne

import json
import os
import errno
import requests
import memsource_cli
from memsource_cli.lib import utils


class ImportSegmentTranslationMemory(Lister):
    """
    Import segments
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(ImportSegmentTranslationMemory,
                       self).get_parser(prog_name)
        parser.add_argument(
            '--filenames',
            help='filenames',
            required=True,
            nargs='+',
            default=[]
        )
        parser.add_argument(
            '--trans-memory-id',
            help='trans_memory_id',
            required=True,
            dest='trans_memory_id',
        )
        parser.add_argument(
            '--strict-lang-matching',
            action='store_true',
            default=False,
            dest='strict_lang_matching',
            help='strict_lang_matching'
        )
        parser.add_argument(
            '--no-strip-native-codes',
            action='store_false',
            default=True,
            dest='strip_native_codes',
            help='strip_native_codes'
        )
        parser.add_argument(
            '--exclude-not-confirmed-segments',
            action='store_true',
            default=False,
            dest='exclude_not_confirmed_segments',
            help='exclude_not_confirmed_segments'
        )
        return parser

    def take_action(self, parsed_args):

        token = self.app.client.configuration.token
        data = []

        column_headers = ('filename',
                          'created_segments_count',
                          'updated_cegments_count',
                          'skipped_segments_count',
                          'accepted_segments_count',
                          'empty')

        for file in parsed_args.filenames:
            _filename = file.split("/")[-1]
            _file = open(file, 'rb')
            response = requests.post(
                utils._url(self, 'v1', '/transMemories/'
                           + parsed_args.trans_memory_id
                           + '/import'
                           + '?token='
                           + token),
                json={
                    'strictLangMatching': parsed_args.strict_lang_matching,
                    'stripNativeCodes': parsed_args.strip_native_codes,
                    'excludeNotConfirmedSegments': parsed_args.exclude_not_confirmed_segments
                },
                headers={
                    'Content-Type': 'application/octet-stream',
                    'Content-Disposition': 'filename*=UTF-8\'\''
                    + _filename
                },
                data=_file
            )
            utils.validate_response(response, 200)
            response = json.loads(response.text)
            data += [(file,
                      response['createdSegmentsCount'],
                      response['updatedSegmentsCount'],
                      response['skippedSegmentsCount'],
                      response['acceptedSegmentsCount'],
                      response['empty'])]

        return((column_headers), (
            (s) for s in data))


class DownloadTranslationMemory(ShowOne):
    """
    Download Translation Memory
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(DownloadTranslationMemory, self).get_parser(prog_name)
        parser.add_argument(
            '--async-req-id',
            help='async_req_id',
            required=True,
            dest='async_req_id',
        )
        parser.add_argument(
            '--target-format',
            help='format',
            default='TMX',
            choices=['TMX', 'XLSX'],
            dest='format',
        )
        parser.add_argument(
            '--filename',
            help='filename',
            required=True,
            dest='filename',
        )
        parser.add_argument(
            '--output-dir',
            help='output_dir',
            dest='output_dir'
        )
        return parser

    def take_action(self, parsed_args):
        token = self.app.client.configuration.token

        if parsed_args.output_dir:
            self.app.configuration.temp_folder_path = parsed_args.output_dir

        if parsed_args.output_dir:
            if not os.path.exists(parsed_args.output_dir):
                try:
                    os.makedirs(parsed_args.output_dir)
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise

        response = requests.get(
            utils._url(self, 'v1', '/transMemories/downloadExport/'
                       + parsed_args.async_req_id
                       + '?token='
                       + token),
            json={
                'format': parsed_args.format
            })
        filename = parsed_args.filename
        if parsed_args.output_dir:
            path = os.path.join(parsed_args.output_dir,
                                filename).replace('%2F', '/')
        else:
            path = filename
        try:
            with open(path, "wb") as f:
                f.write(response.content)
        except:
            with open(path, "w") as f:
                f.write(response.content)

        header = (("format"), ("path"))
        values = ((parsed_args.format),
                  (path))
        return((header), (values))


class WildcardSearchTranslationMemory(Lister):
    """
    Wildcard Search Translation Memory
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(WildcardSearchTranslationMemory,
                       self).get_parser(prog_name)

        parser.add_argument(
            '--trans-memory-id',
            help='trans_memory_id',
            required=True,
            dest='trans_memory_id',
        )
        parser.add_argument(
            '--query',
            help='query',
            required=True,
            dest='query',
        )
        parser.add_argument(
            '--source-lang',
            help='source_lang',
            required=True,
            dest='source_lang',
        )
        parser.add_argument(
            '--target-langs',
            help='target_langs',
            required=True,
            nargs='+',
            default=[],
        )
        return parser

    def take_action(self, parsed_args):
        token = self.app.client.configuration.token
        response = requests.post(
            utils._url(self, 'v1', '/transMemories/'
                       + parsed_args.trans_memory_id
                       + '/wildCardSearch'
                       + '?token='
                       + token),
            json={
                'query': parsed_args.query,
                'targetLangs': parsed_args.target_langs,
                'sourceLang': parsed_args.source_lang,
            }
        )
        utils.validate_response(response, 200)

        output = json.loads(response.content.decode('utf-8'))['searchResults']
        column_headers = ['source_lang', 'source_text',  'target_lang',
                          'target_text', 'project_id', 'project']
        data = []
        for i in range(0, len(output)):
            try:
                project = output[i]['translations'][0]['project']['name']
            except:
                project = None
            if project is None:
                data += [(output[i]['source']['lang'],
                          output[i]['source']['text'],
                          output[i]['translations'][0]['lang'],
                          output[i]['translations'][0]['text'],
                          "None",
                          "None")]
            else:
                data += [(output[i]['source']['lang'],
                          output[i]['source']['text'],
                          output[i]['translations'][0]['lang'],
                          output[i]['translations'][0]['text'],
                          output[i]['translations'][0]['project']['id'],
                          output[i]['translations'][0]['project']['name'])]

        return((column_headers), (data))


class ListTranslationMemories(Lister):
    """
    List Translation Memories
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(ListTranslationMemories, self).get_parser(prog_name)

        all_params = ['name', 'source_lang', 'target_lang',
                      'client_id', 'domain_id',
                      'sub_domain_id', 'business_unit_id']  # noqa: E501

        all_params_int = ['page_number', 'page_size']  # noqa: E501

        for param in all_params:
            parser.add_argument(
                '--' + param.replace('_', '-'),
                help=param,
                dest=param
            )
        for param in all_params_int:
            parser.add_argument(
                '--' + param.replace('_', '-'),
                help=param,
                type=int
            )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.TranslationMemoryApi(self.app.client)
        query_params = vars(parsed_args)
        args = {}
        all_params = ['name', 'source_lang', 'target_lang', 'client_id',
                      'domain_id', 'sub_domain_id', 'business_unit_id',
                      'page_number', 'page_size']  # noqa: E501

        for k, v in query_params.items():
            if k in all_params and v is not None:
                args[k] = v

        response = api.list_trans_memories(token=self.app.client.configuration.token,
                                           **args)

        column_headers = ['id', 'internal_id',  'name',
                          'date_created', 'source_lang', 'target_langs',
                          'created_by', 'note', 'sub_domain', 'domain']
        data = []

        output = response.to_dict()
        content = output['content']

        for i in range(0, len(content)):
            for j in column_headers:
                if isinstance(content[i][j], dict):
                    content[i][j] = json.dumps(content[i][j])
            data += [(content[i]['id'],
                      content[i]['internal_id'],
                      content[i]['name'],
                      json.dumps(content[i]['date_created'],
                                 default=str).replace('"', ''),
                      content[i]['source_lang'],
                      content[i]['target_langs'],
                      content[i]['created_by'],
                      content[i]['note'],
                      json.dumps(content[i]['sub_domain'],
                                 default=str).replace('"', ''),
                      json.dumps(content[i]['domain'],
                                 default=str).replace('"', ''))]

        return((column_headers), (data))
