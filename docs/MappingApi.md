# memsource_cli.MappingApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mapping_for_task**](MappingApi.md#get_mapping_for_task) | **GET** /api2/v1/mappings/tasks/{id} | Returns mapping for taskId (mxliff)


# **get_mapping_for_task**
> TaskMappingDto get_mapping_for_task(id, workflow_level=workflow_level)

Returns mapping for taskId (mxliff)



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.MappingApi()
id = 'id_example' # str | 
workflow_level = 1 # int |  (optional) (default to 1)

try:
    # Returns mapping for taskId (mxliff)
    api_response = api_instance.get_mapping_for_task(id, workflow_level=workflow_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MappingApi->get_mapping_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **workflow_level** | **int**|  | [optional] [default to 1]

### Return type

[**TaskMappingDto**](TaskMappingDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

