# coding: utf-8

"""
    Memsource REST API

    Welcome to Memsource's API documentation.    Please visit our [help center](https://help.memsource.com/hc/en-us/sections/360004205139-Memsource-REST-API) or [blog](https://www.memsource.com/blog/2017/10/24/introducing-rest-apis-qa-with-the-memsource-api-team) for more information about the REST APIs.    To view our legacy APIs that will be deprecated in September 2020, please visit our [help center](https://help.memsource.com/hc/en-us/sections/115000918411-Memsource-Legacy-API).    If you have any questions, please contact [Memsource Support](https://get-help.memsource.com).    Depending on [authentication](#operation/login) style, use either the `Bearer <OAuthToken>` or `ApiToken <ApiToken>` in the `Authorization` header.  # noqa: E501

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class JobUpdateSourceResponseDto(object):
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
        'async_request': 'AsyncRequestReference',
        'jobs': 'list[JobPartUpdateSourceDto]'
    }

    attribute_map = {
        'async_request': 'asyncRequest',
        'jobs': 'jobs'
    }

    def __init__(self, async_request=None, jobs=None):  # noqa: E501
        """JobUpdateSourceResponseDto - a model defined in Swagger"""  # noqa: E501

        self._async_request = None
        self._jobs = None
        self.discriminator = None

        if async_request is not None:
            self.async_request = async_request
        if jobs is not None:
            self.jobs = jobs

    @property
    def async_request(self):
        """Gets the async_request of this JobUpdateSourceResponseDto.  # noqa: E501


        :return: The async_request of this JobUpdateSourceResponseDto.  # noqa: E501
        :rtype: AsyncRequestReference
        """
        return self._async_request

    @async_request.setter
    def async_request(self, async_request):
        """Sets the async_request of this JobUpdateSourceResponseDto.


        :param async_request: The async_request of this JobUpdateSourceResponseDto.  # noqa: E501
        :type: AsyncRequestReference
        """

        self._async_request = async_request

    @property
    def jobs(self):
        """Gets the jobs of this JobUpdateSourceResponseDto.  # noqa: E501


        :return: The jobs of this JobUpdateSourceResponseDto.  # noqa: E501
        :rtype: list[JobPartUpdateSourceDto]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this JobUpdateSourceResponseDto.


        :param jobs: The jobs of this JobUpdateSourceResponseDto.  # noqa: E501
        :type: list[JobPartUpdateSourceDto]
        """

        self._jobs = jobs

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
        if issubclass(JobUpdateSourceResponseDto, dict):
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
        if not isinstance(other, JobUpdateSourceResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
