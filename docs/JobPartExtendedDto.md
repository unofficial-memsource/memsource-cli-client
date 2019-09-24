# JobPartExtendedDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**providers** | [**list[ProviderReference]**](ProviderReference.md) |  | [optional] 
**source_lang** | **str** |  | [optional] 
**target_lang** | **str** |  | [optional] 
**workflow_level** | **int** |  | [optional] 
**workflow_step** | [**ProjectWorkflowStepReference**](ProjectWorkflowStepReference.md) |  | [optional] 
**filename** | **str** |  | [optional] 
**date_due** | **datetime** |  | [optional] 
**words_count** | **int** |  | [optional] 
**begin_index** | **int** |  | [optional] 
**end_index** | **int** |  | [optional] 
**is_parent_job_split** | **bool** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**last_workflow_level** | **int** |  | [optional] 
**work_unit** | [**IdReference**](IdReference.md) |  | [optional] 
**imported** | **bool** |  | [optional] 
**continuous** | **bool** |  | [optional] 
**continuous_job_info** | [**ContinuousJobInfoDto**](ContinuousJobInfoDto.md) |  | [optional] 
**original_file_directory** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


