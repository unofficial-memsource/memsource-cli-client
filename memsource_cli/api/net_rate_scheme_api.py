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


class NetRateSchemeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_discount_scheme(self, **kwargs):  # noqa: E501
        """Create net rate scheme  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_discount_scheme(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DiscountSchemeCreateDto body:
        :return: NetRateScheme
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_discount_scheme_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_discount_scheme_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_discount_scheme_with_http_info(self, **kwargs):  # noqa: E501
        """Create net rate scheme  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_discount_scheme_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DiscountSchemeCreateDto body:
        :return: NetRateScheme
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
                    " to method create_discount_scheme" % key
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
            '/api2/v1/netRateSchemes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NetRateScheme',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_discount_scheme(self, net_rate_scheme_id, **kwargs):  # noqa: E501
        """Get net rate scheme  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_discount_scheme(net_rate_scheme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int net_rate_scheme_id: (required)
        :return: NetRateScheme
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_discount_scheme_with_http_info(net_rate_scheme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_discount_scheme_with_http_info(net_rate_scheme_id, **kwargs)  # noqa: E501
            return data

    def get_discount_scheme_with_http_info(self, net_rate_scheme_id, **kwargs):  # noqa: E501
        """Get net rate scheme  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_discount_scheme_with_http_info(net_rate_scheme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int net_rate_scheme_id: (required)
        :return: NetRateScheme
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['net_rate_scheme_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_discount_scheme" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'net_rate_scheme_id' is set
        if ('net_rate_scheme_id' not in params or
                params['net_rate_scheme_id'] is None):
            raise ValueError("Missing the required parameter `net_rate_scheme_id` when calling `get_discount_scheme`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'net_rate_scheme_id' in params:
            path_params['netRateSchemeId'] = params['net_rate_scheme_id']  # noqa: E501

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
            '/api2/v1/netRateSchemes/{netRateSchemeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NetRateScheme',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_discount_scheme_workflow_step(self, net_rate_scheme_id, net_rate_scheme_workflow_step_id, **kwargs):  # noqa: E501
        """Get scheme for workflow step  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_discount_scheme_workflow_step(net_rate_scheme_id, net_rate_scheme_workflow_step_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int net_rate_scheme_id: (required)
        :param int net_rate_scheme_workflow_step_id: (required)
        :return: NetRateSchemeWorkflowStep
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_discount_scheme_workflow_step_with_http_info(net_rate_scheme_id, net_rate_scheme_workflow_step_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_discount_scheme_workflow_step_with_http_info(net_rate_scheme_id, net_rate_scheme_workflow_step_id, **kwargs)  # noqa: E501
            return data

    def get_discount_scheme_workflow_step_with_http_info(self, net_rate_scheme_id, net_rate_scheme_workflow_step_id, **kwargs):  # noqa: E501
        """Get scheme for workflow step  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_discount_scheme_workflow_step_with_http_info(net_rate_scheme_id, net_rate_scheme_workflow_step_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int net_rate_scheme_id: (required)
        :param int net_rate_scheme_workflow_step_id: (required)
        :return: NetRateSchemeWorkflowStep
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['net_rate_scheme_id', 'net_rate_scheme_workflow_step_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_discount_scheme_workflow_step" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'net_rate_scheme_id' is set
        if ('net_rate_scheme_id' not in params or
                params['net_rate_scheme_id'] is None):
            raise ValueError("Missing the required parameter `net_rate_scheme_id` when calling `get_discount_scheme_workflow_step`")  # noqa: E501
        # verify the required parameter 'net_rate_scheme_workflow_step_id' is set
        if ('net_rate_scheme_workflow_step_id' not in params or
                params['net_rate_scheme_workflow_step_id'] is None):
            raise ValueError("Missing the required parameter `net_rate_scheme_workflow_step_id` when calling `get_discount_scheme_workflow_step`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'net_rate_scheme_id' in params:
            path_params['netRateSchemeId'] = params['net_rate_scheme_id']  # noqa: E501
        if 'net_rate_scheme_workflow_step_id' in params:
            path_params['netRateSchemeWorkflowStepId'] = params['net_rate_scheme_workflow_step_id']  # noqa: E501

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
            '/api2/v1/netRateSchemes/{netRateSchemeId}/workflowStepNetSchemes/{netRateSchemeWorkflowStepId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NetRateSchemeWorkflowStep',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_discount_scheme_workflow_steps(self, net_rate_scheme_id, **kwargs):  # noqa: E501
        """List schemes for workflow step  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_discount_scheme_workflow_steps(net_rate_scheme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int net_rate_scheme_id: (required)
        :param int page_number:
        :param int page_size: Page size, accepts values between 1 and 50, default 50
        :return: PageDtoNetRateSchemeWorkflowStepReference
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_discount_scheme_workflow_steps_with_http_info(net_rate_scheme_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_discount_scheme_workflow_steps_with_http_info(net_rate_scheme_id, **kwargs)  # noqa: E501
            return data

    def get_discount_scheme_workflow_steps_with_http_info(self, net_rate_scheme_id, **kwargs):  # noqa: E501
        """List schemes for workflow step  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_discount_scheme_workflow_steps_with_http_info(net_rate_scheme_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int net_rate_scheme_id: (required)
        :param int page_number:
        :param int page_size: Page size, accepts values between 1 and 50, default 50
        :return: PageDtoNetRateSchemeWorkflowStepReference
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['net_rate_scheme_id', 'page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_discount_scheme_workflow_steps" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'net_rate_scheme_id' is set
        if ('net_rate_scheme_id' not in params or
                params['net_rate_scheme_id'] is None):
            raise ValueError("Missing the required parameter `net_rate_scheme_id` when calling `get_discount_scheme_workflow_steps`")  # noqa: E501

        if 'page_number' in params and params['page_number'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_number` when calling `get_discount_scheme_workflow_steps`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_size' in params and params['page_size'] > 50:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_discount_scheme_workflow_steps`, must be a value less than or equal to `50`")  # noqa: E501
        if 'page_size' in params and params['page_size'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_discount_scheme_workflow_steps`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'net_rate_scheme_id' in params:
            path_params['netRateSchemeId'] = params['net_rate_scheme_id']  # noqa: E501

        query_params = []
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
            '/api2/v1/netRateSchemes/{netRateSchemeId}/workflowStepNetSchemes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDtoNetRateSchemeWorkflowStepReference',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_discount_schemes(self, **kwargs):  # noqa: E501
        """List net rate schemes  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_discount_schemes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number:
        :param int page_size: Page size, accepts values between 1 and 50, default 50
        :return: PageDtoNetRateSchemeReference
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_discount_schemes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_discount_schemes_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_discount_schemes_with_http_info(self, **kwargs):  # noqa: E501
        """List net rate schemes  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_discount_schemes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_number:
        :param int page_size: Page size, accepts values between 1 and 50, default 50
        :return: PageDtoNetRateSchemeReference
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_number', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_discount_schemes" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_number' in params and params['page_number'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_number` when calling `get_discount_schemes`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_size' in params and params['page_size'] > 50:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_discount_schemes`, must be a value less than or equal to `50`")  # noqa: E501
        if 'page_size' in params and params['page_size'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_discount_schemes`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/api2/v1/netRateSchemes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDtoNetRateSchemeReference',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
