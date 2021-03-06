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

from memsource_cli.models.translation_price_set_dto import TranslationPriceSetDto  # noqa: F401,E501


class TranslationPriceListDto(object):
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
        'id': 'str',
        'date_created': 'datetime',
        'name': 'str',
        'currency_code': 'str',
        'billing_unit': 'str',
        'price_sets': 'list[TranslationPriceSetDto]'
    }

    attribute_map = {
        'id': 'id',
        'date_created': 'dateCreated',
        'name': 'name',
        'currency_code': 'currencyCode',
        'billing_unit': 'billingUnit',
        'price_sets': 'priceSets'
    }

    def __init__(self, id=None, date_created=None, name=None, currency_code=None, billing_unit=None, price_sets=None):  # noqa: E501
        """TranslationPriceListDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._date_created = None
        self._name = None
        self._currency_code = None
        self._billing_unit = None
        self._price_sets = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if date_created is not None:
            self.date_created = date_created
        if name is not None:
            self.name = name
        if currency_code is not None:
            self.currency_code = currency_code
        if billing_unit is not None:
            self.billing_unit = billing_unit
        if price_sets is not None:
            self.price_sets = price_sets

    @property
    def id(self):
        """Gets the id of this TranslationPriceListDto.  # noqa: E501


        :return: The id of this TranslationPriceListDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TranslationPriceListDto.


        :param id: The id of this TranslationPriceListDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this TranslationPriceListDto.  # noqa: E501


        :return: The date_created of this TranslationPriceListDto.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this TranslationPriceListDto.


        :param date_created: The date_created of this TranslationPriceListDto.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def name(self):
        """Gets the name of this TranslationPriceListDto.  # noqa: E501


        :return: The name of this TranslationPriceListDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TranslationPriceListDto.


        :param name: The name of this TranslationPriceListDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def currency_code(self):
        """Gets the currency_code of this TranslationPriceListDto.  # noqa: E501


        :return: The currency_code of this TranslationPriceListDto.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this TranslationPriceListDto.


        :param currency_code: The currency_code of this TranslationPriceListDto.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def billing_unit(self):
        """Gets the billing_unit of this TranslationPriceListDto.  # noqa: E501


        :return: The billing_unit of this TranslationPriceListDto.  # noqa: E501
        :rtype: str
        """
        return self._billing_unit

    @billing_unit.setter
    def billing_unit(self, billing_unit):
        """Sets the billing_unit of this TranslationPriceListDto.


        :param billing_unit: The billing_unit of this TranslationPriceListDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Character", "Word", "Page"]  # noqa: E501
        if billing_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_unit, allowed_values)
            )

        self._billing_unit = billing_unit

    @property
    def price_sets(self):
        """Gets the price_sets of this TranslationPriceListDto.  # noqa: E501


        :return: The price_sets of this TranslationPriceListDto.  # noqa: E501
        :rtype: list[TranslationPriceSetDto]
        """
        return self._price_sets

    @price_sets.setter
    def price_sets(self, price_sets):
        """Sets the price_sets of this TranslationPriceListDto.


        :param price_sets: The price_sets of this TranslationPriceListDto.  # noqa: E501
        :type: list[TranslationPriceSetDto]
        """

        self._price_sets = price_sets

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
        if issubclass(TranslationPriceListDto, dict):
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
        if not isinstance(other, TranslationPriceListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
