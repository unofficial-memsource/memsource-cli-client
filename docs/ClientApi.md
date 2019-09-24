# memsource_cli.ClientApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client**](ClientApi.md#create_client) | **POST** /api2/v1/clients | Create client
[**delete_client**](ClientApi.md#delete_client) | **DELETE** /api2/v1/clients/{clientId} | Delete client
[**get_client**](ClientApi.md#get_client) | **GET** /api2/v1/clients/{clientId} | Get client
[**list_clients**](ClientApi.md#list_clients) | **GET** /api2/v1/clients | List clients
[**update_client**](ClientApi.md#update_client) | **PUT** /api2/v1/clients/{clientId} | Edit client


# **create_client**
> ClientDto create_client(body)

Create client



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ClientApi()
body = memsource_cli.ClientEditDto() # ClientEditDto | 

try:
    # Create client
    api_response = api_instance.create_client(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->create_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientEditDto**](ClientEditDto.md)|  | 

### Return type

[**ClientDto**](ClientDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client**
> delete_client(client_id)

Delete client



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ClientApi()
client_id = 789 # int | 

try:
    # Delete client
    api_instance.delete_client(client_id)
except ApiException as e:
    print("Exception when calling ClientApi->delete_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client**
> ClientDto get_client(client_id)

Get client



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ClientApi()
client_id = 789 # int | 

try:
    # Get client
    api_response = api_instance.get_client(client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->get_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 

### Return type

[**ClientDto**](ClientDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clients**
> PageDtoClientDto list_clients(name=name, page_number=page_number, page_size=page_size)

List clients



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ClientApi()
name = 'name_example' # str | Unique name of the Client (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List clients
    api_response = api_instance.list_clients(name=name, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->list_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Unique name of the Client | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoClientDto**](PageDtoClientDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client**
> ClientDto update_client(client_id, body)

Edit client



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ClientApi()
client_id = 789 # int | 
body = memsource_cli.ClientEditDto() # ClientEditDto | 

try:
    # Edit client
    api_response = api_instance.update_client(client_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientApi->update_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **int**|  | 
 **body** | [**ClientEditDto**](ClientEditDto.md)|  | 

### Return type

[**ClientDto**](ClientDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

