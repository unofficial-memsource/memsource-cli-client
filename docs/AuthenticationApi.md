# memsource_cli.AuthenticationApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthenticationApi.md#login) | **POST** /api2/v1/auth/login | Login
[**login_by_google**](AuthenticationApi.md#login_by_google) | **POST** /api2/v1/auth/loginWithGoogle | Login with Google
[**login_other**](AuthenticationApi.md#login_other) | **POST** /api2/v1/auth/loginOther | Login as another user
[**login_to_session**](AuthenticationApi.md#login_to_session) | **POST** /api2/v1/auth/loginToSession | Login to session
[**logout**](AuthenticationApi.md#logout) | **POST** /api2/v1/auth/logout | Logout
[**who_am_i**](AuthenticationApi.md#who_am_i) | **GET** /api2/v1/auth/whoAmI | Who am I


# **login**
> LoginResponseDto login(body=body)

Login



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AuthenticationApi()
body = memsource_cli.LoginDto() # LoginDto |  (optional)

try:
    # Login
    api_response = api_instance.login(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginDto**](LoginDto.md)|  | [optional] 

### Return type

[**LoginResponseDto**](LoginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_by_google**
> LoginResponseDto login_by_google(body=body)

Login with Google



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AuthenticationApi()
body = memsource_cli.LoginWithGoogleDto() # LoginWithGoogleDto |  (optional)

try:
    # Login with Google
    api_response = api_instance.login_by_google(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_by_google: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginWithGoogleDto**](LoginWithGoogleDto.md)|  | [optional] 

### Return type

[**LoginResponseDto**](LoginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_other**
> LoginResponseDto login_other(body=body)

Login as another user

Available only for admin

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AuthenticationApi()
body = memsource_cli.LoginOtherDto() # LoginOtherDto |  (optional)

try:
    # Login as another user
    api_response = api_instance.login_other(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_other: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginOtherDto**](LoginOtherDto.md)|  | [optional] 

### Return type

[**LoginResponseDto**](LoginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_to_session**
> LoginToSessionResponseDto login_to_session(body=body)

Login to session



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AuthenticationApi()
body = memsource_cli.LoginToSessionDto() # LoginToSessionDto |  (optional)

try:
    # Login to session
    api_response = api_instance.login_to_session(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login_to_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginToSessionDto**](LoginToSessionDto.md)|  | [optional] 

### Return type

[**LoginToSessionResponseDto**](LoginToSessionResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout(token=token)

Logout



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AuthenticationApi()
token = 'token_example' # str |  (optional)

try:
    # Logout
    api_instance.logout(token=token)
except ApiException as e:
    print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **who_am_i**
> LoginUserDto who_am_i()

Who am I



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.AuthenticationApi()

try:
    # Who am I
    api_response = api_instance.who_am_i()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->who_am_i: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoginUserDto**](LoginUserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

