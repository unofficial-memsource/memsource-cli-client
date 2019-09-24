#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

from cliff.show import ShowOne

import memsource_cli
from memsource_cli.lib import utils


class CreateProjectFromTemplate(ShowOne):
    """
    Create new project from template
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(CreateProjectFromTemplate, self).get_parser(prog_name)

        all_params = {
            'name': 'name',
            'source_lang': 'sourceLang',
            'date_due': 'datetime',
            'note': 'note',
            'client': 'client',
            'business_unit': 'businessUnit',
            'domain': 'domain',
            'sub_domain': 'subDomain'
        }
        all_params_list = {
            'target_langs': 'targetLangs',
            'workflow_steps': 'workflowSteps',
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
        parser.add_argument(
            '--template-id',
            action='store',
            dest='template_id',
            help='template_id'
        )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.ProjectApi(self.app.client)

        all_params = ['name', 'sourceLang', 'workflowSteps', 'dateDue',
                      'note', 'client', 'businessUnit', 'domain',
                      'subDomain']
        args = {}

        parsed = vars(parsed_args)

        for k, v in parsed.items():
            if k in all_params and v is not None:
                args[k] = v

        response = api.create_project_from_template_v2(token=self.app.client.configuration.token,  # noqa: E501
                                      template_id=parsed_args.template_id,
                                      body=vars(parsed_args))

        return utils._print_output(response)
