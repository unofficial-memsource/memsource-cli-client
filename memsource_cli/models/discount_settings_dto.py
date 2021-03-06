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


class DiscountSettingsDto(object):
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
        'repetition': 'float',
        'tm101': 'float',
        'tm100': 'float',
        'tm95': 'float',
        'tm85': 'float',
        'tm75': 'float',
        'tm50': 'float',
        'tm0': 'float',
        'mt100': 'float',
        'mt95': 'float',
        'mt85': 'float',
        'mt75': 'float',
        'mt50': 'float',
        'mt0': 'float',
        'nt100': 'float',
        'nt99': 'float',
        'nt85': 'float',
        'nt75': 'float',
        'nt50': 'float',
        'nt0': 'float'
    }

    attribute_map = {
        'repetition': 'repetition',
        'tm101': 'tm101',
        'tm100': 'tm100',
        'tm95': 'tm95',
        'tm85': 'tm85',
        'tm75': 'tm75',
        'tm50': 'tm50',
        'tm0': 'tm0',
        'mt100': 'mt100',
        'mt95': 'mt95',
        'mt85': 'mt85',
        'mt75': 'mt75',
        'mt50': 'mt50',
        'mt0': 'mt0',
        'nt100': 'nt100',
        'nt99': 'nt99',
        'nt85': 'nt85',
        'nt75': 'nt75',
        'nt50': 'nt50',
        'nt0': 'nt0'
    }

    def __init__(self, repetition=None, tm101=None, tm100=None, tm95=None, tm85=None, tm75=None, tm50=None, tm0=None, mt100=None, mt95=None, mt85=None, mt75=None, mt50=None, mt0=None, nt100=None, nt99=None, nt85=None, nt75=None, nt50=None, nt0=None):  # noqa: E501
        """DiscountSettingsDto - a model defined in Swagger"""  # noqa: E501

        self._repetition = None
        self._tm101 = None
        self._tm100 = None
        self._tm95 = None
        self._tm85 = None
        self._tm75 = None
        self._tm50 = None
        self._tm0 = None
        self._mt100 = None
        self._mt95 = None
        self._mt85 = None
        self._mt75 = None
        self._mt50 = None
        self._mt0 = None
        self._nt100 = None
        self._nt99 = None
        self._nt85 = None
        self._nt75 = None
        self._nt50 = None
        self._nt0 = None
        self.discriminator = None

        if repetition is not None:
            self.repetition = repetition
        if tm101 is not None:
            self.tm101 = tm101
        if tm100 is not None:
            self.tm100 = tm100
        if tm95 is not None:
            self.tm95 = tm95
        if tm85 is not None:
            self.tm85 = tm85
        if tm75 is not None:
            self.tm75 = tm75
        if tm50 is not None:
            self.tm50 = tm50
        if tm0 is not None:
            self.tm0 = tm0
        if mt100 is not None:
            self.mt100 = mt100
        if mt95 is not None:
            self.mt95 = mt95
        if mt85 is not None:
            self.mt85 = mt85
        if mt75 is not None:
            self.mt75 = mt75
        if mt50 is not None:
            self.mt50 = mt50
        if mt0 is not None:
            self.mt0 = mt0
        if nt100 is not None:
            self.nt100 = nt100
        if nt99 is not None:
            self.nt99 = nt99
        if nt85 is not None:
            self.nt85 = nt85
        if nt75 is not None:
            self.nt75 = nt75
        if nt50 is not None:
            self.nt50 = nt50
        if nt0 is not None:
            self.nt0 = nt0

    @property
    def repetition(self):
        """Gets the repetition of this DiscountSettingsDto.  # noqa: E501


        :return: The repetition of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._repetition

    @repetition.setter
    def repetition(self, repetition):
        """Sets the repetition of this DiscountSettingsDto.


        :param repetition: The repetition of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._repetition = repetition

    @property
    def tm101(self):
        """Gets the tm101 of this DiscountSettingsDto.  # noqa: E501


        :return: The tm101 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._tm101

    @tm101.setter
    def tm101(self, tm101):
        """Sets the tm101 of this DiscountSettingsDto.


        :param tm101: The tm101 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._tm101 = tm101

    @property
    def tm100(self):
        """Gets the tm100 of this DiscountSettingsDto.  # noqa: E501


        :return: The tm100 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._tm100

    @tm100.setter
    def tm100(self, tm100):
        """Sets the tm100 of this DiscountSettingsDto.


        :param tm100: The tm100 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._tm100 = tm100

    @property
    def tm95(self):
        """Gets the tm95 of this DiscountSettingsDto.  # noqa: E501


        :return: The tm95 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._tm95

    @tm95.setter
    def tm95(self, tm95):
        """Sets the tm95 of this DiscountSettingsDto.


        :param tm95: The tm95 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._tm95 = tm95

    @property
    def tm85(self):
        """Gets the tm85 of this DiscountSettingsDto.  # noqa: E501


        :return: The tm85 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._tm85

    @tm85.setter
    def tm85(self, tm85):
        """Sets the tm85 of this DiscountSettingsDto.


        :param tm85: The tm85 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._tm85 = tm85

    @property
    def tm75(self):
        """Gets the tm75 of this DiscountSettingsDto.  # noqa: E501


        :return: The tm75 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._tm75

    @tm75.setter
    def tm75(self, tm75):
        """Sets the tm75 of this DiscountSettingsDto.


        :param tm75: The tm75 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._tm75 = tm75

    @property
    def tm50(self):
        """Gets the tm50 of this DiscountSettingsDto.  # noqa: E501


        :return: The tm50 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._tm50

    @tm50.setter
    def tm50(self, tm50):
        """Sets the tm50 of this DiscountSettingsDto.


        :param tm50: The tm50 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._tm50 = tm50

    @property
    def tm0(self):
        """Gets the tm0 of this DiscountSettingsDto.  # noqa: E501


        :return: The tm0 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._tm0

    @tm0.setter
    def tm0(self, tm0):
        """Sets the tm0 of this DiscountSettingsDto.


        :param tm0: The tm0 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._tm0 = tm0

    @property
    def mt100(self):
        """Gets the mt100 of this DiscountSettingsDto.  # noqa: E501


        :return: The mt100 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._mt100

    @mt100.setter
    def mt100(self, mt100):
        """Sets the mt100 of this DiscountSettingsDto.


        :param mt100: The mt100 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._mt100 = mt100

    @property
    def mt95(self):
        """Gets the mt95 of this DiscountSettingsDto.  # noqa: E501


        :return: The mt95 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._mt95

    @mt95.setter
    def mt95(self, mt95):
        """Sets the mt95 of this DiscountSettingsDto.


        :param mt95: The mt95 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._mt95 = mt95

    @property
    def mt85(self):
        """Gets the mt85 of this DiscountSettingsDto.  # noqa: E501


        :return: The mt85 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._mt85

    @mt85.setter
    def mt85(self, mt85):
        """Sets the mt85 of this DiscountSettingsDto.


        :param mt85: The mt85 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._mt85 = mt85

    @property
    def mt75(self):
        """Gets the mt75 of this DiscountSettingsDto.  # noqa: E501


        :return: The mt75 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._mt75

    @mt75.setter
    def mt75(self, mt75):
        """Sets the mt75 of this DiscountSettingsDto.


        :param mt75: The mt75 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._mt75 = mt75

    @property
    def mt50(self):
        """Gets the mt50 of this DiscountSettingsDto.  # noqa: E501


        :return: The mt50 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._mt50

    @mt50.setter
    def mt50(self, mt50):
        """Sets the mt50 of this DiscountSettingsDto.


        :param mt50: The mt50 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._mt50 = mt50

    @property
    def mt0(self):
        """Gets the mt0 of this DiscountSettingsDto.  # noqa: E501


        :return: The mt0 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._mt0

    @mt0.setter
    def mt0(self, mt0):
        """Sets the mt0 of this DiscountSettingsDto.


        :param mt0: The mt0 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._mt0 = mt0

    @property
    def nt100(self):
        """Gets the nt100 of this DiscountSettingsDto.  # noqa: E501


        :return: The nt100 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._nt100

    @nt100.setter
    def nt100(self, nt100):
        """Sets the nt100 of this DiscountSettingsDto.


        :param nt100: The nt100 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._nt100 = nt100

    @property
    def nt99(self):
        """Gets the nt99 of this DiscountSettingsDto.  # noqa: E501


        :return: The nt99 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._nt99

    @nt99.setter
    def nt99(self, nt99):
        """Sets the nt99 of this DiscountSettingsDto.


        :param nt99: The nt99 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._nt99 = nt99

    @property
    def nt85(self):
        """Gets the nt85 of this DiscountSettingsDto.  # noqa: E501


        :return: The nt85 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._nt85

    @nt85.setter
    def nt85(self, nt85):
        """Sets the nt85 of this DiscountSettingsDto.


        :param nt85: The nt85 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._nt85 = nt85

    @property
    def nt75(self):
        """Gets the nt75 of this DiscountSettingsDto.  # noqa: E501


        :return: The nt75 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._nt75

    @nt75.setter
    def nt75(self, nt75):
        """Sets the nt75 of this DiscountSettingsDto.


        :param nt75: The nt75 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._nt75 = nt75

    @property
    def nt50(self):
        """Gets the nt50 of this DiscountSettingsDto.  # noqa: E501


        :return: The nt50 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._nt50

    @nt50.setter
    def nt50(self, nt50):
        """Sets the nt50 of this DiscountSettingsDto.


        :param nt50: The nt50 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._nt50 = nt50

    @property
    def nt0(self):
        """Gets the nt0 of this DiscountSettingsDto.  # noqa: E501


        :return: The nt0 of this DiscountSettingsDto.  # noqa: E501
        :rtype: float
        """
        return self._nt0

    @nt0.setter
    def nt0(self, nt0):
        """Sets the nt0 of this DiscountSettingsDto.


        :param nt0: The nt0 of this DiscountSettingsDto.  # noqa: E501
        :type: float
        """

        self._nt0 = nt0

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
        if issubclass(DiscountSettingsDto, dict):
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
        if not isinstance(other, DiscountSettingsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
