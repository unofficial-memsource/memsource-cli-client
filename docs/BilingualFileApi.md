# memsource_cli.BilingualFileApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compare_bilingual_file**](BilingualFileApi.md#compare_bilingual_file) | **POST** /api2/v1/bilingualFiles/compare | Compare bilingual file
[**convert_bilingual_file**](BilingualFileApi.md#convert_bilingual_file) | **POST** /api2/v1/bilingualFiles/convert | Convert bilingual file
[**get_bilingual_file**](BilingualFileApi.md#get_bilingual_file) | **POST** /api2/v1/projects/{projectUid}/jobs/bilingualFile | Download bilingual file
[**get_preview_file**](BilingualFileApi.md#get_preview_file) | **POST** /api2/v1/bilingualFiles/preview | Download preview
[**upload_bilingual_file**](BilingualFileApi.md#upload_bilingual_file) | **PUT** /api2/v1/bilingualFiles | Upload bilingual file


# **compare_bilingual_file**
> ComparedSegmentsDto compare_bilingual_file(body=body, workflow_level=workflow_level)

Compare bilingual file

Compares bilingual file to job state. Returns list of compared segments.

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.BilingualFileApi()
body = memsource_cli.InputStream() # InputStream |  (optional)
workflow_level = 1 # int |  (optional) (default to 1)

try:
    # Compare bilingual file
    api_response = api_instance.compare_bilingual_file(body=body, workflow_level=workflow_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BilingualFileApi->compare_bilingual_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputStream**](InputStream.md)|  | [optional] 
 **workflow_level** | **int**|  | [optional] [default to 1]

### Return type

[**ComparedSegmentsDto**](ComparedSegmentsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_bilingual_file**
> convert_bilingual_file(_from, to, body=body)

Convert bilingual file



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.BilingualFileApi()
_from = '_from_example' # str | 
to = 'to_example' # str | 
body = memsource_cli.InputStream() # InputStream |  (optional)

try:
    # Convert bilingual file
    api_instance.convert_bilingual_file(_from, to, body=body)
except ApiException as e:
    print("Exception when calling BilingualFileApi->convert_bilingual_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **str**|  | 
 **to** | **str**|  | 
 **body** | [**InputStream**](InputStream.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bilingual_file**
> get_bilingual_file(project_uid, body=body, format=format)

Download bilingual file



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.BilingualFileApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.JobPartReadyReferences() # JobPartReadyReferences |  (optional)
format = 'MXLF' # str |  (optional) (default to MXLF)

try:
    # Download bilingual file
    api_instance.get_bilingual_file(project_uid, body=body, format=format)
except ApiException as e:
    print("Exception when calling BilingualFileApi->get_bilingual_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**JobPartReadyReferences**](JobPartReadyReferences.md)|  | [optional] 
 **format** | **str**|  | [optional] [default to MXLF]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_file**
> get_preview_file(body=body)

Download preview

Supports mxliff format

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.BilingualFileApi()
body = memsource_cli.InputStream() # InputStream |  (optional)

try:
    # Download preview
    api_instance.get_preview_file(body=body)
except ApiException as e:
    print("Exception when calling BilingualFileApi->get_preview_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputStream**](InputStream.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_bilingual_file**
> JobPartsDto upload_bilingual_file(body=body, format=format, save_to_trans_memory=save_to_trans_memory, set_completed=set_completed)

Upload bilingual file

Returns updated job parts

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.BilingualFileApi()
body = memsource_cli.InputStream() # InputStream |  (optional)
format = 'MXLF' # str |  (optional) (default to MXLF)
save_to_trans_memory = 'Confirmed' # str |  (optional) (default to Confirmed)
set_completed = false # bool |  (optional) (default to false)

try:
    # Upload bilingual file
    api_response = api_instance.upload_bilingual_file(body=body, format=format, save_to_trans_memory=save_to_trans_memory, set_completed=set_completed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BilingualFileApi->upload_bilingual_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputStream**](InputStream.md)|  | [optional] 
 **format** | **str**|  | [optional] [default to MXLF]
 **save_to_trans_memory** | **str**|  | [optional] [default to Confirmed]
 **set_completed** | **bool**|  | [optional] [default to false]

### Return type

[**JobPartsDto**](JobPartsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

