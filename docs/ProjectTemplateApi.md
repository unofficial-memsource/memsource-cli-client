# memsource_cli.ProjectTemplateApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_linguists_from_template**](ProjectTemplateApi.md#assign_linguists_from_template) | **POST** /api2/v1/projects/{projectUid}/applyTemplate/{templateId}/assignProviders | Assigns providers from template
[**assign_linguists_from_template_to_job_parts**](ProjectTemplateApi.md#assign_linguists_from_template_to_job_parts) | **POST** /api2/v1/projects/{projectUid}/applyTemplate/{templateId}/assignProviders/forJobParts | Assigns providers from template (specific jobs)
[**assignable_templates**](ProjectTemplateApi.md#assignable_templates) | **GET** /api2/v1/projects/{projectUid}/assignableTemplates | List assignable templates
[**create_project_from_template_v2**](ProjectTemplateApi.md#create_project_from_template_v2) | **POST** /api2/v2/projects/applyTemplate/{templateId} | Create project from template
[**create_project_template**](ProjectTemplateApi.md#create_project_template) | **POST** /api2/v1/projectTemplates | Create project template
[**delete_project_template**](ProjectTemplateApi.md#delete_project_template) | **DELETE** /api2/v1/projectTemplates/{projectTemplateId} | Delete project template
[**edit_project_template**](ProjectTemplateApi.md#edit_project_template) | **PUT** /api2/v1/projectTemplates/{projectTemplateId} | Edit project template
[**get_analyse_settings_for_project_template**](ProjectTemplateApi.md#get_analyse_settings_for_project_template) | **GET** /api2/v1/projectTemplates/{projectTemplateId}/analyseSettings | Get analyse settings
[**get_machine_translate_settings_for_project_template**](ProjectTemplateApi.md#get_machine_translate_settings_for_project_template) | **GET** /api2/v1/projectTemplates/{projectTemplateId}/mtSettings | Get machine translate settings
[**get_pre_translate_settings_for_project_template**](ProjectTemplateApi.md#get_pre_translate_settings_for_project_template) | **GET** /api2/v1/projectTemplates/{projectTemplateId}/preTranslateSettings | Get Pre-translate settings
[**get_project_template**](ProjectTemplateApi.md#get_project_template) | **GET** /api2/v1/projectTemplates/{projectTemplateId} | Get project template
[**get_project_template_term_bases**](ProjectTemplateApi.md#get_project_template_term_bases) | **GET** /api2/v1/projectTemplates/{projectTemplateId}/termBases | Get term bases
[**get_project_template_trans_memories**](ProjectTemplateApi.md#get_project_template_trans_memories) | **GET** /api2/v1/projectTemplates/{projectTemplateId}/transMemories | Get translation memories
[**get_project_templates**](ProjectTemplateApi.md#get_project_templates) | **GET** /api2/v1/projectTemplates | List project templates
[**set_project_template_term_bases**](ProjectTemplateApi.md#set_project_template_term_bases) | **PUT** /api2/v1/projectTemplates/{projectTemplateId}/termBases | Edit term bases in project template
[**set_project_template_trans_memories**](ProjectTemplateApi.md#set_project_template_trans_memories) | **PUT** /api2/v1/projectTemplates/{projectTemplateId}/transMemories | Edit translation memories


# **assign_linguists_from_template**
> JobPartsDto assign_linguists_from_template(template_id, project_uid)

Assigns providers from template



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectTemplateApi()
template_id = 789 # int | 
project_uid = 'project_uid_example' # str | 

try:
    # Assigns providers from template
    api_response = api_instance.assign_linguists_from_template(template_id, project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->assign_linguists_from_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**|  | 
 **project_uid** | **str**|  | 

### Return type

[**JobPartsDto**](JobPartsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_linguists_from_template_to_job_parts**
> JobPartsDto assign_linguists_from_template_to_job_parts(template_id, project_uid, body=body)

Assigns providers from template (specific jobs)



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectTemplateApi()
template_id = 789 # int | 
project_uid = 'project_uid_example' # str | 
body = memsource_cli.JobPartReferences() # JobPartReferences |  (optional)

try:
    # Assigns providers from template (specific jobs)
    api_response = api_instance.assign_linguists_from_template_to_job_parts(template_id, project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->assign_linguists_from_template_to_job_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**|  | 
 **project_uid** | **str**|  | 
 **body** | [**JobPartReferences**](JobPartReferences.md)|  | [optional] 

### Return type

[**JobPartsDto**](JobPartsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignable_templates**
> AssignableTemplatesDto assignable_templates(project_uid)

List assignable templates



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectTemplateApi()
project_uid = 'project_uid_example' # str | 

try:
    # List assignable templates
    api_response = api_instance.assignable_templates(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->assignable_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**AssignableTemplatesDto**](AssignableTemplatesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_from_template_v2**
> AbstractProjectDtoV2 create_project_from_template_v2(template_id, body=body)

Create project from template



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectTemplateApi()
template_id = 789 # int | 
body = memsource_cli.CreateProjectFromTemplateV2Dto() # CreateProjectFromTemplateV2Dto |  (optional)

try:
    # Create project from template
    api_response = api_instance.create_project_from_template_v2(template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->create_project_from_template_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**|  | 
 **body** | [**CreateProjectFromTemplateV2Dto**](CreateProjectFromTemplateV2Dto.md)|  | [optional] 

### Return type

[**AbstractProjectDtoV2**](AbstractProjectDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_template**
> ProjectTemplateDto create_project_template(body)

Create project template



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectTemplateApi()
body = memsource_cli.ProjectTemplateCreateActionDto() # ProjectTemplateCreateActionDto | 

try:
    # Create project template
    api_response = api_instance.create_project_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->create_project_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectTemplateCreateActionDto**](ProjectTemplateCreateActionDto.md)|  | 

### Return type

[**ProjectTemplateDto**](ProjectTemplateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_template**
> delete_project_template(project_template_id)

Delete project template



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectTemplateApi()
project_template_id = 789 # int | 

try:
    # Delete project template
    api_instance.delete_project_template(project_template_id)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->delete_project_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_project_template**
> ProjectTemplateDto edit_project_template(project_template_id, body)

Edit project template



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectTemplateApi()
project_template_id = 789 # int | 
body = memsource_cli.ProjectTemplateEditDto() # ProjectTemplateEditDto | 

try:
    # Edit project template
    api_response = api_instance.edit_project_template(project_template_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->edit_project_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_id** | **int**|  | 
 **body** | [**ProjectTemplateEditDto**](ProjectTemplateEditDto.md)|  | 

### Return type

[**ProjectTemplateDto**](ProjectTemplateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analyse_settings_for_project_template**
> AnalyseSettingsDto get_analyse_settings_for_project_template(project_template_id)

Get analyse settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectTemplateApi()
project_template_id = 'project_template_id_example' # str | 

try:
    # Get analyse settings
    api_response = api_instance.get_analyse_settings_for_project_template(project_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->get_analyse_settings_for_project_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_id** | **str**|  | 

### Return type

[**AnalyseSettingsDto**](AnalyseSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_machine_translate_settings_for_project_template**
> MTSettingsPerLanguageListDto get_machine_translate_settings_for_project_template(project_template_id)

Get machine translate settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectTemplateApi()
project_template_id = 'project_template_id_example' # str | 

try:
    # Get machine translate settings
    api_response = api_instance.get_machine_translate_settings_for_project_template(project_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->get_machine_translate_settings_for_project_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_id** | **str**|  | 

### Return type

[**MTSettingsPerLanguageListDto**](MTSettingsPerLanguageListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pre_translate_settings_for_project_template**
> PreTranslateSettingsDto get_pre_translate_settings_for_project_template(project_template_id)

Get Pre-translate settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectTemplateApi()
project_template_id = 'project_template_id_example' # str | 

try:
    # Get Pre-translate settings
    api_response = api_instance.get_pre_translate_settings_for_project_template(project_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->get_pre_translate_settings_for_project_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_id** | **str**|  | 

### Return type

[**PreTranslateSettingsDto**](PreTranslateSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_template**
> ProjectTemplateDto get_project_template(project_template_id)

Get project template



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectTemplateApi()
project_template_id = 789 # int | 

try:
    # Get project template
    api_response = api_instance.get_project_template(project_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->get_project_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_id** | **int**|  | 

### Return type

[**ProjectTemplateDto**](ProjectTemplateDto.md)

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
api_instance = memsource_cli.ProjectTemplateApi()
project_template_id = 'project_template_id_example' # str | 

try:
    # Get term bases
    api_response = api_instance.get_project_template_term_bases(project_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->get_project_template_term_bases: %s\n" % e)
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
api_instance = memsource_cli.ProjectTemplateApi()
project_template_id = 'project_template_id_example' # str | 

try:
    # Get translation memories
    api_response = api_instance.get_project_template_trans_memories(project_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->get_project_template_trans_memories: %s\n" % e)
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

# **get_project_templates**
> PageDtoProjectTemplateReference get_project_templates(name=name, client_id=client_id, page_number=page_number, page_size=page_size)

List project templates



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectTemplateApi()
name = 'name_example' # str |  (optional)
client_id = 789 # int |  (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List project templates
    api_response = api_instance.get_project_templates(name=name, client_id=client_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->get_project_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **client_id** | **int**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoProjectTemplateReference**](PageDtoProjectTemplateReference.md)

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
api_instance = memsource_cli.ProjectTemplateApi()
project_template_id = 'project_template_id_example' # str | 
body = memsource_cli.SetProjectTemplateTermBaseDto() # SetProjectTemplateTermBaseDto |  (optional)

try:
    # Edit term bases in project template
    api_response = api_instance.set_project_template_term_bases(project_template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->set_project_template_term_bases: %s\n" % e)
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
api_instance = memsource_cli.ProjectTemplateApi()
project_template_id = 'project_template_id_example' # str | 
body = memsource_cli.SetProjectTemplateTransMemoriesDto() # SetProjectTemplateTransMemoriesDto |  (optional)

try:
    # Edit translation memories
    api_response = api_instance.set_project_template_trans_memories(project_template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplateApi->set_project_template_trans_memories: %s\n" % e)
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

