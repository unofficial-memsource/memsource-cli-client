# memsource_cli.FileApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_url_file**](FileApi.md#create_url_file) | **POST** /api2/v1/files | Upload file
[**deletes_file**](FileApi.md#deletes_file) | **DELETE** /api2/v1/files/{fileUid} | Delete file
[**get_file_json**](FileApi.md#get_file_json) | **GET** /api2/v1/files/{fileUid} | Get file
[**get_files**](FileApi.md#get_files) | **GET** /api2/v1/files | List files


# **create_url_file**
> UploadedFileDto create_url_file(body, content_disposition)

Upload file

Accepts multipart/form-data, application/octet-stream or application/json.

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.FileApi()
body = memsource_cli.RemoteUploadedFileDto() # RemoteUploadedFileDto | file
content_disposition = 'content_disposition_example' # str | must match pattern `filename\\*=UTF-8''(.+)`

try:
    # Upload file
    api_response = api_instance.create_url_file(body, content_disposition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->create_url_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteUploadedFileDto**](RemoteUploadedFileDto.md)| file | 
 **content_disposition** | **str**| must match pattern &#x60;filename\\*&#x3D;UTF-8&#39;&#39;(.+)&#x60; | 

### Return type

[**UploadedFileDto**](UploadedFileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletes_file**
> deletes_file(file_uid)

Delete file



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.FileApi()
file_uid = 'file_uid_example' # str | 

try:
    # Delete file
    api_instance.deletes_file(file_uid)
except ApiException as e:
    print("Exception when calling FileApi->deletes_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_uid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_json**
> UploadedFileDto get_file_json(file_uid)

Get file

Get uploaded file as <b>octet-stream</b> or as <b>json</b> based on 'Accept' header

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.FileApi()
file_uid = 'file_uid_example' # str | 

try:
    # Get file
    api_response = api_instance.get_file_json(file_uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_file_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_uid** | **str**|  | 

### Return type

[**UploadedFileDto**](UploadedFileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> PageDtoUploadedFileDto get_files(page_number=page_number, page_size=page_size, name=name, types=types, created_by=created_by, bigger_than=bigger_than)

List files



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.FileApi()
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)
name = 'name_example' # str |  (optional)
types = ['types_example'] # list[str] |  (optional)
created_by = 789 # int |  (optional)
bigger_than = 789 # int | Size in bytes (optional)

try:
    # List files
    api_response = api_instance.get_files(page_number=page_number, page_size=page_size, name=name, types=types, created_by=created_by, bigger_than=bigger_than)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]
 **name** | **str**|  | [optional] 
 **types** | [**list[str]**](str.md)|  | [optional] 
 **created_by** | **int**|  | [optional] 
 **bigger_than** | **int**| Size in bytes | [optional] 

### Return type

[**PageDtoUploadedFileDto**](PageDtoUploadedFileDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

