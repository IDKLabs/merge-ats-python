"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from MergeATSClient.api_client import ApiClient, Endpoint
from MergeATSClient.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from MergeATSClient.model.eeoc import EEOC
from MergeATSClient.model.paginated_eeoc_list import PaginatedEEOCList


class EeocsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __eeocs_create(
            self,
            x_account_token,
            **kwargs
        ):
            """eeocs_create  # noqa: E501

            Creates an `EEOC` object with the given values.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.eeocs_create(x_account_token, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.

            Keyword Args:
                run_async (bool): Whether or not third-party updates should be run asynchronously.. [optional]
                eeoc (EEOC): [optional]
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
                EEOC
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

        self.eeocs_create = Endpoint(
            settings={
                'response_type': (EEOC,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/eeocs',
                'operation_id': 'eeocs_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'run_async',
                    'eeoc',
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
                    'run_async':
                        (bool,),
                    'eeoc':
                        (EEOC,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'run_async': 'run_async',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'run_async': 'query',
                    'eeoc': 'body',
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
            callable=__eeocs_create
        )

        def __eeocs_list(
            self,
            x_account_token,
            **kwargs
        ):
            """eeocs_list  # noqa: E501

            Returns a list of `EEOC` objects.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.eeocs_list(x_account_token, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.

            Keyword Args:
                candidate_id (str): If provided, will only return EEOC info for this candidate.. [optional]
                created_after (datetime): If provided, will only return objects created after this datetime.. [optional]
                created_before (datetime): If provided, will only return objects created before this datetime.. [optional]
                cursor (str): The pagination cursor value.. [optional]
                expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional] if omitted the server will use the default value of "candidate"
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
                PaginatedEEOCList
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

        self.eeocs_list = Endpoint(
            settings={
                'response_type': (PaginatedEEOCList,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/eeocs',
                'operation_id': 'eeocs_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'candidate_id',
                    'created_after',
                    'created_before',
                    'cursor',
                    'expand',
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
                    'remote_id',
                ],
                'enum': [
                    'expand',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "CANDIDATE": "candidate"
                    },
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'candidate_id':
                        (str,),
                    'created_after':
                        (datetime,),
                    'created_before':
                        (datetime,),
                    'cursor':
                        (str,),
                    'expand':
                        (str,),
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
                    'candidate_id': 'candidate_id',
                    'created_after': 'created_after',
                    'created_before': 'created_before',
                    'cursor': 'cursor',
                    'expand': 'expand',
                    'include_remote_data': 'include_remote_data',
                    'modified_after': 'modified_after',
                    'modified_before': 'modified_before',
                    'page_size': 'page_size',
                    'remote_id': 'remote_id',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'candidate_id': 'query',
                    'created_after': 'query',
                    'created_before': 'query',
                    'cursor': 'query',
                    'expand': 'query',
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
            callable=__eeocs_list
        )

        def __eeocs_retrieve(
            self,
            x_account_token,
            id,
            **kwargs
        ):
            """eeocs_retrieve  # noqa: E501

            Returns an `EEOC` object with the given `id`.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.eeocs_retrieve(x_account_token, id, async_req=True)
            >>> result = thread.get()

            Args:
                x_account_token (str): Token identifying the end user.
                id (str):

            Keyword Args:
                expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional] if omitted the server will use the default value of "candidate"
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
                EEOC
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

        self.eeocs_retrieve = Endpoint(
            settings={
                'response_type': (EEOC,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/eeocs/{id}',
                'operation_id': 'eeocs_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'id',
                    'expand',
                    'include_remote_data',
                ],
                'required': [
                    'x_account_token',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                    'expand',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "CANDIDATE": "candidate"
                    },
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'id':
                        (str,),
                    'expand':
                        (str,),
                    'include_remote_data':
                        (bool,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'id': 'id',
                    'expand': 'expand',
                    'include_remote_data': 'include_remote_data',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'id': 'path',
                    'expand': 'query',
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
            callable=__eeocs_retrieve
        )
