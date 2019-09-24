# memsource_cli.TranslationMemoryApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_target_lang_to_trans_memory**](TranslationMemoryApi.md#add_target_lang_to_trans_memory) | **POST** /api2/v1/transMemories/{transMemoryId}/targetLanguages | Add target language to translation memory
[**clear_trans_memory**](TranslationMemoryApi.md#clear_trans_memory) | **DELETE** /api2/v1/transMemories/{transMemoryId}/segments | Delete all segments
[**create_trans_memory**](TranslationMemoryApi.md#create_trans_memory) | **POST** /api2/v1/transMemories | Create translation memory
[**delete_source_and_translations**](TranslationMemoryApi.md#delete_source_and_translations) | **DELETE** /api2/v1/transMemories/{transMemoryId}/segments/{segmentId} | Delete both source and translation
[**delete_trans_memory**](TranslationMemoryApi.md#delete_trans_memory) | **DELETE** /api2/v1/transMemories/{transMemoryId} | Delete translation memory
[**delete_translation**](TranslationMemoryApi.md#delete_translation) | **DELETE** /api2/v1/transMemories/{transMemoryId}/segments/{segmentId}/lang/{lang} | Delete segment of given language
[**download_search_result**](TranslationMemoryApi.md#download_search_result) | **GET** /api2/v1/transMemories/downloadExport/{asyncRequestId} | Download export
[**edit_trans_memory**](TranslationMemoryApi.md#edit_trans_memory) | **PUT** /api2/v1/transMemories/{transMemoryId} | Edit translation memory
[**export**](TranslationMemoryApi.md#export) | **GET** /api2/v1/transMemories/{transMemoryId}/export | Export translation memory
[**export_by_query_async**](TranslationMemoryApi.md#export_by_query_async) | **POST** /api2/v1/transMemories/{transMemoryId}/exportByQueryAsync | Search translation memory
[**get_background_tasks**](TranslationMemoryApi.md#get_background_tasks) | **GET** /api2/v1/transMemories/{transMemoryId}/lastBackgroundTask | Get last task information
[**get_metadata**](TranslationMemoryApi.md#get_metadata) | **GET** /api2/v1/transMemories/{transMemoryId}/metadata | Get translation memory metadata
[**get_project_template_trans_memories**](TranslationMemoryApi.md#get_project_template_trans_memories) | **GET** /api2/v1/projectTemplates/{projectTemplateId}/transMemories | Get translation memories
[**get_related_projects**](TranslationMemoryApi.md#get_related_projects) | **GET** /api2/v1/transMemories/{transMemoryId}/relatedProjects | List related projects
[**get_trans_memory**](TranslationMemoryApi.md#get_trans_memory) | **GET** /api2/v1/transMemories/{transMemoryId} | Get translation memory
[**get_translation_resources**](TranslationMemoryApi.md#get_translation_resources) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translationResources | Get translation resources
[**import_trans_memory**](TranslationMemoryApi.md#import_trans_memory) | **POST** /api2/v1/transMemories/{transMemoryId}/import | Import segments
[**insert_to_trans_memory**](TranslationMemoryApi.md#insert_to_trans_memory) | **POST** /api2/v1/transMemories/{transMemoryId}/segments | Insert segment
[**list_trans_memories**](TranslationMemoryApi.md#list_trans_memories) | **GET** /api2/v1/transMemories | List translation memories
[**search**](TranslationMemoryApi.md#search) | **POST** /api2/v1/transMemories/{transMemoryId}/search | Search translation memory (sync)
[**search_by_job3**](TranslationMemoryApi.md#search_by_job3) | **POST** /api2/v3/projects/{projectUid}/jobs/{jobUid}/transMemories/search | Search job&#39;s translation memories
[**search_segment**](TranslationMemoryApi.md#search_segment) | **POST** /api2/v1/projects/{projectUid}/transMemories/searchSegmentInProject | Search translation memory for segment in the project
[**search_segment_by_job**](TranslationMemoryApi.md#search_segment_by_job) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/transMemories/searchSegment | Search translation memory for segment by job
[**set_project_template_trans_memories**](TranslationMemoryApi.md#set_project_template_trans_memories) | **PUT** /api2/v1/projectTemplates/{projectTemplateId}/transMemories | Edit translation memories
[**update_translation**](TranslationMemoryApi.md#update_translation) | **PUT** /api2/v1/transMemories/{transMemoryId}/segments/{segmentId} | Edit segment
[**wild_card_search_by_job3**](TranslationMemoryApi.md#wild_card_search_by_job3) | **POST** /api2/v3/projects/{projectUid}/jobs/{jobUid}/transMemories/wildCardSearch | Wildcard search job&#39;s translation memories
[**wildcard_search**](TranslationMemoryApi.md#wildcard_search) | **POST** /api2/v1/transMemories/{transMemoryId}/wildCardSearch | Wildcard search


# **add_target_lang_to_trans_memory**
> TransMemoryDto add_target_lang_to_trans_memory(trans_memory_id, body=body)

Add target language to translation memory



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
body = memsource_cli.TargetLanguageDto() # TargetLanguageDto |  (optional)

try:
    # Add target language to translation memory
    api_response = api_instance.add_target_lang_to_trans_memory(trans_memory_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->add_target_lang_to_trans_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **body** | [**TargetLanguageDto**](TargetLanguageDto.md)|  | [optional] 

### Return type

[**TransMemoryDto**](TransMemoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_trans_memory**
> clear_trans_memory(trans_memory_id)

Delete all segments



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 

try:
    # Delete all segments
    api_instance.clear_trans_memory(trans_memory_id)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->clear_trans_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_trans_memory**
> TransMemoryDto create_trans_memory(body=body)

Create translation memory



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
body = memsource_cli.TransMemoryCreateDto() # TransMemoryCreateDto |  (optional)

try:
    # Create translation memory
    api_response = api_instance.create_trans_memory(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->create_trans_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransMemoryCreateDto**](TransMemoryCreateDto.md)|  | [optional] 

### Return type

[**TransMemoryDto**](TransMemoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source_and_translations**
> delete_source_and_translations(trans_memory_id, segment_id)

Delete both source and translation



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
segment_id = 'segment_id_example' # str | 

try:
    # Delete both source and translation
    api_instance.delete_source_and_translations(trans_memory_id, segment_id)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->delete_source_and_translations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **segment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_trans_memory**
> delete_trans_memory(trans_memory_id, purge=purge)

Delete translation memory



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
purge = false # bool |  (optional) (default to false)

try:
    # Delete translation memory
    api_instance.delete_trans_memory(trans_memory_id, purge=purge)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->delete_trans_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **purge** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_translation**
> delete_translation(trans_memory_id, segment_id, lang)

Delete segment of given language



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
segment_id = 'segment_id_example' # str | 
lang = 'lang_example' # str | 

try:
    # Delete segment of given language
    api_instance.delete_translation(trans_memory_id, segment_id, lang)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->delete_translation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **segment_id** | **str**|  | 
 **lang** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_search_result**
> download_search_result(async_request_id, format=format)

Download export



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
async_request_id = 'async_request_id_example' # str | Request ID
format = 'TMX' # str |  (optional) (default to TMX)

try:
    # Download export
    api_instance.download_search_result(async_request_id, format=format)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->download_search_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_request_id** | **str**| Request ID | 
 **format** | **str**|  | [optional] [default to TMX]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_trans_memory**
> TransMemoryDto edit_trans_memory(trans_memory_id, body=body)

Edit translation memory



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
body = memsource_cli.TransMemoryEditDto() # TransMemoryEditDto |  (optional)

try:
    # Edit translation memory
    api_response = api_instance.edit_trans_memory(trans_memory_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->edit_trans_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **body** | [**TransMemoryEditDto**](TransMemoryEditDto.md)|  | [optional] 

### Return type

[**TransMemoryDto**](TransMemoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export**
> export(trans_memory_id, format=format, target_lang=target_lang)

Export translation memory



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
format = 'TMX' # str |  (optional) (default to TMX)
target_lang = ['target_lang_example'] # list[str] |  (optional)

try:
    # Export translation memory
    api_instance.export(trans_memory_id, format=format, target_lang=target_lang)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **format** | **str**|  | [optional] [default to TMX]
 **target_lang** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_by_query_async**
> AsyncExportTMResponseDto export_by_query_async(trans_memory_id, body=body)

Search translation memory

Use GET searchExport/{asyncRequestId} to download result

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
body = memsource_cli.ExportByQueryDto() # ExportByQueryDto |  (optional)

try:
    # Search translation memory
    api_response = api_instance.export_by_query_async(trans_memory_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->export_by_query_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **body** | [**ExportByQueryDto**](ExportByQueryDto.md)|  | [optional] 

### Return type

[**AsyncExportTMResponseDto**](AsyncExportTMResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_background_tasks**
> BackgroundTasksTmDto get_background_tasks(trans_memory_id)

Get last task information



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 

try:
    # Get last task information
    api_response = api_instance.get_background_tasks(trans_memory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->get_background_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 

### Return type

[**BackgroundTasksTmDto**](BackgroundTasksTmDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> MetadataResponse get_metadata(trans_memory_id, by_language=by_language)

Get translation memory metadata



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
by_language = false # bool |  (optional) (default to false)

try:
    # Get translation memory metadata
    api_response = api_instance.get_metadata(trans_memory_id, by_language=by_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->get_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **by_language** | **bool**|  | [optional] [default to false]

### Return type

[**MetadataResponse**](MetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_template_trans_memories**
> ProjectTemplateTransMemoryListDto get_project_template_trans_memories(project_template_id)

Get translation memories



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
project_template_id = 'project_template_id_example' # str | 

try:
    # Get translation memories
    api_response = api_instance.get_project_template_trans_memories(project_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->get_project_template_trans_memories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_id** | **str**|  | 

### Return type

[**ProjectTemplateTransMemoryListDto**](ProjectTemplateTransMemoryListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_related_projects**
> PageDtoAbstractProjectDto get_related_projects(trans_memory_id, page_number=page_number, page_size=page_size)

List related projects



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List related projects
    api_response = api_instance.get_related_projects(trans_memory_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->get_related_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoAbstractProjectDto**](PageDtoAbstractProjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trans_memory**
> TransMemoryDto get_trans_memory(trans_memory_id)

Get translation memory



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 

try:
    # Get translation memory
    api_response = api_instance.get_trans_memory(trans_memory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->get_trans_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 

### Return type

[**TransMemoryDto**](TransMemoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_translation_resources**
> TranslationResourcesDto get_translation_resources(project_uid, job_uid)

Get translation resources



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 

try:
    # Get translation resources
    api_response = api_instance.get_translation_resources(project_uid, job_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->get_translation_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

### Return type

[**TranslationResourcesDto**](TranslationResourcesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_trans_memory**
> ImportResponse import_trans_memory(trans_memory_id, content_disposition, body=body, strict_lang_matching=strict_lang_matching, strip_native_codes=strip_native_codes, exclude_not_confirmed_segments=exclude_not_confirmed_segments)

Import segments



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
content_disposition = 'content_disposition_example' # str | must match pattern `filename\\*=UTF-8''(.+)`
body = memsource_cli.InputStream() # InputStream |  (optional)
strict_lang_matching = false # bool |  (optional) (default to false)
strip_native_codes = true # bool |  (optional) (default to true)
exclude_not_confirmed_segments = false # bool |  (optional) (default to false)

try:
    # Import segments
    api_response = api_instance.import_trans_memory(trans_memory_id, content_disposition, body=body, strict_lang_matching=strict_lang_matching, strip_native_codes=strip_native_codes, exclude_not_confirmed_segments=exclude_not_confirmed_segments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->import_trans_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **content_disposition** | **str**| must match pattern &#x60;filename\\*&#x3D;UTF-8&#39;&#39;(.+)&#x60; | 
 **body** | [**InputStream**](InputStream.md)|  | [optional] 
 **strict_lang_matching** | **bool**|  | [optional] [default to false]
 **strip_native_codes** | **bool**|  | [optional] [default to true]
 **exclude_not_confirmed_segments** | **bool**|  | [optional] [default to false]

### Return type

[**ImportResponse**](ImportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_to_trans_memory**
> insert_to_trans_memory(trans_memory_id, body=body)

Insert segment



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
body = memsource_cli.SegmentDto() # SegmentDto |  (optional)

try:
    # Insert segment
    api_instance.insert_to_trans_memory(trans_memory_id, body=body)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->insert_to_trans_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **body** | [**SegmentDto**](SegmentDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trans_memories**
> PageDtoTransMemoryDto list_trans_memories(name=name, source_lang=source_lang, target_lang=target_lang, client_id=client_id, domain_id=domain_id, sub_domain_id=sub_domain_id, business_unit_id=business_unit_id, page_number=page_number, page_size=page_size)

List translation memories



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
name = 'name_example' # str |  (optional)
source_lang = 'source_lang_example' # str |  (optional)
target_lang = 'target_lang_example' # str |  (optional)
client_id = 'client_id_example' # str |  (optional)
domain_id = 'domain_id_example' # str |  (optional)
sub_domain_id = 'sub_domain_id_example' # str |  (optional)
business_unit_id = 'business_unit_id_example' # str |  (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List translation memories
    api_response = api_instance.list_trans_memories(name=name, source_lang=source_lang, target_lang=target_lang, client_id=client_id, domain_id=domain_id, sub_domain_id=sub_domain_id, business_unit_id=business_unit_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->list_trans_memories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **source_lang** | **str**|  | [optional] 
 **target_lang** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **domain_id** | **str**|  | [optional] 
 **sub_domain_id** | **str**|  | [optional] 
 **business_unit_id** | **str**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoTransMemoryDto**](PageDtoTransMemoryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResponseListTmDto search(trans_memory_id, body=body)

Search translation memory (sync)



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
body = memsource_cli.SearchRequestDto() # SearchRequestDto |  (optional)

try:
    # Search translation memory (sync)
    api_response = api_instance.search(trans_memory_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **body** | [**SearchRequestDto**](SearchRequestDto.md)|  | [optional] 

### Return type

[**SearchResponseListTmDto**](SearchResponseListTmDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_by_job3**
> SearchResponseListTmDtoV3 search_by_job3(project_uid, job_uid, body=body)

Search job's translation memories



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 
body = memsource_cli.SearchTMByJobRequestDtoV3() # SearchTMByJobRequestDtoV3 |  (optional)

try:
    # Search job's translation memories
    api_response = api_instance.search_by_job3(project_uid, job_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->search_by_job3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**SearchTMByJobRequestDtoV3**](SearchTMByJobRequestDtoV3.md)|  | [optional] 

### Return type

[**SearchResponseListTmDtoV3**](SearchResponseListTmDtoV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_segment**
> SearchResponseListTmDto search_segment(project_uid, body=body)

Search translation memory for segment in the project

Returns at most <i>maxSegments</i>             records with <i>score >= scoreThreshold</i> and at most <i>maxSubsegments</i> records which are subsegment,             i.e. the source text is substring of the query text.

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.SearchTMRequestDto() # SearchTMRequestDto |  (optional)

try:
    # Search translation memory for segment in the project
    api_response = api_instance.search_segment(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->search_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**SearchTMRequestDto**](SearchTMRequestDto.md)|  | [optional] 

### Return type

[**SearchResponseListTmDto**](SearchResponseListTmDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_segment_by_job**
> SearchResponseListTmDto search_segment_by_job(project_uid, job_uid, body=body)

Search translation memory for segment by job

Returns at most <i>maxSegments</i>             records with <i>score >= scoreThreshold</i> and at most <i>maxSubsegments</i> records which are subsegment,             i.e. the source text is substring of the query text.

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 
body = memsource_cli.SearchTMByJobRequestDto() # SearchTMByJobRequestDto |  (optional)

try:
    # Search translation memory for segment by job
    api_response = api_instance.search_segment_by_job(project_uid, job_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->search_segment_by_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**SearchTMByJobRequestDto**](SearchTMByJobRequestDto.md)|  | [optional] 

### Return type

[**SearchResponseListTmDto**](SearchResponseListTmDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_template_trans_memories**
> ProjectTemplateTransMemoryListDto set_project_template_trans_memories(project_template_id, body=body)

Edit translation memories



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
project_template_id = 'project_template_id_example' # str | 
body = memsource_cli.SetProjectTemplateTransMemoriesDto() # SetProjectTemplateTransMemoriesDto |  (optional)

try:
    # Edit translation memories
    api_response = api_instance.set_project_template_trans_memories(project_template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->set_project_template_trans_memories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_id** | **str**|  | 
 **body** | [**SetProjectTemplateTransMemoriesDto**](SetProjectTemplateTransMemoriesDto.md)|  | [optional] 

### Return type

[**ProjectTemplateTransMemoryListDto**](ProjectTemplateTransMemoryListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_translation**
> update_translation(trans_memory_id, segment_id, body=body)

Edit segment



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
segment_id = 'segment_id_example' # str | 
body = memsource_cli.TranslationDto() # TranslationDto |  (optional)

try:
    # Edit segment
    api_instance.update_translation(trans_memory_id, segment_id, body=body)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->update_translation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **segment_id** | **str**|  | 
 **body** | [**TranslationDto**](TranslationDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wild_card_search_by_job3**
> SearchResponseListTmDtoV3 wild_card_search_by_job3(project_uid, job_uid, body=body)

Wildcard search job's translation memories



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 
body = memsource_cli.WildCardSearchByJobRequestDtoV3() # WildCardSearchByJobRequestDtoV3 |  (optional)

try:
    # Wildcard search job's translation memories
    api_response = api_instance.wild_card_search_by_job3(project_uid, job_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->wild_card_search_by_job3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **body** | [**WildCardSearchByJobRequestDtoV3**](WildCardSearchByJobRequestDtoV3.md)|  | [optional] 

### Return type

[**SearchResponseListTmDtoV3**](SearchResponseListTmDtoV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wildcard_search**
> SearchResponseListTmDto wildcard_search(trans_memory_id, body=body)

Wildcard search



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TranslationMemoryApi()
trans_memory_id = 789 # int | 
body = memsource_cli.WildCardSearchRequestDto() # WildCardSearchRequestDto |  (optional)

try:
    # Wildcard search
    api_response = api_instance.wildcard_search(trans_memory_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TranslationMemoryApi->wildcard_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trans_memory_id** | **int**|  | 
 **body** | [**WildCardSearchRequestDto**](WildCardSearchRequestDto.md)|  | [optional] 

### Return type

[**SearchResponseListTmDto**](SearchResponseListTmDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

