# memsource_cli.TermBaseApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**browse_terms**](TermBaseApi.md#browse_terms) | **POST** /api2/v1/termBases/{termBaseId}/browse | Browse term base
[**clear_term_base**](TermBaseApi.md#clear_term_base) | **DELETE** /api2/v1/termBases/{termBaseId}/terms | Clear term base
[**create_term**](TermBaseApi.md#create_term) | **POST** /api2/v1/termBases/{termBaseId}/terms | Create term
[**create_term_base**](TermBaseApi.md#create_term_base) | **POST** /api2/v1/termBases | Create term base
[**create_term_by_job**](TermBaseApi.md#create_term_by_job) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/termBases/createByJob | Create term in job&#39;s term bases
[**delete_concept**](TermBaseApi.md#delete_concept) | **DELETE** /api2/v1/termBases/{termBaseId}/concepts/{conceptId} | Delete concept
[**delete_concepts**](TermBaseApi.md#delete_concepts) | **DELETE** /api2/v1/termBases/{termBaseId}/concepts | Delete concepts
[**delete_term**](TermBaseApi.md#delete_term) | **DELETE** /api2/v1/termBases/{termBaseId}/terms/{termId} | Delete term
[**delete_term_base**](TermBaseApi.md#delete_term_base) | **DELETE** /api2/v1/termBases/{termBaseId} | Delete term base
[**export_term_base**](TermBaseApi.md#export_term_base) | **GET** /api2/v1/termBases/{termBaseId}/export | Export term base
[**get_last_background_task**](TermBaseApi.md#get_last_background_task) | **GET** /api2/v1/termBases/{termBaseId}/lastBackgroundTask | Last import status
[**get_project_template_term_bases**](TermBaseApi.md#get_project_template_term_bases) | **GET** /api2/v1/projectTemplates/{projectTemplateId}/termBases | Get term bases
[**get_term**](TermBaseApi.md#get_term) | **GET** /api2/v1/termBases/{termBaseId}/terms/{termId} | Get term
[**get_term_base**](TermBaseApi.md#get_term_base) | **GET** /api2/v1/termBases/{termBaseId} | Get term base
[**get_term_base_metadata**](TermBaseApi.md#get_term_base_metadata) | **GET** /api2/v1/termBases/{termBaseId}/metadata | Get term base metadata
[**get_translation_resources**](TermBaseApi.md#get_translation_resources) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translationResources | Get translation resources
[**import_term_base**](TermBaseApi.md#import_term_base) | **POST** /api2/v1/termBases/{termBaseId}/upload | Upload term base
[**list_term_bases**](TermBaseApi.md#list_term_bases) | **GET** /api2/v1/termBases | List term bases
[**list_terms_of_concept**](TermBaseApi.md#list_terms_of_concept) | **GET** /api2/v1/termBases/{termBaseId}/concepts/{conceptId}/terms | Get terms of concept
[**search_terms**](TermBaseApi.md#search_terms) | **POST** /api2/v1/termBases/{termBaseId}/search | Search term base
[**search_terms_by_job1**](TermBaseApi.md#search_terms_by_job1) | **POST** /api2/v2/projects/{projectUid}/jobs/{jobUid}/termBases/searchByJob | Search job&#39;s term bases
[**search_terms_in_text_by_job_v2**](TermBaseApi.md#search_terms_in_text_by_job_v2) | **POST** /api2/v2/projects/{projectUid}/jobs/{jobUid}/termBases/searchInTextByJob | Search terms in text
[**set_project_template_term_bases**](TermBaseApi.md#set_project_template_term_bases) | **PUT** /api2/v1/projectTemplates/{projectTemplateId}/termBases | Edit term bases in project template
[**update_term**](TermBaseApi.md#update_term) | **PUT** /api2/v1/termBases/{termBaseId}/terms/{termId} | Edit term
[**update_term_base**](TermBaseApi.md#update_term_base) | **PUT** /api2/v1/termBases/{termBaseId} | Edit term base


# **browse_terms**
> BrowseResponseListDto browse_terms(term_base_id, body=body)

Browse term base



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 
body = memsource_cli.BrowseRequestDto() # BrowseRequestDto |  (optional)

try:
    # Browse term base
    api_response = api_instance.browse_terms(term_base_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->browse_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 
 **body** | [**BrowseRequestDto**](BrowseRequestDto.md)|  | [optional] 

### Return type

[**BrowseResponseListDto**](BrowseResponseListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_term_base**
> clear_term_base(term_base_id)

Clear term base

Deletes all terms

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 

try:
    # Clear term base
    api_instance.clear_term_base(term_base_id)
except ApiException as e:
    print("Exception when calling TermBaseApi->clear_term_base: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_term**
> TermDto create_term(term_base_id, body=body)

Create term

Set conceptId to assign the term to an existing concept, otherwise a new concept will be created.

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 
body = memsource_cli.TermCreateDto() # TermCreateDto |  (optional)

try:
    # Create term
    api_response = api_instance.create_term(term_base_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->create_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 
 **body** | [**TermCreateDto**](TermCreateDto.md)|  | [optional] 

### Return type

[**TermDto**](TermDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_term_base**
> TermBaseDto create_term_base(body=body)

Create term base



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
body = memsource_cli.TermBaseEditDto() # TermBaseEditDto |  (optional)

try:
    # Create term base
    api_response = api_instance.create_term_base(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->create_term_base: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TermBaseEditDto**](TermBaseEditDto.md)|  | [optional] 

### Return type

[**TermBaseDto**](TermBaseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_term_by_job**
> TermPairDto create_term_by_job(job_uid, project_uid, body=body)

Create term in job's term bases

Create new term in the write term base assigned to the job

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
job_uid = 'job_uid_example' # str | 
project_uid = 'project_uid_example' # str | 
body = memsource_cli.CreateTermsDto() # CreateTermsDto |  (optional)

try:
    # Create term in job's term bases
    api_response = api_instance.create_term_by_job(job_uid, project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->create_term_by_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **project_uid** | **str**|  | 
 **body** | [**CreateTermsDto**](CreateTermsDto.md)|  | [optional] 

### Return type

[**TermPairDto**](TermPairDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_concept**
> delete_concept(term_base_id, concept_id)

Delete concept



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 
concept_id = 'concept_id_example' # str | 

try:
    # Delete concept
    api_instance.delete_concept(term_base_id, concept_id)
except ApiException as e:
    print("Exception when calling TermBaseApi->delete_concept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 
 **concept_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_concepts**
> delete_concepts(term_base_id, body=body)

Delete concepts



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 
body = memsource_cli.ConceptListReference() # ConceptListReference |  (optional)

try:
    # Delete concepts
    api_instance.delete_concepts(term_base_id, body=body)
except ApiException as e:
    print("Exception when calling TermBaseApi->delete_concepts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 
 **body** | [**ConceptListReference**](ConceptListReference.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_term**
> delete_term(term_base_id, term_id)

Delete term



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 
term_id = 'term_id_example' # str | 

try:
    # Delete term
    api_instance.delete_term(term_base_id, term_id)
except ApiException as e:
    print("Exception when calling TermBaseApi->delete_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 
 **term_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_term_base**
> delete_term_base(term_base_id, purge=purge)

Delete term base



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 
purge = false # bool | purge=false - the Termbase is can later be restored,                      \"purge=true - the Termbase is completely deleted and cannot be restored (optional) (default to false)

try:
    # Delete term base
    api_instance.delete_term_base(term_base_id, purge=purge)
except ApiException as e:
    print("Exception when calling TermBaseApi->delete_term_base: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 
 **purge** | **bool**| purge&#x3D;false - the Termbase is can later be restored,                      \&quot;purge&#x3D;true - the Termbase is completely deleted and cannot be restored | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_term_base**
> export_term_base(term_base_id, format=format, charset=charset)

Export term base



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 
format = 'Tbx' # str |  (optional) (default to Tbx)
charset = 'UTF-8' # str |  (optional) (default to UTF-8)

try:
    # Export term base
    api_instance.export_term_base(term_base_id, format=format, charset=charset)
except ApiException as e:
    print("Exception when calling TermBaseApi->export_term_base: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 
 **format** | **str**|  | [optional] [default to Tbx]
 **charset** | **str**|  | [optional] [default to UTF-8]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_background_task**
> BackgroundTasksTbDto get_last_background_task(term_base_id)

Last import status



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 

try:
    # Last import status
    api_response = api_instance.get_last_background_task(term_base_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->get_last_background_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 

### Return type

[**BackgroundTasksTbDto**](BackgroundTasksTbDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_template_term_bases**
> ProjectTemplateTermBaseListDto get_project_template_term_bases(project_template_id)

Get term bases



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
project_template_id = 'project_template_id_example' # str | 

try:
    # Get term bases
    api_response = api_instance.get_project_template_term_bases(project_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->get_project_template_term_bases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_id** | **str**|  | 

### Return type

[**ProjectTemplateTermBaseListDto**](ProjectTemplateTermBaseListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_term**
> TermDto get_term(term_base_id, term_id)

Get term



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 
term_id = 'term_id_example' # str | 

try:
    # Get term
    api_response = api_instance.get_term(term_base_id, term_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->get_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 
 **term_id** | **str**|  | 

### Return type

[**TermDto**](TermDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_term_base**
> TermBaseDto get_term_base(term_base_id)

Get term base



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 

try:
    # Get term base
    api_response = api_instance.get_term_base(term_base_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->get_term_base: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 

### Return type

[**TermBaseDto**](TermBaseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_term_base_metadata**
> MetadataTbDto get_term_base_metadata(term_base_id)

Get term base metadata



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 

try:
    # Get term base metadata
    api_response = api_instance.get_term_base_metadata(term_base_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->get_term_base_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 

### Return type

[**MetadataTbDto**](MetadataTbDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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
api_instance = memsource_cli.TermBaseApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 

try:
    # Get translation resources
    api_response = api_instance.get_translation_resources(project_uid, job_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->get_translation_resources: %s\n" % e)
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

# **import_term_base**
> ImportResponse import_term_base(content_disposition, term_base_id, body=body, charset=charset, strict_lang_matching=strict_lang_matching, update_terms=update_terms)

Upload term base

 Terms can be imported from XLS/XLSX and TBX file formats into a term base. See <a target=\"_blank\" href=\"https://help.memsource.com/hc/en-us/articles/115003681851-Term-Bases\">Memsource Wiki</a> 

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
content_disposition = 'content_disposition_example' # str | must match pattern `filename\\*=UTF-8''(.+)`
term_base_id = 789 # int | 
body = memsource_cli.InputStream() # InputStream |  (optional)
charset = 'UTF-8' # str |  (optional) (default to UTF-8)
strict_lang_matching = false # bool |  (optional) (default to false)
update_terms = true # bool |  (optional) (default to true)

try:
    # Upload term base
    api_response = api_instance.import_term_base(content_disposition, term_base_id, body=body, charset=charset, strict_lang_matching=strict_lang_matching, update_terms=update_terms)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->import_term_base: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_disposition** | **str**| must match pattern &#x60;filename\\*&#x3D;UTF-8&#39;&#39;(.+)&#x60; | 
 **term_base_id** | **int**|  | 
 **body** | [**InputStream**](InputStream.md)|  | [optional] 
 **charset** | **str**|  | [optional] [default to UTF-8]
 **strict_lang_matching** | **bool**|  | [optional] [default to false]
 **update_terms** | **bool**|  | [optional] [default to true]

### Return type

[**ImportResponse**](ImportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_term_bases**
> PageDtoTermBaseDto list_term_bases(name=name, lang=lang, client_id=client_id, domain_id=domain_id, sub_domain_id=sub_domain_id, page_number=page_number, page_size=page_size)

List term bases



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
name = 'name_example' # str |  (optional)
lang = ['lang_example'] # list[str] | Language of the term base (optional)
client_id = 'client_id_example' # str |  (optional)
domain_id = 'domain_id_example' # str |  (optional)
sub_domain_id = 'sub_domain_id_example' # str |  (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List term bases
    api_response = api_instance.list_term_bases(name=name, lang=lang, client_id=client_id, domain_id=domain_id, sub_domain_id=sub_domain_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->list_term_bases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **lang** | [**list[str]**](str.md)| Language of the term base | [optional] 
 **client_id** | **str**|  | [optional] 
 **domain_id** | **str**|  | [optional] 
 **sub_domain_id** | **str**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoTermBaseDto**](PageDtoTermBaseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_terms_of_concept**
> ConceptDto list_terms_of_concept(term_base_id, concept_id)

Get terms of concept



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 
concept_id = 'concept_id_example' # str | 

try:
    # Get terms of concept
    api_response = api_instance.list_terms_of_concept(term_base_id, concept_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->list_terms_of_concept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 
 **concept_id** | **str**|  | 

### Return type

[**ConceptDto**](ConceptDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_terms**
> SearchResponseListTbDto search_terms(term_base_id, body=body)

Search term base



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 
body = memsource_cli.TermBaseSearchRequestDto() # TermBaseSearchRequestDto |  (optional)

try:
    # Search term base
    api_response = api_instance.search_terms(term_base_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->search_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 
 **body** | [**TermBaseSearchRequestDto**](TermBaseSearchRequestDto.md)|  | [optional] 

### Return type

[**SearchResponseListTbDto**](SearchResponseListTbDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_terms_by_job1**
> SearchTbResponseListDto search_terms_by_job1(job_uid, project_uid, body=body)

Search job's term bases

Search all read term bases assigned to the job

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
job_uid = 'job_uid_example' # str | 
project_uid = 'project_uid_example' # str | 
body = memsource_cli.SearchTbByJobRequestDto() # SearchTbByJobRequestDto |  (optional)

try:
    # Search job's term bases
    api_response = api_instance.search_terms_by_job1(job_uid, project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->search_terms_by_job1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **project_uid** | **str**|  | 
 **body** | [**SearchTbByJobRequestDto**](SearchTbByJobRequestDto.md)|  | [optional] 

### Return type

[**SearchTbResponseListDto**](SearchTbResponseListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_terms_in_text_by_job_v2**
> SearchInTextResponseList2Dto search_terms_in_text_by_job_v2(job_uid, project_uid, body=body)

Search terms in text

Search in text in all read term bases assigned to the job

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
job_uid = 'job_uid_example' # str | 
project_uid = 'project_uid_example' # str | 
body = memsource_cli.SearchTbInTextByJobRequestDto() # SearchTbInTextByJobRequestDto |  (optional)

try:
    # Search terms in text
    api_response = api_instance.search_terms_in_text_by_job_v2(job_uid, project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->search_terms_in_text_by_job_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **project_uid** | **str**|  | 
 **body** | [**SearchTbInTextByJobRequestDto**](SearchTbInTextByJobRequestDto.md)|  | [optional] 

### Return type

[**SearchInTextResponseList2Dto**](SearchInTextResponseList2Dto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_template_term_bases**
> ProjectTemplateTermBaseListDto set_project_template_term_bases(project_template_id, body=body)

Edit term bases in project template



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
project_template_id = 'project_template_id_example' # str | 
body = memsource_cli.SetProjectTemplateTermBaseDto() # SetProjectTemplateTermBaseDto |  (optional)

try:
    # Edit term bases in project template
    api_response = api_instance.set_project_template_term_bases(project_template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->set_project_template_term_bases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_id** | **str**|  | 
 **body** | [**SetProjectTemplateTermBaseDto**](SetProjectTemplateTermBaseDto.md)|  | [optional] 

### Return type

[**ProjectTemplateTermBaseListDto**](ProjectTemplateTermBaseListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_term**
> TermDto update_term(term_base_id, term_id, body=body)

Edit term



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 
term_id = 'term_id_example' # str | 
body = memsource_cli.TermEditDto() # TermEditDto |  (optional)

try:
    # Edit term
    api_response = api_instance.update_term(term_base_id, term_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->update_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 
 **term_id** | **str**|  | 
 **body** | [**TermEditDto**](TermEditDto.md)|  | [optional] 

### Return type

[**TermDto**](TermDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_term_base**
> TermBaseDto update_term_base(term_base_id, body=body)

Edit term base

It is possible to add new languages only

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.TermBaseApi()
term_base_id = 789 # int | 
body = memsource_cli.TermBaseEditDto() # TermBaseEditDto |  (optional)

try:
    # Edit term base
    api_response = api_instance.update_term_base(term_base_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TermBaseApi->update_term_base: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_base_id** | **int**|  | 
 **body** | [**TermBaseEditDto**](TermBaseEditDto.md)|  | [optional] 

### Return type

[**TermBaseDto**](TermBaseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

