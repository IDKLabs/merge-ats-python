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


class ActivitiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def activities_list(self, x_account_token, **kwargs):  # noqa: E501
        """activities_list  # noqa: E501

        Returns a list of `Activity` objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_list(x_account_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_account_token: Token identifying the end user. (required)
        :param datetime created_after: If provided, will only return objects created after this datetime.
        :param datetime created_before: If provided, will only return objects created before this datetime.
        :param str cursor: The pagination cursor value.
        :param str expand: Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
        :param datetime modified_after: If provided, will only return objects modified after this datetime.
        :param datetime modified_before: If provided, will only return objects modified before this datetime.
        :param int page_size: Number of results to return per page.
        :param str remote_id: The API provider's ID for the given object.
        :param str user_id: If provided, will only return activities done by this user.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaginatedActivityList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.activities_list_with_http_info(x_account_token, **kwargs)  # noqa: E501

    def activities_list_with_http_info(self, x_account_token, **kwargs):  # noqa: E501
        """activities_list  # noqa: E501

        Returns a list of `Activity` objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_list_with_http_info(x_account_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_account_token: Token identifying the end user. (required)
        :param datetime created_after: If provided, will only return objects created after this datetime.
        :param datetime created_before: If provided, will only return objects created before this datetime.
        :param str cursor: The pagination cursor value.
        :param str expand: Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
        :param datetime modified_after: If provided, will only return objects modified after this datetime.
        :param datetime modified_before: If provided, will only return objects modified before this datetime.
        :param int page_size: Number of results to return per page.
        :param str remote_id: The API provider's ID for the given object.
        :param str user_id: If provided, will only return activities done by this user.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaginatedActivityList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'x_account_token',
            'created_after',
            'created_before',
            'cursor',
            'expand',
            'modified_after',
            'modified_before',
            'page_size',
            'remote_id',
            'user_id'
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
                    " to method activities_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'x_account_token' is set
        if self.api_client.client_side_validation and ('x_account_token' not in local_var_params or  # noqa: E501
                                                        local_var_params['x_account_token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_account_token` when calling `activities_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'created_after' in local_var_params and local_var_params['created_after'] is not None:  # noqa: E501
            query_params.append(('created_after', local_var_params['created_after']))  # noqa: E501
        if 'created_before' in local_var_params and local_var_params['created_before'] is not None:  # noqa: E501
            query_params.append(('created_before', local_var_params['created_before']))  # noqa: E501
        if 'cursor' in local_var_params and local_var_params['cursor'] is not None:  # noqa: E501
            query_params.append(('cursor', local_var_params['cursor']))  # noqa: E501
        if 'expand' in local_var_params and local_var_params['expand'] is not None:  # noqa: E501
            query_params.append(('expand', local_var_params['expand']))  # noqa: E501
        if 'modified_after' in local_var_params and local_var_params['modified_after'] is not None:  # noqa: E501
            query_params.append(('modified_after', local_var_params['modified_after']))  # noqa: E501
        if 'modified_before' in local_var_params and local_var_params['modified_before'] is not None:  # noqa: E501
            query_params.append(('modified_before', local_var_params['modified_before']))  # noqa: E501
        if 'page_size' in local_var_params and local_var_params['page_size'] is not None:  # noqa: E501
            query_params.append(('page_size', local_var_params['page_size']))  # noqa: E501
        if 'remote_id' in local_var_params and local_var_params['remote_id'] is not None:  # noqa: E501
            query_params.append(('remote_id', local_var_params['remote_id']))  # noqa: E501
        if 'user_id' in local_var_params and local_var_params['user_id'] is not None:  # noqa: E501
            query_params.append(('user_id', local_var_params['user_id']))  # noqa: E501

        header_params = {}
        if 'x_account_token' in local_var_params:
            header_params['X-Account-Token'] = local_var_params['x_account_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/activities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedActivityList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def activities_retrieve(self, x_account_token, id, **kwargs):  # noqa: E501
        """activities_retrieve  # noqa: E501

        Returns an `Activity` object with the given `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_retrieve(x_account_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_account_token: Token identifying the end user. (required)
        :param str id: (required)
        :param str expand: Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Activity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.activities_retrieve_with_http_info(x_account_token, id, **kwargs)  # noqa: E501

    def activities_retrieve_with_http_info(self, x_account_token, id, **kwargs):  # noqa: E501
        """activities_retrieve  # noqa: E501

        Returns an `Activity` object with the given `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activities_retrieve_with_http_info(x_account_token, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_account_token: Token identifying the end user. (required)
        :param str id: (required)
        :param str expand: Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Activity, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'x_account_token',
            'id',
            'expand'
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
                    " to method activities_retrieve" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'x_account_token' is set
        if self.api_client.client_side_validation and ('x_account_token' not in local_var_params or  # noqa: E501
                                                        local_var_params['x_account_token'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `x_account_token` when calling `activities_retrieve`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `activities_retrieve`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'expand' in local_var_params and local_var_params['expand'] is not None:  # noqa: E501
            query_params.append(('expand', local_var_params['expand']))  # noqa: E501

        header_params = {}
        if 'x_account_token' in local_var_params:
            header_params['X-Account-Token'] = local_var_params['x_account_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/activities/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Activity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
