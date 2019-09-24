# memsource_cli.DomainApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_domain**](DomainApi.md#create_domain) | **POST** /api2/v1/domains | Create domain
[**delete_domain**](DomainApi.md#delete_domain) | **DELETE** /api2/v1/domains/{domainId} | Delete domain
[**get_domain**](DomainApi.md#get_domain) | **GET** /api2/v1/domains/{domainId} | Get domain
[**list_domains**](DomainApi.md#list_domains) | **GET** /api2/v1/domains | List of domains
[**update_domain**](DomainApi.md#update_domain) | **PUT** /api2/v1/domains/{domainId} | Edit domain


# **create_domain**
> DomainDto create_domain(body=body)

Create domain



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.DomainApi()
body = memsource_cli.DomainEditDto() # DomainEditDto |  (optional)

try:
    # Create domain
    api_response = api_instance.create_domain(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->create_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainEditDto**](DomainEditDto.md)|  | [optional] 

### Return type

[**DomainDto**](DomainDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain**
> delete_domain(domain_id)

Delete domain



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.DomainApi()
domain_id = 789 # int | 

try:
    # Delete domain
    api_instance.delete_domain(domain_id)
except ApiException as e:
    print("Exception when calling DomainApi->delete_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain**
> DomainDto get_domain(domain_id)

Get domain



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.DomainApi()
domain_id = 789 # int | 

try:
    # Get domain
    api_response = api_instance.get_domain(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->get_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**|  | 

### Return type

[**DomainDto**](DomainDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domains**
> PageDtoDomainDto list_domains(page_number=page_number, page_size=page_size)

List of domains



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.DomainApi()
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List of domains
    api_response = api_instance.list_domains(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->list_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoDomainDto**](PageDtoDomainDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain**
> DomainDto update_domain(domain_id, body=body)

Edit domain



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.DomainApi()
domain_id = 789 # int | 
body = memsource_cli.DomainEditDto() # DomainEditDto |  (optional)

try:
    # Edit domain
    api_response = api_instance.update_domain(domain_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->update_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**|  | 
 **body** | [**DomainEditDto**](DomainEditDto.md)|  | [optional] 

### Return type

[**DomainDto**](DomainDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

