# coding: utf-8

"""
    Memsource REST API

    Welcome to Memsource's API documentation. To view our legacy APIs please [visit our documentation](https://wiki.memsource.com/wiki/Memsource_API) and for more information about our new APIs, [visit our blog](https://www.memsource.com/blog/2017/10/24/introducing-rest-apis-qa-with-the-memsource-api-team/).    If you have any questions, please contact [Memsource Support](<mailto:support@memsource.com>).  # noqa: E501

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from memsource_cli.models.quality_assurance_run_dto_v3 import QualityAssuranceRunDtoV3  # noqa: F401,E501
from memsource_cli.models.uid_reference import UidReference  # noqa: F401,E501


class QualityAssuranceBatchRunDtoV3(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'jobs': 'list[UidReference]',
        'settings': 'QualityAssuranceRunDtoV3',
        'max_qa_warnings_count': 'int'
    }

    attribute_map = {
        'jobs': 'jobs',
        'settings': 'settings',
        'max_qa_warnings_count': 'maxQaWarningsCount'
    }

    def __init__(self, jobs=None, settings=None, max_qa_warnings_count=None):  # noqa: E501
        """QualityAssuranceBatchRunDtoV3 - a model defined in Swagger"""  # noqa: E501

        self._jobs = None
        self._settings = None
        self._max_qa_warnings_count = None
        self.discriminator = None

        self.jobs = jobs
        if settings is not None:
            self.settings = settings
        if max_qa_warnings_count is not None:
            self.max_qa_warnings_count = max_qa_warnings_count

    @property
    def jobs(self):
        """Gets the jobs of this QualityAssuranceBatchRunDtoV3.  # noqa: E501


        :return: The jobs of this QualityAssuranceBatchRunDtoV3.  # noqa: E501
        :rtype: list[UidReference]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this QualityAssuranceBatchRunDtoV3.


        :param jobs: The jobs of this QualityAssuranceBatchRunDtoV3.  # noqa: E501
        :type: list[UidReference]
        """
        if jobs is None:
            raise ValueError("Invalid value for `jobs`, must not be `None`")  # noqa: E501

        self._jobs = jobs

    @property
    def settings(self):
        """Gets the settings of this QualityAssuranceBatchRunDtoV3.  # noqa: E501


        :return: The settings of this QualityAssuranceBatchRunDtoV3.  # noqa: E501
        :rtype: QualityAssuranceRunDtoV3
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this QualityAssuranceBatchRunDtoV3.


        :param settings: The settings of this QualityAssuranceBatchRunDtoV3.  # noqa: E501
        :type: QualityAssuranceRunDtoV3
        """

        self._settings = settings

    @property
    def max_qa_warnings_count(self):
        """Gets the max_qa_warnings_count of this QualityAssuranceBatchRunDtoV3.  # noqa: E501

        Maximum number of QA warnings in result, default: 100. For efficiency reasons QA warnings are processed with minimum segments chunk size 10, therefore slightly more warnings are returned.  # noqa: E501

        :return: The max_qa_warnings_count of this QualityAssuranceBatchRunDtoV3.  # noqa: E501
        :rtype: int
        """
        return self._max_qa_warnings_count

    @max_qa_warnings_count.setter
    def max_qa_warnings_count(self, max_qa_warnings_count):
        """Sets the max_qa_warnings_count of this QualityAssuranceBatchRunDtoV3.

        Maximum number of QA warnings in result, default: 100. For efficiency reasons QA warnings are processed with minimum segments chunk size 10, therefore slightly more warnings are returned.  # noqa: E501

        :param max_qa_warnings_count: The max_qa_warnings_count of this QualityAssuranceBatchRunDtoV3.  # noqa: E501
        :type: int
        """
        if max_qa_warnings_count is not None and max_qa_warnings_count > 1000:  # noqa: E501
            raise ValueError("Invalid value for `max_qa_warnings_count`, must be a value less than or equal to `1000`")  # noqa: E501
        if max_qa_warnings_count is not None and max_qa_warnings_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `max_qa_warnings_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_qa_warnings_count = max_qa_warnings_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(QualityAssuranceBatchRunDtoV3, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QualityAssuranceBatchRunDtoV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
