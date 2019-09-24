# memsource_cli.SegmentationRulesApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_segmentation_rule**](SegmentationRulesApi.md#create_segmentation_rule) | **POST** /api2/v1/segmentationRules | Create segmentation rule
[**deletes_segmentation_rule**](SegmentationRulesApi.md#deletes_segmentation_rule) | **DELETE** /api2/v1/segmentationRules/{segRuleId} | Delete segmentation rule
[**get_list_of_segmentation_rules**](SegmentationRulesApi.md#get_list_of_segmentation_rules) | **GET** /api2/v1/segmentationRules | List segmentation rules
[**get_segmentation_rule**](SegmentationRulesApi.md#get_segmentation_rule) | **GET** /api2/v1/segmentationRules/{segRuleId} | Get segmentation rule
[**updates_segmentation_rule**](SegmentationRulesApi.md#updates_segmentation_rule) | **PUT** /api2/v1/segmentationRules/{segRuleId} | Edit segmentation rule


# **create_segmentation_rule**
> SegmentationRuleDto create_segmentation_rule(body, seg_rule)

Create segmentation rule

Creates new Segmentation Rule with file and segRule JSON Object as header parameter. The same object is used for GET action.

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SegmentationRulesApi()
body = memsource_cli.InputStream() # InputStream | streamed file
seg_rule = '\"{name:'name', locale:'en', primary:'false', filename:'extra_file.xml'}\"' # str | 

try:
    # Create segmentation rule
    api_response = api_instance.create_segmentation_rule(body, seg_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentationRulesApi->create_segmentation_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InputStream**](InputStream.md)| streamed file | 
 **seg_rule** | **str**|  | 

### Return type

[**SegmentationRuleDto**](SegmentationRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletes_segmentation_rule**
> deletes_segmentation_rule(seg_rule_id)

Delete segmentation rule



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SegmentationRulesApi()
seg_rule_id = 789 # int | 

try:
    # Delete segmentation rule
    api_instance.deletes_segmentation_rule(seg_rule_id)
except ApiException as e:
    print("Exception when calling SegmentationRulesApi->deletes_segmentation_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seg_rule_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_segmentation_rules**
> PageDtoSegmentationRuleReference get_list_of_segmentation_rules(page_number=page_number, page_size=page_size)

List segmentation rules



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SegmentationRulesApi()
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List segmentation rules
    api_response = api_instance.get_list_of_segmentation_rules(page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentationRulesApi->get_list_of_segmentation_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoSegmentationRuleReference**](PageDtoSegmentationRuleReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segmentation_rule**
> SegmentationRuleDto get_segmentation_rule(seg_rule_id)

Get segmentation rule



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SegmentationRulesApi()
seg_rule_id = 789 # int | 

try:
    # Get segmentation rule
    api_response = api_instance.get_segmentation_rule(seg_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentationRulesApi->get_segmentation_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seg_rule_id** | **int**|  | 

### Return type

[**SegmentationRuleDto**](SegmentationRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_segmentation_rule**
> SegmentationRuleDto updates_segmentation_rule(seg_rule_id, body=body)

Edit segmentation rule



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SegmentationRulesApi()
seg_rule_id = 789 # int | 
body = memsource_cli.EditSegmentationRuleDto() # EditSegmentationRuleDto |  (optional)

try:
    # Edit segmentation rule
    api_response = api_instance.updates_segmentation_rule(seg_rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentationRulesApi->updates_segmentation_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seg_rule_id** | **int**|  | 
 **body** | [**EditSegmentationRuleDto**](EditSegmentationRuleDto.md)|  | [optional] 

### Return type

[**SegmentationRuleDto**](SegmentationRuleDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

