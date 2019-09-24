#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import memsource_cli
from memsource_cli.lib import utils

from cliff.show import ShowOne


class Login(ShowOne):
    """
    Login
    """
    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(Login, self).get_parser(prog_name)
        model = memsource_cli.models.LoginDto.attribute_map

        for k, v in model.items():
            parser.add_argument(
                '--' + k.replace('_', '-'),
                help=k,
                dest=v
            )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.AuthenticationApi(self.app.client)
        response = api.login(body=vars(parsed_args))

        return utils._print_output(response)
