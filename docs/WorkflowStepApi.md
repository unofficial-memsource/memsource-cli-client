# memsource_cli.WorkflowStepApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_wf_steps**](WorkflowStepApi.md#list_wf_steps) | **GET** /api2/v1/workflowSteps | List workflow steps
[**list_workflow_steps**](WorkflowStepApi.md#list_workflow_steps) | **GET** /api2/v1/users/{userId}/workflowSteps | List assigned workflow steps


# **list_wf_steps**
> PageDtoWorkflowStepDto list_wf_steps(page_number=page_number, page_size=page_size)

List workflow steps



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.WorkflowStepApi()
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List workflow steps
    api_response = api_instance.list_wf_steps(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowStepApi->list_wf_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoWorkflowStepDto**](PageDtoWorkflowStepDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_steps**
> PageDtoWorkflowStepReference list_workflow_steps(user_id, status=status, project_uid=project_uid, target_lang=target_lang, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)

List assigned workflow steps



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.WorkflowStepApi()
user_id = 789 # int | 
status = ['status_example'] # list[str] |  (optional)
project_uid = 'project_uid_example' # str |  (optional)
target_lang = ['target_lang_example'] # list[str] |  (optional)
due_in_hours = 56 # int | -1 for jobs that are overdue (optional)
filename = 'filename_example' # str |  (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    # List assigned workflow steps
    api_response = api_instance.list_workflow_steps(user_id, status=status, project_uid=project_uid, target_lang=target_lang, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowStepApi->list_workflow_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **status** | [**list[str]**](str.md)|  | [optional] 
 **project_uid** | **str**|  | [optional] 
 **target_lang** | [**list[str]**](str.md)|  | [optional] 
 **due_in_hours** | **int**| -1 for jobs that are overdue | [optional] 
 **filename** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoWorkflowStepReference**](PageDtoWorkflowStepReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

