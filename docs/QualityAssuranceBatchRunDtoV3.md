# QualityAssuranceBatchRunDtoV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**list[UidReference]**](UidReference.md) |  | 
**settings** | [**QualityAssuranceRunDtoV3**](QualityAssuranceRunDtoV3.md) |  | [optional] 
**max_qa_warnings_count** | **int** | Maximum number of QA warnings in result, default: 100. For efficiency reasons QA warnings are processed with minimum segments chunk size 10, therefore slightly more warnings are returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


