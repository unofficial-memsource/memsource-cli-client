# ProjectTemplateEditDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**template_name** | **str** |  | 
**source_lang** | **str** |  | [optional] 
**target_langs** | **list[str]** |  | [optional] 
**notify_provider** | [**ProjectTemplateNotifyProviderDto**](ProjectTemplateNotifyProviderDto.md) | use to notify assigned providers,         notificationIntervalInMinutes 0 or empty value means immediate notification to all providers | [optional] 
**work_flow_settings** | [**list[WorkflowStepSettingsEditDto]**](WorkflowStepSettingsEditDto.md) |  | [optional] 
**client** | [**IdReference**](IdReference.md) |  | [optional] 
**business_unit** | [**IdReference**](IdReference.md) |  | [optional] 
**domain** | [**IdReference**](IdReference.md) |  | [optional] 
**sub_domain** | [**IdReference**](IdReference.md) |  | [optional] 
**note** | **str** |  | [optional] 
**assigned_to** | [**list[ProjectTemplateWorkflowSettingsAssignedToDto]**](ProjectTemplateWorkflowSettingsAssignedToDto.md) | only use for projects without workflows; otherwise specify in the workflowSettings object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


