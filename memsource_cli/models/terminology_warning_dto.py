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

from memsource_cli.models.segment_warning import SegmentWarning  # noqa: F401,E501


class TerminologyWarningDto(SegmentWarning):
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
        'missing_terms': 'list[str]',
        'forbidden_terms': 'list[str]'
    }

    attribute_map = {
        'missing_terms': 'missingTerms',
        'forbidden_terms': 'forbiddenTerms'
    }

    def __init__(self, missing_terms=None, forbidden_terms=None):  # noqa: E501
        """TerminologyWarningDto - a model defined in Swagger"""  # noqa: E501

        self._missing_terms = None
        self._forbidden_terms = None
        self.discriminator = None

        if missing_terms is not None:
            self.missing_terms = missing_terms
        if forbidden_terms is not None:
            self.forbidden_terms = forbidden_terms

    @property
    def missing_terms(self):
        """Gets the missing_terms of this TerminologyWarningDto.  # noqa: E501


        :return: The missing_terms of this TerminologyWarningDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._missing_terms

    @missing_terms.setter
    def missing_terms(self, missing_terms):
        """Sets the missing_terms of this TerminologyWarningDto.


        :param missing_terms: The missing_terms of this TerminologyWarningDto.  # noqa: E501
        :type: list[str]
        """

        self._missing_terms = missing_terms

    @property
    def forbidden_terms(self):
        """Gets the forbidden_terms of this TerminologyWarningDto.  # noqa: E501


        :return: The forbidden_terms of this TerminologyWarningDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._forbidden_terms

    @forbidden_terms.setter
    def forbidden_terms(self, forbidden_terms):
        """Sets the forbidden_terms of this TerminologyWarningDto.


        :param forbidden_terms: The forbidden_terms of this TerminologyWarningDto.  # noqa: E501
        :type: list[str]
        """

        self._forbidden_terms = forbidden_terms

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
        if issubclass(TerminologyWarningDto, dict):
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
        if not isinstance(other, TerminologyWarningDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
