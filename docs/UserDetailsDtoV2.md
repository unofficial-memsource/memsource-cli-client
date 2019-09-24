# UserDetailsDtoV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**date_deleted** | **datetime** |  | [optional] 
**created_by** | [**UserReference**](UserReference.md) |  | [optional] 
**role** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**may_edit_approved_terms** | **bool** | Default: false | [optional] 
**may_reject_jobs** | **bool** | Default: false | [optional] 
**editor_machine_translate_enabled** | **bool** | Default: true | [optional] 
**receive_newsletter** | **bool** | Default: true | [optional] 
**may_edit_translation_memory** | **bool** | Default: false | [optional] 
**source_langs** | **list[str]** |  | [optional] 
**target_langs** | **list[str]** |  | [optional] 
**workflow_steps** | [**list[WorkflowStepReference]**](WorkflowStepReference.md) |  | [optional] 
**clients** | [**list[ClientReference]**](ClientReference.md) |  | [optional] 
**domains** | [**list[DomainReference]**](DomainReference.md) |  | [optional] 
**sub_domains** | [**list[SubDomainReference]**](SubDomainReference.md) |  | [optional] 
**project_business_units** | [**list[BusinessUnitReference]**](BusinessUnitReference.md) |  | [optional] 
**organization** | [**IdReference**](IdReference.md) |  | [optional] 
**price_list** | [**PriceListReference**](PriceListReference.md) |  | [optional] 
**net_rate_scheme** | [**DiscountSchemeReference**](DiscountSchemeReference.md) |  | [optional] 
**active** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


