<a id="exporters-selector-descriptions"></a>

# Selector Descriptions

This section provides a brief overview of each selector and highlights implementation issues.

Additional implementation details are at the end of the chapter.

---

<a id="exporters-selector-descriptions-exselstartup"></a>

## exSelStartup

- param1 - [exExporterInfoRec\*](structure-descriptions.md#exporters-structure-descriptions-exexporterinforec)
- param2 - `unused`

Sent during application launch, unless the exporter has been cached.

A single exporter can support multiple codecs and file extensions.

`exExporterInfoRec` describes the exporter’s attributes, such as the format display name.

---

<a id="exporters-selector-descriptions-exselbegininstance"></a>

## exSelBeginInstance

- param1 - [exExporterInstanceRec\*](structure-descriptions.md#exporters-structure-descriptions-exexporterinstancerec)
- param2 - `unused`

Allocate any private data.

---

<a id="exporters-selector-descriptions-exselgeneratedefaultparams"></a>

## exSelGenerateDefaultParams

- param1 - [exGenerateDefaultParamRec\*](structure-descriptions.md#exporters-structure-descriptions-exgeneratedefaultparamrec)
- param2 - `unused`

Set the exporter’s default parameters using the [Export Param Suite](suites.md#exporters-suites-export-param-suite).

---

<a id="exporters-selector-descriptions-exselpostprocessparams"></a>

## exSelPostProcessParams

- param1 - [exPostProcessParamsRec\*](structure-descriptions.md#exporters-structure-descriptions-expostprocessparamsrec)
- param2 - `unused`

Post process parameters. This is where the localized strings for the parameter UI must be provided.

---

<a id="exporters-selector-descriptions-exselvalidateparamchanged"></a>

## exSelValidateParamChanged

- param1 - [exParamChangedRec\*](structure-descriptions.md#exporters-structure-descriptions-exparamchangedrec)
- param2 - `unused`

Validate any parameters that have changed. Based on a change to a parameter value, the exporter may update other parameter values, or show/hide certain parameter controls, using the [Export Param Suite](suites.md#exporters-suites-export-param-suite).

To notify the host that the plugin is changing other parameters, set `exParamChangedRec.rebuildAllParams` to a non-zero value.

---

<a id="exporters-selector-descriptions-exselgetparamsummary"></a>

## exSelGetParamSummary

- param1 - [exParamSummaryRec\*](structure-descriptions.md#exporters-structure-descriptions-exparamsummaryrec)
- param2 - `unused`

Provide a text summary of the current parameter settings, which will be displayed in the summary area of the Export Settings dialog.

---

<a id="exporters-selector-descriptions-exselparambutton"></a>

## exSelParamButton

- param1 - [exParamButtonRec\*](structure-descriptions.md#exporters-structure-descriptions-exparambuttonrec)
- param2 - `unused`

Sent if exporter has one or more buttons in its parameter UI, and the user clicks one of the buttons in the Export Settings.

The ID of the button pressed is passed in `exParamButtonRec.buttonParamIdentifier`.

Display any dialog using platform-specific UI, collect any user input, and save any changes back to `privateData`.

If the user cancels the dialog, return `exportReturn_ParamButtonCancel` to signify that nothing in the `privateData` has changed.

---

<a id="exporters-selector-descriptions-exselexport"></a>

## exSelExport

- param1 - [exDoExportRec\*](structure-descriptions.md#exporters-structure-descriptions-exdoexportrec)
- param2 - `unused`

Do the export! Sent when the user starts an export to the format supported by the exporter, or if the exporter is used in an Editing Mode and the user renders the work area.

Single file exporters are sent this selector only once per export (e.g. AVI, QuickTime). To create a single file, setup a loop where you request each frame in the startTime to endTime range using one of the render calls in the [Sequence Render Suite](suites.md#exporters-suites-sequence-render-suite) and GetAudio in the [Sequence Audio Suite](suites.md#exporters-suites-sequence-audio-suite). For better performance, you can use the asynchronous calls in the [Sequence Render Suite](suites.md#exporters-suites-sequence-render-suite) to have the host render multiple frames on multiple threads.

Still frame exporters are sent `exSelExport` for each frame in the sequence (e.g. numbered TIFFs). The host will name the files appropriately.

Save render time by checking to see if frames are repeated. Inspect the SequenceRender_GetFrameReturnRec.repeatCount returned from a render call, which holds a frame repeat count.

---

<a id="exporters-selector-descriptions-exselexport2"></a>

## exSelExport2

- param1 - [exDoExportRec2\*](structure-descriptions.md#exporters-structure-descriptions-exdoexportrec2)
- param2 - `unused`

Do the export! Identical to exSelExport, except that exDoExportRec2 (which contains a LUT description) is passed.

Exporter can specify the ID of the LUT that needs to be applied as last step in export processing. This is for including LUT for doing color space conversion in export path.

In case LUT is specified, `ExportColorSpace` signifies the output color space of LUT.

---

<a id="exporters-selector-descriptions-exselqueryexportfileextension"></a>

## exSelQueryExportFileExtension

- param1 - [exQueryExportFileExtensionRec\*](structure-descriptions.md#exporters-structure-descriptions-exqueryexportfileextensionrec)
- param2 - `unused`

For exporters that support more than one file extension, specify an extension given the file type.

If this selector is not supported by the exporter, the extension is specified by the exporter in `exExporterInfoRec.fileTypeDefaultExtension`.

---

<a id="exporters-selector-descriptions-exselqueryoutputfilelist"></a>

## exSelQueryOutputFileList

- param1 - [exQueryOutputFileListRec\*](structure-descriptions.md#exporters-structure-descriptions-exqueryoutputfilelistrec)
- param2 - `unused`

For exporters that export to more than one file. This is called before an export for the host to find out which files would need to be overwritten.

It is called after an export so the host will know about all the files created, for any post encoding tasks, such as FTP. If this selector is not supported by the exporter, the host application will only know about the original path.

This selector will be called three times. On the first call, the plugin fills out numOutputFiles. The host will then make numOutputFiles count of outputFileRecs, but empty.

On the second call, the plugin fills out the path length (incl trailing null) for each exOutputFileRec element in outputFileRecs. The host will then allocate all paths in each outputFileRec.

On the third call, the plugin fills in the path members of the outputFileRecs.

---

<a id="exporters-selector-descriptions-exselquerystillsequence"></a>

## exSelQueryStillSequence

- param1 - [exQueryStillSequenceRec\*](structure-descriptions.md#exporters-structure-descriptions-exquerystillsequencerec)
- param2 - `unused`

The host application asks a still-only exporter if it wants to export as a sequence, and at what frame rate.

---

<a id="exporters-selector-descriptions-exselqueryoutputsettings"></a>

## exSelQueryOutputSettings

- param1 - [exQueryOutputSettingsRec\*](structure-descriptions.md#exporters-structure-descriptions-exqueryoutputsettingsrec)
- param2 - `unused`

The host application asks the exporter for general details about the current settings. This is a required selector.

---

<a id="exporters-selector-descriptions-exselvalidateoutputsettings"></a>

## exSelValidateOutputSettings

- param1 - [exValidateOutputSettingsRec\*](structure-descriptions.md#exporters-structure-descriptions-exvalidateoutputsettingsrec)
- param2 - `unused`

The host application asks the exporter if it can export with the current settings.

The exporter should return `exportReturn_ErrLastErrorSet` if not, and the error string should be set to a description of the failure.

---

<a id="exporters-selector-descriptions-exselendinstance"></a>

## exSelEndInstance

- param1 - [exExporterInstanceRec\*](structure-descriptions.md#exporters-structure-descriptions-exexporterinstancerec)
- param2 - `unused`

Deallocate any private data.

---

<a id="exporters-selector-descriptions-exselshutdown"></a>

## exSelShutdown

- param1 - `unused`
- param2 - `unused`

Sent immediately before shutdown. Free all remaining memory and close any open file handles.

---

<a id="exporters-selector-descriptions-exselqueryexportcolorspace"></a>

## exSelQueryExportColorSpace

- param1 - [exExporterInstanceRec\*](structure-descriptions.md#exporters-structure-descriptions-exqueryexportcolorspacerec)
- param2 - `unused`

Describe the color space to be used during export.
