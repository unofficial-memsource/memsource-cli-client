# memsource_cli.SpellCheckApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_word**](SpellCheckApi.md#add_word) | **POST** /api2/v1/spellCheck/words | Add word to dictionary
[**check**](SpellCheckApi.md#check) | **POST** /api2/v1/spellCheck/check | Spell check
[**check_by_job**](SpellCheckApi.md#check_by_job) | **POST** /api2/v1/spellCheck/check/{jobUid} | Spell check for job
[**suggest**](SpellCheckApi.md#suggest) | **POST** /api2/v1/spellCheck/suggest | Suggest a word


# **add_word**
> add_word(body=body)

Add word to dictionary



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SpellCheckApi()
body = memsource_cli.DictionaryItemDto() # DictionaryItemDto |  (optional)

try:
    # Add word to dictionary
    api_instance.add_word(body=body)
except ApiException as e:
    print("Exception when calling SpellCheckApi->add_word: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DictionaryItemDto**](DictionaryItemDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check**
> SpellCheckResponseDto check(body=body)

Spell check

Spell check using the settings of the user's organization

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SpellCheckApi()
body = memsource_cli.SpellCheckRequestDto() # SpellCheckRequestDto |  (optional)

try:
    # Spell check
    api_response = api_instance.check(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpellCheckApi->check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpellCheckRequestDto**](SpellCheckRequestDto.md)|  | [optional] 

### Return type

[**SpellCheckResponseDto**](SpellCheckResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_by_job**
> SpellCheckResponseDto check_by_job(job_uid, body=body)

Spell check for job

Spell check using the settings from the project of the job

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SpellCheckApi()
job_uid = 'job_uid_example' # str | 
body = memsource_cli.SpellCheckRequestDto() # SpellCheckRequestDto |  (optional)

try:
    # Spell check for job
    api_response = api_instance.check_by_job(job_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpellCheckApi->check_by_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **body** | [**SpellCheckRequestDto**](SpellCheckRequestDto.md)|  | [optional] 

### Return type

[**SpellCheckResponseDto**](SpellCheckResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggest**
> SuggestResponseDto suggest(body=body)

Suggest a word

Spell check suggest using the users's spell check dictionary

### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.SpellCheckApi()
body = memsource_cli.SuggestRequestDto() # SuggestRequestDto |  (optional)

try:
    # Suggest a word
    api_response = api_instance.suggest(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpellCheckApi->suggest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SuggestRequestDto**](SuggestRequestDto.md)|  | [optional] 

### Return type

[**SuggestResponseDto**](SuggestResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

