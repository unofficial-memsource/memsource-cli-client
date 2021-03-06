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

from memsource_cli.models.update_ignored_warning import UpdateIgnoredWarning  # noqa: F401,E501


class UpdateIgnoredSegment(object):
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
        'uid': 'str',
        'warnings': 'list[UpdateIgnoredWarning]'
    }

    attribute_map = {
        'uid': 'uid',
        'warnings': 'warnings'
    }

    def __init__(self, uid=None, warnings=None):  # noqa: E501
        """UpdateIgnoredSegment - a model defined in Swagger"""  # noqa: E501

        self._uid = None
        self._warnings = None
        self.discriminator = None

        self.uid = uid
        self.warnings = warnings

    @property
    def uid(self):
        """Gets the uid of this UpdateIgnoredSegment.  # noqa: E501


        :return: The uid of this UpdateIgnoredSegment.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this UpdateIgnoredSegment.


        :param uid: The uid of this UpdateIgnoredSegment.  # noqa: E501
        :type: str
        """
        if uid is None:
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

    @property
    def warnings(self):
        """Gets the warnings of this UpdateIgnoredSegment.  # noqa: E501


        :return: The warnings of this UpdateIgnoredSegment.  # noqa: E501
        :rtype: list[UpdateIgnoredWarning]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this UpdateIgnoredSegment.


        :param warnings: The warnings of this UpdateIgnoredSegment.  # noqa: E501
        :type: list[UpdateIgnoredWarning]
        """
        if warnings is None:
            raise ValueError("Invalid value for `warnings`, must not be `None`")  # noqa: E501

        self._warnings = warnings

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
        if issubclass(UpdateIgnoredSegment, dict):
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
        if not isinstance(other, UpdateIgnoredSegment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
