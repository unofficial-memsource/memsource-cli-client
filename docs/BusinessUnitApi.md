# memsource_cli.BusinessUnitApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_business_unit**](BusinessUnitApi.md#create_business_unit) | **POST** /api2/v1/businessUnits | Create business unit
[**delete_business_unit**](BusinessUnitApi.md#delete_business_unit) | **DELETE** /api2/v1/businessUnits/{businessUnitId} | Delete business unit
[**get_business_unit**](BusinessUnitApi.md#get_business_unit) | **GET** /api2/v1/businessUnits/{businessUnitId} | Get business unit
[**list_business_units**](BusinessUnitApi.md#list_business_units) | **GET** /api2/v1/businessUnits | List business units
[**update_business_unit**](BusinessUnitApi.md#update_business_unit) | **PUT** /api2/v1/businessUnits/{businessUnitId} | Edit business unit


# **create_business_unit**
> BusinessUnitDto create_business_unit(body=body)

Create business unit



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.BusinessUnitApi()
body = memsource_cli.BusinessUnitEditDto() # BusinessUnitEditDto |  (optional)

try:
    # Create business unit
    api_response = api_instance.create_business_unit(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessUnitApi->create_business_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BusinessUnitEditDto**](BusinessUnitEditDto.md)|  | [optional] 

### Return type

[**BusinessUnitDto**](BusinessUnitDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_business_unit**
> delete_business_unit(business_unit_id)

Delete business unit



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.BusinessUnitApi()
business_unit_id = 789 # int | 

try:
    # Delete business unit
    api_instance.delete_business_unit(business_unit_id)
except ApiException as e:
    print("Exception when calling BusinessUnitApi->delete_business_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_unit_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_unit**
> BusinessUnitDto get_business_unit(business_unit_id)

Get business unit



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.BusinessUnitApi()
business_unit_id = 789 # int | 

try:
    # Get business unit
    api_response = api_instance.get_business_unit(business_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessUnitApi->get_business_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_unit_id** | **int**|  | 

### Return type

[**BusinessUnitDto**](BusinessUnitDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_business_units**
> PageDtoBusinessUnitDto list_business_units(name=name, page_number=page_number, page_size=page_size)

List business units



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.BusinessUnitApi()
name = 'name_example' # str | Unique name of the business unit (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List business units
    api_response = api_instance.list_business_units(name=name, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessUnitApi->list_business_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Unique name of the business unit | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoBusinessUnitDto**](PageDtoBusinessUnitDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_business_unit**
> BusinessUnitDto update_business_unit(business_unit_id, body=body)

Edit business unit



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.BusinessUnitApi()
business_unit_id = 789 # int | 
body = memsource_cli.BusinessUnitEditDto() # BusinessUnitEditDto |  (optional)

try:
    # Edit business unit
    api_response = api_instance.update_business_unit(business_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BusinessUnitApi->update_business_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_unit_id** | **int**|  | 
 **body** | [**BusinessUnitEditDto**](BusinessUnitEditDto.md)|  | [optional] 

### Return type

[**BusinessUnitDto**](BusinessUnitDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

