# SearchRequestDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 
**source_lang** | **str** |  | 
**target_langs** | **list[str]** |  | [optional] 
**previous_segment** | **str** |  | [optional] 
**next_segment** | **str** |  | [optional] 
**tag_metadata** | [**list[TagMetadataDto]**](TagMetadataDto.md) |  | [optional] 
**trim_query** | **bool** | Remove leading and trailing whitespace from query. Default: true | [optional] 
**phrase_query** | **bool** | Return both wildcard and exact search results. Default: true | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


