# memsource_cli.ConnectorApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connector**](ConnectorApi.md#get_connector) | **GET** /api2/v1/connectors/{connectorId} | Get a connector
[**get_connector_list**](ConnectorApi.md#get_connector_list) | **GET** /api2/v1/connectors | List connectors
[**get_file**](ConnectorApi.md#get_file) | **GET** /api2/v1/connectors/{connectorId}/folders/{folder}/files/{file} | Download file
[**get_folder**](ConnectorApi.md#get_folder) | **GET** /api2/v1/connectors/{connectorId}/folders/{folder} | List files in a subfolder
[**get_root_folder**](ConnectorApi.md#get_root_folder) | **GET** /api2/v1/connectors/{connectorId}/folders | List files in root
[**upload_file**](ConnectorApi.md#upload_file) | **POST** /api2/v1/connectors/{connectorId}/folders/{folder} | Upload a file to a subfolder of the selected connector


# **get_connector**
> ConnectorDto get_connector(connector_id)

Get a connector



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConnectorApi()
connector_id = 'connector_id_example' # str | 

try:
    # Get a connector
    api_response = api_instance.get_connector(connector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->get_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 

### Return type

[**ConnectorDto**](ConnectorDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_list**
> ConnectorListDto get_connector_list(type=type)

List connectors



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConnectorApi()
type = 'type_example' # str |  (optional)

try:
    # List connectors
    api_response = api_instance.get_connector_list(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->get_connector_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 

### Return type

[**ConnectorListDto**](ConnectorListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> InputStreamLength get_file(connector_id, folder, file)

Download file

Download a file from a subfolder of the selected connector

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConnectorApi()
connector_id = 'connector_id_example' # str | 
folder = 'folder_example' # str | 
file = 'file_example' # str | 

try:
    # Download file
    api_response = api_instance.get_file(connector_id, folder, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **folder** | **str**|  | 
 **file** | **str**|  | 

### Return type

[**InputStreamLength**](InputStreamLength.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder**
> FileListDto get_folder(connector_id, folder, file_type=file_type, sort=sort, direction=direction)

List files in a subfolder

List files in a subfolder of the selected connector

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConnectorApi()
connector_id = 'connector_id_example' # str | 
folder = 'folder_example' # str | 
file_type = 'ALL' # str |  (optional) (default to ALL)
sort = 'NAME' # str |  (optional) (default to NAME)
direction = 'ASCENDING' # str |  (optional) (default to ASCENDING)

try:
    # List files in a subfolder
    api_response = api_instance.get_folder(connector_id, folder, file_type=file_type, sort=sort, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->get_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **folder** | **str**|  | 
 **file_type** | **str**|  | [optional] [default to ALL]
 **sort** | **str**|  | [optional] [default to NAME]
 **direction** | **str**|  | [optional] [default to ASCENDING]

### Return type

[**FileListDto**](FileListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_folder**
> FileListDto get_root_folder(connector_id, file_type=file_type, sort=sort, direction=direction)

List files in root

List files in a root folder of the selected connector

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConnectorApi()
connector_id = 'connector_id_example' # str | 
file_type = 'ALL' # str |  (optional) (default to ALL)
sort = 'NAME' # str |  (optional) (default to NAME)
direction = 'ASCENDING' # str |  (optional) (default to ASCENDING)

try:
    # List files in root
    api_response = api_instance.get_root_folder(connector_id, file_type=file_type, sort=sort, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->get_root_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **file_type** | **str**|  | [optional] [default to ALL]
 **sort** | **str**|  | [optional] [default to NAME]
 **direction** | **str**|  | [optional] [default to ASCENDING]

### Return type

[**FileListDto**](FileListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> UploadResultDto upload_file(connector_id, folder, content_type, file, source_file_name=source_file_name, subfolder_name=subfolder_name, mime_type=mime_type, commit_message=commit_message)

Upload a file to a subfolder of the selected connector

Upload a file to a subfolder of the selected connector

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConnectorApi()
connector_id = 'connector_id_example' # str | 
folder = 'folder_example' # str | 
content_type = 'content_type_example' # str | 
file = '/path/to/file.txt' # file | Translated file to upload
source_file_name = 'source_file_name_example' # str | Name or ID of the original file (optional)
subfolder_name = 'subfolder_name_example' # str | Optional subfolder to upload the file to (optional)
mime_type = 'mime_type_example' # str | Mime type of the file to upload (optional)
commit_message = 'commit_message_example' # str | Commit message for upload to Git, etc. (optional)

try:
    # Upload a file to a subfolder of the selected connector
    api_response = api_instance.upload_file(connector_id, folder, content_type, file, source_file_name=source_file_name, subfolder_name=subfolder_name, mime_type=mime_type, commit_message=commit_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_id** | **str**|  | 
 **folder** | **str**|  | 
 **content_type** | **str**|  | 
 **file** | **file**| Translated file to upload | 
 **source_file_name** | **str**| Name or ID of the original file | [optional] 
 **subfolder_name** | **str**| Optional subfolder to upload the file to | [optional] 
 **mime_type** | **str**| Mime type of the file to upload | [optional] 
 **commit_message** | **str**| Commit message for upload to Git, etc. | [optional] 

### Return type

[**UploadResultDto**](UploadResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

