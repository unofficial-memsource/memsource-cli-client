#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

from cliff.show import ShowOne
from cliff.lister import Lister

import memsource_cli
from memsource_cli.lib import utils

class ListTemplate(Lister): 
    """
    List templates
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(ListTemplate, self).get_parser(prog_name)
        all_params = ['name']  # noqa: E501                      
        all_params_int = ['client_id', 'page_number', 'page_size']  # noqa: E501
    
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
        api = memsource_cli.ProjectTemplateApi(self.app.client)
        query_params = vars(parsed_args)
        args = {}
        all_params = ['name', 'client_id', 'page_number', 'page_size']  # noqa: E501

        for k, v in query_params.items():
            if k in all_params and v is not None:
                args[k] = v

        
        response = api.get_project_templates(token=self.app.client.configuration.token,  # noqa: E501
                                             **args)

        response = response.to_dict()

        return(('id',
            'target_langs',
            'source_lang',
            'template_name'),(
            (response['content'][i]['id'],
            response['content'][i]['target_langs'],
            response['content'][i]['source_lang'],
            response['content'][i]['template_name'])
            for i in range(0, len(response['content']))))

class ShowTemplate(ShowOne): 
    """
    Show template
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(ShowTemplate, self).get_parser(prog_name)

        parser.add_argument(
            '--project-template-id',
            type=int,
            dest='project_template_id',
            help='project_template_id'
        )

        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.ProjectTemplateApi(self.app.client)
        response = api.get_project_template(token=self.app.client.configuration.token,  # noqa: E501
                                            project_template_id=parsed_args.project_template_id)

        return utils._print_output(response)
