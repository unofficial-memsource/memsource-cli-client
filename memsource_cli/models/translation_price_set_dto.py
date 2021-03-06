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

from memsource_cli.models.translation_price_dto import TranslationPriceDto  # noqa: F401,E501


class TranslationPriceSetDto(object):
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
        'source_lang': 'str',
        'target_lang': 'str',
        'minimum_price': 'float',
        'prices': 'list[TranslationPriceDto]'
    }

    attribute_map = {
        'source_lang': 'sourceLang',
        'target_lang': 'targetLang',
        'minimum_price': 'minimumPrice',
        'prices': 'prices'
    }

    def __init__(self, source_lang=None, target_lang=None, minimum_price=None, prices=None):  # noqa: E501
        """TranslationPriceSetDto - a model defined in Swagger"""  # noqa: E501

        self._source_lang = None
        self._target_lang = None
        self._minimum_price = None
        self._prices = None
        self.discriminator = None

        if source_lang is not None:
            self.source_lang = source_lang
        if target_lang is not None:
            self.target_lang = target_lang
        if minimum_price is not None:
            self.minimum_price = minimum_price
        if prices is not None:
            self.prices = prices

    @property
    def source_lang(self):
        """Gets the source_lang of this TranslationPriceSetDto.  # noqa: E501


        :return: The source_lang of this TranslationPriceSetDto.  # noqa: E501
        :rtype: str
        """
        return self._source_lang

    @source_lang.setter
    def source_lang(self, source_lang):
        """Sets the source_lang of this TranslationPriceSetDto.


        :param source_lang: The source_lang of this TranslationPriceSetDto.  # noqa: E501
        :type: str
        """

        self._source_lang = source_lang

    @property
    def target_lang(self):
        """Gets the target_lang of this TranslationPriceSetDto.  # noqa: E501


        :return: The target_lang of this TranslationPriceSetDto.  # noqa: E501
        :rtype: str
        """
        return self._target_lang

    @target_lang.setter
    def target_lang(self, target_lang):
        """Sets the target_lang of this TranslationPriceSetDto.


        :param target_lang: The target_lang of this TranslationPriceSetDto.  # noqa: E501
        :type: str
        """

        self._target_lang = target_lang

    @property
    def minimum_price(self):
        """Gets the minimum_price of this TranslationPriceSetDto.  # noqa: E501


        :return: The minimum_price of this TranslationPriceSetDto.  # noqa: E501
        :rtype: float
        """
        return self._minimum_price

    @minimum_price.setter
    def minimum_price(self, minimum_price):
        """Sets the minimum_price of this TranslationPriceSetDto.


        :param minimum_price: The minimum_price of this TranslationPriceSetDto.  # noqa: E501
        :type: float
        """

        self._minimum_price = minimum_price

    @property
    def prices(self):
        """Gets the prices of this TranslationPriceSetDto.  # noqa: E501


        :return: The prices of this TranslationPriceSetDto.  # noqa: E501
        :rtype: list[TranslationPriceDto]
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """Sets the prices of this TranslationPriceSetDto.


        :param prices: The prices of this TranslationPriceSetDto.  # noqa: E501
        :type: list[TranslationPriceDto]
        """

        self._prices = prices

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
        if issubclass(TranslationPriceSetDto, dict):
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
        if not isinstance(other, TranslationPriceSetDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
