# memsource_cli.ProviderApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project_assignments**](ProviderApi.md#get_project_assignments) | **GET** /api2/v1/projects/{projectUid}/providers | List project providers
[**list_providers**](ProviderApi.md#list_providers) | **POST** /api2/v1/projects/{projectUid}/providers/suggest | Get suggested providers
[**list_providers1**](ProviderApi.md#list_providers1) | **POST** /api2/v1/projects/{projectUid}/jobs/{jobUid}/providers/suggest | Get suggested providers


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
api_instance = memsource_cli.ProviderApi()
project_uid = 'project_uid_example' # str | 
provider_name = 'provider_name_example' # str |  (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List project providers
    api_response = api_instance.get_project_assignments(project_uid, provider_name=provider_name, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->get_project_assignments: %s\n" % e)
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
api_instance = memsource_cli.ProviderApi()
project_uid = 'project_uid_example' # str | 

try:
    # Get suggested providers
    api_response = api_instance.list_providers(project_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->list_providers: %s\n" % e)
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

# **list_providers1**
> ProviderListDto list_providers1(project_uid, job_uid)

Get suggested providers



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProviderApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 

try:
    # Get suggested providers
    api_response = api_instance.list_providers1(project_uid, job_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->list_providers1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 

### Return type

[**ProviderListDto**](ProviderListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

