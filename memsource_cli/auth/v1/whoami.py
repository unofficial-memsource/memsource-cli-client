#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import memsource_cli
from memsource_cli.lib import utils

from cliff.show import ShowOne


class WhoAmI(ShowOne):
    """
    Who am I
    """

    def take_action(self, parsed_args):
        api = memsource_cli.AuthenticationApi(self.app.client)
        response = api.who_am_i(token=self.app.client.configuration.token)

        return utils._print_output(response)
