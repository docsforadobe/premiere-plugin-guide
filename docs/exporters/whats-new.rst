.. _exporters/whats-new:

Whats New
################################################################################

What's New in CC
================================================================================

A new Captions tab has been added to the Export Settings, for Closed Captioning export. For all formats, a sidecar file containing the captions can be exported. To learn how exporters can optionally embed Closed Captioning directly in the output file, see the Closed Captioning section.

Two new selectors have been added to GetExportSourceInfo in the :ref:`exporters/suites.export-info-suite`. You can use kExportInfo_UsePreviewFiles to check if the user has checked "Use Previews" in the Export Settings dialog. If so, if possible, reuse any preview files already rendered. You can use kExportInfo_NumAudioChannels to get the number of audio channels in a given source.

This can be used to automatically initialize the audio channel parameter in the Audio tab of the Export Settings to match the source.

In the :ref:`exporters/suites.export-param-suite`, a new function, MoveParam(), can be used to move an existing parameter to a new location.

----

What's New in CS6
================================================================================

Exporters can now use the :ref:`exporters/suites.exporter-utility-suite` for "push" model compression. The exporter host can simply push frames to a thread-safe exporter-specified callback. This will cut down on the code previously required for render loop management. It should also yield substantial performance increases for exporters that haven't finely tuned their multithreaded rendering. The "pull" model is still supported, and required for Encore and legacy versions of Premiere Pro and Media Encoder.

The new :ref:`exporters/suites.export-standard-param-suite` provides the standard parameters used in many built-in exporters. This can greatly reduce the amount of code needed to manage standard parameters for a typical exporter, and guarantee consistency with built-in exporters.

Stereoscopic video is now supported when exporting directly from Premiere Pro. In other words, when exports are queued to run in Adobe Media Encoder, they can not get stereoscopic video. Note that currently stereoscopic exporters must use the "pull" model and the new

MakeVideoRendererForTimelineWithStreamLabel() to get rendered frames from multiple video streams.

:ref:`exporters/suites.export-param-suite` now adds SetParamDescription(), to set tooltip strings for parameters. For the three line Export Summary description in the Export Settings dialog, we've swapped the 2nd and 3rd lines so that the bitrate summary comes after the audio summary. We've renamed the structure to make developers aware of this during a recompile.

Adobe Media Encoder now includes a Preset Browser that provides more organization for presets. Make sure your presets take advantage of this organization, and are shown in your desired proper location in the Preset Browser.

Exporters can now set events (error, warning, or info) for a specific encode in progress in the Adobe Media Encoder render queue. The existing call in the :ref:`universals/sweetpea-suites.error-suite` is not sufficient for AME to relate the event to a specific encode. So the new :ref:`exporters/suites.exporter-utility-suite` provides a way for exporters running either in Premiere Pro or Adobe Media Encoder to log events. These events are displayed in the application UI, and are also added to the AME encoding log.

Multiple exporters are now supported in a single plug-in. To support this, exExporterIn foRec is now set to exporters on *exShutdown*.

exQueryOutputSettingsRec has a new member, outUseMaximumRenderPreci­ sion, moving knowledge of this render parameter to the exporter.

----

What's New in CS5.5
================================================================================

A new call, ``RenderVideoFrameAndConformToPixelFormat``, has been added to the :ref:`exporters/suites.sequence-render-suite`. This allows an exporter to request a rendered frame and then conform it to a specific pixel format.

A new return value, ``exportReturn_ParamButtonCancel``, has been added to signify that an exporter is returning from ``exSelParamButton`` without modifying anything.

Export Controller API
********************************************************************************

We have opened up a new export controller API that can drive any exporter to generate a file in any format and perform custom post-processing operations. Developers wanting to integrate Premiere Pro with an asset management system will want to use this API instead.

----

What's New in CS5
================================================================================

``exQueryOutputFileListAfterExportRec`` is now ``exQueryOutputFileListRec``, with a slight change to the structure order.

We've also fixed a few bugs, such as bug 1925419, where all sliders would be given a checkbox to disable the control, as if exParamFlag_optional had been set.

We've made a couple new attributes available to exporters via the ``GetExportSourceInfo()`` call - the video poster frame time, and the source timecode.

3rd-party exporters can now be used to transcode assets to MPEG-2 or Blu-ray compliant files. Please refer to the Guidelines for Exporters in Encore for instructions on how to set up your exporter so that Encore can use it for transcoding.

----

Porting From the Compiler API
================================================================================

The export API replaces the old compiler API from CS3 and earlier versions. The export API combines the processing speed and quality of the old compiler API, with the UI flexibility of Media Encoder. Although the selectors and structures have been renamed and reorganized, much of the code that deals with rendering and writing frames is mostly the same.

The parameter UI is what has changed the most. Rather than having a standard set of parameters as standard compilers had, or having a completely custom UI as custom compilers had, in

the new exporter API, all parameters must be explicitly added using the :ref:`exporters/suites.export-param-suite`. First register the parameters during ``exSelGenerateDefaultParams``, and then provide the localized strings and constrained parameter values during ``exSelPostProcessParams``. When the exporter is sent ``exSelExport`` to export, get the parameter values, again using the :ref:`exporters/suites.export-param-suite`.
