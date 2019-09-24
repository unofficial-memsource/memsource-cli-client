# memsource_cli.MachineTranslationSettingsApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list**](MachineTranslationSettingsApi.md#get_list) | **GET** /api2/v1/machineTranslateSettings | List machine translate settings
[**get_machine_translate_settings_for_project_template**](MachineTranslationSettingsApi.md#get_machine_translate_settings_for_project_template) | **GET** /api2/v1/projectTemplates/{projectTemplateId}/mtSettings | Get machine translate settings
[**get_mt_settings**](MachineTranslationSettingsApi.md#get_mt_settings) | **GET** /api2/v1/machineTranslateSettings/{id} | Get machine translate settings
[**get_status**](MachineTranslationSettingsApi.md#get_status) | **GET** /api2/v1/machineTranslateSettings/{id}/status | Get status of machine translate engine
[**get_translation_resources**](MachineTranslationSettingsApi.md#get_translation_resources) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/translationResources | Get translation resources


# **get_list**
> PageDtoMachineTranslateSettingsPbmDto get_list(page_number=page_number, page_size=page_size)

List machine translate settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.MachineTranslationSettingsApi()
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List machine translate settings
    api_response = api_instance.get_list(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineTranslationSettingsApi->get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoMachineTranslateSettingsPbmDto**](PageDtoMachineTranslateSettingsPbmDto.md)

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
api_instance = memsource_cli.MachineTranslationSettingsApi()
project_template_id = 'project_template_id_example' # str | 

try:
    # Get machine translate settings
    api_response = api_instance.get_machine_translate_settings_for_project_template(project_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineTranslationSettingsApi->get_machine_translate_settings_for_project_template: %s\n" % e)
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

# **get_mt_settings**
> MachineTranslateSettingsPbmDto get_mt_settings(id)

Get machine translate settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.MachineTranslationSettingsApi()
id = 789 # int | 

try:
    # Get machine translate settings
    api_response = api_instance.get_mt_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineTranslationSettingsApi->get_mt_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MachineTranslateSettingsPbmDto**](MachineTranslateSettingsPbmDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> MachineTranslateStatusDto get_status(id)

Get status of machine translate engine



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.MachineTranslationSettingsApi()
id = 789 # int | 

try:
    # Get status of machine translate engine
    api_response = api_instance.get_status(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineTranslationSettingsApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MachineTranslateStatusDto**](MachineTranslateStatusDto.md)

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
api_instance = memsource_cli.MachineTranslationSettingsApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 

try:
    # Get translation resources
    api_response = api_instance.get_translation_resources(project_uid, job_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MachineTranslationSettingsApi->get_translation_resources: %s\n" % e)
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

