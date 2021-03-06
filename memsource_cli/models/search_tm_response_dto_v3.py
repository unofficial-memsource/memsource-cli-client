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

from memsource_cli.models.search_tm_segment_dto_v3 import SearchTMSegmentDtoV3  # noqa: F401,E501
from memsource_cli.models.search_tm_trans_memory_dto_v3 import SearchTMTransMemoryDtoV3  # noqa: F401,E501


class SearchTMResponseDtoV3(object):
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
        'segment_id': 'str',
        'source': 'SearchTMSegmentDtoV3',
        'translations': 'list[SearchTMSegmentDtoV3]',
        'trans_memory': 'SearchTMTransMemoryDtoV3',
        'gross_score': 'float',
        'score': 'float',
        'sub_segment': 'bool'
    }

    attribute_map = {
        'segment_id': 'segmentId',
        'source': 'source',
        'translations': 'translations',
        'trans_memory': 'transMemory',
        'gross_score': 'grossScore',
        'score': 'score',
        'sub_segment': 'subSegment'
    }

    def __init__(self, segment_id=None, source=None, translations=None, trans_memory=None, gross_score=None, score=None, sub_segment=None):  # noqa: E501
        """SearchTMResponseDtoV3 - a model defined in Swagger"""  # noqa: E501

        self._segment_id = None
        self._source = None
        self._translations = None
        self._trans_memory = None
        self._gross_score = None
        self._score = None
        self._sub_segment = None
        self.discriminator = None

        if segment_id is not None:
            self.segment_id = segment_id
        if source is not None:
            self.source = source
        if translations is not None:
            self.translations = translations
        if trans_memory is not None:
            self.trans_memory = trans_memory
        if gross_score is not None:
            self.gross_score = gross_score
        if score is not None:
            self.score = score
        if sub_segment is not None:
            self.sub_segment = sub_segment

    @property
    def segment_id(self):
        """Gets the segment_id of this SearchTMResponseDtoV3.  # noqa: E501


        :return: The segment_id of this SearchTMResponseDtoV3.  # noqa: E501
        :rtype: str
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """Sets the segment_id of this SearchTMResponseDtoV3.


        :param segment_id: The segment_id of this SearchTMResponseDtoV3.  # noqa: E501
        :type: str
        """

        self._segment_id = segment_id

    @property
    def source(self):
        """Gets the source of this SearchTMResponseDtoV3.  # noqa: E501


        :return: The source of this SearchTMResponseDtoV3.  # noqa: E501
        :rtype: SearchTMSegmentDtoV3
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SearchTMResponseDtoV3.


        :param source: The source of this SearchTMResponseDtoV3.  # noqa: E501
        :type: SearchTMSegmentDtoV3
        """

        self._source = source

    @property
    def translations(self):
        """Gets the translations of this SearchTMResponseDtoV3.  # noqa: E501


        :return: The translations of this SearchTMResponseDtoV3.  # noqa: E501
        :rtype: list[SearchTMSegmentDtoV3]
        """
        return self._translations

    @translations.setter
    def translations(self, translations):
        """Sets the translations of this SearchTMResponseDtoV3.


        :param translations: The translations of this SearchTMResponseDtoV3.  # noqa: E501
        :type: list[SearchTMSegmentDtoV3]
        """

        self._translations = translations

    @property
    def trans_memory(self):
        """Gets the trans_memory of this SearchTMResponseDtoV3.  # noqa: E501


        :return: The trans_memory of this SearchTMResponseDtoV3.  # noqa: E501
        :rtype: SearchTMTransMemoryDtoV3
        """
        return self._trans_memory

    @trans_memory.setter
    def trans_memory(self, trans_memory):
        """Sets the trans_memory of this SearchTMResponseDtoV3.


        :param trans_memory: The trans_memory of this SearchTMResponseDtoV3.  # noqa: E501
        :type: SearchTMTransMemoryDtoV3
        """

        self._trans_memory = trans_memory

    @property
    def gross_score(self):
        """Gets the gross_score of this SearchTMResponseDtoV3.  # noqa: E501


        :return: The gross_score of this SearchTMResponseDtoV3.  # noqa: E501
        :rtype: float
        """
        return self._gross_score

    @gross_score.setter
    def gross_score(self, gross_score):
        """Sets the gross_score of this SearchTMResponseDtoV3.


        :param gross_score: The gross_score of this SearchTMResponseDtoV3.  # noqa: E501
        :type: float
        """

        self._gross_score = gross_score

    @property
    def score(self):
        """Gets the score of this SearchTMResponseDtoV3.  # noqa: E501


        :return: The score of this SearchTMResponseDtoV3.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this SearchTMResponseDtoV3.


        :param score: The score of this SearchTMResponseDtoV3.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def sub_segment(self):
        """Gets the sub_segment of this SearchTMResponseDtoV3.  # noqa: E501


        :return: The sub_segment of this SearchTMResponseDtoV3.  # noqa: E501
        :rtype: bool
        """
        return self._sub_segment

    @sub_segment.setter
    def sub_segment(self, sub_segment):
        """Sets the sub_segment of this SearchTMResponseDtoV3.


        :param sub_segment: The sub_segment of this SearchTMResponseDtoV3.  # noqa: E501
        :type: bool
        """

        self._sub_segment = sub_segment

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
        if issubclass(SearchTMResponseDtoV3, dict):
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
        if not isinstance(other, SearchTMResponseDtoV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
