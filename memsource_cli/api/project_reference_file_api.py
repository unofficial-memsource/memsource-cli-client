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


class ProjectReferenceFileApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_note_ref(self, project_uid, **kwargs):  # noqa: E501
        """Create project reference file  # noqa: E501

        Accepts application/octet-stream or application/json.<br>                                                                     <b>application/json</b> - Note will be converted to .txt.<br>                                                                     <b>application/octet-stream</b> - Content-Disposition header is required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_note_ref(project_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_uid: (required)
        :param CreateReferenceFileNoteDto body:
        :param str content_disposition: <b>Required</b> for application/octet-stream.<br> Example: filename*=UTF-8''YourFileName.txt
        :return: ReferenceFileReference
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_note_ref_with_http_info(project_uid, **kwargs)  # noqa: E501
        else:
            (data) = self.create_note_ref_with_http_info(project_uid, **kwargs)  # noqa: E501
            return data

    def create_note_ref_with_http_info(self, project_uid, **kwargs):  # noqa: E501
        """Create project reference file  # noqa: E501

        Accepts application/octet-stream or application/json.<br>                                                                     <b>application/json</b> - Note will be converted to .txt.<br>                                                                     <b>application/octet-stream</b> - Content-Disposition header is required  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_note_ref_with_http_info(project_uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_uid: (required)
        :param CreateReferenceFileNoteDto body:
        :param str content_disposition: <b>Required</b> for application/octet-stream.<br> Example: filename*=UTF-8''YourFileName.txt
        :return: ReferenceFileReference
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_uid', 'body', 'content_disposition']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_note_ref" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_uid' is set
        if ('project_uid' not in params or
                params['project_uid'] is None):
            raise ValueError("Missing the required parameter `project_uid` when calling `create_note_ref`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_uid' in params:
            path_params['projectUid'] = params['project_uid']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_disposition' in params:
            header_params['Content-Disposition'] = params['content_disposition']  # noqa: E501

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
            ['application/json', 'application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api2/v1/projects/{projectUid}/references', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReferenceFileReference',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_reference(self, project_uid, reference_file_id, **kwargs):  # noqa: E501
        """Get project reference  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_reference(project_uid, reference_file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_uid: (required)
        :param str reference_file_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_reference_with_http_info(project_uid, reference_file_id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_reference_with_http_info(project_uid, reference_file_id, **kwargs)  # noqa: E501
            return data

    def download_reference_with_http_info(self, project_uid, reference_file_id, **kwargs):  # noqa: E501
        """Get project reference  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_reference_with_http_info(project_uid, reference_file_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_uid: (required)
        :param str reference_file_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_uid', 'reference_file_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_reference" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_uid' is set
        if ('project_uid' not in params or
                params['project_uid'] is None):
            raise ValueError("Missing the required parameter `project_uid` when calling `download_reference`")  # noqa: E501
        # verify the required parameter 'reference_file_id' is set
        if ('reference_file_id' not in params or
                params['reference_file_id'] is None):
            raise ValueError("Missing the required parameter `reference_file_id` when calling `download_reference`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_uid' in params:
            path_params['projectUid'] = params['project_uid']  # noqa: E501
        if 'reference_file_id' in params:
            path_params['referenceFileId'] = params['reference_file_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api2/v1/projects/{projectUid}/references/{referenceFileId}', 'GET',
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