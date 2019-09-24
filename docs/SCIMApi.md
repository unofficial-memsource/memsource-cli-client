# memsource_cli.SCIMApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_scim**](SCIMApi.md#create_user_scim) | **POST** /api2/v1/scim/Users | Create user using SCIM
[**delete_user**](SCIMApi.md#delete_user) | **DELETE** /api2/v1/scim/Users/{userId} | Delete user using SCIM
[**edit_user**](SCIMApi.md#edit_user) | **PUT** /api2/v1/scim/Users/{userId} | Edit user using SCIM
[**get_resource_types**](SCIMApi.md#get_resource_types) | **GET** /api2/v1/scim/ResourceTypes | List the types of SCIM Resources available
[**get_schema_by_urn**](SCIMApi.md#get_schema_by_urn) | **GET** /api2/v1/scim/Schemas/{schemaUrn} | Get supported SCIM Schema by urn
[**get_schemas**](SCIMApi.md#get_schemas) | **GET** /api2/v1/scim/Schemas | Get supported SCIM Schemas
[**get_scim_user**](SCIMApi.md#get_scim_user) | **GET** /api2/v1/scim/Users/{userId} | Get user
[**get_service_provider_config_dto**](SCIMApi.md#get_service_provider_config_dto) | **GET** /api2/v1/scim/ServiceProviderConfig | Retrieve the Service Provider&#39;s Configuration
[**patch_user**](SCIMApi.md#patch_user) | **PATCH** /api2/v1/scim/Users/{userId} | Patch user using SCIM
[**search_users**](SCIMApi.md#search_users) | **GET** /api2/v1/scim/Users | Search users


# **create_user_scim**
> ScimUserCoreDto create_user_scim(body=body, authorization=authorization)

Create user using SCIM

 Supported schema: `\"urn:ietf:params:scim:schemas:core:2.0:User\"`  Create active user: ``` {     \"schemas\": [         \"urn:ietf:params:scim:schemas:core:2.0:User\"     ],     \"active\": true,     \"userName\": \"john.doe\",     \"emails\": [         {             \"primary\": true,             \"value\": \"john.doe@example.com\",             \"type\": \"work\"         }     ],     \"name\": {         \"givenName\": \"John\",         \"familyName\": \"Doe\"     } } ``` 

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SCIMApi()
body = memsource_cli.ScimUserCoreDto() # ScimUserCoreDto |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Create user using SCIM
    api_response = api_instance.create_user_scim(body=body, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->create_user_scim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScimUserCoreDto**](ScimUserCoreDto.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**ScimUserCoreDto**](ScimUserCoreDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json
 - **Accept**: application/json, application/scim+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id, authorization=authorization)

Delete user using SCIM



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SCIMApi()
user_id = 789 # int | 
authorization = 'authorization_example' # str |  (optional)

try:
    # Delete user using SCIM
    api_instance.delete_user(user_id, authorization=authorization)
except ApiException as e:
    print("Exception when calling SCIMApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_user**
> ScimUserCoreDto edit_user(user_id, body=body, authorization=authorization)

Edit user using SCIM



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SCIMApi()
user_id = 789 # int | 
body = memsource_cli.ScimUserCoreDto() # ScimUserCoreDto |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Edit user using SCIM
    api_response = api_instance.edit_user(user_id, body=body, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->edit_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **body** | [**ScimUserCoreDto**](ScimUserCoreDto.md)|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**ScimUserCoreDto**](ScimUserCoreDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/scim+json
 - **Accept**: application/json, application/scim+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_types**
> ScimResourceTypeSchema get_resource_types()

List the types of SCIM Resources available



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SCIMApi()

try:
    # List the types of SCIM Resources available
    api_response = api_instance.get_resource_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_resource_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ScimResourceTypeSchema**](ScimResourceTypeSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_by_urn**
> ScimResourceSchema get_schema_by_urn(schema_urn)

Get supported SCIM Schema by urn



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SCIMApi()
schema_urn = 'schema_urn_example' # str | 

try:
    # Get supported SCIM Schema by urn
    api_response = api_instance.get_schema_by_urn(schema_urn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_schema_by_urn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_urn** | **str**|  | 

### Return type

[**ScimResourceSchema**](ScimResourceSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schemas**
> ScimResourceSchema get_schemas()

Get supported SCIM Schemas



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SCIMApi()

try:
    # Get supported SCIM Schemas
    api_response = api_instance.get_schemas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_schemas: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ScimResourceSchema**](ScimResourceSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scim_user**
> ScimUserCoreDto get_scim_user(user_id, authorization=authorization)

Get user



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SCIMApi()
user_id = 789 # int | 
authorization = 'authorization_example' # str |  (optional)

try:
    # Get user
    api_response = api_instance.get_scim_user(user_id, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_scim_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**ScimUserCoreDto**](ScimUserCoreDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_provider_config_dto**
> ServiceProviderConfigDto get_service_provider_config_dto()

Retrieve the Service Provider's Configuration



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SCIMApi()

try:
    # Retrieve the Service Provider's Configuration
    api_response = api_instance.get_service_provider_config_dto()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->get_service_provider_config_dto: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServiceProviderConfigDto**](ServiceProviderConfigDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_user**
> ScimUserCoreDto patch_user(user_id, body=body, authorization=authorization)

Patch user using SCIM



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SCIMApi()
user_id = 789 # int | 
body = NULL # object |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    # Patch user using SCIM
    api_response = api_instance.patch_user(user_id, body=body, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->patch_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **body** | **object**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

[**ScimUserCoreDto**](ScimUserCoreDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> ScimResourceDto search_users(authorization=authorization, filter=filter, attributes=attributes, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)

Search users

 This operation supports <a href=\"http://ldapwiki.com/wiki/SCIM%20Filtering\" target=\"_blank\">SCIM Filter</a>,  <a href=\"http://ldapwiki.com/wiki/SCIM%20Search%20Request\" target=\"_blank\">SCIM attributes</a> and  <a href=\"http://ldapwiki.com/wiki/SCIM%20Sorting\" target=\"_blank\">SCIM sort</a>  Supported attributes:   - `id`   - `active`   - `userName`   - `name.givenName`   - `name.familyName`   - `emails.value`   - `meta.created` 

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SCIMApi()
authorization = 'authorization_example' # str |  (optional)
filter = 'filter_example' # str | See method description (optional)
attributes = 'attributes_example' # str | See method description (optional)
sort_by = 'sort_by_example' # str | See method description (optional)
sort_order = 'ascending' # str | See method description (optional) (default to ascending)
start_index = 1 # int | The 1-based index of the first search result. Default 1 (optional) (default to 1)
count = 50 # int | Non-negative Integer. Specifies the desired maximum number of search results per page; e.g., 10. (optional) (default to 50)

try:
    # Search users
    api_response = api_instance.search_users(authorization=authorization, filter=filter, attributes=attributes, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SCIMApi->search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 
 **filter** | **str**| See method description | [optional] 
 **attributes** | **str**| See method description | [optional] 
 **sort_by** | **str**| See method description | [optional] 
 **sort_order** | **str**| See method description | [optional] [default to ascending]
 **start_index** | **int**| The 1-based index of the first search result. Default 1 | [optional] [default to 1]
 **count** | **int**| Non-negative Integer. Specifies the desired maximum number of search results per page; e.g., 10. | [optional] [default to 50]

### Return type

[**ScimResourceDto**](ScimResourceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

