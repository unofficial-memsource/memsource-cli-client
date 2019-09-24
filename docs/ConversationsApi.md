# memsource_cli.ConversationsApi

All URIs are relative to *https://cloud.memsource.com/web*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_lqa_comment**](ConversationsApi.md#add_lqa_comment) | **POST** /api2/v1/jobs/{jobUid}/conversations/lqas/{conversationId}/comments | Add LQA comment
[**add_plain_comment**](ConversationsApi.md#add_plain_comment) | **POST** /api2/v1/jobs/{jobUid}/conversations/plains/{conversationId}/comments | Add plain comment
[**create_lqa_conversation**](ConversationsApi.md#create_lqa_conversation) | **POST** /api2/v1/jobs/{jobUid}/conversations/lqas | Create LQA conversation
[**create_segment_target_conversation**](ConversationsApi.md#create_segment_target_conversation) | **POST** /api2/v1/jobs/{jobUid}/conversations/plains | Create plain conversation
[**delete_lqa_comment**](ConversationsApi.md#delete_lqa_comment) | **DELETE** /api2/v1/jobs/{jobUid}/conversations/lqas/{conversationId}/comments/{commentId} | Delete LQA comment
[**delete_lqa_conversation**](ConversationsApi.md#delete_lqa_conversation) | **DELETE** /api2/v1/jobs/{jobUid}/conversations/lqas/{conversationId} | Delete conversation
[**delete_plain_comment**](ConversationsApi.md#delete_plain_comment) | **DELETE** /api2/v1/jobs/{jobUid}/conversations/plains/{conversationId}/comments/{commentId} | Delete plain comment
[**delete_plain_conversation**](ConversationsApi.md#delete_plain_conversation) | **DELETE** /api2/v1/jobs/{jobUid}/conversations/plains/{conversationId} | Delete plain conversation
[**find_conversations**](ConversationsApi.md#find_conversations) | **POST** /api2/v1/jobs/conversations/find | Find all conversation
[**get_lqa_conversation**](ConversationsApi.md#get_lqa_conversation) | **GET** /api2/v1/jobs/{jobUid}/conversations/lqas/{conversationId} | Get LQA conversation
[**get_plain_conversation**](ConversationsApi.md#get_plain_conversation) | **GET** /api2/v1/jobs/{jobUid}/conversations/plains/{conversationId} | Get plain conversation
[**list_all_conversations**](ConversationsApi.md#list_all_conversations) | **GET** /api2/v1/jobs/{jobUid}/conversations | List all conversations
[**list_lqa_conversations**](ConversationsApi.md#list_lqa_conversations) | **GET** /api2/v1/jobs/{jobUid}/conversations/lqas | List LQA conversations
[**list_plain_conversations**](ConversationsApi.md#list_plain_conversations) | **GET** /api2/v1/jobs/{jobUid}/conversations/plains | List plain conversations
[**update_lqa_comment**](ConversationsApi.md#update_lqa_comment) | **PUT** /api2/v1/jobs/{jobUid}/conversations/lqas/{conversationId}/comments/{commentId} | Edit LQA comment
[**update_lqa_conversation**](ConversationsApi.md#update_lqa_conversation) | **PUT** /api2/v1/jobs/{jobUid}/conversations/lqas/{conversationId} | Edit LQA conversation
[**update_plain_comment**](ConversationsApi.md#update_plain_comment) | **PUT** /api2/v1/jobs/{jobUid}/conversations/plains/{conversationId}/comments/{commentId} | Edit plain comment
[**update_plain_conversation**](ConversationsApi.md#update_plain_conversation) | **PUT** /api2/v1/jobs/{jobUid}/conversations/plains/{conversationId} | Edit plain conversation


# **add_lqa_comment**
> LQAConversationDto add_lqa_comment(job_uid, conversation_id, body=body)

Add LQA comment



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
conversation_id = 'conversation_id_example' # str | 
body = memsource_cli.AddCommentDto() # AddCommentDto |  (optional)

try:
    # Add LQA comment
    api_response = api_instance.add_lqa_comment(job_uid, conversation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->add_lqa_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **conversation_id** | **str**|  | 
 **body** | [**AddCommentDto**](AddCommentDto.md)|  | [optional] 

### Return type

[**LQAConversationDto**](LQAConversationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_plain_comment**
> PlainConversationDto add_plain_comment(job_uid, conversation_id, body=body)

Add plain comment



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
conversation_id = 'conversation_id_example' # str | 
body = memsource_cli.AddCommentDto() # AddCommentDto |  (optional)

try:
    # Add plain comment
    api_response = api_instance.add_plain_comment(job_uid, conversation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->add_plain_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **conversation_id** | **str**|  | 
 **body** | [**AddCommentDto**](AddCommentDto.md)|  | [optional] 

### Return type

[**PlainConversationDto**](PlainConversationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_lqa_conversation**
> LQAConversationDto create_lqa_conversation(job_uid, body=body)

Create LQA conversation



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
body = memsource_cli.CreateLQAConversationDto() # CreateLQAConversationDto |  (optional)

try:
    # Create LQA conversation
    api_response = api_instance.create_lqa_conversation(job_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->create_lqa_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **body** | [**CreateLQAConversationDto**](CreateLQAConversationDto.md)|  | [optional] 

### Return type

[**LQAConversationDto**](LQAConversationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_segment_target_conversation**
> PlainConversationDto create_segment_target_conversation(job_uid, body=body)

Create plain conversation



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
body = memsource_cli.CreatePlainConversationDto() # CreatePlainConversationDto |  (optional)

try:
    # Create plain conversation
    api_response = api_instance.create_segment_target_conversation(job_uid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->create_segment_target_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **body** | [**CreatePlainConversationDto**](CreatePlainConversationDto.md)|  | [optional] 

### Return type

[**PlainConversationDto**](PlainConversationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lqa_comment**
> delete_lqa_comment(job_uid, conversation_id, comment_id)

Delete LQA comment



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
conversation_id = 'conversation_id_example' # str | 
comment_id = 'comment_id_example' # str | 

try:
    # Delete LQA comment
    api_instance.delete_lqa_comment(job_uid, conversation_id, comment_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_lqa_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **conversation_id** | **str**|  | 
 **comment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lqa_conversation**
> delete_lqa_conversation(job_uid, conversation_id)

Delete conversation



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
conversation_id = 'conversation_id_example' # str | 

try:
    # Delete conversation
    api_instance.delete_lqa_conversation(job_uid, conversation_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_lqa_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **conversation_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plain_comment**
> delete_plain_comment(job_uid, conversation_id, comment_id)

Delete plain comment



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
conversation_id = 'conversation_id_example' # str | 
comment_id = 'comment_id_example' # str | 

try:
    # Delete plain comment
    api_instance.delete_plain_comment(job_uid, conversation_id, comment_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_plain_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **conversation_id** | **str**|  | 
 **comment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plain_conversation**
> delete_plain_conversation(job_uid, conversation_id)

Delete plain conversation



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
conversation_id = 'conversation_id_example' # str | 

try:
    # Delete plain conversation
    api_instance.delete_plain_conversation(job_uid, conversation_id)
except ApiException as e:
    print("Exception when calling ConversationsApi->delete_plain_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **conversation_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_conversations**
> ConversationListDto find_conversations(body=body)

Find all conversation



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
body = memsource_cli.FindConversationsDto() # FindConversationsDto |  (optional)

try:
    # Find all conversation
    api_response = api_instance.find_conversations(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->find_conversations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FindConversationsDto**](FindConversationsDto.md)|  | [optional] 

### Return type

[**ConversationListDto**](ConversationListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lqa_conversation**
> LQAConversationDto get_lqa_conversation(job_uid, conversation_id)

Get LQA conversation



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
conversation_id = 'conversation_id_example' # str | 

try:
    # Get LQA conversation
    api_response = api_instance.get_lqa_conversation(job_uid, conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_lqa_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **conversation_id** | **str**|  | 

### Return type

[**LQAConversationDto**](LQAConversationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plain_conversation**
> PlainConversationDto get_plain_conversation(job_uid, conversation_id)

Get plain conversation



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
conversation_id = 'conversation_id_example' # str | 

try:
    # Get plain conversation
    api_response = api_instance.get_plain_conversation(job_uid, conversation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->get_plain_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **conversation_id** | **str**|  | 

### Return type

[**PlainConversationDto**](PlainConversationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_conversations**
> ConversationListDto list_all_conversations(job_uid, include_deleted=include_deleted, since=since)

List all conversations



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
include_deleted = false # bool |  (optional) (default to false)
since = 'since_example' # str |  (optional)

try:
    # List all conversations
    api_response = api_instance.list_all_conversations(job_uid, include_deleted=include_deleted, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->list_all_conversations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **include_deleted** | **bool**|  | [optional] [default to false]
 **since** | **str**|  | [optional] 

### Return type

[**ConversationListDto**](ConversationListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lqa_conversations**
> LQAConversationsListDto list_lqa_conversations(job_uid, include_deleted=include_deleted, since=since)

List LQA conversations



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
include_deleted = false # bool |  (optional) (default to false)
since = 'since_example' # str |  (optional)

try:
    # List LQA conversations
    api_response = api_instance.list_lqa_conversations(job_uid, include_deleted=include_deleted, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->list_lqa_conversations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **include_deleted** | **bool**|  | [optional] [default to false]
 **since** | **str**|  | [optional] 

### Return type

[**LQAConversationsListDto**](LQAConversationsListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_plain_conversations**
> PlainConversationsListDto list_plain_conversations(job_uid, include_deleted=include_deleted, since=since)

List plain conversations



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
include_deleted = false # bool |  (optional) (default to false)
since = 'since_example' # str |  (optional)

try:
    # List plain conversations
    api_response = api_instance.list_plain_conversations(job_uid, include_deleted=include_deleted, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->list_plain_conversations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **include_deleted** | **bool**|  | [optional] [default to false]
 **since** | **str**|  | [optional] 

### Return type

[**PlainConversationsListDto**](PlainConversationsListDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lqa_comment**
> LQAConversationDto update_lqa_comment(job_uid, conversation_id, comment_id, body=body)

Edit LQA comment



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
conversation_id = 'conversation_id_example' # str | 
comment_id = 'comment_id_example' # str | 
body = memsource_cli.AddCommentDto() # AddCommentDto |  (optional)

try:
    # Edit LQA comment
    api_response = api_instance.update_lqa_comment(job_uid, conversation_id, comment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->update_lqa_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **conversation_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **body** | [**AddCommentDto**](AddCommentDto.md)|  | [optional] 

### Return type

[**LQAConversationDto**](LQAConversationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lqa_conversation**
> LQAConversationDto update_lqa_conversation(job_uid, conversation_id, body=body)

Edit LQA conversation



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
conversation_id = 'conversation_id_example' # str | 
body = memsource_cli.EditLQAConversationDto() # EditLQAConversationDto |  (optional)

try:
    # Edit LQA conversation
    api_response = api_instance.update_lqa_conversation(job_uid, conversation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->update_lqa_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **conversation_id** | **str**|  | 
 **body** | [**EditLQAConversationDto**](EditLQAConversationDto.md)|  | [optional] 

### Return type

[**LQAConversationDto**](LQAConversationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plain_comment**
> PlainConversationDto update_plain_comment(job_uid, conversation_id, comment_id, body=body)

Edit plain comment



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
conversation_id = 'conversation_id_example' # str | 
comment_id = 'comment_id_example' # str | 
body = memsource_cli.AddCommentDto() # AddCommentDto |  (optional)

try:
    # Edit plain comment
    api_response = api_instance.update_plain_comment(job_uid, conversation_id, comment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->update_plain_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **conversation_id** | **str**|  | 
 **comment_id** | **str**|  | 
 **body** | [**AddCommentDto**](AddCommentDto.md)|  | [optional] 

### Return type

[**PlainConversationDto**](PlainConversationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plain_conversation**
> PlainConversationDto update_plain_conversation(job_uid, conversation_id, body=body)

Edit plain conversation



### Example
```python
from __future__ import print_function
import time
import memsource_cli
from memsource_cli.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = memsource_cli.ConversationsApi()
job_uid = 'job_uid_example' # str | 
conversation_id = 'conversation_id_example' # str | 
body = memsource_cli.EditPlainConversationDto() # EditPlainConversationDto |  (optional)

try:
    # Edit plain conversation
    api_response = api_instance.update_plain_conversation(job_uid, conversation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConversationsApi->update_plain_conversation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_uid** | **str**|  | 
 **conversation_id** | **str**|  | 
 **body** | [**EditPlainConversationDto**](EditPlainConversationDto.md)|  | [optional] 

### Return type

[**PlainConversationDto**](PlainConversationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

