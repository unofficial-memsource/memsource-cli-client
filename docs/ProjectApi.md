# memsource_cli.ProjectApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_target_language_to_project**](ProjectApi.md#add_target_language_to_project) | **POST** /api2/v1/projects/{projectUid}/targetLangs | Add target languages
[**add_workflow_steps**](ProjectApi.md#add_workflow_steps) | **POST** /api2/v1/projects/{projectUid}/workflowSteps | Add workflow steps
[**assign_linguists_from_template**](ProjectApi.md#assign_linguists_from_template) | **POST** /api2/v1/projects/{projectUid}/applyTemplate/{templateId}/assignProviders | Assigns providers from template
[**assign_linguists_from_template_to_job_parts**](ProjectApi.md#assign_linguists_from_template_to_job_parts) | **POST** /api2/v1/projects/{projectUid}/applyTemplate/{templateId}/assignProviders/forJobParts | Assigns providers from template (specific jobs)
[**assign_vendor_to_project**](ProjectApi.md#assign_vendor_to_project) | **POST** /api2/v1/projects/{projectUid}/assignVendor | Assign vendor
[**assignable_templates**](ProjectApi.md#assignable_templates) | **GET** /api2/v1/projects/{projectUid}/assignableTemplates | List assignable templates
[**clone_project**](ProjectApi.md#clone_project) | **POST** /api2/v1/projects/{projectUid}/clone | Clone project
[**create_note_ref**](ProjectApi.md#create_note_ref) | **POST** /api2/v1/projects/{projectUid}/references | Create project reference file
[**create_project**](ProjectApi.md#create_project) | **POST** /api2/v1/projects | Create project
[**create_project_from_template_v2**](ProjectApi.md#create_project_from_template_v2) | **POST** /api2/v2/projects/applyTemplate/{templateId} | Create project from template
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /api2/v1/projects/{projectUid} | Delete project
[**download_reference**](ProjectApi.md#download_reference) | **GET** /api2/v1/projects/{projectUid}/references/{referenceFileId} | Get project reference
[**edit_project**](ProjectApi.md#edit_project) | **PUT** /api2/v1/projects/{projectUid} | Edit project
[**edit_project_access_settings**](ProjectApi.md#edit_project_access_settings) | **PUT** /api2/v1/projects/{projectUid}/accessSettings | Edit access and security settings
[**enabled_quality_checks**](ProjectApi.md#enabled_quality_checks) | **GET** /api2/v1/projects/{projectUid}/qaSettingsChecks | Get QA checks
[**get_analyse_settings_for_project**](ProjectApi.md#get_analyse_settings_for_project) | **GET** /api2/v1/projects/{projectUid}/analyseSettings | Get analyse settings
[**get_financial_settings**](ProjectApi.md#get_financial_settings) | **GET** /api2/v1/projects/{projectUid}/financialSettings | Get financial settings
[**get_import_settings2**](ProjectApi.md#get_import_settings2) | **GET** /api2/v1/projects/{projectUid}/importSettings | Get projects&#39;s default import settings
[**get_mt_settings_for_project**](ProjectApi.md#get_mt_settings_for_project) | **GET** /api2/v1/projects/{projectUid}/mtSettings | Get machine translate settings
[**get_pre_translate_settings_for_project**](ProjectApi.md#get_pre_translate_settings_for_project) | **GET** /api2/v1/projects/{projectUid}/preTranslateSettings | Get Pre-translate settings
[**get_project**](ProjectApi.md#get_project) | **GET** /api2/v1/projects/{projectUid} | Get project
[**get_project_access_settings**](ProjectApi.md#get_project_access_settings) | **GET** /api2/v1/projects/{projectUid}/accessSettings | Get access and security settings
[**get_project_assignments**](ProjectApi.md#get_project_assignments) | **GET** /api2/v1/projects/{projectUid}/providers | List project providers
[**get_project_qa_settings_v2**](ProjectApi.md#get_project_qa_settings_v2) | **GET** /api2/v2/projects/{projectUid}/qaSettings | Get quality assurance settings
[**get_project_settings**](ProjectApi.md#get_project_settings) | **GET** /api2/v1/projects/{projectUid}/lqaSettings | Get LQA settings
[**get_project_term_bases**](ProjectApi.md#get_project_term_bases) | **GET** /api2/v1/projects/{projectUid}/termBases | Get term bases
[**get_project_trans_memories**](ProjectApi.md#get_project_trans_memories) | **GET** /api2/v1/projects/{projectUid}/transMemories | Get translation memories
[**get_project_workflow_steps**](ProjectApi.md#get_project_workflow_steps) | **GET** /api2/v1/projects/{projectUid}/workflowSteps | Get workflow steps
[**get_quotes_for_project**](ProjectApi.md#get_quotes_for_project) | **GET** /api2/v1/projects/{projectUid}/quotes | List quotes
[**list_assigned_projects**](ProjectApi.md#list_assigned_projects) | **GET** /api2/v1/users/{userId}/projects | List assigned projects
[**list_by_project_v2**](ProjectApi.md#list_by_project_v2) | **GET** /api2/v2/projects/{projectUid}/analyses | List analyses by project
[**list_projects**](ProjectApi.md#list_projects) | **GET** /api2/v1/projects | List projects
[**list_providers**](ProjectApi.md#list_providers) | **POST** /api2/v1/projects/{projectUid}/providers/suggest | Get suggested providers
[**search_segment**](ProjectApi.md#search_segment) | **POST** /api2/v1/projects/{projectUid}/transMemories/searchSegmentInProject | Search translation memory for segment in the project
[**set_financial_settings**](ProjectApi.md#set_financial_settings) | **PUT** /api2/v1/projects/{projectUid}/financialSettings | Edit financial settings
[**set_mt_settings_for_project**](ProjectApi.md#set_mt_settings_for_project) | **PUT** /api2/v1/projects/{projectUid}/mtSettings | Edit machine translate settings
[**set_mt_settings_per_language_for_project**](ProjectApi.md#set_mt_settings_per_language_for_project) | **PUT** /api2/v1/projects/{projectUid}/mtSettingsPerLanguage | Edit machine translate settings per language
[**set_project_qa_settings_v2**](ProjectApi.md#set_project_qa_settings_v2) | **PUT** /api2/v2/projects/{projectUid}/qaSettings | Edit quality assurance settings
[**set_project_status**](ProjectApi.md#set_project_status) | **POST** /api2/v1/projects/{projectUid}/setStatus | Edit project status
[**set_project_term_bases**](ProjectApi.md#set_project_term_bases) | **PUT** /api2/v1/projects/{projectUid}/termBases | Edit term bases
[**set_project_trans_memories_v2**](ProjectApi.md#set_project_trans_memories_v2) | **PUT** /api2/v2/projects/{projectUid}/transMemories | Edit translation memories


# **add_target_language_to_project**
> add_target_language_to_project(project_uid, body=body)

Add target languages

Add target languages to project

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.AddTargetLangDto() # AddTargetLangDto |  (optional)

try:
    # Add target languages
    api_instance.add_target_language_to_project(project_uid, body=body)
except ApiException as e:
    print("Exception when calling ProjectApi->add_target_language_to_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**AddTargetLangDto**](AddTargetLangDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_workflow_steps**
> add_workflow_steps(project_uid, body=body)

Add workflow steps



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.AddWorkflowStepsDto() # AddWorkflowStepsDto |  (optional)

try:
    # Add workflow steps
    api_instance.add_workflow_steps(project_uid, body=body)
except ApiException as e:
    print("Exception when calling ProjectApi->add_workflow_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**AddWorkflowStepsDto**](AddWorkflowStepsDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = memsource_cli.ProjectApi()
template_id = 789 # int | 
project_uid = 'project_uid_example' # str | 

try:
    # Assigns providers from template
    api_response = api_instance.assign_linguists_from_template(template_id, project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->assign_linguists_from_template: %s\n" % e)
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
api_instance = memsource_cli.ProjectApi()
template_id = 789 # int | 
project_uid = 'project_uid_example' # str | 
body = memsource_cli.JobPartReferences() # JobPartReferences |  (optional)

try:
    # Assigns providers from template (specific jobs)
    api_response = api_instance.assign_linguists_from_template_to_job_parts(template_id, project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->assign_linguists_from_template_to_job_parts: %s\n" % e)
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

# **assign_vendor_to_project**
> assign_vendor_to_project(project_uid, body=body)

Assign vendor



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.AssignVendorDto() # AssignVendorDto |  (optional)

try:
    # Assign vendor
    api_instance.assign_vendor_to_project(project_uid, body=body)
except ApiException as e:
    print("Exception when calling ProjectApi->assign_vendor_to_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**AssignVendorDto**](AssignVendorDto.md)|  | [optional] 

### Return type

void (empty response body)

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
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # List assignable templates
    api_response = api_instance.assignable_templates(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->assignable_templates: %s\n" % e)
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

# **clone_project**
> AbstractProjectDto clone_project(project_uid, body=body)

Clone project



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.CloneProjectDto() # CloneProjectDto |  (optional)

try:
    # Clone project
    api_response = api_instance.clone_project(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->clone_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**CloneProjectDto**](CloneProjectDto.md)|  | [optional] 

### Return type

[**AbstractProjectDto**](AbstractProjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_note_ref**
> ReferenceFileReference create_note_ref(project_uid, body=body, content_disposition=content_disposition)

Create project reference file

Accepts application/octet-stream or application/json.<br>                                                                     <b>application/json</b> - Note will be converted to .txt.<br>                                                                     <b>application/octet-stream</b> - Content-Disposition header is required

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.CreateReferenceFileNoteDto() # CreateReferenceFileNoteDto |  (optional)
content_disposition = 'content_disposition_example' # str | <b>Required</b> for application/octet-stream.<br> Example: filename*=UTF-8''YourFileName.txt (optional)

try:
    # Create project reference file
    api_response = api_instance.create_note_ref(project_uid, body=body, content_disposition=content_disposition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_note_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**CreateReferenceFileNoteDto**](CreateReferenceFileNoteDto.md)|  | [optional] 
 **content_disposition** | **str**| &lt;b&gt;Required&lt;/b&gt; for application/octet-stream.&lt;br&gt; Example: filename*&#x3D;UTF-8&#39;&#39;YourFileName.txt | [optional] 

### Return type

[**ReferenceFileReference**](ReferenceFileReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> AbstractProjectDto create_project(body=body)

Create project



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
body = memsource_cli.CreateProjectDto() # CreateProjectDto |  (optional)

try:
    # Create project
    api_response = api_instance.create_project(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateProjectDto**](CreateProjectDto.md)|  | [optional] 

### Return type

[**AbstractProjectDto**](AbstractProjectDto.md)

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
api_instance = memsource_cli.ProjectApi()
template_id = 789 # int | 
body = memsource_cli.CreateProjectFromTemplateV2Dto() # CreateProjectFromTemplateV2Dto |  (optional)

try:
    # Create project from template
    api_response = api_instance.create_project_from_template_v2(template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project_from_template_v2: %s\n" % e)
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

# **delete_project**
> delete_project(project_uid, purge=purge)

Delete project



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
purge = false # bool |  (optional) (default to false)

try:
    # Delete project
    api_instance.delete_project(project_uid, purge=purge)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **purge** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_reference**
> download_reference(project_uid, reference_file_id)

Get project reference



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
reference_file_id = 'reference_file_id_example' # str | 

try:
    # Get project reference
    api_instance.download_reference(project_uid, reference_file_id)
except ApiException as e:
    print("Exception when calling ProjectApi->download_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **reference_file_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_project**
> AbstractProjectDto edit_project(project_uid, body=body)

Edit project



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.EditProjectDto() # EditProjectDto |  (optional)

try:
    # Edit project
    api_response = api_instance.edit_project(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->edit_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**EditProjectDto**](EditProjectDto.md)|  | [optional] 

### Return type

[**AbstractProjectDto**](AbstractProjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_project_access_settings**
> ProjectSecuritySettingsDto edit_project_access_settings(project_uid, body=body)

Edit access and security settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.EditProjectSecuritySettingsDto() # EditProjectSecuritySettingsDto |  (optional)

try:
    # Edit access and security settings
    api_response = api_instance.edit_project_access_settings(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->edit_project_access_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**EditProjectSecuritySettingsDto**](EditProjectSecuritySettingsDto.md)|  | [optional] 

### Return type

[**ProjectSecuritySettingsDto**](ProjectSecuritySettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enabled_quality_checks**
> EnabledQualityChecksDto enabled_quality_checks(project_uid)

Get QA checks

Returns enabled quality assurance settings.

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get QA checks
    api_response = api_instance.enabled_quality_checks(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->enabled_quality_checks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**EnabledQualityChecksDto**](EnabledQualityChecksDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analyse_settings_for_project**
> AnalyseSettingsDto get_analyse_settings_for_project(project_uid)

Get analyse settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get analyse settings
    api_response = api_instance.get_analyse_settings_for_project(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_analyse_settings_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**AnalyseSettingsDto**](AnalyseSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_financial_settings**
> FinancialSettingsDto get_financial_settings(project_uid)

Get financial settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get financial settings
    api_response = api_instance.get_financial_settings(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_financial_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**FinancialSettingsDto**](FinancialSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_settings2**
> FileImportSettingsDto get_import_settings2(project_uid)

Get projects's default import settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get projects's default import settings
    api_response = api_instance.get_import_settings2(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_import_settings2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**FileImportSettingsDto**](FileImportSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mt_settings_for_project**
> MTSettingsPerLanguageListDto get_mt_settings_for_project(project_uid)

Get machine translate settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get machine translate settings
    api_response = api_instance.get_mt_settings_for_project(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_mt_settings_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**MTSettingsPerLanguageListDto**](MTSettingsPerLanguageListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pre_translate_settings_for_project**
> PreTranslateSettingsDto get_pre_translate_settings_for_project(project_uid)

Get Pre-translate settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get Pre-translate settings
    api_response = api_instance.get_pre_translate_settings_for_project(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_pre_translate_settings_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**PreTranslateSettingsDto**](PreTranslateSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> AbstractProjectDto get_project(project_uid)

Get project



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get project
    api_response = api_instance.get_project(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**AbstractProjectDto**](AbstractProjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_access_settings**
> ProjectSecuritySettingsDto get_project_access_settings(project_uid)

Get access and security settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get access and security settings
    api_response = api_instance.get_project_access_settings(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_access_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**ProjectSecuritySettingsDto**](ProjectSecuritySettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_assignments**
> PageDtoProviderReference get_project_assignments(project_uid, provider_name=provider_name, page_number=page_number, page_size=page_size)

List project providers



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
provider_name = 'provider_name_example' # str |  (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List project providers
    api_response = api_instance.get_project_assignments(project_uid, provider_name=provider_name, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **provider_name** | **str**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoProviderReference**](PageDtoProviderReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_qa_settings_v2**
> QASettingsDtoV2 get_project_qa_settings_v2(project_uid)

Get quality assurance settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get quality assurance settings
    api_response = api_instance.get_project_qa_settings_v2(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_qa_settings_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**QASettingsDtoV2**](QASettingsDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_settings**
> LqaSettingsDto get_project_settings(project_uid, workflow_level=workflow_level)

Get LQA settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
workflow_level = 1 # int |  (optional) (default to 1)

try:
    # Get LQA settings
    api_response = api_instance.get_project_settings(project_uid, workflow_level=workflow_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **workflow_level** | **int**|  | [optional] [default to 1]

### Return type

[**LqaSettingsDto**](LqaSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_term_bases**
> ProjectTermBaseListDto get_project_term_bases(project_uid)

Get term bases



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get term bases
    api_response = api_instance.get_project_term_bases(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_term_bases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**ProjectTermBaseListDto**](ProjectTermBaseListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_trans_memories**
> ProjectTransMemoryListDto get_project_trans_memories(project_uid)

Get translation memories



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get translation memories
    api_response = api_instance.get_project_trans_memories(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_trans_memories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**ProjectTransMemoryListDto**](ProjectTransMemoryListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_workflow_steps**
> ProjectWorkflowStepListDto get_project_workflow_steps(project_uid)

Get workflow steps



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get workflow steps
    api_response = api_instance.get_project_workflow_steps(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_workflow_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**ProjectWorkflowStepListDto**](ProjectWorkflowStepListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quotes_for_project**
> PageDtoQuoteDto get_quotes_for_project(project_uid, page_number=page_number, page_size=page_size)

List quotes



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List quotes
    api_response = api_instance.get_quotes_for_project(project_uid, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_quotes_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoQuoteDto**](PageDtoQuoteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assigned_projects**
> PageDtoProjectReference list_assigned_projects(user_id, status=status, target_lang=target_lang, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, project_name=project_name, page_number=page_number, page_size=page_size)

List assigned projects



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
user_id = 789 # int | 
status = ['status_example'] # list[str] |  (optional)
target_lang = ['target_lang_example'] # list[str] |  (optional)
workflow_step_id = 789 # int |  (optional)
due_in_hours = 56 # int | -1 for jobs that are overdue (optional)
filename = 'filename_example' # str |  (optional)
project_name = 'project_name_example' # str |  (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    # List assigned projects
    api_response = api_instance.list_assigned_projects(user_id, status=status, target_lang=target_lang, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, project_name=project_name, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_assigned_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **status** | [**list[str]**](str.md)|  | [optional] 
 **target_lang** | [**list[str]**](str.md)|  | [optional] 
 **workflow_step_id** | **int**|  | [optional] 
 **due_in_hours** | **int**| -1 for jobs that are overdue | [optional] 
 **filename** | **str**|  | [optional] 
 **project_name** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoProjectReference**](PageDtoProjectReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List analyses by project
    api_response = api_instance.list_by_project_v2(project_uid, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_by_project_v2: %s\n" % e)
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

# **list_projects**
> PageDtoAbstractProjectDto list_projects(name=name, client_id=client_id, client_name=client_name, business_unit_name=business_unit_name, statuses=statuses, target_langs=target_langs, domain_name=domain_name, sub_domain_name=sub_domain_name, cost_center_id=cost_center_id, cost_center_name=cost_center_name, due_in_hours=due_in_hours, created_in_last_hours=created_in_last_hours, source_langs=source_langs, owner_id=owner_id, job_statuses=job_statuses, job_status_group=job_status_group, buyer_id=buyer_id, page_number=page_number, page_size=page_size)

List projects



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
name = 'name_example' # str |  (optional)
client_id = 789 # int |  (optional)
client_name = 'client_name_example' # str |  (optional)
business_unit_name = 'business_unit_name_example' # str |  (optional)
statuses = ['statuses_example'] # list[str] |  (optional)
target_langs = ['target_langs_example'] # list[str] |  (optional)
domain_name = 'domain_name_example' # str |  (optional)
sub_domain_name = 'sub_domain_name_example' # str |  (optional)
cost_center_id = 789 # int |  (optional)
cost_center_name = 'cost_center_name_example' # str |  (optional)
due_in_hours = 56 # int | -1 for projects that are overdue (optional)
created_in_last_hours = 56 # int |  (optional)
source_langs = ['source_langs_example'] # list[str] |  (optional)
owner_id = 789 # int |  (optional)
job_statuses = ['job_statuses_example'] # list[str] | Allowed for linguists only (optional)
job_status_group = 'job_status_group_example' # str | Allowed for linguists only (optional)
buyer_id = 789 # int |  (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List projects
    api_response = api_instance.list_projects(name=name, client_id=client_id, client_name=client_name, business_unit_name=business_unit_name, statuses=statuses, target_langs=target_langs, domain_name=domain_name, sub_domain_name=sub_domain_name, cost_center_id=cost_center_id, cost_center_name=cost_center_name, due_in_hours=due_in_hours, created_in_last_hours=created_in_last_hours, source_langs=source_langs, owner_id=owner_id, job_statuses=job_statuses, job_status_group=job_status_group, buyer_id=buyer_id, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **client_id** | **int**|  | [optional] 
 **client_name** | **str**|  | [optional] 
 **business_unit_name** | **str**|  | [optional] 
 **statuses** | [**list[str]**](str.md)|  | [optional] 
 **target_langs** | [**list[str]**](str.md)|  | [optional] 
 **domain_name** | **str**|  | [optional] 
 **sub_domain_name** | **str**|  | [optional] 
 **cost_center_id** | **int**|  | [optional] 
 **cost_center_name** | **str**|  | [optional] 
 **due_in_hours** | **int**| -1 for projects that are overdue | [optional] 
 **created_in_last_hours** | **int**|  | [optional] 
 **source_langs** | [**list[str]**](str.md)|  | [optional] 
 **owner_id** | **int**|  | [optional] 
 **job_statuses** | [**list[str]**](str.md)| Allowed for linguists only | [optional] 
 **job_status_group** | **str**| Allowed for linguists only | [optional] 
 **buyer_id** | **int**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoAbstractProjectDto**](PageDtoAbstractProjectDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers**
> ProviderListDto list_providers(project_uid)

Get suggested providers



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get suggested providers
    api_response = api_instance.list_providers(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 

### Return type

[**ProviderListDto**](ProviderListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.SearchTMRequestDto() # SearchTMRequestDto |  (optional)

try:
    # Search translation memory for segment in the project
    api_response = api_instance.search_segment(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->search_segment: %s\n" % e)
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

# **set_financial_settings**
> FinancialSettingsDto set_financial_settings(project_uid, body=body)

Edit financial settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.SetFinancialSettingsDto() # SetFinancialSettingsDto |  (optional)

try:
    # Edit financial settings
    api_response = api_instance.set_financial_settings(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_financial_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**SetFinancialSettingsDto**](SetFinancialSettingsDto.md)|  | [optional] 

### Return type

[**FinancialSettingsDto**](FinancialSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_mt_settings_for_project**
> MTSettingsPerLanguageListDto set_mt_settings_for_project(project_uid, body=body)

Edit machine translate settings

This will erase all mtSettings per language for project.         To remove all machine translate settings from project call without a machineTranslateSettings parameter.

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.EditProjectMTSettingsDto() # EditProjectMTSettingsDto |  (optional)

try:
    # Edit machine translate settings
    api_response = api_instance.set_mt_settings_for_project(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_mt_settings_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**EditProjectMTSettingsDto**](EditProjectMTSettingsDto.md)|  | [optional] 

### Return type

[**MTSettingsPerLanguageListDto**](MTSettingsPerLanguageListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_mt_settings_per_language_for_project**
> MTSettingsPerLanguageListDto set_mt_settings_per_language_for_project(project_uid, body=body)

Edit machine translate settings per language

This will erase mtSettings for project

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.EditProjectMTSettPerLangListDto() # EditProjectMTSettPerLangListDto |  (optional)

try:
    # Edit machine translate settings per language
    api_response = api_instance.set_mt_settings_per_language_for_project(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_mt_settings_per_language_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**EditProjectMTSettPerLangListDto**](EditProjectMTSettPerLangListDto.md)|  | [optional] 

### Return type

[**MTSettingsPerLanguageListDto**](MTSettingsPerLanguageListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_qa_settings_v2**
> QASettingsDtoV2 set_project_qa_settings_v2(project_uid, body=body)

Edit quality assurance settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.EditQASettingsDtoV2() # EditQASettingsDtoV2 |  (optional)

try:
    # Edit quality assurance settings
    api_response = api_instance.set_project_qa_settings_v2(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_project_qa_settings_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**EditQASettingsDtoV2**](EditQASettingsDtoV2.md)|  | [optional] 

### Return type

[**QASettingsDtoV2**](QASettingsDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_status**
> set_project_status(project_uid, body=body)

Edit project status



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.SetProjectStatusDto() # SetProjectStatusDto |  (optional)

try:
    # Edit project status
    api_instance.set_project_status(project_uid, body=body)
except ApiException as e:
    print("Exception when calling ProjectApi->set_project_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**SetProjectStatusDto**](SetProjectStatusDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_term_bases**
> ProjectTermBaseListDto set_project_term_bases(project_uid, body=body)

Edit term bases



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.SetTermBaseDto() # SetTermBaseDto |  (optional)

try:
    # Edit term bases
    api_response = api_instance.set_project_term_bases(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_project_term_bases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**SetTermBaseDto**](SetTermBaseDto.md)|  | [optional] 

### Return type

[**ProjectTermBaseListDto**](ProjectTermBaseListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_project_trans_memories_v2**
> ProjectTransMemoryListDtoV2 set_project_trans_memories_v2(project_uid, body=body)

Edit translation memories



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.SetProjectTransMemoriesV2Dto() # SetProjectTransMemoriesV2Dto |  (optional)

try:
    # Edit translation memories
    api_response = api_instance.set_project_trans_memories_v2(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->set_project_trans_memories_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**SetProjectTransMemoriesV2Dto**](SetProjectTransMemoriesV2Dto.md)|  | [optional] 

### Return type

[**ProjectTransMemoryListDtoV2**](ProjectTransMemoryListDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

