# PreTranslateJobsDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**list[UidReference]**](UidReference.md) |  | 
**use_translation_memory** | **bool** | Default: true | [optional] 
**use_machine_translation** | **bool** | Default: true | [optional] 
**translation_memory_treshold** | **float** | default: 0.7 | [optional] 
**insert_machine_translation_into_target** | **bool** | Default: false | [optional] 
**pre_translate_non_translatables** | **bool** | Default: false | [optional] 
**confirm100_non_translatable_matches** | **bool** | Default: false | [optional] 
**confirm100_translation_memory_matches** | **bool** | Default: false | [optional] 
**confirm101_translation_memory_matches** | **bool** | Default: false | [optional] 
**lock100_non_translatable_matches** | **bool** | Default: false | [optional] 
**lock100_translation_memory_matches** | **bool** | Default: false | [optional] 
**lock101_translation_memory_matches** | **bool** | Default: false | [optional] 
**overwrite** | **bool** | Default: false | [optional] 
**segment_filters** | **list[str]** |  | [optional] 
**use_project_pre_translate_settings** | **bool** | Default: false | [optional] 
**callback_url** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


