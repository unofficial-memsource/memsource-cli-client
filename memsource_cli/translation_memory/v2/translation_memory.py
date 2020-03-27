#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

from cliff import command
from cliff.lister import Lister
from cliff.show import ShowOne

import json
import requests
import memsource_cli
from memsource_cli.lib import utils


class ExportTranslationMemory(Lister):
    """
    Export Translation Memory
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(ExportTranslationMemory, self).get_parser(prog_name)

        parser.add_argument(
            '--trans-memory-id',
            help='trans_memory_id',
            required=True,
            dest='trans_memory_id',
        )
        parser.add_argument(
            '--target-format',
            help='format',
            default='TMX',
            choices=['TMX', 'XLSX'],
            dest='format',
        )
        return parser

    def take_action(self, parsed_args):
        token = self.app.client.configuration.token

        response = requests.post(
            utils._url(self, 'v2', '/transMemories/'
                       + parsed_args.trans_memory_id
                       + '/export'
                       + '?token='
                       + token),
            json={
                'format': parsed_args.format
            })
        utils.validate_response(response, 200)

        data = []
        column_headers = ['id', 'action', 'created_by', 'date_created',
                          'project', 'parent', 'async_export']
        output = json.loads(response.content.decode('utf-8'))
        data += [(output['asyncRequest']['id'],
                  output['asyncRequest']['action'],
                  output['asyncRequest']['createdBy'],
                  output['asyncRequest']['dateCreated'],
                  output['asyncRequest']['project'],
                  output['asyncRequest']['parent'],
                  output['asyncExport'])]

        return((column_headers), (data))
