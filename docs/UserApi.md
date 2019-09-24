# memsource_cli.UserApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_deletion**](UserApi.md#cancel_deletion) | **POST** /api2/v1/users/{userId}/undelete | Restore user
[**create_user_v2**](UserApi.md#create_user_v2) | **POST** /api2/v2/users | Create user
[**delete_user1**](UserApi.md#delete_user1) | **DELETE** /api2/v1/users/{userId} | Delete user
[**get_list_of_users_filtered**](UserApi.md#get_list_of_users_filtered) | **GET** /api2/v1/users | List users
[**get_user_v2**](UserApi.md#get_user_v2) | **GET** /api2/v2/users/{userId} | Get user
[**list_assigned_projects**](UserApi.md#list_assigned_projects) | **GET** /api2/v1/users/{userId}/projects | List assigned projects
[**list_jobs**](UserApi.md#list_jobs) | **GET** /api2/v1/users/{userId}/jobs | List assigned jobs
[**list_target_langs**](UserApi.md#list_target_langs) | **GET** /api2/v1/users/{userId}/targetLangs | List assigned target languages
[**list_workflow_steps**](UserApi.md#list_workflow_steps) | **GET** /api2/v1/users/{userId}/workflowSteps | List assigned workflow steps
[**login_activity**](UserApi.md#login_activity) | **GET** /api2/v1/users/{userId}/loginStatistics | Login statistics
[**send_login_info**](UserApi.md#send_login_info) | **POST** /api2/v1/users/{userId}/emailLoginInformation | Send login information
[**update_password**](UserApi.md#update_password) | **POST** /api2/v1/users/{userId}/updatePassword | Update password
[**update_user_v2**](UserApi.md#update_user_v2) | **PUT** /api2/v2/users/{userId} | Edit user


# **cancel_deletion**
> UserDto cancel_deletion(user_id)

Restore user



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.UserApi()
user_id = 789 # int | 

try:
    # Restore user
    api_response = api_instance.cancel_deletion(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->cancel_deletion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_v2**
> UserDetailsDtoV2 create_user_v2(body=body)

Create user



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.UserApi()
body = memsource_cli.UserCreateDtoV2() # UserCreateDtoV2 |  (optional)

try:
    # Create user
    api_response = api_instance.create_user_v2(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreateDtoV2**](UserCreateDtoV2.md)|  | [optional] 

### Return type

[**UserDetailsDtoV2**](UserDetailsDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user1**
> delete_user1(user_id)

Delete user



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.UserApi()
user_id = 789 # int | 

try:
    # Delete user
    api_instance.delete_user1(user_id)
except ApiException as e:
    print("Exception when calling UserApi->delete_user1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_users_filtered**
> PageDtoUserDto get_list_of_users_filtered(user_name=user_name, email=email, role=role, include_deleted=include_deleted, page_number=page_number, page_size=page_size)

List users



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.UserApi()
user_name = 'user_name_example' # str |  (optional)
email = 'email_example' # str |  (optional)
role = ['role_example'] # list[str] |  (optional)
include_deleted = false # bool |  (optional) (default to false)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List users
    api_response = api_instance.get_list_of_users_filtered(user_name=user_name, email=email, role=role, include_deleted=include_deleted, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_list_of_users_filtered: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 
 **role** | [**list[str]**](str.md)|  | [optional] 
 **include_deleted** | **bool**|  | [optional] [default to false]
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoUserDto**](PageDtoUserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_v2**
> UserDetailsDtoV2 get_user_v2(user_id)

Get user



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.UserApi()
user_id = 789 # int | 

try:
    # Get user
    api_response = api_instance.get_user_v2(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**UserDetailsDtoV2**](UserDetailsDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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
api_instance = memsource_cli.UserApi()
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
    print("Exception when calling UserApi->list_assigned_projects: %s\n" % e)
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

# **list_jobs**
> PageDtoAssignedJobDto list_jobs(user_id, status=status, project_uid=project_uid, target_lang=target_lang, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)

List assigned jobs



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.UserApi()
user_id = 789 # int | 
status = ['status_example'] # list[str] |  (optional)
project_uid = 'project_uid_example' # str |  (optional)
target_lang = ['target_lang_example'] # list[str] |  (optional)
workflow_step_id = 789 # int |  (optional)
due_in_hours = 56 # int | -1 for jobs that are overdue (optional)
filename = 'filename_example' # str |  (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    # List assigned jobs
    api_response = api_instance.list_jobs(user_id, status=status, project_uid=project_uid, target_lang=target_lang, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **status** | [**list[str]**](str.md)|  | [optional] 
 **project_uid** | **str**|  | [optional] 
 **target_lang** | [**list[str]**](str.md)|  | [optional] 
 **workflow_step_id** | **int**|  | [optional] 
 **due_in_hours** | **int**| -1 for jobs that are overdue | [optional] 
 **filename** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoAssignedJobDto**](PageDtoAssignedJobDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_target_langs**
> PageDtoString list_target_langs(user_id, status=status, project_uid=project_uid, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)

List assigned target languages



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.UserApi()
user_id = 789 # int | 
status = ['status_example'] # list[str] |  (optional)
project_uid = 'project_uid_example' # str |  (optional)
workflow_step_id = 789 # int |  (optional)
due_in_hours = 56 # int | -1 for jobs that are overdue (optional)
filename = 'filename_example' # str |  (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    # List assigned target languages
    api_response = api_instance.list_target_langs(user_id, status=status, project_uid=project_uid, workflow_step_id=workflow_step_id, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_target_langs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **status** | [**list[str]**](str.md)|  | [optional] 
 **project_uid** | **str**|  | [optional] 
 **workflow_step_id** | **int**|  | [optional] 
 **due_in_hours** | **int**| -1 for jobs that are overdue | [optional] 
 **filename** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoString**](PageDtoString.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_workflow_steps**
> PageDtoWorkflowStepReference list_workflow_steps(user_id, status=status, project_uid=project_uid, target_lang=target_lang, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)

List assigned workflow steps



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.UserApi()
user_id = 789 # int | 
status = ['status_example'] # list[str] |  (optional)
project_uid = 'project_uid_example' # str |  (optional)
target_lang = ['target_lang_example'] # list[str] |  (optional)
due_in_hours = 56 # int | -1 for jobs that are overdue (optional)
filename = 'filename_example' # str |  (optional)
page_number = 0 # int |  (optional) (default to 0)
page_size = 50 # int |  (optional) (default to 50)

try:
    # List assigned workflow steps
    api_response = api_instance.list_workflow_steps(user_id, status=status, project_uid=project_uid, target_lang=target_lang, due_in_hours=due_in_hours, filename=filename, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_workflow_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **status** | [**list[str]**](str.md)|  | [optional] 
 **project_uid** | **str**|  | [optional] 
 **target_lang** | [**list[str]**](str.md)|  | [optional] 
 **due_in_hours** | **int**| -1 for jobs that are overdue | [optional] 
 **filename** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] [default to 0]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**PageDtoWorkflowStepReference**](PageDtoWorkflowStepReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_activity**
> UserStatisticsListDto login_activity(user_id)

Login statistics



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.UserApi()
user_id = 789 # int | 

try:
    # Login statistics
    api_response = api_instance.login_activity(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->login_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**UserStatisticsListDto**](UserStatisticsListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_login_info**
> send_login_info(user_id)

Send login information



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.UserApi()
user_id = 789 # int | 

try:
    # Send login information
    api_instance.send_login_info(user_id)
except ApiException as e:
    print("Exception when calling UserApi->send_login_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> update_password(user_id, body=body)

Update password



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.UserApi()
user_id = 789 # int | 
body = memsource_cli.UserPasswordEditDto() # UserPasswordEditDto |  (optional)

try:
    # Update password
    api_instance.update_password(user_id, body=body)
except ApiException as e:
    print("Exception when calling UserApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **body** | [**UserPasswordEditDto**](UserPasswordEditDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_v2**
> UserDetailsDtoV2 update_user_v2(user_id, body=body)

Edit user



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.UserApi()
user_id = 789 # int | 
body = memsource_cli.UserEditDtoV2() # UserEditDtoV2 |  (optional)

try:
    # Edit user
    api_response = api_instance.update_user_v2(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **body** | [**UserEditDtoV2**](UserEditDtoV2.md)|  | [optional] 

### Return type

[**UserDetailsDtoV2**](UserDetailsDtoV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

