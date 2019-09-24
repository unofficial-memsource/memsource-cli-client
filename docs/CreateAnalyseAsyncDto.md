# CreateAnalyseAsyncDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**list[UidReference]**](UidReference.md) |  | 
**type** | **str** | default: PreAnalyse | [optional] 
**include_fuzzy_repetitions** | **bool** | Default: true | [optional] 
**include_confirmed_segments** | **bool** | Default: true | [optional] 
**include_numbers** | **bool** | Default: true | [optional] 
**include_locked_segments** | **bool** | Default: true | [optional] 
**count_source_units** | **bool** | Default: true | [optional] 
**include_trans_memory** | **bool** | Default: true | [optional] 
**include_non_translatables** | **bool** | Default: false. Works only for type&#x3D;PreAnalyse. | [optional] 
**include_machine_translation_matches** | **bool** | Default: false. Works only for type&#x3D;PreAnalyse. | [optional] 
**trans_memory_post_editing** | **bool** | Default: false. Works only for type&#x3D;PostAnalyse. | [optional] 
**non_translatable_post_editing** | **bool** | Default: false. Works only for type&#x3D;PostAnalyse. | [optional] 
**machine_translate_post_editing** | **bool** | Default: false. Works only for type&#x3D;PostAnalyse. | [optional] 
**name** | **str** |  | [optional] 
**net_rate_scheme** | [**IdReference**](IdReference.md) |  | [optional] 
**compare_workflow_level** | **int** | Required for type&#x3D;Compare | [optional] 
**use_project_analysis_settings** | **bool** | Default: false. Use default project settings. Will be overwritten with setting sent         in the API call. | [optional] 
**linguist** | [**IdReference**](IdReference.md) |  | [optional] 
**callback_url** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


