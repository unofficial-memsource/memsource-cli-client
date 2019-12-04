#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import sys
import os

from cliff.app import App
from cliff.commandmanager import CommandManager

import memsource_cli
from memsource_cli.lib import utils


class MemsourceCli(App):

    def __init__(self):
        super(MemsourceCli, self).__init__(
            description='Unofficial Memsource CLI client',
            version=memsource_cli.__version__,
            command_manager=CommandManager('memsource.cli'),
            deferred_help=True,
        )

    def initialize_app(self, argv):
        super(MemsourceCli, self).initialize_app(argv)
        os.environ['CLIFF_FIT_WIDTH'] = '1'

        self.configuration = memsource_cli.Configuration()

    def build_option_parser(self, description, version):
        """Command argument parsing."""
        parser = super(MemsourceCli, self).build_option_parser(
            description,
            version,
        )
        parser.add_argument(
            '--ms-username',
            action="store",
            metavar='<auth-username>',
            default=utils.env('MEMSOURCE_USERNAME'),
            help='Authentication username (Env: MEMSOURCE_USERNAME)'
        )
        parser.add_argument(
            '--ms-password',
            action="store",
            metavar='<auth-password>',
            default=utils.env('MEMSOURCE_PASSWORD'),
            help='Authentication password (Env: MEMSOURCE_PASSWORD)'
        )
        parser.add_argument(
            '--ms-token',
            action="store",
            metavar='<auth-token>',
            default=utils.env('MEMSOURCE_TOKEN'),
            help='Authentication token (Env: MEMSOURCE_TOKEN)'
        )
        parser.add_argument(
            '--ms-auth-url',
            action="store",
            metavar='<auth-url>',
            default=utils.env('MEMSOURCE_URL'),
            help='Authentication URL (Env: MEMSOURCE_URL)'
        )

        return parser

    def prepare_to_run_command(self, cmd):
        """Set up auth and API versions"""

        if self.options.debug:
            self.configuration.debug = True
        if self.options.log_file:
            self.configuration.logger_file = self.options.log_file
        if self.options.ms_auth_url:
            self.configuration.host = self.options.ms_auth_url

        if not self.options.ms_token:
            if not self.options.ms_username:
                print(
                    "You must provide a username via"
                    " either --ms-username or env[MEMSOURCE_USERNAME]")
            self.configuration.username = self.options.ms_username

            if not self.options.ms_password:
                print("You must provide a password via"
                      " either --ms-password or env[MEMSOURCE_PASSWORD]")
            self.configuration.password = self.options.ms_password

        else:
            self.configuration.token = self.options.ms_token

        self.client = memsource_cli.ApiClient(configuration=self.configuration)

        return

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    memsource = MemsourceCli()
    return memsource.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
