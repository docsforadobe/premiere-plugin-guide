.. _exporters/suites:

Suites
################################################################################

For information on how to acquire and manage suites, see the SweetPea Suites section.

----

.. _exporters/suites.export-file-suite:

Export File Suite
================================================================================

A cross-platform suite for writing to files on disk. Also provides a call to get the file path, given the file object.

Version 2 resolves a mismatch in seek modes in version 1, where ``fileSeekMode_End`` was handled as ``fileSeekMode_Current`` and visa versa.

See PrSDKExportFileSuite.h.

----

.. _exporters/suites.export-info-suite:

Export Info Suite
================================================================================

GetExportSourceInfo
********************************************************************************

Get information on the source currently being exported.

::

  prSuiteError (*GetExportSourceInfo)(
    csSDK_uint32                inExporterPluginID,
    PrExportSourceInfoSelector  inSelector,
    PrParam                     *outSourceInfo);

+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                **Value**                 |  **Type**   |                                                                                         **Description**                                                                                         |
+==========================================+=============+=================================================================================================================================================================================================+
| ``kExportInfo_VideoWidth``               | Int32       | Width of source video                                                                                                                                                                           |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_VideoHeight``              | Int32       | Height of source video                                                                                                                                                                          |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_VideoFrameRate``           | PrTime      | Frame rate                                                                                                                                                                                      |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_VideoFieldType``           | Int32       | One of the prFieldType values                                                                                                                                                                   |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_VideoDuration``            | Int64       | A PrTime value                                                                                                                                                                                  |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_PixelAspectNumerator``     | Int32       | Pixel aspect ratio (PAR) numerator                                                                                                                                                              |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_PixelAspectDenominator``   | Int32       | Pixel aspect ratio denominator                                                                                                                                                                  |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_AudioDuration``            | Int64       | A PrTime value                                                                                                                                                                                  |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_AudioChannelsType``        | Int32       | One of the ``PrAudioChannelType`` values.                                                                                                                                                       |
|                                          |             |                                                                                                                                                                                                 |
|                                          |             | Returns 0 (which is undefined) if there's no audio.                                                                                                                                             |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_AudioSampleRate``          | Float64     |                                                                                                                                                                                                 |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_SourceHasAudio``           | Bool        | Non-zero if source has audio                                                                                                                                                                    |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_SourceHasVideo``           | Bool        | Non-zero if source has video                                                                                                                                                                    |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_RenderAsPreview``          | Bool        | Returns a non-zero value if currently rendering preview files.                                                                                                                                  |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_SequenceGUID``             | Guid        | A ``PrPluginID``, which is a unique GUID for the sequence.                                                                                                                                      |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_SessionFilePath``          | PrMemoryPtr | A ``prUTF16Char`` array. The exporter should release the pointer using the :ref:`universals/sweetpea-suites.memory-manager-suite`.                                                              |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_VideoPosterFrameTickTime`` | Int64       | New in CS5. A PrTime value.                                                                                                                                                                     |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_SourceTimecode``           | PrMemoryPtr | New in CS5.0.2. The timecode of the source clip or sequence.                                                                                                                                    |
|                                          |             |                                                                                                                                                                                                 |
|                                          |             | The sequence timecode is set by the Start Time of a sequence using the sequence wing-menu. A pointer to a ExporterTimecodeRec structure.                                                        |
|                                          |             |                                                                                                                                                                                                 |
|                                          |             | The exporter should release the pointer using the :ref:`universals/sweetpea-suites.memory-manager-suite`.                                                                                       |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_UsePreviewFiles``          | Bool        | New in CC. Use this to check if the user has checked "Use Previews" in the Export Settings dialog.                                                                                              |
|                                          |             |                                                                                                                                                                                                 |
|                                          |             | If so, if possible, reuse any preview files already rendered, which can be retrieved using ``AcquireVideoSegmentsWithPreviewsID`` in the :ref:`universals/sweetpea-suites.video-segment-suite`. |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``kExportInfo_NumAudioChannels``         | Int32       | New in CC. Get the number of audio channels in a given source.                                                                                                                                  |
|                                          |             |                                                                                                                                                                                                 |
|                                          |             | This can be used to automatically initialize the audio channel parameter in the Audio tab of the Export Settings to match the source.                                                           |
+------------------------------------------+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

::

  typedef struct {
    csSDK_int64  mTimecodeTicks;
    csSDK_int64  mTicksPerFrame;
    bool         mTimecodeStartPrefersDropFrame;
  } ExporterTimecodeRec;

----

.. _exporters/suites.export-param-suite:

Export Param Suite
================================================================================

Specify all parameters for your exporter UI. See PrSDKExportParamSuite.h.

Also, see the SDK Export sample for a demonstration of how to use this suite.

To provide either a set of radio buttons or a drop-down list of choices, use AddConstrainedValuePair().

Adding two choices will result in a pair of radio buttons side-by-side.

Three or more choices will be displayed as a drop-down box.

Adding only one value will result in a hard-coded string.

In CS5, and later fixed in 5.0.2, there is an issue where width and height ranges aren't correctly set.

You may notice this when adjusting the width and height in the Export Settings UI.

By unclicking the chain that constrains width and height ratio, you will be able to modify the width and height.

As a side-effect of this bug, if the exporter is used to render preview files in an Editing Mode, the user will be able to choose any preview frame size between 24x24 and 10240x8192.

CS6 adds SetParamDescription(), to set tooltip strings for parameters.

CC adds MoveParam(), to move an existing parameter to a new location. This can be used for both standard parameters and group parameters.

----

.. _exporters/suites.export-progress-suite:

Export Progress Suite
================================================================================

For pull-model exporters. Report progress during the export. Also, handle the case where the user pauses or cancels an export. See PrSDKExportProgressSuite.h.

----

.. _exporters/suites.export-standard-param-suite:

Export Standard Param Suite
================================================================================

New in CS6. A suite for registering one of several common parameter sets, reducing parameter management code on the plug-in side.

AddStandardParams
********************************************************************************

Register a set of standard parameters to be used by the exporter.

Call during ``exSelGenerateDefaultParams``.

::

  prSuiteError (*AddStandardParams)(
    csSDK_uint32       inExporterID,
    PrSDKStdParamType  inSDKStdParamType);

+-----------------------+------------------------------------------------------+
|     **Parameter**     |                   **Description**                    |
+=======================+======================================================+
| ``inExporterID``      | Pass in ``exporterPluginID`` from ``exDoExportRec``. |
+-----------------------+------------------------------------------------------+
| ``inSDKStdParamType`` | Use one of the following:                            |
|                       |                                                      |
|                       | ::                                                   |
|                       |                                                      |
|                       |   enum PrSDKStdParamType {                           |
|                       |     SDKStdParams_Video,                              |
|                       |     SDKStdParams_Audio,                              |
|                       |     SDKStdParams_Still,                              |
|                       |     SDKStdParams_VideoBitrateGroup,                  |
|                       |     SDKStdParams_Video_NoRenderMax,                  |
|                       |     SDKStdParams_Video_AddRenderMax,                 |
|                       |     SDKStdParams_AudioTabOnly,                       |
|                       |     SDKStdParams_AudioBitrateGroup,                  |
|                       |     SDKStdParams_VideoWithSizePopup                  |
|                       |   };                                                 |
+-----------------------+------------------------------------------------------+

PostProcessParamNames
********************************************************************************

Call during ``exSelPostProcessParams``.

::

  prSuiteError (*PostProcessParamNames)(
    csSDK_uint32        inExporterID,
    PrAudioChannelType  inSourceAudioChannelType);

+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
|        **Parameter**         |                                                            **Description**                                                             |
+==============================+========================================================================================================================================+
| ``inExporterID``             | Pass in ``exporterPluginID`` from ``exDoExportRec``.                                                                                   |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``inSourceAudioChannelType`` | Pass in the source audio channel type, which can be queried from GetExportSourceInfo in the :ref:`exporters/suites.export-info-suite`. |
+------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

QueryOutputSettings
********************************************************************************

Call during ``exSelQueryOutputSettings``.

::

  prSuiteError (*QueryOutputSettings)(
    csSDK_uint32               inExporterID,
    exQueryOutputSettingsRec*  outOutputSettings);

+-----------------------+-----------------------------------------------------------------------------+
|     **Parameter**     |                               **Description**                               |
+=======================+=============================================================================+
| ``inExporterID``      | Pass in exporterPluginID from exDoExportRec.                                |
+-----------------------+-----------------------------------------------------------------------------+
| ``outOutputSettings`` | This structure will be filled out based on the standard parameter settings. |
+-----------------------+-----------------------------------------------------------------------------+

MakeParamSummary
********************************************************************************

Call during ``exSelGetParamSummary``.

::

  prSuiteError (*MakeParamSummary)(
    csSDK_uint32  inExporterID,
    csSDK_int32   inDoVideo,
    csSDK_int32   inDoAudio,
    prUTF16Char*  outVideoDescription,
    prUTF16Char*  outAudioDescription);

+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|      **Parameter**      |                                                                **Description**                                                                 |
+=========================+================================================================================================================================================+
| ``inExporterID``        | Pass in ``exporterPluginID`` from ``exDoExportRec``.                                                                                           |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inDoVideo``           | Pass in ``exParamSummaryRec.exportVideo`` / ``exportAudio`` so that the summary will be set based on whether video / audio are being exported. |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inDoAudio``           |                                                                                                                                                |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| ``outVideoDescription`` | These will be filled out based on the standard parameter settings.                                                                             |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| ``outAudioDescription`` |                                                                                                                                                |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

----

.. _exporters/suites.exporter-utility-suite:

Exporter Utility Suite
================================================================================

New in CS6. Provides functions for push-model exporters, and also provides a way to register an export event (error, warning, or info) to be displayed by the host and written to the log.

DoMultiPassExportLoop
********************************************************************************

Register the callback to be made to push video frames to the exporter. This function assumes that your exporter supports ``exSelQueryOutputSettings``, which will be called.

::

  prSuiteError (*DoMultiPassExportLoop)(
    csSDK_uint32                                     inExporterID,
    const ExportLoopRenderParams*                    inRenderParams,
    csSDK_uint32                                     inNumberOfPasses,
    PrSDKMultipassExportLoopFrameCompletionFunction  inCompletionFunction,
    void*                                            inCompletionParam);

+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      **Parameter**       |                                                                                                              **Description**                                                                                                              |
+==========================+===========================================================================================================================================================================================================================================+
| ``inExporterID``         | Pass in ``exporterPluginID`` from ``exDoExportRec``.                                                                                                                                                                                      |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inRenderParams``       | Pass in the parameters that will be used for the render loop that will push rendered frames via the provided callback ``inCompletionFunction``.                                                                                           |
|                          |                                                                                                                                                                                                                                           |
|                          | ``inReservedProgressPreRender`` and ``inReservedProgressPostRender`` should be set to the amount of progress to be shown in any progress bar before starting the render loop, and how much is remaining after finishing the render loop.  |
|                          |                                                                                                                                                                                                                                           |
|                          | These values default to zero.                                                                                                                                                                                                             |
|                          |                                                                                                                                                                                                                                           |
|                          | ::                                                                                                                                                                                                                                        |
|                          |                                                                                                                                                                                                                                           |
|                          |   typedef struct {                                                                                                                                                                                                                        |
|                          |     csSDK_int32    inRenderParamsSize;                                                                                                                                                                                                    |
|                          |     csSDK_int32    inRenderParamsVersion;                                                                                                                                                                                                 |
|                          |     PrPixelFormat  inFinalPixelFormat;                                                                                                                                                                                                    |
|                          |     PrTime         inStartTime;                                                                                                                                                                                                           |
|                          |     PrTime         inEndTime;                                                                                                                                                                                                             |
|                          |     float          inReservedProgressPreRender;                                                                                                                                                                                           |
|                          |     float          inReservedProgressPostRender;                                                                                                                                                                                          |
|                          |   } ExportLoopRenderParams;                                                                                                                                                                                                               |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inNumberOfPasses``     | Set to 1, unless you need multipass encoding such as two-pass or three-pass encoding.                                                                                                                                                     |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inCompletionFunction`` | Provide your own callback here, which will be called when the host pushes rendered frames. Use the following function signature:                                                                                                          |
|                          |                                                                                                                                                                                                                                           |
|                          | ::                                                                                                                                                                                                                                        |
|                          |                                                                                                                                                                                                                                           |
|                          |   typedef prSuiteError (*PrSDKMultipassExportLoop FrameCompletionFunction)(                                                                                                                                                               |
|                          |     csSDK_uint32  inWhichPass,                                                                                                                                                                                                            |
|                          |     csSDK_uint32  inFrameNumber,                                                                                                                                                                                                          |
|                          |     csSDK_uint32  inFrameRepeatCount,                                                                                                                                                                                                     |
|                          |     PPixHand      inRenderedFrame,                                                                                                                                                                                                        |
|                          |     void*         inCallbackData);                                                                                                                                                                                                        |
|                          |                                                                                                                                                                                                                                           |
|                          | Currently, there is no simple way to ensure that pushed frames survive longer than the life of the function call.                                                                                                                         |
|                          |                                                                                                                                                                                                                                           |
|                          | If you are interested in this capability, please contact us and explain your need.                                                                                                                                                        |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inCompletionParam``    | Pass in a void * to the data you wish to send to your ``inCompletionFunction`` above in ``inCallbackData``.                                                                                                                               |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

ReportIntermediateProgressForRepeatedVideoFrame
********************************************************************************

Register the callback to be made to push video frames to the exporter.

This function assumes that your exporter supports ``exSelQueryOutputSettings``, which will be called.

::

  prSuiteError (*ReportIntermediateProgressForRepeatedVideoFrame)(
    csSDK_uint32  inExporterID,
    csSDK_uint32  inRepetitionsProcessedSinceLastUpdate);

+-------------------------------------------+---------------------------------------------------------------------------------------+
|               **Parameter**               |                                    **Description**                                    |
+===========================================+=======================================================================================+
| ``inExporterID``                          | Pass in ``exporterPluginID`` from ``exDoExportRec``.                                  |
+-------------------------------------------+---------------------------------------------------------------------------------------+
| ``inRepetitionsProcessedSinceLastUpdate`` | Pass in the number of repeated frames processed since the last call was made, if any. |
+-------------------------------------------+---------------------------------------------------------------------------------------+

ReportEvent
********************************************************************************

Report an event to the host, for a specific encode in progress in the Adobe Media Encoder render queue or Premiere Pro.

These events are displayed in the application UI, and are also added to the AME encoding log.

::

  prSuiteError (*ReportEvent)(
    csSDK_uint32        inExporterID,
    csSDK_uint32        inEventType,
    const prUTF16Char*  inEventTitle,
    const prUTF16Char*  inEventDescription);

+------------------------+------------------------------------------------------------------------------+
|     **Parameter**      |                               **Description**                                |
+========================+==============================================================================+
| ``inExporterID``       | Pass in ``exporterPluginID`` from ``exDoExportRec``.                         |
+------------------------+------------------------------------------------------------------------------+
| ``inEventType``        | Use one of the types from the :ref:`universals/sweetpea-suites.error-suite`: |
|                        |                                                                              |
|                        | - ``kEventTypeInformational``,                                               |
|                        | - ``kEventTypeWarning``, or                                                  |
|                        | - ``kEventTypeError``                                                        |
+------------------------+------------------------------------------------------------------------------+
| ``inEventTitle``       | Provide information about the event for the user.                            |
+------------------------+------------------------------------------------------------------------------+
| ``inEventDescription`` |                                                                              |
+------------------------+------------------------------------------------------------------------------+

----

.. _exporters/suites.palette-suite:

Palette Suite
================================================================================

A seldom-used suite for palettizing an image, for example, for GIFs. See PrSDKPaletteSuite.h.

----

.. _exporters/suites.sequence-audio-suite:

Sequence Audio Suite
================================================================================

Get audio from the host.

MakeAudioRenderer
********************************************************************************

Create an audio renderer, in preparation to get rendered audio from the host.

::

  prSuiteError (*MakeAudioRenderer)(
    csSDK_uint32        inPluginID,
    PrTime              inStartTime,
    PrAudioChannelType  inChannelType,
    PrAudioSampleType   inSampleType,
    float               inSampleRate,
    csSDK_uint32*       outAudioRenderID);

+----------------------+---------------------------------------------------------------------------------------+
|    **Parameter**     |                                    **Description**                                    |
+======================+=======================================================================================+
| ``inPluginID``       | Pass in ``exporterPluginID`` from ``exDoExportRec``.                                  |
+----------------------+---------------------------------------------------------------------------------------+
| ``inStartTime``      | Start time for the audio requests.                                                    |
+----------------------+---------------------------------------------------------------------------------------+
| ``inChannelType``    | ``PrAudioChannelType`` enum value for the channel type needed.                        |
+----------------------+---------------------------------------------------------------------------------------+
| ``inSampleType``     | This should always be ``kPrAudioSampleType_32BitFloat``. Other types are unsupported. |
+----------------------+---------------------------------------------------------------------------------------+
| ``inSampleRate``     | Samples per second.                                                                   |
+----------------------+---------------------------------------------------------------------------------------+
| ``outAudioRenderID`` | This ID passed back is needed for subsequent calls to this suite.                     |
+----------------------+---------------------------------------------------------------------------------------+

ReleaseAudioRenderer
********************************************************************************

Release the audio renderer when the exporter is done requesting audio.

::

  prSuiteError (*ReleaseAudioRenderer)(
    csSDK_uint32  inPluginID,
    csSDK_uint32  inAudioRenderID);

+---------------------+--------------------------------------------------------+
|    **Parameter**    |                    **Description**                     |
+=====================+========================================================+
| ``inPluginID``      | Pass in ``exporterPluginID`` from ``exDoExportRec``.   |
+---------------------+--------------------------------------------------------+
| ``inAudioRenderID`` | The call will release the audio renderer with this ID. |
+---------------------+--------------------------------------------------------+

GetAudio
********************************************************************************

Returns from the host the next contiguous requested number of audio sample frames, specified in inFrameCount, in inBuffer as arrays of uninterleaved floating point values.

Returns ``suiteError_NoError`` if no error.

The plug-in must manage the memory allocation of inBuffer, which must point to n buffers of floating point values of length inFrameCount, where n is the number of channels.

When inClipAudio is non-zero, this parameter makes GetAudio clip the audio samples at +/- 1.0.

::

  prSuiteError (*GetAudio)(
    csSDK_uint32  inAudioRenderID,
    csSDK_uint32  inFrameCount,
    float**       inBuffer,
    char          inClipAudio);

+---------------------+------------------------------------------------------------------------------------------------------------------+
|    **Parameter**    |                                                 **Description**                                                  |
+=====================+==================================================================================================================+
| ``inAudioRenderID`` | Pass in the ``outAudioRenderID`` returned from ``MakeAudioRenderer()``.                                          |
|                     |                                                                                                                  |
|                     | This gives the host the context of the audio render.                                                             |
+---------------------+------------------------------------------------------------------------------------------------------------------+
| ``inFrameCount``    | The number of audio frames to return in inBuffer.                                                                |
|                     |                                                                                                                  |
|                     | The next contiguous audio frames will always be returned, unless ``ResetAudioToBeginning`` has just been called. |
+---------------------+------------------------------------------------------------------------------------------------------------------+
| ``inBuffer``        | An array of float arrays, allocated by the exporter.                                                             |
|                     |                                                                                                                  |
|                     | The host returns the samples for each audio channel in a separate array.                                         |
+---------------------+------------------------------------------------------------------------------------------------------------------+
| ``inClipAudio``     | When true, ``GetAudio`` will return audio clipped at +/- 1.0. Otherwise, it will return unclipped audio.         |
+---------------------+------------------------------------------------------------------------------------------------------------------+

ResetAudioToBeginning
********************************************************************************

This call will reset the position on the audio generation to time zero. This can be used for multipass encoding.

::

  prSuiteError (*ResetAudioToBeginning)(
    csSDK_uint32  inAudioRenderID);

GetMaxBlip
********************************************************************************

Returns the maximum number of audio sample frames that can be requested from one call to ``GetAudio`` in ``maxBlipSize``.

::

  prSuiteError (*GetMaxBlip)(
    csSDK_uint32  inAudioRenderID,
    PrTime        inTicksPerFrame,
    csSDK_uint32*  maxBlipSize);

----

.. _exporters/suites.sequence-render-suite:

Sequence Render Suite
================================================================================

Get rendered video from one of the renderers available to the host. This may use one of the host's built-in renderers, or a plug-in renderer, if available For best performance, use the asynchronous render requests with the source media prefetching calls, although synchronous rendering is available too.

Version 4, new in CS5.5, adds ``RenderVideoFrameAndConformToPixelFormat()``.

MakeVideoRenderer()
********************************************************************************

Create a video renderer, in preparation to get rendered video.

::

  prSuiteError (*MakeVideoRenderer)(
    csSDK_uint32   pluginID,
    csSDK_uint32*  outVideoRenderID
    PrTime         inFrameRate);

+----------------------+-------------------------------------------------------------------+
|    **Parameter**     |                          **Description**                          |
+======================+===================================================================+
| ``pluginID``         | Pass in ``exporterPluginID`` from ``exDoExportRec``.              |
+----------------------+-------------------------------------------------------------------+
| ``outVideoRenderID`` | This ID passed back is needed for subsequent calls to this suite. |
+----------------------+-------------------------------------------------------------------+
| ``inFrameRate``      | Frame rate, in ticks.                                             |
+----------------------+-------------------------------------------------------------------+

ReleaseVideoRenderer()
********************************************************************************

Release the video renderer when the exporter is done requesting video.

::

  prSuiteError (*ReleaseVideoRenderer)(
    csSDK_uint32  pluginID,
    csSDK_uint32  inVideoRenderID);

+---------------------+--------------------------------------------------------+
|    **Parameter**    |                    **Description**                     |
+=====================+========================================================+
| ``pluginID``        | Pass in ``exporterPluginID`` from ``exDoExportRec``.   |
+---------------------+--------------------------------------------------------+
| ``inVideoRenderID`` | The call will release the video renderer with this ID. |
+---------------------+--------------------------------------------------------+

struct SequenceRender_ParamsRec
********************************************************************************

Fill this structure in before calling ``RenderVideoFrame()``, ``QueueAsyncVideoFrameRender()``, or ``PrefetchMediaWithRenderParameters()``.

Note that if the frame aspect ratio of the request does not match that of the sequence, the frame will be letterboxed or pillarboxed, rather than stretched to fit the frame.

::

  typedef struct {
    const PrPixelFormat*  inRequestedPixelFormatArray;
    csSDK_int32           inRequestedPixelFormatArrayCount;
    csSDK_int32           inWidth;
    csSDK_int32           inHeight;
    csSDK_int32           inPixelAspectRatioNumerator;
    csSDK_int32           inPixelAspectRatioDenominator;
    PrRenderQuality       inRenderQuality;
    prFieldType           inFieldType;
    csSDK_int32           inDeinterlace;
    PrRenderQuality       inDeinterlaceQuality;
    csSDK_int32           inCompositeOnBlack;
  } SequenceRender_ParamsRec;

+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|              **Member**              |                                                                                    **Description**                                                                                     |
+======================================+========================================================================================================================================================================================+
| ``inRequestedPixelFormatArray``      | An array of PrPixelFormats that list your format preferences in order.                                                                                                                 |
+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inRequestedPixelFormatArrayCount`` | Size of the pixel format array.                                                                                                                                                        |
+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inWidth``                          | Width to render at.                                                                                                                                                                    |
+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inHeight``                         | Height to render at.                                                                                                                                                                   |
+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inPixelAspectRatioNumerator``      | Numerator of the pixel aspect ratio.                                                                                                                                                   |
+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inPixelAspectRatioDenominator``    | Denominator of the pixel aspect ratio.                                                                                                                                                 |
+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inRenderQuality``                  | Use one of the PrRenderQuality enumerated values.                                                                                                                                      |
+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inFieldType``                      | Use one of the prFieldType constants.                                                                                                                                                  |
+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inDeinterlace``                    | Set to non-zero, to force an explicit deinterlace. Otherwise, the renderer will use the output field setting to determine whether to automatically deinterlace any interlaced sources. |
+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inDeinterlaceQuality``             | Use one of the PrRenderQuality enumerated values.                                                                                                                                      |
+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inCompositeOnBlack``               | Set to non-zero, to composite the render on black.                                                                                                                                     |
+--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

struct SequenceRender_GetFrameReturnRec
********************************************************************************

Returned from ``RenderVideoFrame()`` and passed by ``PrSDKSequenceAsyncRenderCompletionProc()``.

::

  typedef struct {
    void*        asyncCompletionData;
    csSDK_int32  returnVal;
    csSDK_int32  repeatCount;
    csSDK_int32  onMarker;
    PPixHand     outFrame;
  } SequenceRender_GetFrameReturnRec;

+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
|       **Member**        |                                                                 **Description**                                                                  |
+=========================+==================================================================================================================================================+
| ``asyncCompletionData`` | Passed to ``PrSDKSequenceAsyncRenderCompletionProc()`` from ``QueueAsyncVideoFrameRender()``.                                                    |
|                         |                                                                                                                                                  |
|                         | Not used by ``RenderVideoFrame()``.                                                                                                              |
+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ``returnVal``           | ``ErrNone``, ``Abort``, ``Done``, or an error code.                                                                                              |
+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ``repeatCount``         | The number of repeated frames from this frame forward.                                                                                           |
|                         |                                                                                                                                                  |
|                         | In the output file, this could be writing NULL frames, changing the current frame's duration, or whatever is appropriate according to the codec. |
+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onMarker``            | If non-zero, there is a marker on this frame.                                                                                                    |
+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| ``outFrame``            | Returned from ``RenderVideoFrame()``. Not returned from ``PrSDKSequenceAsyncRenderCompletionProc()``                                             |
+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

RenderVideoFrame()
********************************************************************************

The basic, synchronous call to get a rendered frame from the host.

Returns:

- ``suiteError_NoError`` if you can continue exporting,
- ``exportReturn_Abort`` if the user aborted the export,
- ``exportReturn_Done`` if the export has finished, or
- an error code.

::

  prSuiteError (*RenderVideoFrame)(
    csSDK_uint32                       inVideoRenderID,
    PrTime                             inTime,
    SequenceRender_ParamsRec*          inRenderParams,
    PrRenderCacheType                  inCacheFlags,
    SequenceRender_GetFrameReturnRec*  getFrameReturn);

+---------------------+-----------------------------------------------------------------------------------------------------+
|    **Parameter**    |                                           **Description**                                           |
+=====================+=====================================================================================================+
| ``inVideoRenderID`` | Pass in the ``outVideoRenderID`` returned from ``MakeVideoRenderer()``.                             |
|                     |                                                                                                     |
|                     | This gives the host the context of the video render.                                                |
+---------------------+-----------------------------------------------------------------------------------------------------+
| ``inTime``          | The frame time requested.                                                                           |
+---------------------+-----------------------------------------------------------------------------------------------------+
| ``inRenderParams``  | The details of the render.                                                                          |
+---------------------+-----------------------------------------------------------------------------------------------------+
| ``inCacheFlags``    | One or more cache flags.                                                                            |
+---------------------+-----------------------------------------------------------------------------------------------------+
| ``getFrameReturn``  | Passes back a structure that contains info about the frame returned, and the rendered frame itself. |
+---------------------+-----------------------------------------------------------------------------------------------------+

GetFrameInfo()
********************************************************************************

Gets information about a given frame.

Currently, ``SequenceRender_FrameInfoRec`` only contains ``repeatCount``, which is the number of repeated frames from this frame forward.

::

  prSuiteError (*GetFrameInfo)(
    csSDK_uint32                 inVideoRenderID,
    PrTime                       inTime,
    SequenceRender_FrameInfoRec*  outFrameInfo);

SetAsyncRenderCompletionProc()
********************************************************************************

Register a notification callback for getting asynchronously rendered frames when the render completes.

``asyncGetFrameCallback`` should have the signature described in ``PrSDKSequenceAsyncRenderCompletionProc`` below.

::

  prSuiteError (*SetAsyncRenderCompletionProc)(
    csSDK_uint32                            inVideoRenderID,
    PrSDKSequenceAsyncRenderCompletionProc  asyncGetFrameCallback,
    long                                    callbackRef);

+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
|       **Parameter**       |                                                            **Description**                                                             |
+===========================+========================================================================================================================================+
| ``inVideoRenderID``       | Pass in the ``outVideoRenderID`` returned from ``MakeVideoRenderer()``.                                                                |
|                           |                                                                                                                                        |
|                           | This will be passed to ``PrSDKSequenceAsyncRenderCompletionProc``.                                                                     |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``asyncGetFrameCallback`` | The notification callback.                                                                                                             |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``inCallbackRef``         | A pointer holding data private to the exporter.                                                                                        |
|                           |                                                                                                                                        |
|                           | This could be, for example, a pointer to an exporter instance. This will also be passed to ``PrSDKSequenceAsyncRenderCompletionProc``. |
+---------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

PrSDKSequenceAsyncRenderCompletionProc()
********************************************************************************

Use this function signature for your callback used for async frame notification, passed to ``SetAsyncRenderCompletionProc``.

Error status (error or abort) is returned in ``inGetFrameReturn``.

::

  void (*PrSDKSequenceAsyncRenderCompletionProc)(
    csSDK_uint32                      inVideoRenderID,
    void*                              inCallbackRef,
    PrTime                            inTime,
    PPixHand                          inRenderedFrame,
    SequenceRender_GetFrameReturnRec  *inGetFrameReturn);

+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|    **Parameter**     |                                                                           **Description**                                                                           |
+======================+=====================================================================================================================================================================+
| ``inVideoRenderID``  | The outVideoRenderID that the exporter passed to ``SetAsyncRenderCompletionProc`` earlier.                                                                          |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inCallbackRef``    | A pointer that the exporter sets using ``SetAsyncRenderCompletionProc()``.                                                                                          |
|                      |                                                                                                                                                                     |
|                      | This could be, for example, a pointer to an exporter instance.                                                                                                      |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inTime``           | The frame time requested.                                                                                                                                           |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inRenderedFrame``  | The rendered frame. The exporter is reponsible for ``disposing`` of this PPixHand using the ``Dispose()`` call in the :ref:`universals/sweetpea-suites.ppix-suite`. |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inGetFrameReturn`` | A structure that contains info about the frame returned, and it includes the ``inAsyncCompletionData`` originally passed to ``QueueAsyncVideoFrameRender()``.       |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

QueueAsyncVideoFrameRender()
********************************************************************************

Use this call rather than ``RenderVideoFrame()`` to queue up a request to render a specific frame asynchronously.

The rendering can happen on a separate thread or processor.

When the render is completed, the ``PrSDKSequenceAsyncRenderCompletionProc`` that was set using ``SetAsyncRenderCompletionProc`` will be called.

::

  prSuiteError (*QueueAsyncVideoFrameRender)(
    csSDK_uint32               inVideoRenderID,
    PrTime                     inTime,
    csSDK_uint32*              outRequestID,
    SequenceRender_ParamsRec*  inRenderParams,
    PrRenderCacheType          inCacheFlags,
    void*                      inAsyncCompletionData);

+---------------------------+-------------------------------------------------------------------------------------------------------------------------+
|       **Parameter**       |                                                     **Description**                                                     |
+===========================+=========================================================================================================================+
| ``inVideoRenderID``       | Pass in the ``outVideoRenderID`` returned from ``MakeVideoRenderer()``.                                                 |
|                           |                                                                                                                         |
|                           | This gives the host the context of the video render.                                                                    |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``inTime``                | The frame time requested.                                                                                               |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``outRequestID``          | Passes back a request ID, which... doesn't seem to have any use.                                                        |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``inRenderParams``        | The details of the render.                                                                                              |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``inCacheFlags``          | One or more cache flags.                                                                                                |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``inAsyncCompletionData`` | This data will be passed to the ``PrSDKSequenceAsyncRenderCompletionProc`` in ``inGetFrameReturn.asyncCompletionData``. |
+---------------------------+-------------------------------------------------------------------------------------------------------------------------+

PrefetchMedia()
********************************************************************************

Prefetch the media needed to render this frame. This is a hint to the importers to begin reading media needed to render this video frame.

::

  prSuiteError (*PrefetchMedia)(
    csSDK_uint32  inVideoRenderID,
    PrTime        inFrame);

PrefetchMediaWithRenderParameters()
********************************************************************************

Prefetch the media needed to render this frame, using all of the parameters used to render the frame.

This is a hint to the importers to begin reading media needed to render this video frame.

::

  prSuiteError (*PrefetchMediaWithRenderParameters)(
    csSDK_uint32               inVideoRenderID,
    PrTime                     inTime,
    SequenceRender_ParamsRec*  inRenderParams);

CancelAllOutstandingMediaPrefetches()
********************************************************************************

Cancel all media prefetches that are still outstanding.

::

  prSuiteError (*PrefetchMedia)(
    csSDK_uint32  inVideoRenderID);

IsPrefetchedMediaReady()
********************************************************************************

Check on the status of a prefetch request.

::

  prSuiteError (*IsPrefetchedMediaReady)(
    csSDK_uint32  inVideoRenderID,
    PrTime        inTime,
    prBool*       outMediaReady);

MakeVideoRendererForTimeline()
********************************************************************************

Similar to MakeVideoRenderer, but for use by renderer plug-ins.

Creates a video renderer, in preparation to get rendered video from the host.

The ``TimelineID`` in question must refer to a top-level sequence.

::

  prSuiteError (*MakeVideoRendererForTimeline)(
    PrTimelineID   inTimeline,
    csSDK_uint32*  outVideoRendererID);

MakeVideoRendererForTimelineWithFrameRate()
********************************************************************************

Similar to MakeVideoRendererForTimeline, with an additional frame rate parameter.

This is useful for the case of a nested multicam sequence.

::

  prSuiteError (*MakeVideoRendererForTimelineWithFrameRate)(
    PrTimelineID   inTimeline,
    PrTime         inFrameRate,
    csSDK_uint32*  outVideoRendererID);

ReleaseVideoRendererForTimeline()
********************************************************************************

Similar to ReleaseVideoRenderer, but for use by renderer plug-ins. Release the video renderer when the renderer plug-in is done requesting video.

::

  prSuiteError (*ReleaseVideoRendererForTimeline)(
    csSDK_uint32  inVideoRendererID);

RenderVideoFrameAndConformToPixelFormat()
********************************************************************************

New in CS5.5. Similar to RenderVideoFrame., but conforms the resulting frame to a specific pixel format.

Allows an exporter to request a frame in a specific pixel format.

::

  prSuiteError (*RenderVideoFrameAndConformToPixelFormat)(
    csSDK_uint32                       inVideoRenderID,
    PrTime                             inTime,
    SequenceRender_ParamsRec*          inRenderParams,
    PrRenderCacheType                  inCacheFlags,
    PrPixelFormat                      inConformToFormat,
    SequenceRender_GetFrameReturnRec*  getFrameReturn);

MakeVideoRendererForTimelineWithStreamLabel()
********************************************************************************

New in CS6. Similar to ``MakeVideoRenderer``, but is stream label-aware.

Allows an exporter to request rendered frames from multiple video streams.

::

  prSuiteError (*MakeVideoRendererForTimelineWithStreamLabel)(
    PrTimelineID      inTimeline,
    PrSDKStreamLabel  inStreamLabel,
    csSDK_uint32*     outVideoRendererID);
