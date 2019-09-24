# memsource_cli.AnalyticsApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate**](AnalyticsApi.md#aggregate) | **POST** /api2/v1/analytics/{type} | Run analytics aggregation


# **aggregate**
> AnalyticsResponseDto aggregate(type, body=body)

Run analytics aggregation

For more information check <a target=\"_blank\" href=\"https://wiki.memsource.com/wiki/Analytics_Aggregations\">Memsource Wiki</a>

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalyticsApi()
type = 'type_example' # str | This value is case sensitive
body = memsource_cli.AnalyticsDto() # AnalyticsDto |  (optional)

try:
    # Run analytics aggregation
    api_response = api_instance.aggregate(type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->aggregate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| This value is case sensitive | 
 **body** | [**AnalyticsDto**](AnalyticsDto.md)|  | [optional] 

### Return type

[**AnalyticsResponseDto**](AnalyticsResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

