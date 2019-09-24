# memsource_cli.WorkflowChangesApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_workflow_changes**](WorkflowChangesApi.md#download_workflow_changes) | **POST** /api2/v2/jobs/workflowChanges | Download workflow changes report


# **download_workflow_changes**
> Response download_workflow_changes(body=body)

Download workflow changes report



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.WorkflowChangesApi()
body = memsource_cli.WorkflowChangesDto() # WorkflowChangesDto |  (optional)

try:
    # Download workflow changes report
    api_response = api_instance.download_workflow_changes(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowChangesApi->download_workflow_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkflowChangesDto**](WorkflowChangesDto.md)|  | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

