# memsource_cli.ProjectReferenceFileApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_note_ref**](ProjectReferenceFileApi.md#create_note_ref) | **POST** /api2/v1/projects/{projectUid}/references | Create project reference file
[**download_reference**](ProjectReferenceFileApi.md#download_reference) | **GET** /api2/v1/projects/{projectUid}/references/{referenceFileId} | Get project reference


# **create_note_ref**
> ReferenceFileReference create_note_ref(project_uid, body=body, content_disposition=content_disposition)

Create project reference file

Accepts application/octet-stream or application/json.<br>                                                                     <b>application/json</b> - Note will be converted to .txt.<br>                                                                     <b>application/octet-stream</b> - Content-Disposition header is required

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectReferenceFileApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.CreateReferenceFileNoteDto() # CreateReferenceFileNoteDto |  (optional)
content_disposition = 'content_disposition_example' # str | <b>Required</b> for application/octet-stream.<br> Example: filename*=UTF-8''YourFileName.txt (optional)

try:
    # Create project reference file
    api_response = api_instance.create_note_ref(project_uid, body=body, content_disposition=content_disposition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectReferenceFileApi->create_note_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**CreateReferenceFileNoteDto**](CreateReferenceFileNoteDto.md)|  | [optional] 
 **content_disposition** | **str**| &lt;b&gt;Required&lt;/b&gt; for application/octet-stream.&lt;br&gt; Example: filename*&#x3D;UTF-8&#39;&#39;YourFileName.txt | [optional] 

### Return type

[**ReferenceFileReference**](ReferenceFileReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_reference**
> download_reference(project_uid, reference_file_id)

Get project reference



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ProjectReferenceFileApi()
project_uid = 'project_uid_example' # str | 
reference_file_id = 'reference_file_id_example' # str | 

try:
    # Get project reference
    api_instance.download_reference(project_uid, reference_file_id)
except ApiException as e:
    print("Exception when calling ProjectReferenceFileApi->download_reference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **reference_file_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

