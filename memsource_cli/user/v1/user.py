import memsource_cli
import json
import datetime
from memsource_cli.lib import utils

from cliff.show import ShowOne
from cliff import command
from cliff.lister import Lister


class ListUser(Lister):
    """
    List users
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(ListUser, self).get_parser(prog_name)
        all_params = ['user_name', 'email' ]  # noqa: E501
        all_params_int = ['page_number', 'page_size' ]  # noqa: E501
    
        for param in all_params:
            parser.add_argument(
                '--' + param.replace('_', '-'),
                help=param,
                dest=param
            )

        for param_int in all_params_int:
            parser.add_argument(
                '--' + param_int.replace('_', '-'),
                help=param_int,
                type=int,
                dest=param_int
            )

        parser.add_argument(
            '--include-deleted',
            action='store_true',
            dest='include_deleted',
            help='include_deleted'
        )

        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.UserApi(self.app.client)
        query_params = vars(parsed_args)
        args = {}
        all_params = ['user_name', 'email','page_number', 'page_size',
                      'include_deleted']  # noqa: E501

        for k, v in query_params.items():
            if k in all_params and v is not None:
                args[k] = v

        response = api.get_list_of_users_filtered(token=self.app.client.configuration.token,**args)
        
        output = response.to_dict()
        content = output['content']

        data = []
        column_headers = ['user_name', 'first_name', 'last_name', 'id',
                        'date_created', 'date_deleted', 'email', 'active', 'note',
                        'source_langs', 'target_langs', 'terminologist', 'created_by',
                        'timezone', 'role']

        for i in range(0, len(content)):
            data += [(content[i]['user_name'],
                        content[i]['first_name'],
                        content[i]['last_name'],
                        content[i]['id'],
                        json.dumps(content[i]['date_created'],
                                    default=str).replace('"', ''),
                        json.dumps(content[i]['date_deleted'],
                                    default=str).replace('"', ''),
                        content[i]['email'],
                        content[i]['active'],
                        content[i]['note'],
                        content[i]['source_langs'],
                        content[i]['target_langs'],
                        content[i]['terminologist'],
                        content[i]['created_by']['user_name'],
                        content[i]['timezone'],
                        content[i]['role'])]
        return((column_headers), (data))
