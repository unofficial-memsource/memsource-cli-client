# coding: utf-8

"""
    Memsource REST API

    Welcome to Memsource's API documentation. To view our legacy APIs please [visit our documentation](https://wiki.memsource.com/wiki/Memsource_API) and for more information about our new APIs, [visit our blog](https://www.memsource.com/blog/2017/10/24/introducing-rest-apis-qa-with-the-memsource-api-team/).    If you have any questions, please contact [Memsource Support](<mailto:support@memsource.com>).  # noqa: E501

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import memsource_cli
from memsource_cli.api.quality_assurance_api import QualityAssuranceApi  # noqa: E501
from memsource_cli.rest import ApiException


class TestQualityAssuranceApi(unittest.TestCase):
    """QualityAssuranceApi unit test stubs"""

    def setUp(self):
        self.api = memsource_cli.api.quality_assurance_api.QualityAssuranceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_ignored_warnings(self):
        """Test case for add_ignored_warnings

        Add ignored warnings  # noqa: E501
        """
        pass

    def test_delete_ignored_warnings(self):
        """Test case for delete_ignored_warnings

        Delete ignored warnings  # noqa: E501
        """
        pass

    def test_enabled_quality_checks_for_job(self):
        """Test case for enabled_quality_checks_for_job

        Get QA settings  # noqa: E501
        """
        pass

    def test_run_qa_for_job_part_v3(self):
        """Test case for run_qa_for_job_part_v3

        Run quality assurance  # noqa: E501
        """
        pass

    def test_run_qa_for_job_parts_v3(self):
        """Test case for run_qa_for_job_parts_v3

        Run quality assurance (batch)  # noqa: E501
        """
        pass

    def test_run_qa_for_segments_v3(self):
        """Test case for run_qa_for_segments_v3

        Run quality assurance on selected segments  # noqa: E501
        """
        pass

    def test_update_ignored_checks(self):
        """Test case for update_ignored_checks

        Edit ignored checks  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()