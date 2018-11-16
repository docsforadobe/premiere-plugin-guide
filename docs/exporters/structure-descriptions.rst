.. _exporters/structure-descriptions:

Structure Descriptions
################################################################################

exDoExportRec
================================================================================

Selector: ``exSelExport``

Provides general export settings. The exporter should retrieve the parameter settings from the :ref:`exporters/suites.export-param-suite`.

::

  typedef struct {
    csSDK_uint32  exporterPluginID;
    void*         privateData;
    csSDK_uint32  fileType;
    csSDK_int32   exportAudio;
    csSDK_int32   exportVideo;
    PrTime        startTime;
    PrTime        endTime;
    csSDK_uint32  fileObject;
    PrTimelineID  timelineData;
    csSDK_int32   reserveMetaDataSpace;
    csSDK_int32   maximumRenderQuality;
    csSDK_int32   embedCaptions
  } exDoExportRec;

+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``exporterPluginID``     | The host's internal identifier for this exporter, used for various suite calls, such as in the :ref:`exporters/suites.sequence-render-suite` and :ref:`exporters/suites.sequence-audio-suite`. |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``privateData``          | Data allocated and managed by the exporter.                                                                                                                                                    |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fileType``             | The file format four character code set by the exporter during ``exSelStartup``.                                                                                                               |
|                          |                                                                                                                                                                                                |
|                          | Indicates which format the exporter should write, since exporters can support multiple formats.                                                                                                |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``exportAudio``          | If non-zero, export audio.                                                                                                                                                                     |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``exportVideo``          | If non-zero, export video.                                                                                                                                                                     |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``startTime``            | The start time of the sequence to export.                                                                                                                                                      |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``endTime``              | The end time of the sequence to export. If startTime is 0, also the total durection to export.                                                                                                 |
|                          |                                                                                                                                                                                                |
|                          | Range specified is ``[startTime, endTime)``, meaning the ``endTime`` is not actually included in the range.                                                                                    |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fileObject``           | For use with the :ref:`exporters/suites.export-file-suite`, to get and manipulate the file specified by the user.                                                                              |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``timelineData``         | Handle used for the Timeline Functions.                                                                                                                                                        |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``reserveMetaDataSpace`` | Amount to reserve in a file for metadata storage.                                                                                                                                              |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``maximumRenderQuality`` | If non-zero, the exporter should set ``SequenceRender_ParamsRec.inRenderQuality`` and ``inDeinterlaceQuality`` to ``kPrRenderQuality_Max``.                                                    |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``embedCaptions``        | New in CC. If non-zero, the exporter should embed captions obtained from the :ref:`universals/sweetpea-suites.captioning-suite`.                                                               |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

exExporterInfoRec
================================================================================

Selector: ``exSelStartup`` and ``exSelShutdown`` (starting in CS6)

Describe the exporter's capabilities by filling out this structure during ``exSelStartup``. For each filetype, populate exExporterInfoRec and return ``exportReturnIterateExporter``.

``exSelStartup`` will then be resent. Repeat the process until there are no more file formats to describe, then return ``exportReturn_IterateExporterDone``.

The fileType indicates which format the exporter should currently work with in subsequent calls.

::

  typedef struct {
    csSDK_uint32  unused;
    csSDK_uint32  fileType;
    prUTF16Char   fileTypeName[256];
    prUTF16Char   fileTypeDefaultExtension[256];
    csSDK_uint32  classID;
    csSDK_int32   exportReqIndex;
    csSDK_int32   wantsNoProgressBar;
    csSDK_int32   hideInUI;
    csSDK_int32   doesNotSupportAudioOnly;
    csSDK_int32   canExportVideo;
    csSDK_int32   canExportAudio;
    csSDK_int32   singleFrameOnly;
    csSDK_int32   maxAudiences;
    csSDK_int32   interfaceVersion;
    csSDK_uint32  isCacheable;
    csSDK_uint32  canConformToMatchParams;
    csSDK_uint32  canEmbedCaptions;
  } exExporterInfoRec;

+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fileType``                 | The file format four character code (e.g. 'AVIV' = Video for Windows, 'MooV' = QuickTime).                                                                                                                              |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fileTypeName``             | The localized display name for the fileype.                                                                                                                                                                             |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fileTypeDefaultExtension`` | The default extension for the filetype. An exporter can support multiple extensions per filetype, by implementing ``exSelQueryExportFileExtension``.                                                                    |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``classID``                  | Class identifier for the module, differentiates between exporters that support the same filetype and creates associations between different Media Abstraction Layer plug-ins.                                           |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``exportReqIndex``           | If an exporter supports multiple filetypes, this index will be incremented by the host for each call, as the exporter is requested to describe its capabilities for each filetype.                                      |
|                              |                                                                                                                                                                                                                         |
|                              | Initially zero, incremented by the host each time the exporter returns ``exportReturn_IterateExporter``.                                                                                                                |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``wantsNoProgressBar``       | If non-zero, the default exporter progress dialog will be turned off, allowing the exporter to display its own progress dialog.                                                                                         |
|                              |                                                                                                                                                                                                                         |
|                              | The exporter also will not get ``exportReturn_Abort`` errors from the host during callbacks – it must detect an abort on its own, and return ``exportReturn_Abort`` from ``exSelExport`` if the user aborts the export. |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``hideInUI``                 | Set this to non-zero if this filetype should only be used for making preview files, and should not be visible as a general export choice.                                                                               |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``doesNotSupportAudioOnly``  | Set this to non-zero for filetypes that do not support audio-only exports.                                                                                                                                              |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canExportVideo``           | Set this to non-zero if the exporter can output video.                                                                                                                                                                  |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canExportAudio``           | Set this to non-zero if the exporter can output audio.                                                                                                                                                                  |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``singleFrameOnly``          | Set this to non-zero if the exporter makes single frames (used by still image exporters).                                                                                                                               |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``maxAudiences``             |                                                                                                                                                                                                                         |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``interfaceVersion``         | Exporter API version that the plug-in supports.                                                                                                                                                                         |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``isCacheable``              | New in CS5. Set this non-zero to have Premiere Pro cache this exporter.                                                                                                                                                 |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canConformToMatchParams``  | New in CC. Set this to non-zero if the exporter wants to support the Match Source button.                                                                                                                               |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canEmbedCaptions``         | New in CC. Set this to non-zero if the exporter can embed Closed Captioning directly in the file.                                                                                                                       |
+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

exExporterInstanceRec
================================================================================

Selector: ``exSelBeginInstance`` and ``exSelEndInstance``

Provides access to the privateData for the indicated filetype, so that the exporter can allocate privateData and pass it to the host, or deallocate it.

::

  typedef struct {
    csSDK_uint32  exporterPluginID;
    csSDK_uint32  fileType;
    void*         privateData;
  } exExporterInstanceRec;

+----------------------+----------------------------------------------------------------------------------+
| ``exporterPluginID`` | The host's internal identifier for this exporter. Do not modify.                 |
+----------------------+----------------------------------------------------------------------------------+
| ``fileType``         | The file format four character code set by the exporter during ``exSelStartup``. |
+----------------------+----------------------------------------------------------------------------------+
| ``privateData``      | Data allocated and managed by the exporter.                                      |
+----------------------+----------------------------------------------------------------------------------+

----

exGenerateDefaultParamRec
================================================================================

Selector: ``exSelGenerateDefaultParams``

Provides access to the privateData for the indicated filetype, so that the exporter can generate the default parameter set.

::

  typedef struct {
    csSDK_uint32  exporterPluginID;
    void*         privateData;
    csSDK_uint32  fileType;
  } exExporterInstanceRec;

+----------------------+----------------------------------------------------------------------------------+
| ``exporterPluginID`` | The host's internal identifier for this exporter. Do not modify.                 |
+----------------------+----------------------------------------------------------------------------------+
| ``privateData``      | Data allocated and managed by the exporter.                                      |
+----------------------+----------------------------------------------------------------------------------+
| ``fileType``         | The file format four character code set by the exporter during ``exSelStartup``. |
+----------------------+----------------------------------------------------------------------------------+

----

exParamButtonRec
================================================================================

Selector: ``exSelParamButton``

Provides access to the privateData for the indicated filetype, and discloses the specific button hit by the user, since there can be multiple button parameters.

::

  typedef struct {
    csSDK_uint32       exporterPluginID;
    void*              privateData;
    csSDK_uint32       fileType;
    csSDK_int32        exportAudio;
    csSDK_int32        exportVideo;
    csSDK_int32        multiGroupIndex;
    exParamIdentifier  buttonParamIdentifier;
  } exParamButtonRec;

+---------------------------+----------------------------------------------------------------------------------+
| ``exporterPluginID``      | The host's internal identifier for this exporter. Do not modify.                 |
+---------------------------+----------------------------------------------------------------------------------+
| ``privateData``           | Data allocated and managed by the exporter.                                      |
+---------------------------+----------------------------------------------------------------------------------+
| ``fileType``              | The file format four character code set by the exporter during ``exSelStartup``. |
+---------------------------+----------------------------------------------------------------------------------+
| ``exportAudio``           | If non-zero, the current settings are set to export audio.                       |
+---------------------------+----------------------------------------------------------------------------------+
| ``exportVideo``           | If non-zero, the current settings are set to export video.                       |
+---------------------------+----------------------------------------------------------------------------------+
| ``multiGroupIndex``       | Discloses the index of the multi-group, containing the button hit by the user.   |
+---------------------------+----------------------------------------------------------------------------------+
| ``buttonParamIdentifier`` | Discloses the parameter ID of the button hit by the user.                        |
+---------------------------+----------------------------------------------------------------------------------+

----

exParamChangedRec
================================================================================

Selector: ``exSelValidateParamChanged``

Provides access to the privateData for the indicated filetype, and discloses the specific parameter changed by the user.

To notify the host that the plug-in is changing other parameters, set ``rebuildAllParams`` to a non-zero value.

::

  typedef struct {
    csSDK_uint32       exporterPluginID;
    void*              privateData;
    csSDK_uint32       fileType;
    csSDK_int32        exportAudio;
    csSDK_int32        exportVideo;
    csSDK_int32        multiGroupIndex;
    exParamIdentifier  changedParamIdentifier;
    csSDK_int32        rebuildAllParams;
  } exParamChangedRec;

+----------------------------+--------------------------------------------------------------------------------------------------------+
| ``exporterPluginID``       | The host's internal identifier for this exporter. Do not modify.                                       |
+----------------------------+--------------------------------------------------------------------------------------------------------+
| ``privateData``            | Data allocated and managed by the exporter.                                                            |
+----------------------------+--------------------------------------------------------------------------------------------------------+
| ``fileType``               | The file format four character code set by the exporter during ``exSelStartup``.                       |
+----------------------------+--------------------------------------------------------------------------------------------------------+
| ``exportAudio``            | If non-zero, the current settings are set to export audio.                                             |
+----------------------------+--------------------------------------------------------------------------------------------------------+
| ``exportVideo``            | If non-zero, the current settings are set to export video.                                             |
+----------------------------+--------------------------------------------------------------------------------------------------------+
| ``multiGroupIndex``        | Discloses the index of the multi-group, containing the parameter changed by the user.                  |
+----------------------------+--------------------------------------------------------------------------------------------------------+
| ``changedParamIdentifier`` | Discloses the parameter ID of the parameter changed by the user.                                       |
|                            |                                                                                                        |
|                            | May be empty if the changed item was exportAudio, exportVideo or the current multiGroupIndex.          |
+----------------------------+--------------------------------------------------------------------------------------------------------+
| ``rebuildAllParams``       | Set this to non-zero to tell the host to refresh ALL parameters using the latest provided information. |
|                            |                                                                                                        |
|                            | This can solve various problems when dynamically updating parameter visibility, valid ranges, etc.     |
+----------------------------+--------------------------------------------------------------------------------------------------------+

----

exParamSummaryRec
================================================================================

Selector: ``exSelGetParamSummary``

Provides access to the privateData for the indicated filetype, and provides buffers for the exporter to fill in with a localized summary of the parameters.

::

  typedef struct {
    csSDK_uint32  exporterPluginID;
    void*         privateData;
    csSDK_int32   exportAudio;
    csSDK_int32   exportVideo;
    prUTF16Char   videoSummary[256];
    prUTF16Char   audioSummary[256];
    prUTF16Char   bitrateSummary[256];
  } exParamSummaryRec;

+----------------------+---------------------------------------------------------------------+
| ``exporterPluginID`` | The host's internal identifier for this exporter. Do not modify.    |
+----------------------+---------------------------------------------------------------------+
| ``privateData``      | Data allocated and managed by the exporter.                         |
+----------------------+---------------------------------------------------------------------+
| ``exportAudio``      | If non-zero, the current settings are set to export audio.          |
+----------------------+---------------------------------------------------------------------+
| ``exportVideo``      | If non-zero, the current settings are set to export video.          |
+----------------------+---------------------------------------------------------------------+
| ``videoSummary``     | Fill these in with a line of a localized summary of the parameters. |
+----------------------+---------------------------------------------------------------------+
| ``audioSummary``     |                                                                     |
+----------------------+---------------------------------------------------------------------+
| ``bitrateSummary``   |                                                                     |
+----------------------+---------------------------------------------------------------------+

----

exPostProcessParamsRec
================================================================================

Selector: ``exSelPostProcessParams``

Provides access to the privateData for the indicated filetype.

::

  typedef struct {
    csSDK_uint32  exporterPluginID;
    void*         privateData;
    csSDK_uint32  fileType;
    csSDK_int32   exportAudio;
    csSDK_int32   exportVideo;
    csSDK_int32   doConformToMatchParams;
  } exPostProcessParamsRec;

+----------------------------+----------------------------------------------------------------------------------+
| ``exporterPluginID``       | The host's internal identifier for this exporter. Do not modify.                 |
+----------------------------+----------------------------------------------------------------------------------+
| ``privateData``            | Data allocated and managed by the exporter.                                      |
+----------------------------+----------------------------------------------------------------------------------+
| ``fileType``               | The file format four character code set by the exporter during ``exSelStartup``. |
+----------------------------+----------------------------------------------------------------------------------+
| ``exportAudio``            | If non-zero, the current settings are set to export audio.                       |
+----------------------------+----------------------------------------------------------------------------------+
| ``exportVideo``            | If non-zero, the current settings are set to export video.                       |
+----------------------------+----------------------------------------------------------------------------------+
| ``doConformToMatchParams`` | New in CC.                                                                       |
+----------------------------+----------------------------------------------------------------------------------+

----

exQueryExportFileExtensionRec
================================================================================

Selector: ``exSelQueryExportFileExtension``

Provides access to the privateData for the indicated filetype, and provides a buffer for the exporter to fill in with the file extension.

::

  typedef struct {
    csSDK_uint32  exporterPluginID;
    void*         privateData;
    csSDK_uint32  fileType;
    prUTF16Char   outFileExtension[256];
  } exQueryExportFileExtensionRec;

+----------------------+----------------------------------------------------------------------------------+
| ``exporterPluginID`` | The host's internal identifier for this exporter. Do not modify.                 |
+----------------------+----------------------------------------------------------------------------------+
| ``privateData``      | Data allocated and managed by the exporter.                                      |
+----------------------+----------------------------------------------------------------------------------+
| ``fileType``         | The file format four character code set by the exporter during ``exSelStartup``. |
+----------------------+----------------------------------------------------------------------------------+
| ``outFileExtension`` | Provide the file extension here, given the current parameter settings.           |
+----------------------+----------------------------------------------------------------------------------+

----

exQueryOutputFileListRec
================================================================================

Selector: ``exSelQueryOutputFileList``

Provides access to the privateData for the indicated filetype, and provides a pointer to a array of ``exOutputFileRecs`` for the exporter to fill in with the file paths.

::

  typedef struct {
    csSDK_uint32     exporterPluginID;
    void*            privateData;
    csSDK_uint32     fileType;
    csSDK_uint32     numOutputFiles;
    PrSDKString      path;
    exOutputFileRec  *outputFileRecs;
  } exQueryOutputFileListRec;

+----------------------+--------------------------------------------------------------------------------------------------------------+
| ``exporterPluginID`` | The host's internal identifier for this exporter. Do not modify.                                             |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| ``privateData``      | Data allocated and managed by the exporter.                                                                  |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| ``fileType``         | The file format four character code set by the exporter during ``exSelStartup``.                             |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| ``numOutputFiles``   | On the first call to ``exSelQueryOutputFileList``, provide the number of file paths here.                    |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| ``path``             | New in CS5. Contains the primary intended destination path provided by the host.                             |
+----------------------+--------------------------------------------------------------------------------------------------------------+
| ``outputFileRecs``   | An array of ``exOutputFileRecs``.                                                                            |
|                      |                                                                                                              |
|                      | On the second call to ``exSelQueryOutputFileList``, the path length (including trailing null) for each path. |
|                      |                                                                                                              |
|                      | On the third call, fill in the path of each exOutputFileRec.                                                 |
|                      |                                                                                                              |
|                      | ::                                                                                                           |
|                      |                                                                                                              |
|                      |   typedef struct {                                                                                           |
|                      |     int           pathLength;                                                                                |
|                      |     prUTF16Char*  path;                                                                                      |
|                      |   } exOutputFileRec;                                                                                         |
+----------------------+--------------------------------------------------------------------------------------------------------------+

----

exQueryOutputSettingsRec
================================================================================

Selector: ``exSelQueryOutputSettings``

Provides access to the privateData for the indicated filetype, and provides a set of members for the exporter to fill in with the current export settings.

::

  typedef struct {
    csSDK_uint32        exporterPluginID;
    void*               privateData;
    csSDK_uint32        fileType;
    csSDK_int32         inMultiGroupIndex;
    csSDK_int32         inExportVideo;
    csSDK_int32         inExportAudio;
    csSDK_int32         outVideoWidth;
    csSDK_int32         outVideoHeight;
    PrTime              outVideoFrameRate;
    csSDK_int32         outVideoAspectNum;
    csSDK_int32         outVideoAspectDen;
    csSDK_int32         outVideoFieldType;
    double              outAudioSampleRate;
    PrAudioSampleType   outAudioSampleType;
    PrAudioChannelType  outAudioChannelType;
    csSDK_uint32        outBitratePerSecond;
    csSDK_int32         outUseMaximumRenderPrecision;
  } exQueryOutputSettingsRec;

+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``exporterPluginID``             | The host's internal identifier for this exporter. Do not modify.                                                                   |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``privateData``                  | Data allocated and managed by the exporter.                                                                                        |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``fileType``                     | The file format four character code set by the exporter during ``exSelStartup``.                                                   |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``inMultiGroupIndex``            | Return the parameter settings of the multi-group with this index.                                                                  |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``inExportVideo``                | If non-zero, the current settings are set to export video.                                                                         |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``inExportAudio``                | If non-zero, the current settings are set to export audio.                                                                         |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``outVideoWidth``                | Return each parameter setting, by getting the current value of the parameter using the :ref:`exporters/suites.export-param-suite`. |
| ``outVideoHeight``               |                                                                                                                                    |
|                                  | Some settings, such as ``outVideoFieldType``, may be implicit, for example if the format only supports progressive frames.         |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``outUseMaximumRenderPrecision`` | New in CS6. If non-zero, renders will always be made at maximum bit-depth.                                                         |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

----

exQueryStillSequenceRec
================================================================================

Selector: ``exSelQueryStillSequence``

Provides access to the privateData for the indicated filetype, and provides a set of members for the exporter to provide information on how it would export the sequence of stills.

::

  typedef struct {
    csSDK_uint32  exporterPluginID;
    void*         privateData;
    csSDK_uint32  fileType;
    csSDK_int32   exportAsStillSequence;
    PrTime        exportFrameRate;
  } exQueryStillSequenceRec;

+---------------------------+----------------------------------------------------------------------------------------------+
| ``exporterPluginID``      | The host's internal identifier for this exporter. Do not modify.                             |
+---------------------------+----------------------------------------------------------------------------------------------+
| ``privateData``           | Data allocated and managed by the exporter.                                                  |
+---------------------------+----------------------------------------------------------------------------------------------+
| ``fileType``              | The file format four character code set by the exporter during ``exSelStartup``.             |
+---------------------------+----------------------------------------------------------------------------------------------+
| ``exportAsStillSequence`` | Set this to non-zero to tell the host that the exporter can export the stills as a sequence. |
+---------------------------+----------------------------------------------------------------------------------------------+
| ``exportFrameRate``       | Set this to the frame rate of the still sequence.                                            |
+---------------------------+----------------------------------------------------------------------------------------------+

----

exValidateOutputSettingsRec
================================================================================

Selector: ``exSelValidateOutputSettings``

Provides access to the privateData for the indicated filetype, so that the exporter can validate the current parameter settings.

::

  typedef struct {
    csSDK_uint32  exporterPluginID;
    void*         privateData;
    csSDK_uint32  fileType;
  } exExporterInstanceRec;

+----------------------+----------------------------------------------------------------------------------+
| ``exporterPluginID`` | The host's internal identifier for this exporter. Do not modify.                 |
+----------------------+----------------------------------------------------------------------------------+
| ``privateData``      | Data allocated and managed by the exporter.                                      |
+----------------------+----------------------------------------------------------------------------------+
| ``fileType``         | The file format four character code set by the exporter during ``exSelStartup``. |
+----------------------+----------------------------------------------------------------------------------+
