# PreTranslateSettingsDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**translation_memory** | **bool** | Pre-translate from translation memory. Default: false | [optional] 
**translation_memory_threshold** | **float** | Pre-translation threshold percent | [optional] 
**auto_propagate_repetitions** | **bool** | Propagate repetitions. Default: false | [optional] 
**machine_translation** | **bool** | Pre-translate from machine translation. Default: false | [optional] 
**non_translatables** | **bool** | Pre-translate non-translatables. Default: false | [optional] 
**repetitions_as_confirmed** | **bool** | Set segment status to confirmed for: Repetitions. Default: false | [optional] 
**matches100_as_translated** | **bool** | Set segment status to confirmed for: 100% translation memory matches. Default: false | [optional] 
**matches101_as_translate** | **bool** | Set segment status to confirmed for: 101% translation memory matches. Default: false | [optional] 
**non_translatables_as_translated** | **bool** | Set segment status to confirmed for: 100% non-translatable matches. Default: false | [optional] 
**pre_translate_on_job_creation** | **bool** | Pre-translate &amp; set job to completed: Pre-translate on job creation. Default: false | [optional] 
**set_job_status_completed** | **bool** | Pre-translate &amp; set job to completed: Set job to completed once pre-translated. Default: false | [optional] 
**set_job_status_completed_when_confirmed** | **bool** | Pre-translate &amp; set job to completed when all segments confirmed: Set job to completed once pre-translated and all segments are confirmed. Default: false | [optional] 
**set_project_status_completed** | **bool** | Pre-translate &amp; set job to completed: Set project to completed once all jobs pre-translated.         Default: false | [optional] 
**lock_non_translatables** | **bool** | Lock 100% non-translatable matches. Default: false | [optional] 
**lock100** | **bool** | Lock 100% translation memory matches. Default: false | [optional] 
**lock101** | **bool** | Lock 101% translation memory matches. Default: false | [optional] 
**non_translatables_in_editors** | **bool** | Non translatables enabled in Editors. Default: false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


