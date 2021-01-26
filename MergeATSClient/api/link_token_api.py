# coding: utf-8

"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from MergeATSClient.api_client import ApiClient
from MergeATSClient.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class LinkTokenApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def link_token_create(self, end_user_details, **kwargs):  # noqa: E501
        """link_token_create  # noqa: E501

        Creates a link token to be used when linking a new end user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.link_token_create(end_user_details, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param EndUserDetails end_user_details: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: LinkToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.link_token_create_with_http_info(end_user_details, **kwargs)  # noqa: E501

    def link_token_create_with_http_info(self, end_user_details, **kwargs):  # noqa: E501
        """link_token_create  # noqa: E501

        Creates a link token to be used when linking a new end user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.link_token_create_with_http_info(end_user_details, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param EndUserDetails end_user_details: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(LinkToken, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'end_user_details'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method link_token_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'end_user_details' is set
        if self.api_client.client_side_validation and ('end_user_details' not in local_var_params or  # noqa: E501
                                                        local_var_params['end_user_details'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `end_user_details` when calling `link_token_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'end_user_details' in local_var_params:
            body_params = local_var_params['end_user_details']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/link-token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LinkToken',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
