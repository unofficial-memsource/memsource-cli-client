#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

from cliff.lister import Lister
from cliff import command
from cliff.show import ShowOne
import requests
import json

import memsource_cli
from memsource_cli.lib import utils


class CreateJob(Lister):
    """
    Creates job in project
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(CreateJob, self).get_parser(prog_name)
        parser.add_argument(
            '--filenames',
            help='filenames',
            nargs='+',
            default=[]
        )
        parser.add_argument(
            '--project-id',
            help='project_uid',
            dest='project_uid',
        )
        parser.add_argument(
            '--target-langs',
            help='target_langs',
            nargs='+',
            default=[],
        )
        return parser

    def take_action(self, parsed_args):

        token = self.app.client.configuration.token
        data = []
        column_headers = ('id',
                          'status',
                          'date_created',
                          'filename',
                          'target_langs')

        for file in parsed_args.filenames:
            _filename = file.split("/")[-1]
            _file = open(file, 'rb')
            response = requests.post(
                utils._url('v1', '/projects/'
                           + parsed_args.project_uid
                           + '/jobs'
                           + '?token='
                           + token),
                json={
                    'targetLangs': parsed_args.target_langs,
                    'useProjectFileImportSettings': True
                },
                headers={
                    'Content-Type': 'application/octet-stream',
                    'Content-Disposition': 'filename='
                    + _filename,
                    'Memsource': '{\'targetLangs\': '
                    + str(parsed_args.target_langs)
                    + ',\'useProjectFileImportSettings\': \'true\'}'
                },
                data=_file
                )
            utils.validate_response(response, 201)
            response = json.loads(response.text)
            data += [(response['jobs'][i]['uid'],
                      response['jobs'][i]['status'],
                      response['jobs'][i]['dateCreated'],
                      response['jobs'][i]['filename'],
                      response['jobs'][i]['targetLang'])
                     for i in range(0, len(response['jobs']))]

        return((column_headers), (
               (s) for s in data))


class DeleteJobs(command.Command):
    """
    Delete jobs
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(DeleteJobs, self).get_parser(prog_name)
        parser.add_argument(
            '--project-id',
            help='project_uid',
            dest='project_uid',
            required=True
        )
        parser.add_argument(
            '--purge',
            action='store_true',
            dest='purge',
            help='purge'
        )
        parser.add_argument(
            'job_ids',
            help='job_ids',
            nargs='+',
            default=[]
        )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.JobApi(self.app.client)

        _job_ids = []
        for i in parsed_args.job_ids:
            _job_ids.append({'uid': i})

        print("Accepted request to delete jobs: %s in project %s"
              % (parsed_args.job_ids, parsed_args.project_uid))

        api.delete_parts(token=self.app.client.configuration.token,
                         project_uid=parsed_args.project_uid,
                         purge=parsed_args.purge,
                         body={"jobs": _job_ids})


class ShowJob(ShowOne):
    """
    Get job
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(ShowJob, self).get_parser(prog_name)
        parser.add_argument(
            '--project-id',
            help='project_uid',
            dest='project_uid',
        )
        parser.add_argument(
            '--job-id',
            help='job_uid',
            dest='job_uid',
        )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.JobApi(self.app.client)
        response = api.get_part(token=self.app.client.configuration.token,
                                project_uid=parsed_args.project_uid,
                                job_uid=parsed_args.job_uid)

        return utils._print_output(response)
