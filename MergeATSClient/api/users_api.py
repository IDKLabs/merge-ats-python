"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from MergeATSClient.api_client import ApiClient, Endpoint as _Endpoint
from MergeATSClient.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from MergeATSClient.model.paginated_remote_user_list import PaginatedRemoteUserList
from MergeATSClient.model.remote_user import RemoteUser
from MergeATSClient.model.remote_user_request import RemoteUserRequest


class UsersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __users_create(
            self,
            x_account_token,
            remote_user_id,
            **kwargs
        ):
            """users_create  # noqa: E501

            Creates a `RemoteUser` object with the given values.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.users_create(x_account_token, remote_user_id, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.
                remote_user_id (str): The ID of the RemoteUser deleting the resource. This can be found in the ID field (not remote_id) in the RemoteUser table.

            Keyword Args:
                run_async (bool): Whether or not third-party updates should be run asynchronously.. [optional]
                remote_user_request (RemoteUserRequest): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                RemoteUser
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_account_token'] = \
                x_account_token
            kwargs['remote_user_id'] = \
                remote_user_id
            return self.call_with_http_info(**kwargs)

        self.users_create = _Endpoint(
            settings={
                'response_type': (RemoteUser,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/users',
                'operation_id': 'users_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'remote_user_id',
                    'run_async',
                    'remote_user_request',
                ],
                'required': [
                    'x_account_token',
                    'remote_user_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'remote_user_id':
                        (str,),
                    'run_async':
                        (bool,),
                    'remote_user_request':
                        (RemoteUserRequest,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'remote_user_id': 'remote_user_id',
                    'run_async': 'run_async',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'remote_user_id': 'query',
                    'run_async': 'query',
                    'remote_user_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ]
            },
            api_client=api_client,
            callable=__users_create
        )

        def __users_list(
            self,
            x_account_token,
            **kwargs
        ):
            """users_list  # noqa: E501

            Returns a list of `RemoteUser` objects.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.users_list(x_account_token, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.

            Keyword Args:
                created_after (datetime): If provided, will only return objects created after this datetime.. [optional]
                created_before (datetime): If provided, will only return objects created before this datetime.. [optional]
                cursor (str): The pagination cursor value.. [optional]
                email (str, none_type): If provided, will only return remote users with the given email address. [optional]
                include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
                modified_after (datetime): If provided, will only return objects modified after this datetime.. [optional]
                modified_before (datetime): If provided, will only return objects modified before this datetime.. [optional]
                page_size (int): Number of results to return per page.. [optional]
                remote_id (str, none_type): The API provider's ID for the given object.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PaginatedRemoteUserList
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_account_token'] = \
                x_account_token
            return self.call_with_http_info(**kwargs)

        self.users_list = _Endpoint(
            settings={
                'response_type': (PaginatedRemoteUserList,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/users',
                'operation_id': 'users_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'created_after',
                    'created_before',
                    'cursor',
                    'email',
                    'include_remote_data',
                    'modified_after',
                    'modified_before',
                    'page_size',
                    'remote_id',
                ],
                'required': [
                    'x_account_token',
                ],
                'nullable': [
                    'email',
                    'remote_id',
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'created_after':
                        (datetime,),
                    'created_before':
                        (datetime,),
                    'cursor':
                        (str,),
                    'email':
                        (str, none_type,),
                    'include_remote_data':
                        (bool,),
                    'modified_after':
                        (datetime,),
                    'modified_before':
                        (datetime,),
                    'page_size':
                        (int,),
                    'remote_id':
                        (str, none_type,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'created_after': 'created_after',
                    'created_before': 'created_before',
                    'cursor': 'cursor',
                    'email': 'email',
                    'include_remote_data': 'include_remote_data',
                    'modified_after': 'modified_after',
                    'modified_before': 'modified_before',
                    'page_size': 'page_size',
                    'remote_id': 'remote_id',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'created_after': 'query',
                    'created_before': 'query',
                    'cursor': 'query',
                    'email': 'query',
                    'include_remote_data': 'query',
                    'modified_after': 'query',
                    'modified_before': 'query',
                    'page_size': 'query',
                    'remote_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__users_list
        )

        def __users_retrieve(
            self,
            x_account_token,
            id,
            **kwargs
        ):
            """users_retrieve  # noqa: E501

            Returns a `RemoteUser` object with the given `id`.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.users_retrieve(x_account_token, id, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.
                id (str):

            Keyword Args:
                include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                RemoteUser
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_account_token'] = \
                x_account_token
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.users_retrieve = _Endpoint(
            settings={
                'response_type': (RemoteUser,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/users/{id}',
                'operation_id': 'users_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'id',
                    'include_remote_data',
                ],
                'required': [
                    'x_account_token',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'id':
                        (str,),
                    'include_remote_data':
                        (bool,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'id': 'id',
                    'include_remote_data': 'include_remote_data',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'id': 'path',
                    'include_remote_data': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__users_retrieve
        )
