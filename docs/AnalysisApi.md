# memsource_cli.AnalysisApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_edit_analyses**](AnalysisApi.md#batch_edit_analyses) | **PUT** /api2/v1/analyses/bulk | Edit analyses (batch)
[**bulk_delete_analyses**](AnalysisApi.md#bulk_delete_analyses) | **DELETE** /api2/v1/analyses/bulk | Delete analyses (batch)
[**create_analyse_async**](AnalysisApi.md#create_analyse_async) | **POST** /api2/v1/analyses | Create analysis
[**create_analyses_for_langs**](AnalysisApi.md#create_analyses_for_langs) | **POST** /api2/v1/analyses/byLanguages | Create analyses by languages
[**create_analyses_for_providers**](AnalysisApi.md#create_analyses_for_providers) | **POST** /api2/v1/analyses/byProviders | Create analyses by providers
[**delete**](AnalysisApi.md#delete) | **DELETE** /api2/v1/analyses/{analyseId} | Delete analysis
[**download_analyse**](AnalysisApi.md#download_analyse) | **GET** /api2/v1/analyses/{analyseId}/download | Download analysis
[**get_analyse_language_part**](AnalysisApi.md#get_analyse_language_part) | **GET** /api2/v1/analyses/{analyseId}/analyseLanguageParts/{analyseLanguagePartId} | Get analysis language part
[**get_analyse_v2**](AnalysisApi.md#get_analyse_v2) | **GET** /api2/v2/analyses/{analyseId} | Get analysis
[**get_job_part_analyse**](AnalysisApi.md#get_job_part_analyse) | **GET** /api2/v1/analyses/{analyseId}/jobs/{jobUid} | Get jobs analysis
[**list_by_project_v2**](AnalysisApi.md#list_by_project_v2) | **GET** /api2/v2/projects/{projectUid}/analyses | List analyses by project
[**list_job_parts**](AnalysisApi.md#list_job_parts) | **GET** /api2/v1/analyses/{analyseId}/analyseLanguageParts/{analyseLanguagePartId}/jobs | List jobs of analyses
[**list_part_analyse1**](AnalysisApi.md#list_part_analyse1) | **GET** /api2/v2/projects/{projectUid}/jobs/{jobUid}/analyses | List analyses


# **batch_edit_analyses**
> list[AnalyseDto] batch_edit_analyses(body=body)

Edit analyses (batch)



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalysisApi()
body = memsource_cli.BulkEditAnalyseDto() # BulkEditAnalyseDto |  (optional)

try:
    # Edit analyses (batch)
    api_response = api_instance.batch_edit_analyses(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->batch_edit_analyses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkEditAnalyseDto**](BulkEditAnalyseDto.md)|  | [optional] 

### Return type

[**list[AnalyseDto]**](AnalyseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_analyses**
> bulk_delete_analyses(body=body)

Delete analyses (batch)



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalysisApi()
body = memsource_cli.BulkDeleteAnalyseDto() # BulkDeleteAnalyseDto |  (optional)

try:
    # Delete analyses (batch)
    api_instance.bulk_delete_analyses(body=body)
except ApiException as e:
    print("Exception when calling AnalysisApi->bulk_delete_analyses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkDeleteAnalyseDto**](BulkDeleteAnalyseDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_analyse_async**
> AsyncAnalyseResponseDto create_analyse_async(body=body)

Create analysis



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalysisApi()
body = memsource_cli.CreateAnalyseAsyncDto() # CreateAnalyseAsyncDto |  (optional)

try:
    # Create analysis
    api_response = api_instance.create_analyse_async(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->create_analyse_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAnalyseAsyncDto**](CreateAnalyseAsyncDto.md)|  | [optional] 

### Return type

[**AsyncAnalyseResponseDto**](AsyncAnalyseResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_analyses_for_langs**
> AsyncAnalyseListResponseDto create_analyses_for_langs(body=body)

Create analyses by languages



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalysisApi()
body = memsource_cli.CreateAnalyseListAsyncDto() # CreateAnalyseListAsyncDto |  (optional)

try:
    # Create analyses by languages
    api_response = api_instance.create_analyses_for_langs(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->create_analyses_for_langs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAnalyseListAsyncDto**](CreateAnalyseListAsyncDto.md)|  | [optional] 

### Return type

[**AsyncAnalyseListResponseDto**](AsyncAnalyseListResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_analyses_for_providers**
> AsyncAnalyseListResponseDto create_analyses_for_providers(body=body)

Create analyses by providers



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalysisApi()
body = memsource_cli.CreateAnalyseListAsyncDto() # CreateAnalyseListAsyncDto |  (optional)

try:
    # Create analyses by providers
    api_response = api_instance.create_analyses_for_providers(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->create_analyses_for_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAnalyseListAsyncDto**](CreateAnalyseListAsyncDto.md)|  | [optional] 

### Return type

[**AsyncAnalyseListResponseDto**](AsyncAnalyseListResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(analyse_id, purge=purge)

Delete analysis



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalysisApi()
analyse_id = 'analyse_id_example' # str | 
purge = true # bool |  (optional)

try:
    # Delete analysis
    api_instance.delete(analyse_id, purge=purge)
except ApiException as e:
    print("Exception when calling AnalysisApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyse_id** | **str**|  | 
 **purge** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_analyse**
> download_analyse(analyse_id, format)

Download analysis



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalysisApi()
analyse_id = 789 # int | 
format = 'format_example' # str | 

try:
    # Download analysis
    api_instance.download_analyse(analyse_id, format)
except ApiException as e:
    print("Exception when calling AnalysisApi->download_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyse_id** | **int**|  | 
 **format** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analyse_language_part**
> AnalyseLanguagePartDto get_analyse_language_part(analyse_id, analyse_language_part_id)

Get analysis language part

Returns analysis language pair

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalysisApi()
analyse_id = 789 # int | 
analyse_language_part_id = 789 # int | 

try:
    # Get analysis language part
    api_response = api_instance.get_analyse_language_part(analyse_id, analyse_language_part_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->get_analyse_language_part: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyse_id** | **int**|  | 
 **analyse_language_part_id** | **int**|  | 

### Return type

[**AnalyseLanguagePartDto**](AnalyseLanguagePartDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analyse_v2**
> AnalyseV2Dto get_analyse_v2(analyse_id)

Get analysis



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalysisApi()
analyse_id = 789 # int | 

try:
    # Get analysis
    api_response = api_instance.get_analyse_v2(analyse_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->get_analyse_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyse_id** | **int**|  | 

### Return type

[**AnalyseV2Dto**](AnalyseV2Dto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_part_analyse**
> AnalyseJobDto get_job_part_analyse(analyse_id, job_uid)

Get jobs analysis

Returns job's analyse

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalysisApi()
analyse_id = 789 # int | 
job_uid = 'job_uid_example' # str | 

try:
    # Get jobs analysis
    api_response = api_instance.get_job_part_analyse(analyse_id, job_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->get_job_part_analyse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyse_id** | **int**|  | 
 **job_uid** | **str**|  | 

### Return type

[**AnalyseJobDto**](AnalyseJobDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_by_project_v2**
> PageDtoAnalyseV2Dto list_by_project_v2(project_uid, page_number=page_number, page_size=page_size)

List analyses by project



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalysisApi()
project_uid = 'project_uid_example' # str | 
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List analyses by project
    api_response = api_instance.list_by_project_v2(project_uid, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->list_by_project_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoAnalyseV2Dto**](PageDtoAnalyseV2Dto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_job_parts**
> PageDtoAnalyseJobDto list_job_parts(analyse_id, analyse_language_part_id, page_number=page_number, page_size=page_size)

List jobs of analyses

Returns list of job's analyses

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalysisApi()
analyse_id = 789 # int | 
analyse_language_part_id = 789 # int | 
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List jobs of analyses
    api_response = api_instance.list_job_parts(analyse_id, analyse_language_part_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->list_job_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyse_id** | **int**|  | 
 **analyse_language_part_id** | **int**|  | 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoAnalyseJobDto**](PageDtoAnalyseJobDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_part_analyse1**
> PageDtoAnalyseV2Dto list_part_analyse1(project_uid, job_uid, page_number=page_number, page_size=page_size)

List analyses



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AnalysisApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    # List analyses
    api_response = api_instance.list_part_analyse1(project_uid, job_uid, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalysisApi->list_part_analyse1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoAnalyseV2Dto**](PageDtoAnalyseV2Dto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

