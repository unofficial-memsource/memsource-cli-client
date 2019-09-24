# memsource_cli.WebhookApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_web_hook**](WebhookApi.md#create_web_hook) | **POST** /api2/v1/webhooks | Create webhook
[**delete_web_hook**](WebhookApi.md#delete_web_hook) | **DELETE** /api2/v1/webhooks/{webHookId} | Delete webhook
[**get_web_hook**](WebhookApi.md#get_web_hook) | **GET** /api2/v1/webhooks/{webHookId} | Get webhook
[**get_web_hook_list**](WebhookApi.md#get_web_hook_list) | **GET** /api2/v1/webhooks | Lists webhooks
[**update_web_hook**](WebhookApi.md#update_web_hook) | **PUT** /api2/v1/webhooks/{webHookId} | Edit webhook


# **create_web_hook**
> WebHookDto create_web_hook(body=body)

Create webhook



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.WebhookApi()
body = memsource_cli.WebHookDto() # WebHookDto |  (optional)

try:
    # Create webhook
    api_response = api_instance.create_web_hook(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->create_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebHookDto**](WebHookDto.md)|  | [optional] 

### Return type

[**WebHookDto**](WebHookDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_web_hook**
> delete_web_hook(web_hook_id)

Delete webhook



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.WebhookApi()
web_hook_id = 789 # int | 

try:
    # Delete webhook
    api_instance.delete_web_hook(web_hook_id)
except ApiException as e:
    print("Exception when calling WebhookApi->delete_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_hook**
> WebHookDto get_web_hook(web_hook_id)

Get webhook



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.WebhookApi()
web_hook_id = 789 # int | 

try:
    # Get webhook
    api_response = api_instance.get_web_hook(web_hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_id** | **int**|  | 

### Return type

[**WebHookDto**](WebHookDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_hook_list**
> PageDtoWebHookDto get_web_hook_list(page_number=page_number, page_size=page_size)

Lists webhooks



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.WebhookApi()
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # Lists webhooks
    api_response = api_instance.get_web_hook_list(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->get_web_hook_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoWebHookDto**](PageDtoWebHookDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_web_hook**
> WebHookDto update_web_hook(web_hook_id, body=body)

Edit webhook



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.WebhookApi()
web_hook_id = 789 # int | 
body = memsource_cli.WebHookDto() # WebHookDto |  (optional)

try:
    # Edit webhook
    api_response = api_instance.update_web_hook(web_hook_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->update_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_id** | **int**|  | 
 **body** | [**WebHookDto**](WebHookDto.md)|  | [optional] 

### Return type

[**WebHookDto**](WebHookDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

