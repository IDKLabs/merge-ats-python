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
from MergeATSClient.model.paginated_sync_status_list import PaginatedSyncStatusList
from MergeATSClient.model.sync_status import SyncStatus


class SyncStatusApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __sync_status_list(
            self,
            x_account_token,
            **kwargs
        ):
            """sync_status_list  # noqa: E501

            Get syncing status.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.sync_status_list(x_account_token, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.

            Keyword Args:
                cursor (int): The pagination cursor value.. [optional]
                page_size (int): Number of results to return per page.. [optional]
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
                PaginatedSyncStatusList
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

        self.sync_status_list = _Endpoint(
            settings={
                'response_type': (PaginatedSyncStatusList,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/sync-status',
                'operation_id': 'sync_status_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'cursor',
                    'page_size',
                ],
                'required': [
                    'x_account_token',
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
                    'cursor':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'cursor': 'cursor',
                    'page_size': 'page_size',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'cursor': 'query',
                    'page_size': 'query',
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
            callable=__sync_status_list
        )

        def __sync_status_resync_create(
            self,
            x_account_token,
            **kwargs
        ):
            """sync_status_resync_create  # noqa: E501

            Force resync of all models.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.sync_status_resync_create(x_account_token, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.

            Keyword Args:
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
                SyncStatus
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

        self.sync_status_resync_create = _Endpoint(
            settings={
                'response_type': (SyncStatus,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/sync-status/resync',
                'operation_id': 'sync_status_resync_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                ],
                'required': [
                    'x_account_token',
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
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                },
                'location_map': {
                    'x_account_token': 'header',
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
            callable=__sync_status_resync_create
        )
