# memsource_cli.EmailTemplateApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_org_email_template**](EmailTemplateApi.md#get_org_email_template) | **GET** /api2/v1/emailTemplates/{templateId} | Get email template
[**list_org_email_templates**](EmailTemplateApi.md#list_org_email_templates) | **GET** /api2/v1/emailTemplates | List email templates


# **get_org_email_template**
> OrganizationEmailTemplateDto get_org_email_template(template_id)

Get email template



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.EmailTemplateApi()
template_id = 789 # int | 

try:
    # Get email template
    api_response = api_instance.get_org_email_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->get_org_email_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**|  | 

### Return type

[**OrganizationEmailTemplateDto**](OrganizationEmailTemplateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_org_email_templates**
> PageDtoOrganizationEmailTemplateDto list_org_email_templates(type=type, page_number=page_number, page_size=page_size)

List email templates



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.EmailTemplateApi()
type = 'type_example' # str |  (optional)
page_number = 0 # int | Page number, starting with 0, default 0 (optional) (default to 0)
page_size = 50 # int | Page size, accepts values between 1 and 50, default 50 (optional) (default to 50)

try:
    # List email templates
    api_response = api_instance.list_org_email_templates(type=type, page_number=page_number, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailTemplateApi->list_org_email_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **page_number** | **int**| Page number, starting with 0, default 0 | [optional] [default to 0]
 **page_size** | **int**| Page size, accepts values between 1 and 50, default 50 | [optional] [default to 50]

### Return type

[**PageDtoOrganizationEmailTemplateDto**](PageDtoOrganizationEmailTemplateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

