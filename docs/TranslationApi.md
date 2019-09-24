# memsource_cli.TranslationApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**human_translate**](TranslationApi.md#human_translate) | **POST** /api2/v1/projects/{projectUid}/jobs/humanTranslate | Human translate (Gengo or Unbabel)
[**machine_translation_job**](TranslationApi.md#machine_translation_job) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translations/translateWithMachineTranslation | Translate using machine translation
[**pre_translate**](TranslationApi.md#pre_translate) | **POST** /api2/v1/projects/{projectUid}/jobs/preTranslate | Pre-translate job


# **human_translate**
> AsyncRequestWrapperDto human_translate(project_uid, body=body)

Human translate (Gengo or Unbabel)



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.HumanTranslateJobsDto() # HumanTranslateJobsDto |  (optional)

try:
    # Human translate (Gengo or Unbabel)
    api_response = api_instance.human_translate(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationApi->human_translate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**HumanTranslateJobsDto**](HumanTranslateJobsDto.md)|  | [optional] 

### Return type

[**AsyncRequestWrapperDto**](AsyncRequestWrapperDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **machine_translation_job**
> MachineTranslateResponse machine_translation_job(project_uid, job_uid, body=body)

Translate using machine translation

Configured machine translate settings is used

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 
body = memsource_cli.TranslationRequestDto() # TranslationRequestDto |  (optional)

try:
    # Translate using machine translation
    api_response = api_instance.machine_translation_job(project_uid, job_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationApi->machine_translation_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**TranslationRequestDto**](TranslationRequestDto.md)|  | [optional] 

### Return type

[**MachineTranslateResponse**](MachineTranslateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_translate**
> AsyncRequestWrapperDto pre_translate(project_uid, body=body)

Pre-translate job



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.PreTranslateJobsDto() # PreTranslateJobsDto |  (optional)

try:
    # Pre-translate job
    api_response = api_instance.pre_translate(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationApi->pre_translate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**PreTranslateJobsDto**](PreTranslateJobsDto.md)|  | [optional] 

### Return type

[**AsyncRequestWrapperDto**](AsyncRequestWrapperDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

