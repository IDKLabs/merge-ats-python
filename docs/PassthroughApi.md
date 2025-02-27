# MergeATSClient.PassthroughApi

All URIs are relative to *https://api.merge.dev/api/ats/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**passthrough_create**](PassthroughApi.md#passthrough_create) | **POST** /passthrough | 


# **passthrough_create**
> RemoteResponse passthrough_create(x_account_token, data_passthrough_request)



Pull data from an endpoint not currently supported by Merge.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import MergeATSClient
from MergeATSClient.api import passthrough_api
from MergeATSClient.model.remote_response import RemoteResponse
from MergeATSClient.model.data_passthrough_request import DataPassthroughRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/ats/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergeATSClient.Configuration(
    host = "https://api.merge.dev/api/ats/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergeATSClient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = passthrough_api.PassthroughApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    data_passthrough_request = DataPassthroughRequest(
        method=,
        path="/scooters",
        base_url_override="base_url_override_example",
        data="{"company": "Lime", "model": "Gen 2.5"}",
        headers={
            "key": None,
        },
        request_format=,
    ) # DataPassthroughRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.passthrough_create(x_account_token, data_passthrough_request)
        pprint(api_response)
    except MergeATSClient.ApiException as e:
        print("Exception when calling PassthroughApi->passthrough_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **data_passthrough_request** | [**DataPassthroughRequest**](DataPassthroughRequest.md)|  |

### Return type

[**RemoteResponse**](RemoteResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

