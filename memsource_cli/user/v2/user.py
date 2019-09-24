import memsource_cli
from memsource_cli.lib import utils

from cliff.show import ShowOne
from cliff import command


class GetUser(ShowOne):
    """
    Get user
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(GetUser, self).get_parser(prog_name)
        parser.add_argument(
            '--user-id',
            help='user_id',
            required=True
        )
        return parser

    def take_action(self, parsed_args):

        api = memsource_cli.UserApi(self.app.client)
        response = api.get_user_v2(user_id=parsed_args.user_id,
                                   token=self.app.client.configuration.token)
        return utils._print_output(response)


class CreateUser(command.Command):
    """
    Create user
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(CreateUser, self).get_parser(prog_name)
        model = memsource_cli.models.UserCreateDtoV2.attribute_map

        for k, v in model.items():
            parser.add_argument(
                '--' + k.replace('_', '-'),
                help=k,
                dest=v
            )
        return parser

    def take_action(self, parsed_args):

        api = memsource_cli.UserApi(self.app.client)
        api.create_user_v2(body=vars(parsed_args),
                           token=self.app.client.configuration.token)
