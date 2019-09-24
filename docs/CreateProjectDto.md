# CreateProjectDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**source_lang** | **str** |  | 
**target_langs** | **list[str]** |  | 
**client** | [**IdReference**](IdReference.md) | Client referenced by id | [optional] 
**business_unit** | [**IdReference**](IdReference.md) |  | [optional] 
**domain** | [**IdReference**](IdReference.md) |  | [optional] 
**sub_domain** | [**IdReference**](IdReference.md) |  | [optional] 
**use_default_project_settings** | **bool** | Default: false | [optional] 
**purchase_order** | **str** |  | [optional] 
**workflow_steps** | [**list[IdReference]**](IdReference.md) |  | [optional] 
**date_due** | **datetime** |  | [optional] 
**note** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


