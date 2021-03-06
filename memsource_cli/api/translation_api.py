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


class TranslationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def human_translate(self, project_uid, **kwargs):  # noqa: E501
        """Human translate (Gengo or Unbabel)  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.human_translate(project_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_uid: (required)
        :param HumanTranslateJobsDto body:
        :return: AsyncRequestWrapperDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.human_translate_with_http_info(project_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.human_translate_with_http_info(project_uid, **kwargs)  # noqa: E501
            return data

    def human_translate_with_http_info(self, project_uid, **kwargs):  # noqa: E501
        """Human translate (Gengo or Unbabel)  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.human_translate_with_http_info(project_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_uid: (required)
        :param HumanTranslateJobsDto body:
        :return: AsyncRequestWrapperDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_uid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method human_translate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_uid' is set
        if ('project_uid' not in params or
                params['project_uid'] is None):
            raise ValueError("Missing the required parameter `project_uid` when calling `human_translate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_uid' in params:
            path_params['projectUid'] = params['project_uid']  # noqa: E501

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
            '/api2/v1/projects/{projectUid}/jobs/humanTranslate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncRequestWrapperDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def machine_translation_job(self, project_uid, job_uid, **kwargs):  # noqa: E501
        """Translate using machine translation  # noqa: E501

        Configured machine translate settings is used  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.machine_translation_job(project_uid, job_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_uid: (required)
        :param str job_uid: (required)
        :param TranslationRequestDto body:
        :return: MachineTranslateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.machine_translation_job_with_http_info(project_uid, job_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.machine_translation_job_with_http_info(project_uid, job_uid, **kwargs)  # noqa: E501
            return data

    def machine_translation_job_with_http_info(self, project_uid, job_uid, **kwargs):  # noqa: E501
        """Translate using machine translation  # noqa: E501

        Configured machine translate settings is used  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.machine_translation_job_with_http_info(project_uid, job_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_uid: (required)
        :param str job_uid: (required)
        :param TranslationRequestDto body:
        :return: MachineTranslateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_uid', 'job_uid', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method machine_translation_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_uid' is set
        if ('project_uid' not in params or
                params['project_uid'] is None):
            raise ValueError("Missing the required parameter `project_uid` when calling `machine_translation_job`")  # noqa: E501
        # verify the required parameter 'job_uid' is set
        if ('job_uid' not in params or
                params['job_uid'] is None):
            raise ValueError("Missing the required parameter `job_uid` when calling `machine_translation_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_uid' in params:
            path_params['projectUid'] = params['project_uid']  # noqa: E501
        if 'job_uid' in params:
            path_params['jobUid'] = params['job_uid']  # noqa: E501

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
            '/api2/v1/projects/{projectUid}/jobs/{jobUid}/translations/translateWithMachineTranslation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MachineTranslateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pre_translate(self, project_uid, **kwargs):  # noqa: E501
        """Pre-translate job  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pre_translate(project_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_uid: (required)
        :param PreTranslateJobsDto body:
        :return: AsyncRequestWrapperDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pre_translate_with_http_info(project_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.pre_translate_with_http_info(project_uid, **kwargs)  # noqa: E501
            return data

    def pre_translate_with_http_info(self, project_uid, **kwargs):  # noqa: E501
        """Pre-translate job  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pre_translate_with_http_info(project_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_uid: (required)
        :param PreTranslateJobsDto body:
        :return: AsyncRequestWrapperDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_uid', 'body', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pre_translate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_uid' is set
        if ('project_uid' not in params or
                params['project_uid'] is None):
            raise ValueError("Missing the required parameter `project_uid` when calling `pre_translate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_uid' in params:
            path_params['projectUid'] = params['project_uid']  # noqa: E501

        query_params = []
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

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
            '/api2/v1/projects/{projectUid}/jobs/preTranslate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsyncRequestWrapperDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
