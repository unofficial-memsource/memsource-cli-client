# memsource_cli.SegmentApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_segments_count**](SegmentApi.md#get_segments_count) | **POST** /api2/v1/projects/{projectUid}/jobs/segmentsCount | Get segments count
[**list_segments**](SegmentApi.md#list_segments) | **GET** /api2/v1/projects/{projectUid}/jobs/{jobUid}/segments | Get segments


# **get_segments_count**
> SegmentsCountsResponseListDto get_segments_count(project_uid, body=body)

Get segments count

Provides segments count (progress data)

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SegmentApi()
project_uid = 'project_uid_example' # str | 
body = memsource_cli.JobPartReadyReferences() # JobPartReadyReferences |  (optional)

try:
    # Get segments count
    api_response = api_instance.get_segments_count(project_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentApi->get_segments_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **body** | [**JobPartReadyReferences**](JobPartReadyReferences.md)|  | [optional] 

### Return type

[**SegmentsCountsResponseListDto**](SegmentsCountsResponseListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_segments**
> SegmentListDto list_segments(project_uid, job_uid, begin_index=begin_index, end_index=end_index)

Get segments



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SegmentApi()
project_uid = 'project_uid_example' # str | 
job_uid = 'job_uid_example' # str | 
begin_index = 0 # int |  (optional) (default to 0)
end_index = 0 # int |  (optional) (default to 0)

try:
    # Get segments
    api_response = api_instance.list_segments(project_uid, job_uid, begin_index=begin_index, end_index=end_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentApi->list_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uid** | **str**|  | 
 **job_uid** | **str**|  | 
 **begin_index** | **int**|  | [optional] [default to 0]
 **end_index** | **int**|  | [optional] [default to 0]

### Return type

[**SegmentListDto**](SegmentListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

