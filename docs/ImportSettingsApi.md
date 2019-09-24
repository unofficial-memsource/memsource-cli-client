# memsource_cli.ImportSettingsApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_import_settings**](ImportSettingsApi.md#create_import_settings) | **POST** /api2/v1/importSettings | Create import settings
[**delete_import_settings**](ImportSettingsApi.md#delete_import_settings) | **DELETE** /api2/v1/importSettings/{uid} | Delete import settings
[**get_import_settings**](ImportSettingsApi.md#get_import_settings) | **GET** /api2/v1/importSettings/default | Get organization&#39;s default import settings
[**get_import_settings1**](ImportSettingsApi.md#get_import_settings1) | **GET** /api2/v1/importSettings/{uid} | Get import settings
[**list_import_settings**](ImportSettingsApi.md#list_import_settings) | **GET** /api2/v1/importSettings | List import settings


# **create_import_settings**
> ImportSettingsDto create_import_settings(body=body)

Create import settings

Pre-defined import settings is handy for [Create Job](#operation/createJob).                   See [supported file types](https://wiki.memsource.com/wiki/API_File_Type_List)

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ImportSettingsApi()
body = memsource_cli.ImportSettingsCreateDto() # ImportSettingsCreateDto |  (optional)

try:
    # Create import settings
    api_response = api_instance.create_import_settings(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportSettingsApi->create_import_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportSettingsCreateDto**](ImportSettingsCreateDto.md)|  | [optional] 

### Return type

[**ImportSettingsDto**](ImportSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_import_settings**
> delete_import_settings(uid)

Delete import settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ImportSettingsApi()
uid = 'uid_example' # str | 

try:
    # Delete import settings
    api_instance.delete_import_settings(uid)
except ApiException as e:
    print("Exception when calling ImportSettingsApi->delete_import_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_settings**
> ImportSettingsDto get_import_settings()

Get organization's default import settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ImportSettingsApi()

try:
    # Get organization's default import settings
    api_response = api_instance.get_import_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportSettingsApi->get_import_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ImportSettingsDto**](ImportSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_settings1**
> ImportSettingsDto get_import_settings1(uid)

Get import settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ImportSettingsApi()
uid = 'uid_example' # str | 

try:
    # Get import settings
    api_response = api_instance.get_import_settings1(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportSettingsApi->get_import_settings1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**ImportSettingsDto**](ImportSettingsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_import_settings**
> PageDtoImportSettingsReference list_import_settings(name=name, page_number=page_number, page_size=page_size)

List import settings



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ImportSettingsApi()
name = 'name_example' # str |  (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List import settings
    api_response = api_instance.list_import_settings(name=name, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportSettingsApi->list_import_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoImportSettingsReference**](PageDtoImportSettingsReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

