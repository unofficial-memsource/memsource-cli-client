# coding: utf-8

"""
    Memsource REST API

    Welcome to Memsource's API documentation. To view our legacy APIs please [visit our documentation](https://wiki.memsource.com/wiki/Memsource_API) and for more information about our new APIs, [visit our blog](https://www.memsource.com/blog/2017/10/24/introducing-rest-apis-qa-with-the-memsource-api-team/).    If you have any questions, please contact [Memsource Support](<mailto:support@memsource.com>).  # noqa: E501

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from memsource_cli.api_client import ApiClient


class BusinessUnitApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_business_unit(self, **kwargs):  # noqa: E501
        """Create business unit  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_business_unit(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BusinessUnitEditDto body:
        :return: BusinessUnitDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_business_unit_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_business_unit_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_business_unit_with_http_info(self, **kwargs):  # noqa: E501
        """Create business unit  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_business_unit_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BusinessUnitEditDto body:
        :return: BusinessUnitDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_business_unit" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api2/v1/businessUnits', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BusinessUnitDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_business_unit(self, business_unit_id, **kwargs):  # noqa: E501
        """Delete business unit  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_business_unit(business_unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int business_unit_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_business_unit_with_http_info(business_unit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_business_unit_with_http_info(business_unit_id, **kwargs)  # noqa: E501
            return data

    def delete_business_unit_with_http_info(self, business_unit_id, **kwargs):  # noqa: E501
        """Delete business unit  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_business_unit_with_http_info(business_unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int business_unit_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_business_unit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params or
                params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `delete_business_unit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api2/v1/businessUnits/{businessUnitId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_business_unit(self, business_unit_id, **kwargs):  # noqa: E501
        """Get business unit  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_business_unit(business_unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int business_unit_id: (required)
        :return: BusinessUnitDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_business_unit_with_http_info(business_unit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_business_unit_with_http_info(business_unit_id, **kwargs)  # noqa: E501
            return data

    def get_business_unit_with_http_info(self, business_unit_id, **kwargs):  # noqa: E501
        """Get business unit  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_business_unit_with_http_info(business_unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int business_unit_id: (required)
        :return: BusinessUnitDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_business_unit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params or
                params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `get_business_unit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api2/v1/businessUnits/{businessUnitId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BusinessUnitDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_business_units(self, **kwargs):  # noqa: E501
        """List business units  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_business_units(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Unique name of the business unit
        :param int page_number: Page number, starting with 0, default 0
        :param int page_size: Page size, accepts values between 1 and 50, default 50
        :return: PageDtoBusinessUnitDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_business_units_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_business_units_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_business_units_with_http_info(self, **kwargs):  # noqa: E501
        """List business units  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_business_units_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Unique name of the business unit
        :param int page_number: Page number, starting with 0, default 0
        :param int page_size: Page size, accepts values between 1 and 50, default 50
        :return: PageDtoBusinessUnitDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_business_units" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_number' in params and params['page_number'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_number` when calling `list_business_units`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_size' in params and params['page_size'] > 50:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `list_business_units`, must be a value less than or equal to `50`")  # noqa: E501
        if 'page_size' in params and params['page_size'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `list_business_units`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('pageNumber', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api2/v1/businessUnits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDtoBusinessUnitDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_business_unit(self, business_unit_id, **kwargs):  # noqa: E501
        """Edit business unit  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_business_unit(business_unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int business_unit_id: (required)
        :param BusinessUnitEditDto body:
        :return: BusinessUnitDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_business_unit_with_http_info(business_unit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_business_unit_with_http_info(business_unit_id, **kwargs)  # noqa: E501
            return data

    def update_business_unit_with_http_info(self, business_unit_id, **kwargs):  # noqa: E501
        """Edit business unit  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_business_unit_with_http_info(business_unit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int business_unit_id: (required)
        :param BusinessUnitEditDto body:
        :return: BusinessUnitDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['business_unit_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_business_unit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'business_unit_id' is set
        if ('business_unit_id' not in params or
                params['business_unit_id'] is None):
            raise ValueError("Missing the required parameter `business_unit_id` when calling `update_business_unit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'business_unit_id' in params:
            path_params['businessUnitId'] = params['business_unit_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api2/v1/businessUnits/{businessUnitId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BusinessUnitDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
