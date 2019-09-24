# coding: utf-8

"""
    Memsource REST API

    Welcome to Memsource's API documentation. To view our legacy APIs please [visit our documentation](https://wiki.memsource.com/wiki/Memsource_API) and for more information about our new APIs, [visit our blog](https://www.memsource.com/blog/2017/10/24/introducing-rest-apis-qa-with-the-memsource-api-team/).    If you have any questions, please contact [Memsource Support](<mailto:support@memsource.com>).  # noqa: E501

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import memsource_cli
from memsource_cli.api.authentication_api import AuthenticationApi  # noqa: E501
from memsource_cli.rest import ApiException


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = memsource_cli.api.authentication_api.AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login(self):
        """Test case for login

        Login  # noqa: E501
        """
        pass

    def test_login_by_google(self):
        """Test case for login_by_google

        Login with Google  # noqa: E501
        """
        pass

    def test_login_other(self):
        """Test case for login_other

        Login as another user  # noqa: E501
        """
        pass

    def test_login_to_session(self):
        """Test case for login_to_session

        Login to session  # noqa: E501
        """
        pass

    def test_logout(self):
        """Test case for logout

        Logout  # noqa: E501
        """
        pass

    def test_who_am_i(self):
        """Test case for who_am_i

        Who am I  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()