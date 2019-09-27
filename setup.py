from setuptools import setup, find_packages

PROJECT = 'memsource_cli'
VERSION = '0.2'

if __name__ == "__main__":

    with open('README.md') as f:
        long_description = f.read()

    setup(
        name=PROJECT,
        version=VERSION,
        description="Unofficial Memsource CLI client",
        long_description=long_description,
	long_description_content_type="text/markdown",
        keywords='memsource',
        url="https://github.com/unofficial-memsource/memsource-cli-client",
        author="Robin Černín",
        author_email="cerninr@gmail.com",
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            'cliff',
            'certifi>=2017.4.17',
            'python-dateutil>=2.1',
            'six>=1.10',
            'urllib3>=1.23',
	    'requests'
        ],
        entry_points={
            'console_scripts': [
                'memsource = memsource_cli.memsource:main'
            ],
            'memsource.cli': [
            # memsource_cli.user.v2
                'user_get = memsource_cli.user.v2.user:GetUser',
                'user_create = memsource_cli.user.v2.user:CreateUser',
            # memsource_cli.auth.v1
                'auth_whoami = memsource_cli.auth.v1.whoami:WhoAmI',
                'auth_login = memsource_cli.auth.v1.login:Login',
            # memsource_cli.project.v1
                'project_list = memsource_cli.project.v1.project:ListProjects',
                'project_show = memsource_cli.project.v1.project:ShowProject',
                'project_delete = memsource_cli.project.v1.project:DeleteProject',  # noqa: E501
                'project_create = memsource_cli.project.v1.project:CreateProject',  # noqa: E501
            # memsource_cli.project.v2
                'project_template_create = memsource_cli.project.v2.project:CreateProjectFromTemplate',  # noqa: E501
            # memsource_cli.job.v2
                'job_list = memsource_cli.job.v2.job:ListJobs',
            # memsource_cli.job.v1
                'job_show = memsource_cli.job.v1.job:ShowJob',
                'job_create = memsource_cli.job.v1.job:CreateJob',
                'job_delete = memsource_cli.job.v1.job:DeleteJobs',
            # memsource_cli.analysis.v1
                'analyse_create = memsource_cli.analysis.v1.analysis:CreateAnalysis',  # noqa: E501
                'analyse_delete = memsource_cli.analysis.v1.analysis:DeleteAnalysis',  # noqa: E501
                'analyse_language_create = memsource_cli.analysis.v1.analysis:CreateAnalysisByLanguages',  # noqa: E501
            # memsource_cli.analysis.v2
                'analyse_project_list = memsource_cli.analysis.v2.analysis:ListAnalysisByProject',  # noqa: E501
                'analyse_show = memsource_cli.analysis.v2.analysis:ShowAnalysis',  # noqa: E501
            ],
        },
        zip_safe=False,
    )
