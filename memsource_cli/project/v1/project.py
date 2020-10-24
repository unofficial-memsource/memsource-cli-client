#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

from cliff import command
from cliff.lister import Lister
from cliff.show import ShowOne

import json
import memsource_cli
from memsource_cli.lib import utils


class CreateProject(ShowOne):
    """
    Create new project
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(CreateProject, self).get_parser(prog_name)

        all_params = {
            'uid': 'uid',
            'id': 'id',
            'name': 'name',
            'date_created': 'dateCreated',
            'domain': 'domain',
            'sub_domain': 'subDomain',
            'owner': 'owner',
            'source_lang': 'sourceLang',
            'user_role': 'userRole',
            'note': 'note',
            'client': 'client',
            'date_due': 'datetime',
            'business_unit': 'businessUnit',
        }
        all_params_int = {
            'internal_id': 'internalId',
        }
        all_params_list = {
            'target_langs': 'targetLangs',
            'references': 'references',
            'workflow_steps': 'workflowSteps',
        }

        for k, v in all_params.items():
            parser.add_argument(
                '--' + k.replace('_', '-'),
                help=v,
                dest=v
            )
        for k, v in all_params_int.items():
            parser.add_argument(
                '--' + k.replace('_', '-'),
                help=v,
                dest=v,
                type=int
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
        if parsed_args.template_id:
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
        
        api = memsource_cli.ProjectApi(self.app.client)
        response = api.create_project(token=self.app.client.configuration.token,  # noqa: E501
                                      body=vars(parsed_args))

        return utils._print_output(response)


class AssignsProvidersFromTemplate(command.Command):
    """
    Assigns providers from template
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(AssignsProvidersFromTemplate, self).get_parser(prog_name)
        parser.add_argument(
            '--project-id',
            action='store',
            dest='project_uid',
            help='project_uid',
            required=True
        )
        parser.add_argument(
            '--template-id',
            action='store',
            dest='template_id',
            help='template_id',
            required=True
        )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.ProjectApi(self.app.client)
        api.assign_linguists_from_template(token=self.app.client.configuration.token,
                           project_uid=parsed_args.project_uid,
                           template_id=parsed_args.template_id)


class DeleteProject(command.Command):
    """
    Deletes a project
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(DeleteProject, self).get_parser(prog_name)
        parser.add_argument(
            '--project-id',
            action='store',
            dest='project_uid',
            help='project_uid'
        )
        parser.add_argument(
            '--purge',
            action='store_true',
            dest='purge',
            help='purge'
        )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.ProjectApi(self.app.client)
        api.delete_project(token=self.app.client.configuration.token,
                           project_uid=parsed_args.project_uid,
                           purge=parsed_args.purge)


class ShowProject(ShowOne):
    """
    Get project
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(ShowProject, self).get_parser(prog_name)
        parser.add_argument(
            '--project-id',
            action='store',
            dest='project_uid',
            help='project_uid'
        )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.ProjectApi(self.app.client)
        response = api.get_project(token=self.app.client.configuration.token,
                                   project_uid=parsed_args.project_uid)

        return utils._print_output(response)


class ListProjects(Lister):
    """
    List projects
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(ListProjects, self).get_parser(prog_name)

        all_params = ['name', 'client_name', 'business_unit_name',
                      'domain_name', 'sub_domain_name',
                      'cost_center_name', 'job_status_group']  # noqa: E501

        all_params_int = ['client_id', 'cost_center_id',
                          'due_in_hours', 'created_in_last_hours', 'owner_id',
                          'buyer_id', 'page_number', 'page_size']  # noqa: E501

        all_params_list = ['statuses', 'target_langs', 'source_langs',
                           'job_statuses']

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
        for param in all_params_list:
            parser.add_argument(
                '--' + param.replace('_', '-'),
                help=param,
                nargs='+',
                default=[]
            )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.ProjectApi(self.app.client)
        query_params = vars(parsed_args)
        args = {}
        all_params = ['name', 'client_id', 'client_name', 'business_unit_name',
                      'statuses', 'target_langs', 'domain_name',
                      'sub_domain_name', 'cost_center_id', 'cost_center_name',
                      'due_in_hours', 'created_in_last_hours', 'source_langs',
                      'owner_id', 'job_statuses', 'job_status_group',
                      'buyer_id', 'page_number', 'page_size', 'token']  # noqa: E501

        for k, v in query_params.items():
            if k in all_params and v is not None:
                args[k] = v

        response = api.list_projects(token=self.app.client.configuration.token,
                                     **args)

        column_headers = ['uid', 'internal_id', 'id', 'name',
                          'date_created', 'domain', 'sub_domain',
                          'owner', 'source_lang', 'target_langs',
                          'references', 'user_role']
        data = []

        output = response.to_dict()
        content = output['content']

        for i in range(0, len(content)):
            for j in column_headers:
                if isinstance(content[i][j], dict):
                    content[i][j] = json.dumps(content[i][j])
            data += [(content[i]['uid'],
                      content[i]['internal_id'],
                      content[i]['id'],
                      content[i]['name'],
                      json.dumps(content[i]['date_created'],
                                 default=str).replace('"', ''),
                      content[i]['domain'],
                      content[i]['sub_domain'],
                      content[i]['owner'],
                      content[i]['source_lang'],
                      content[i]['target_langs'],
                      json.dumps(content[i]['references']),
                      content[i]['user_role'])]

        return((column_headers), (data))
