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

from memsource_cli.models.qa_check_dto_v2 import QACheckDtoV2  # noqa: F401,E501


class VOID(QACheckDtoV2):
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
        'ignorable': 'bool',
        'enabled': 'bool'
    }

    attribute_map = {
        'ignorable': 'ignorable',
        'enabled': 'enabled'
    }

    def __init__(self, ignorable=None, enabled=None):  # noqa: E501
        """VOID - a model defined in Swagger"""  # noqa: E501

        self._ignorable = None
        self._enabled = None
        self.discriminator = None

        if ignorable is not None:
            self.ignorable = ignorable
        if enabled is not None:
            self.enabled = enabled

    @property
    def ignorable(self):
        """Gets the ignorable of this VOID.  # noqa: E501


        :return: The ignorable of this VOID.  # noqa: E501
        :rtype: bool
        """
        return self._ignorable

    @ignorable.setter
    def ignorable(self, ignorable):
        """Sets the ignorable of this VOID.


        :param ignorable: The ignorable of this VOID.  # noqa: E501
        :type: bool
        """

        self._ignorable = ignorable

    @property
    def enabled(self):
        """Gets the enabled of this VOID.  # noqa: E501


        :return: The enabled of this VOID.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this VOID.


        :param enabled: The enabled of this VOID.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if issubclass(VOID, dict):
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
        if not isinstance(other, VOID):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
