#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import errno
import json
import os

import requests

import memsource_cli
from cliff import command
from cliff.lister import Lister
from cliff.show import ShowOne
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
            required=True,
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
                utils._url(self, 'v1', '/projects/'
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
                      json.dumps(response['jobs'][i]['dateCreated'], default=str).replace(
                          '"', ''),
                      response['jobs'][i]['filename'],
                      response['jobs'][i]['targetLang'])
                     for i in range(0, len(response['jobs']))]

        return((column_headers), (
               (s) for s in data))


class EditJob(ShowOne):
    """
    Edit job
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(EditJob, self).get_parser(prog_name)
        parser.add_argument(
            '--project-id',
            help='project_uid',
            dest='project_uid',
            required=True
        )
        parser.add_argument(
            '--job-id',
            help='job_uid',
            dest='job_uid',
            required=True
        )
        parser.add_argument(
            '--status',
            help='status',
            dest='status',
            required=True
        )
        parser.add_argument(
            '--date-due',
            help='date_due',
            dest='date_due',
        )
        parser.add_argument(
            '--providers',
            help='providers',
            dest='providers',
            nargs='+',
            default=[]
        )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.JobApi(self.app.client)

        _providers = []
        for i in parsed_args.providers:
            provider = i.split('=')
            provider_type = provider[0]
            provider_id = provider[1]
            _providers.append({'type': provider_type, 'id': provider_id})

            # _jobs = []
            # for i in parsed_args.jobs:
            #     _jobs.append({'uid': i})

        response = api.edit_part(token=self.app.client.configuration.token,
                                 project_uid=parsed_args.project_uid,
                                 job_uid=parsed_args.job_uid,
                                 body={"status": parsed_args.status, "providers": _providers, "dateDue": parsed_args.date_due})
        return utils._print_output(response)


class EditJobs(ShowOne):
    """
    Edit jobs
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(EditJobs, self).get_parser(prog_name)
        parser.add_argument(
            '--project-id',
            help='project_uid',
            dest='project_uid',
            required=True
        )
        parser.add_argument(
            '--jobs',
            help='jobs',
            dest='jobs',
            nargs='+',
            default=[]
        )
        parser.add_argument(
            '--status',
            help='status',
            dest='status',
            required=True
        )
        parser.add_argument(
            '--date-due',
            help='date_due',
            dest='date_due',
        )
        parser.add_argument(
            '--providers',
            help='providers',
            dest='providers',
            nargs='+',
            default=[]
        )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.JobApi(self.app.client)

        _providers = []
        for i in parsed_args.providers:
            provider = i.split('=')
            provider_type = provider[0]
            provider_id = provider[1]
            _providers.append({'type': provider_type, 'id': provider_id})

        _jobs = []
        for i in parsed_args.jobs:
            _jobs.append({'uid': i})

        response = api.edit_parts(token=self.app.client.configuration.token,
                                  project_uid=parsed_args.project_uid,
                                  body={"status": parsed_args.status, "providers": _providers, "dateDue": parsed_args.date_due, "jobs": _jobs})
        return utils._print_output(response)


class DeleteTranslations(command.Command):
    """
    Delete translations
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(DeleteTranslations, self).get_parser(prog_name)
        parser.add_argument(
            '--project-id',
            help='project_uid',
            dest='project_uid',
            required=True
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

        print("Accepted request to delete all translations in project %s for jobs %s"
              % (parsed_args.project_uid, parsed_args.job_ids))

        api.delete_all_translations(token=self.app.client.configuration.token,
                                    project_uid=parsed_args.project_uid,
                                    body={"jobs": _job_ids})


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


class DownloadJob(ShowOne):
    """
    Download job file
    """

    def get_parser(self, prog_name):
        """Command argument parsing."""
        parser = super(DownloadJob, self).get_parser(prog_name)
        parser.add_argument(
            '--project-id',
            help='project_uid',
            dest='project_uid',
        )
        parser.add_argument(
            '--type',
            help='type',
            default='target',
            dest='type',
            choices=['target', 'original', 'bilingual'],
        )
        parser.add_argument(
            '--output-dir',
            help='output_dir',
            dest='output_dir'
        )
        parser.add_argument(
            '--job-id',
            required=True,
            help='job_uid',
            dest='job_uid',
            nargs='+',
            default=[]
        )
        parser.add_argument(
            '--target-format',
            help='target_format',
            default='ORIGINAL',
            choices=['ORIGINAL', 'PDF'],
            dest='target_format',
        )
        parser.add_argument(
            '--bilingual-format',
            help='bilingual_format',
            default='MXLF',
            choices=['MXLF', 'DOCX', 'XLIFF'],
            dest='bilingual_format',
        )
        return parser

    def take_action(self, parsed_args):
        api = memsource_cli.JobApi(self.app.client)
        if parsed_args.output_dir:
            self.app.configuration.temp_folder_path = parsed_args.output_dir

        if parsed_args.output_dir:
            if not os.path.exists(parsed_args.output_dir):
                try:
                    os.makedirs(parsed_args.output_dir)
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise

        file_paths = []
        if parsed_args.type == "target":
            for job_uid in parsed_args.job_uid:
                path = api.completed_file(token=self.app.client.configuration.token,
                                          project_uid=parsed_args.project_uid,
                                          job_uid=job_uid,
                                          format=parsed_args.target_format)
                file_paths.append(path)
            header = (("type"), ("format"), ("path"))
            values = ((parsed_args.type),
                      (parsed_args.target_format), (file_paths))

        elif parsed_args.type == "original":
            for job_uid in parsed_args.job_uid:
                path = api.get_original_file(token=self.app.client.configuration.token,
                                             project_uid=parsed_args.project_uid,
                                             job_uid=job_uid)
                file_paths.append(path)
            header = (("type"), ("path"))
            values = ((parsed_args.type), (file_paths))

        elif parsed_args.type == "bilingual":
            _job_ids = []
            for job_uid in parsed_args.job_uid:
                _job_ids.append({'uid': job_uid})
            path = api.get_bilingual_file(token=self.app.client.configuration.token,
                                          project_uid=parsed_args.project_uid,
                                          body={"jobs": _job_ids},
                                          format=parsed_args.bilingual_format)
            file_paths.append(path)
            header = (("type"), ("format"), ("path"))
            values = ((parsed_args.type),
                      (parsed_args.bilingual_format), (file_paths))

        return((header), (values))
