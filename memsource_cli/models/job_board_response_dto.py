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

from memsource_cli.models.user_reference import UserReference  # noqa: F401,E501


class JobBoardResponseDto(object):
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
        'created_by': 'UserReference',
        'date_created': 'datetime',
        'name': 'str',
        'email': 'str',
        'sample_translation': 'str',
        'word_rate': 'float',
        'profile_url': 'str',
        'note': 'str'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'date_created': 'dateCreated',
        'name': 'name',
        'email': 'email',
        'sample_translation': 'sampleTranslation',
        'word_rate': 'wordRate',
        'profile_url': 'profileUrl',
        'note': 'note'
    }

    def __init__(self, created_by=None, date_created=None, name=None, email=None, sample_translation=None, word_rate=None, profile_url=None, note=None):  # noqa: E501
        """JobBoardResponseDto - a model defined in Swagger"""  # noqa: E501

        self._created_by = None
        self._date_created = None
        self._name = None
        self._email = None
        self._sample_translation = None
        self._word_rate = None
        self._profile_url = None
        self._note = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        if date_created is not None:
            self.date_created = date_created
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if sample_translation is not None:
            self.sample_translation = sample_translation
        if word_rate is not None:
            self.word_rate = word_rate
        if profile_url is not None:
            self.profile_url = profile_url
        if note is not None:
            self.note = note

    @property
    def created_by(self):
        """Gets the created_by of this JobBoardResponseDto.  # noqa: E501


        :return: The created_by of this JobBoardResponseDto.  # noqa: E501
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this JobBoardResponseDto.


        :param created_by: The created_by of this JobBoardResponseDto.  # noqa: E501
        :type: UserReference
        """

        self._created_by = created_by

    @property
    def date_created(self):
        """Gets the date_created of this JobBoardResponseDto.  # noqa: E501


        :return: The date_created of this JobBoardResponseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this JobBoardResponseDto.


        :param date_created: The date_created of this JobBoardResponseDto.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def name(self):
        """Gets the name of this JobBoardResponseDto.  # noqa: E501


        :return: The name of this JobBoardResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobBoardResponseDto.


        :param name: The name of this JobBoardResponseDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this JobBoardResponseDto.  # noqa: E501


        :return: The email of this JobBoardResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this JobBoardResponseDto.


        :param email: The email of this JobBoardResponseDto.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def sample_translation(self):
        """Gets the sample_translation of this JobBoardResponseDto.  # noqa: E501


        :return: The sample_translation of this JobBoardResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._sample_translation

    @sample_translation.setter
    def sample_translation(self, sample_translation):
        """Sets the sample_translation of this JobBoardResponseDto.


        :param sample_translation: The sample_translation of this JobBoardResponseDto.  # noqa: E501
        :type: str
        """

        self._sample_translation = sample_translation

    @property
    def word_rate(self):
        """Gets the word_rate of this JobBoardResponseDto.  # noqa: E501


        :return: The word_rate of this JobBoardResponseDto.  # noqa: E501
        :rtype: float
        """
        return self._word_rate

    @word_rate.setter
    def word_rate(self, word_rate):
        """Sets the word_rate of this JobBoardResponseDto.


        :param word_rate: The word_rate of this JobBoardResponseDto.  # noqa: E501
        :type: float
        """

        self._word_rate = word_rate

    @property
    def profile_url(self):
        """Gets the profile_url of this JobBoardResponseDto.  # noqa: E501


        :return: The profile_url of this JobBoardResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._profile_url

    @profile_url.setter
    def profile_url(self, profile_url):
        """Sets the profile_url of this JobBoardResponseDto.


        :param profile_url: The profile_url of this JobBoardResponseDto.  # noqa: E501
        :type: str
        """

        self._profile_url = profile_url

    @property
    def note(self):
        """Gets the note of this JobBoardResponseDto.  # noqa: E501


        :return: The note of this JobBoardResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this JobBoardResponseDto.


        :param note: The note of this JobBoardResponseDto.  # noqa: E501
        :type: str
        """

        self._note = note

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
        if issubclass(JobBoardResponseDto, dict):
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
        if not isinstance(other, JobBoardResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
