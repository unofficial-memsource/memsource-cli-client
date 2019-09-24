# UserCreateDtoV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**password** | **str** |  | 
**role** | **str** |  | 
**timezone** | **str** |  | 
**note** | **str** |  | [optional] 
**may_edit_approved_terms** | **bool** | In previous version as terminologist. Default: false | [optional] 
**may_reject_jobs** | **bool** | Default: false | [optional] 
**editor_machine_translate_enabled** | **bool** | Applies only to Linguist or Guest. Default: true | [optional] 
**receive_newsletter** | **bool** | Default: true | [optional] 
**may_edit_translation_memory** | **bool** | Default: false | [optional] 
**source_langs** | **list[str]** |  | [optional] 
**target_langs** | **list[str]** |  | [optional] 
**workflow_steps** | [**list[IdReference]**](IdReference.md) |  | [optional] 
**clients** | [**list[IdReference]**](IdReference.md) |  | [optional] 
**domains** | [**list[IdReference]**](IdReference.md) |  | [optional] 
**sub_domains** | [**list[IdReference]**](IdReference.md) |  | [optional] 
**project_business_units** | [**list[IdReference]**](IdReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


