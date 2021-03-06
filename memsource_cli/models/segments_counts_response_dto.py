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

from memsource_cli.models.previous_workflow_dto import PreviousWorkflowDto  # noqa: F401,E501
from memsource_cli.models.segments_counts_dto import SegmentsCountsDto  # noqa: F401,E501


class SegmentsCountsResponseDto(object):
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
        'job_part_uid': 'str',
        'counts': 'SegmentsCountsDto',
        'previous_workflow': 'PreviousWorkflowDto'
    }

    attribute_map = {
        'job_part_uid': 'jobPartUid',
        'counts': 'counts',
        'previous_workflow': 'previousWorkflow'
    }

    def __init__(self, job_part_uid=None, counts=None, previous_workflow=None):  # noqa: E501
        """SegmentsCountsResponseDto - a model defined in Swagger"""  # noqa: E501

        self._job_part_uid = None
        self._counts = None
        self._previous_workflow = None
        self.discriminator = None

        if job_part_uid is not None:
            self.job_part_uid = job_part_uid
        if counts is not None:
            self.counts = counts
        if previous_workflow is not None:
            self.previous_workflow = previous_workflow

    @property
    def job_part_uid(self):
        """Gets the job_part_uid of this SegmentsCountsResponseDto.  # noqa: E501


        :return: The job_part_uid of this SegmentsCountsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._job_part_uid

    @job_part_uid.setter
    def job_part_uid(self, job_part_uid):
        """Sets the job_part_uid of this SegmentsCountsResponseDto.


        :param job_part_uid: The job_part_uid of this SegmentsCountsResponseDto.  # noqa: E501
        :type: str
        """

        self._job_part_uid = job_part_uid

    @property
    def counts(self):
        """Gets the counts of this SegmentsCountsResponseDto.  # noqa: E501


        :return: The counts of this SegmentsCountsResponseDto.  # noqa: E501
        :rtype: SegmentsCountsDto
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        """Sets the counts of this SegmentsCountsResponseDto.


        :param counts: The counts of this SegmentsCountsResponseDto.  # noqa: E501
        :type: SegmentsCountsDto
        """

        self._counts = counts

    @property
    def previous_workflow(self):
        """Gets the previous_workflow of this SegmentsCountsResponseDto.  # noqa: E501


        :return: The previous_workflow of this SegmentsCountsResponseDto.  # noqa: E501
        :rtype: PreviousWorkflowDto
        """
        return self._previous_workflow

    @previous_workflow.setter
    def previous_workflow(self, previous_workflow):
        """Sets the previous_workflow of this SegmentsCountsResponseDto.


        :param previous_workflow: The previous_workflow of this SegmentsCountsResponseDto.  # noqa: E501
        :type: PreviousWorkflowDto
        """

        self._previous_workflow = previous_workflow

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
        if issubclass(SegmentsCountsResponseDto, dict):
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
        if not isinstance(other, SegmentsCountsResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
