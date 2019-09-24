# memsource_cli.QualityAssuranceApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ignored_warnings**](QualityAssuranceApi.md#add_ignored_warnings) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/ignoredWarnings | Add ignored warnings
[**delete_ignored_warnings**](QualityAssuranceApi.md#delete_ignored_warnings) | **DELETE** /api2/v1/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/ignoredWarnings | Delete ignored warnings
[**enabled_quality_checks_for_job**](QualityAssuranceApi.md#enabled_quality_checks_for_job) | **GET** /api2/v2/projects/{projectUid}/jobs/qualityAssurances/settings | Get QA settings
[**run_qa_for_job_part_v3**](QualityAssuranceApi.md#run_qa_for_job_part_v3) | **POST** /api2/v3/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/run | Run quality assurance
[**run_qa_for_job_parts_v3**](QualityAssuranceApi.md#run_qa_for_job_parts_v3) | **POST** /api2/v3/projects/{projectUid}/jobs/qualityAssurances/run | Run quality assurance (batch)
[**run_qa_for_segments_v3**](QualityAssuranceApi.md#run_qa_for_segments_v3) | **POST** /api2/v3/projects/{projectUid}/jobs/qualityAssurances/segments/run | Run quality assurance on selected segments
[**update_ignored_checks**](QualityAssuranceApi.md#update_ignored_checks) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/qualityAssurances/ignoreChecks | Edit ignored checks


# **add_ignored_warnings**
> UpdateIgnoredWarningsDto add_ignored_warnings(project_uid, job_uid, body=body)

Add ignored warnings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.QualityAssuranceApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 
body = memsource_cli.UpdateIgnoredWarningsDto() # UpdateIgnoredWarningsDto |  (optional)

try:
    # Add ignored warnings
    api_response = api_instance.add_ignored_warnings(project_uid, job_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityAssuranceApi->add_ignored_warnings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**UpdateIgnoredWarningsDto**](UpdateIgnoredWarningsDto.md)|  | [optional] 

### Return type

[**UpdateIgnoredWarningsDto**](UpdateIgnoredWarningsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ignored_warnings**
> delete_ignored_warnings(project_uid, job_uid, body=body)

Delete ignored warnings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.QualityAssuranceApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 
body = memsource_cli.UpdateIgnoredWarningsDto() # UpdateIgnoredWarningsDto |  (optional)

try:
    # Delete ignored warnings
    api_instance.delete_ignored_warnings(project_uid, job_uid, body=body)
except ApiException as e:
    print("Exception when calling QualityAssuranceApi->delete_ignored_warnings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**UpdateIgnoredWarningsDto**](UpdateIgnoredWarningsDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enabled_quality_checks_for_job**
> QualityAssuranceChecksDto enabled_quality_checks_for_job(project_uid)

Get QA settings

Returns enabled quality assurance checks and settings.

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.QualityAssuranceApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get QA settings
    api_response = api_instance.enabled_quality_checks_for_job(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityAssuranceApi->enabled_quality_checks_for_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**QualityAssuranceChecksDto**](QualityAssuranceChecksDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_qa_for_job_part_v3**
> QualityAssuranceResponseDto run_qa_for_job_part_v3(project_uid, job_uid, body=body)

Run quality assurance

Call \"Get QA settings\" endpoint to get the list of enabled QA checks

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.QualityAssuranceApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 
body = memsource_cli.QualityAssuranceRunDtoV3() # QualityAssuranceRunDtoV3 |  (optional)

try:
    # Run quality assurance
    api_response = api_instance.run_qa_for_job_part_v3(project_uid, job_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityAssuranceApi->run_qa_for_job_part_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**QualityAssuranceRunDtoV3**](QualityAssuranceRunDtoV3.md)|  | [optional] 

### Return type

[**QualityAssuranceResponseDto**](QualityAssuranceResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_qa_for_job_parts_v3**
> QualityAssuranceResponseDto run_qa_for_job_parts_v3(project_uid, body=body)

Run quality assurance (batch)

Call \"Get QA settings\" endpoint to get the list of enabled QA checks

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.QualityAssuranceApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.QualityAssuranceBatchRunDtoV3() # QualityAssuranceBatchRunDtoV3 |  (optional)

try:
    # Run quality assurance (batch)
    api_response = api_instance.run_qa_for_job_parts_v3(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityAssuranceApi->run_qa_for_job_parts_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**QualityAssuranceBatchRunDtoV3**](QualityAssuranceBatchRunDtoV3.md)|  | [optional] 

### Return type

[**QualityAssuranceResponseDto**](QualityAssuranceResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_qa_for_segments_v3**
> QualityAssuranceResponseDto run_qa_for_segments_v3(project_uid, body=body)

Run quality assurance on selected segments

By default runs only fast running checks. Source and target language of jobs have to match.

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.QualityAssuranceApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.QualityAssuranceSegmentsRunDtoV3() # QualityAssuranceSegmentsRunDtoV3 |  (optional)

try:
    # Run quality assurance on selected segments
    api_response = api_instance.run_qa_for_segments_v3(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QualityAssuranceApi->run_qa_for_segments_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**QualityAssuranceSegmentsRunDtoV3**](QualityAssuranceSegmentsRunDtoV3.md)|  | [optional] 

### Return type

[**QualityAssuranceResponseDto**](QualityAssuranceResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ignored_checks**
> update_ignored_checks(project_uid, job_uid, body=body)

Edit ignored checks



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.QualityAssuranceApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 
body = memsource_cli.UpdateIgnoredChecksDto() # UpdateIgnoredChecksDto |  (optional)

try:
    # Edit ignored checks
    api_instance.update_ignored_checks(project_uid, job_uid, body=body)
except ApiException as e:
    print("Exception when calling QualityAssuranceApi->update_ignored_checks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**UpdateIgnoredChecksDto**](UpdateIgnoredChecksDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

