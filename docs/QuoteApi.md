# memsource_cli.QuoteApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quote**](QuoteApi.md#create_quote) | **POST** /api2/v1/quotes | Create quote
[**delete_quote**](QuoteApi.md#delete_quote) | **DELETE** /api2/v1/quotes/{quoteId} | Delete quote
[**get1**](QuoteApi.md#get1) | **GET** /api2/v1/quotes/{quoteId} | Get quote


# **create_quote**
> QuoteDto create_quote(body=body)

Create quote



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.QuoteApi()
body = memsource_cli.QuoteCreateDto() # QuoteCreateDto |  (optional)

try:
    # Create quote
    api_response = api_instance.create_quote(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteApi->create_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuoteCreateDto**](QuoteCreateDto.md)|  | [optional] 

### Return type

[**QuoteDto**](QuoteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quote**
> delete_quote(quote_id)

Delete quote



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.QuoteApi()
quote_id = 789 # int | 

try:
    # Delete quote
    api_instance.delete_quote(quote_id)
except ApiException as e:
    print("Exception when calling QuoteApi->delete_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get1**
> QuoteDto get1(quote_id)

Get quote



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.QuoteApi()
quote_id = 789 # int | 

try:
    # Get quote
    api_response = api_instance.get1(quote_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteApi->get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **int**|  | 

### Return type

[**QuoteDto**](QuoteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

