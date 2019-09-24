# memsource_cli.SupportedLanguagesApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_of_languages**](SupportedLanguagesApi.md#list_of_languages) | **GET** /api2/v1/languages | List supported languages


# **list_of_languages**
> LanguageListDto list_of_languages()

List supported languages



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SupportedLanguagesApi()

try:
    # List supported languages
    api_response = api_instance.list_of_languages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportedLanguagesApi->list_of_languages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LanguageListDto**](LanguageListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

