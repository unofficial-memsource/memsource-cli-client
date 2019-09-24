# memsource_cli.AsyncRequestApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_async_request**](AsyncRequestApi.md#get_async_request) | **GET** /api2/v1/async/{asyncRequestId} | Get asynchronous request
[**list_pending_requests**](AsyncRequestApi.md#list_pending_requests) | **GET** /api2/v1/async | List pending requests


# **get_async_request**
> AsyncRequestDto get_async_request(async_request_id)

Get asynchronous request



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AsyncRequestApi()
async_request_id = 789 # int | 

try:
    # Get asynchronous request
    api_response = api_instance.get_async_request(async_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsyncRequestApi->get_async_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_request_id** | **int**|  | 

### Return type

[**AsyncRequestDto**](AsyncRequestDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pending_requests**
> PageDtoAsyncRequestDto list_pending_requests(all=all, page_number=page_number, page_size=page_size)

List pending requests



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AsyncRequestApi()
all = false # bool | Pending requests for organization instead of current user. Only for ADMIN. (optional) (default to false)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List pending requests
    api_response = api_instance.list_pending_requests(all=all, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsyncRequestApi->list_pending_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| Pending requests for organization instead of current user. Only for ADMIN. | [optional] [default to false]
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoAsyncRequestDto**](PageDtoAsyncRequestDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

