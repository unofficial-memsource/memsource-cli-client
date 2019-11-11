#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

from cliff.show import ShowOne

import memsource_cli
from memsource_cli.lib import utils

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
