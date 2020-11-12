.. _importers/structure-descriptions:

Structure Descriptions
################################################################################

.. _importers/structure-descriptions.imAcceleratorRec:

imAcceleratorRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imRetargetAccelerator`

Describes the path to the new media and new accelerator created when the Project Manager copies media and its accelerator.

::

  typedef struct {
    const prUTF16Char *inOriginalPath;
    const prUTF16Char *inAcceleratorPath;
  } imAcceleratorRec;

+-----------------------+------------------------------------------------------+
| ``inOriginalPath``    | The unicode path and name of the copied media.       |
+-----------------------+------------------------------------------------------+
| ``inAcceleratorPath`` | The unicode path and name of the copied accelerator. |
+-----------------------+------------------------------------------------------+

----

.. _importers/structure-descriptions.imAnalysisRec:

imAnalysisRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imAnalysis`

Sending back analysis data is a two step process. First, set buffersize to the size of your character buffer and return imNoErr.

Premiere will immediately send ``imAnalysis`` again; populate the buffer with text. Previously-stored preferences and privateData are returned in this structure.

::

  typedef struct {
    void         *privatedata;
    void         *prefs;
    csSDK_int32  buffersize;
    char         *buffer;
    csSDK_int32  *timecodeFormat;
  } imAnalysisRec;

+--------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``privatedata``    | Instance data from ``imGetInfo8`` or ``imGetPrefs8``.                                                                                    |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``prefs``          | Clip Source Settings data from ``imGetPrefs8`` (setup dialog info).                                                                      |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``buffersize``     | Set to the desired size and return imNoErr to Premiere, which will re-size and call the plug-in again with the ``imGetPrefs8`` selector. |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``buffer``         | Text buffer. Terminate lines with line endings (CR and LF).                                                                              |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``timecodeFormat`` | Preferred timecode format, sent by the host.                                                                                             |
+--------------------+------------------------------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imAsyncImporterCreationRec:

imAsyncImporterCreationRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imCreateAsyncImporter`

Create an asynchronous importer object using the data provided, and store it here.

::

  typedef struct {
    void                *inPrivateData;
    void                *inPrefs;
    AsyncImporterEntry  outAsyncEntry;
    void                *outAsyncPrivateData;
  }

+-------------------------+---------------------------------------------------------------------------------------+
| ``inPrivateData``       | Instance data from ``imGetInfo8`` or ``imGetPrefs8``.                                 |
+-------------------------+---------------------------------------------------------------------------------------+
| ``inPrefs``             | Clip Source Settings from ``imGetPrefs8`` (setup dialog info).                        |
+-------------------------+---------------------------------------------------------------------------------------+
| ``outAsyncEntry``       | Provide the entry point for async selectors sent to the asynchronous importer object. |
+-------------------------+---------------------------------------------------------------------------------------+
| ``outAsyncPrivateData`` | ``PrivateData`` for the asynchronous importer object.                                 |
+-------------------------+---------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imAudioInfoRec7:

imAudioInfoRec7
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetInfo8` (member of :ref:`importers/structure-descriptions.imFileInfoRec8`)

Audio data properties of the file (or of the data you will generate, if synthetic).

::

  typedef struct {
    csSDK_int32        numChannels;
    float              sampleRate;
    PrAudioSampleType  sampleType;
  }

+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``numChannels`` | Number of audio channels in the audio stream.                                                                                                            |
|                 |                                                                                                                                                          |
|                 | Either 1, 2, or 6.                                                                                                                                       |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``sampleRate``  | In hertz.                                                                                                                                                |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``sampleType``  | This is for informational use only, to disclose the format of the audio on disk, before it is converted to 32-bit float, uninterleaved, by the importer. |
|                 |                                                                                                                                                          |
|                 | The audio sample types are listed in :ref:`universals/universals`.                                                                                       |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imCalcSizeRec:

imCalcSizeRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imCalcSize8`

Asks the importer for an estimate of disk space used by the clip, given the provided trim boundaries.

::

  typedef struct {
    void         *privatedata;
    void         *prefs;
    csSDK_int32  trimIn;
    csSDK_int32  duration;
    prInt64      sizeInBytes;
    csSDK_int32  scale;
    csSDK_int32  sampleSize;
  } imCalcSizeRec;

+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ``privatedata`` | Instance data gathered from ``imGetInfo8`` or ``imGetPrefs8``.                                                               |
+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ``prefs``       | Clip Source Settings gathered from ``imGetPrefs8`` (setup dialog info).                                                      |
+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ``trimIn``      | In point of the trimmed clip the importer should calculate the size for, in the timebase specified by scale over sampleSize. |
+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ``duration``    | Duration of the trimmed clip the importer should calculate the size for.                                                     |
|                 |                                                                                                                              |
|                 | If 0, then the importer should calculate the size of the untrimmed clip.                                                     |
+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ``sizeInBytes`` | Return the calculated size in bytes.                                                                                         |
+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ``scale``       | The frame rate of the video clip, represented as scale over sampleSize.                                                      |
+-----------------+------------------------------------------------------------------------------------------------------------------------------+
| ``sampleSize``  |                                                                                                                              |
+-----------------+------------------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imCheckTrimRec:

imCheckTrimRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imCheckTrim8`

Provides the requested trim boundaries to the importer, and allows adjusted trim boundaries to be passed back to Premiere.

::

  typedef struct {
    void         *privatedata;
    void         *prefs;
    csSDK_int32  trimIn;
    csSDK_int32  duration;
    csSDK_int32  keepAudio;
    csSDK_int32  keepVideo;
    csSDK_int32  newTrimIn;
    csSDK_int32  newDuration;
    csSDK_int32  scale;
    csSDK_int32  sampleSize;
  } imCheckTrimRec;

+-----------------+--------------------------------------------------------------------------------------------------------+
| ``privatedata`` | Instance data gathered from ``imGetInfo8`` or ``imGetPrefs8``.                                         |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``prefs``       | Clip Source Settings gathered from ``imGetPrefs8`` (setup dialog info).                                |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``trimIn``      | Requested in point of the trimmed clip, in the timebase specified by scale over sampleSize.            |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``duration``    | Requested duration. If 0, then the request is to leave the clip untrimmed, and at the current duration |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``keepAudio``   | If non-zero, the request is to keep the audio in the trimmed result.                                   |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``keepVideo``   | If non-zero, the request is to keep the video in the trimmed result.                                   |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``newTrimIn``   | Return the acceptable in point of the trimmed clip. It must be at or before the requested in point.    |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``newDuration`` | Return the acceptable duration. newTrimIn + newDuration must be at or after the trimIn + duration.     |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``scale``       | The frame rate of the video clip, represented as scale over sampleSize.                                |
+-----------------+--------------------------------------------------------------------------------------------------------+
| ``sampleSize``  |                                                                                                        |
+-----------------+--------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imClipFrameDescriptorRec:

imClipFrameDescriptorRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imSelectClipFrameDescriptor`

Based on the request in ``inDesiredClipFrameDescriptor`` and the importer's Source Settings, modify ``outBestFrameDescriptor`` as needed to describe what format the importer will provide.

::

  typedef struct {
    void*                inPrivateData;
    void*                inPrefs;
    ClipFrameDescriptor  inDesiredClipFrameDescriptor;
    ClipFrameDescriptor  outBestFrameDescriptor;
  } imClipFrameDescriptorRec;

+----------------------------------+-------------------------------------------------------------------------+
| ``inPrivatedata``                | Instance data gathered from ``imGetInfo8`` or ``imGetPrefs8``.          |
+----------------------------------+-------------------------------------------------------------------------+
| ``inPrefs``                      | Clip Source Settings gathered from ``imGetPrefs8`` (setup dialog info). |
+----------------------------------+-------------------------------------------------------------------------+
| ``inDesiredClipFrameDescriptor`` | Requested frame properties, as described by the host.                   |
|                                  |                                                                         |
|                                  | The ``ClipFrameDescriptor`` struct is defined in PrSDKImporterShared.h. |
+----------------------------------+-------------------------------------------------------------------------+
| ``outBestFrameDescriptor``       | Frame properties to be produced, filled in with initial guesses         |
+----------------------------------+-------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imCompleteAsyncClosedCaptionScanRec:

imCompleteAsyncClosedCaptionScanRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imCompleteAsyncClosedCaptionScan`

This structure is passed to provide one last chance to cleanup and dispose of ``inAsyncCaptionScanPrivateData``, and to mark whether the closed caption scan completed without error.

::

  typedef struct {
    void*        inPrivateData;
    const void*  inPrefs;
    void*        inAsyncCaptionScanPrivateData;
    prBool       inScanCompletedWithoutError;
  } imCompleteAsyncClosedCaptionScanRec;

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``inPrivatedata``                 | Instance data gathered from ``imGetInfo8`` or ``imGetPrefs8``.                                                                 |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``inPrefs``                       | Clip Source Settings gathered from ``imGetPrefs8`` (setup dialog info).                                                        |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``inAsyncCaptionScanPrivateData`` | Cleanup and dispose of any data here that was allocated in ``imInitiateAsyncClosedCaptionScan`` or ``imGetNextClosedCaption``. |
|                                   |                                                                                                                                |
|                                   | This data should not be accessed after returning from this call.                                                               |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``inScanCompletedWithoutError``   | Set to true if no error.                                                                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imIndColorProfileRec:

imIndColorProfileRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetIndColorProfile`

Deprecated as of 13.0. Describes a color profile supported by a clip.

The first time ``imGetIndColorProfile`` is sent, ``inDestinationBuffer`` will be NULL, and ``ioBufferSize`` will be 0.

Set ``ioBufferSize`` to the required size for the buffer, and the host will allocate the memory and call the importer again, with a valid ``inDestinationBuffer``, and ``ioBufferSize`` set to the value just provided by the importer.

::

  typedef struct {
    void         *inPrivateData;
    csSDK_int32  ioBufferSize;
    void         *inDestinationBuffer;
    PrSDKString  outName;
  } imIndColorProfileRec;

----

.. _importers/structure-descriptions.imCopyFileRec:

imCopyFileRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imCopyFile`

Describes how to copy a clip. Also provides a callback to update the progress bar and check if the user has cancelled.

::

  typedef struct {
    void                *inPrivateData;
    csSDK_int32         *inPrefs;
    const prUTF16Char   *inSourcePath;
    const prUTF16Char   *inDestPath;
    importProgressFunc  inProgressCallback;
    void                *inProgressCallbackID;
  } imTrimFileRec;

+--------------------------+-----------------------------------------------------------------------------------------------------+
| ``inPrivateData``        | Instance data gathered during ``imGetInfo8`` or ``imGetPrefs8``.                                    |
+--------------------------+-----------------------------------------------------------------------------------------------------+
| ``inPrefs``              | Clip Source Settings gathered during ``imGetPrefs8`` (setup dialog).                                |
+--------------------------+-----------------------------------------------------------------------------------------------------+
| ``inSourcePath``         | Full unicode path of the source file.                                                               |
+--------------------------+-----------------------------------------------------------------------------------------------------+
| ``inDestPath``           | Full unicode path of the destination file.                                                          |
+--------------------------+-----------------------------------------------------------------------------------------------------+
| ``inProgressCallback``   | importProgressFunc callback to call repeatedly to provide progress and to check for cancel by user. |
|                          | May be a NULL pointer, so make sure the function pointer is valid before calling.                   |
+--------------------------+-----------------------------------------------------------------------------------------------------+
| ``inProgressCallbackID`` | Pass to ``progressCallback``.                                                                       |
+--------------------------+-----------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imDataRateAnalysisRec:

imDataRateAnalysisRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imDataRateAnalysis`

Specify the desired buffersize, return to Premiere with ``imNoErr``; upon the next call fill buffer with ``imDataSamples``, and specify a base data rate for audio (if any).

This structure is used like ``imAnalysisRec``.

::

  typedef struct {
    void         *privatedata;
    void         *prefs;
    csSDK_int32  buffersize;
    char         *buffer;
    csSDK_int32  baserate;
  } imDataRateAnalysisRec;

+-----------------+---------------------------------------------------------------------------------------------+
| ``privatedata`` | Instance data gathered from ``imGetInfo8`` or ``imGetPrefs8``.                              |
+-----------------+---------------------------------------------------------------------------------------------+
| ``prefs``       | Clip Source Settings gathered from ``imGetPrefs8`` (setup dialog info).                     |
+-----------------+---------------------------------------------------------------------------------------------+
| ``buffersize``  | The size of the buffer you request from Premiere prior to passing data back data in buffer. |
+-----------------+---------------------------------------------------------------------------------------------+
| ``buffer``      | Pointer to the analysis buffer to be filled with ``imDataSamples`` (see structure below).   |
+-----------------+---------------------------------------------------------------------------------------------+
| ``baserate``    | ``Audio`` data rate (bytes per second) of the file.                                         |
+-----------------+---------------------------------------------------------------------------------------------+

::

  typedef struct {
    csSDK_uint32  sampledur;
    csSDK_uint32  samplesize;
  } imDataSample;

+----------------+-------------------------------------------------------------------------------------------------------------+
| ``sampledur``  | Duration of one sample in video timebase, in samplesize increments; set the high bit if this is a keyframe. |
+----------------+-------------------------------------------------------------------------------------------------------------+
| ``samplesize`` | ``Size`` of this sample in bytes.                                                                           |
+----------------+-------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imDeferredProcessingRec:

imDeferredProcessingRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imDeferredProcessing`

Describes the current progress of the deferred processing on the clip referred to by inPrivateData.

::

  typedef struct {
    void   *inPrivateData;
    float  outProgress;
    char   outInvalidateFile;
    char   outCallAgain;
  } imDeferredProcessingRec;

+-----------------------+----------------------------------------------------------------------------+
| ``inPrivateData``     | Instance data gathered from ``imGetInfo8`` or ``imGetPrefs8``.             |
+-----------------------+----------------------------------------------------------------------------+
| ``outProgress``       | Set this to the current progress, from 0.0 to 1.0.                         |
+-----------------------+----------------------------------------------------------------------------+
| ``outInvalidateFile`` | The importer has updated information about the file.                       |
+-----------------------+----------------------------------------------------------------------------+
| ``outCallAgain``      | Set this to true to request that the importer be called again immediately. |
+-----------------------+----------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imDeleteFileRec:

imDeleteFileRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imDeleteFile`

Describes the file to be deleted.

::

  typedef struct {
    csSDK_int32        filetype;
    const prUTF16Char  deleteFile;
  } imDeleteFileRec;

+----------------+---------------------------------------------------------------------+
| ``filetype``   | The file's unique four character code, defined in the IMPT resource |
+----------------+---------------------------------------------------------------------+
| ``deleteFile`` | Specifies the name (and path) of the file to be deleted.            |
+----------------+---------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imFileAccessRec8:

imFileAccessRec8
================================================================================

Selectors: ``imGetInfo8`` and ``imGetPrefs8``

Describes the file being imported.

::

  typedef struct {
    void               *importID;
    csSDK_int32        filetype;
    const prUTF16Char  *filepath;
    imFileRef          fileref;
    PrMemoryPtr        newfilename;
  } imFileAccessRec;

+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``importID``    | Unique ID provided by Premiere. Do not modify!                                                                                                                                  |
+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``filetype``    | The file's unique four character code, defined in the IMPT resource.                                                                                                            |
+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``filepath``    | The unicode file path and name.                                                                                                                                                 |
+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fileref``     | A Windows HANDLE. Premiere does not overload this value by using it internally, although setting it to the constant kBadFileRef may cause Premiere to think the file is closed. |
|                 |                                                                                                                                                                                 |
|                 | This value is always valid.                                                                                                                                                     |
+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``newfilename`` | If the file is synthetic, the importer can specify the displayable name here as a prUTF16Char string during ``imGetPrefs8``.                                                    |
+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imFileAttributesRec:

imFileAttributesRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetFileAttributes`

New in Premiere Pro 3.1. Provide the clip creation date.

::

  typedef struct {
    prDateStamp  creationDateStamp;
    csSDK_int32  reserved[40];
  } imFileAttributesRec;

+-----------------------+----------------------------------------------+
| ``creationDateStamp`` | Structure to store when the clip was created |
+-----------------------+----------------------------------------------+

----

.. _importers/structure-descriptions.imFileInfoRec8:

imFileInfoRec8
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetInfo8`

Describes the clip, or the stream with the ID streamIdx. Set the clip or stream attributes from the file header or data source. Create and store any privateData.

When a synthetic clip is created, and the user provides the desired resolution, frame rate, pixel aspect ratio, and audio sample rate in the New Synthetic dialog, these values will be pre-initialized by Premiere.

If importing stereoscopic footage, import the left-eye video channel for streamID 0, and the right-eye video channel for streamID 1.

::

  typedef struct {
    char             hasVideo;
    char             hasAudio;
    imImageInfoRec   vidInfo;
    csSDK_int32      vidScale;
    csSDK_int32      vidSampleSize;
    csSDK_int32      vidDuration;
    imAudioInfoRec7  audInfo;
    PrAudioSample    audDuration;
    csSDK_int32      accessModes;
    void             *privatedata;
    void             *prefs;
    char             hasDataRate;
    csSDK_int32      streamIdx;
    char             streamsAsComp;
    prUTF16Char      streamName[256];
    csSDK_int32      sessionPluginID;
    char             alwaysUnquiet;
    char             unused;
    prUTF16Char      filePath[2048];
    char             canProvidePeakData;
    char             mayBeGrowing;
  } imFileInfoRec8;

+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``hasVideo``           | If non-zero, the file contains video.                                                                                                                                                                                                           |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``hasAudio``           | If non-zero, the file contains audio.                                                                                                                                                                                                           |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vidInfo``            | If there is video in the file, fill out the imImageInfoRec structure (e.g. height, width, alpha info, etc.).                                                                                                                                    |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vidScale``           | The frame rate of the video, represented as scale over sampleSize.                                                                                                                                                                              |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vidSampleSize``      |                                                                                                                                                                                                                                                 |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vidDuration``        | The total number of frames of video, in the video timebase.                                                                                                                                                                                     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``audInfo``            | If there is audio in the file, fill out the imAudioInfoRec7 structure.                                                                                                                                                                          |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``audDuration``        | The total number of audio sample frames.                                                                                                                                                                                                        |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``accessModes``        | The access mode of this file. Use one of the following constants:                                                                                                                                                                               |
|                        |                                                                                                                                                                                                                                                 |
|                        | - ``kRandomAccessImport`` - This file can be read by random access (default)                                                                                                                                                                    |
|                        | - ``kSequentialAudioOnly`` - When accessing audio, only sequential reads allowed (for variable bit rate files)                                                                                                                                  |
|                        | - ``kSequentialVideoOnly`` - When accessing video, only sequential reads allowed                                                                                                                                                                |
|                        | - ``kSequentialOnly`` - Both sequential audio and video                                                                                                                                                                                         |
|                        | - ``kSeparateSequentialAudio`` - Both random access and sequential access.                                                                                                                                                                      |
|                        |                                                                                                                                                                                                                                                 |
|                        | This setting allows audio to be retrieved for scrubbing or playback even during audio conforming.                                                                                                                                               |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``privatedata``        | Private instance data.                                                                                                                                                                                                                          |
|                        | Allocate a handle using Premiere's memory functions and store it here.                                                                                                                                                                          |
|                        | Premiere will return the handle with subsequent selectors.                                                                                                                                                                                      |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``prefs``              | Clip Source Settings data gathered from ``imGetPrefs8`` (setup dialog info).                                                                                                                                                                    |
|                        | When a synthetic clip is created using File > New, ``imGetPrefs8`` is sent ``beforeimGetInfo8`` so this settings structure will already be valid.                                                                                               |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``hasDataRate``        | If set, the importer can read or generate data rate information for this file and will be sent ``imDataRateAnalysis``.                                                                                                                          |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``streamIdx``          | The Premiere-specified stream index number.                                                                                                                                                                                                     |
|                        | Only useful if clip uses multiple streams.                                                                                                                                                                                                      |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``streamsAsComp``      | If multiple streams and this is stream zero, indicate whether to import as a composition or multiple clips.                                                                                                                                     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``streamName``         | Optional. The unicode name of this stream if there are multiple streams.                                                                                                                                                                        |
|                        |                                                                                                                                                                                                                                                 |
|                        | New in Premiere Pro 3.1, an importer may use this to set the clip name based on metadata rather than the filename.                                                                                                                              |
|                        |                                                                                                                                                                                                                                                 |
|                        | The importer should set ``imImportInfoRec.canSupplyMetadataClipName`` to true, and fill out the name here.                                                                                                                                      |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``sessionPluginID``    | This ID should be used in the :ref:`universals/sweetpea-suites.file-registration-suite` for registering external files (such as textures, logos, etc) that are used by an importer instance but do not appear as footage in the Project Window. |
|                        |                                                                                                                                                                                                                                                 |
|                        | Registered files will be taken into account when trimming or copying a project using the Project Manager.                                                                                                                                       |
|                        |                                                                                                                                                                                                                                                 |
|                        | The ``sessionPluginID`` is valid only for the call that it is passed on.                                                                                                                                                                        |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``alwaysUnquiet``      | Set to non-zero to tell Premiere if the clip should always be unquieted immediately when the application regains focus.                                                                                                                         |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``filepath``           | Added in Premiere Pro 4.1. For clips that have audio in files separate from the video file, set the filename here, so that UMIDs can properly be generated when exporting sequences to AAF.                                                     |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canProvidePeakData`` | New in Premiere Pro CS6. This allows an importer to toggle whether or not it wants to provide peak audio data on a clip-by-clip basis.                                                                                                          |
|                        |                                                                                                                                                                                                                                                 |
|                        | It defaults to the setting set in ``imImportInfoRec.canProvidePeakAudio``.                                                                                                                                                                      |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``mayBeGrowing``       | New in Premiere Pro CS6.0.2. Set to non-zero if this clip is growing and should be refreshed at the interval set in the Media Preferences.                                                                                                      |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imFileOpenRec8:

imFileOpenRec8
================================================================================

Selector: :ref:`importers/selector-descriptions.imOpenFile8`

The file Premiere wants the importer to open.

::

  typedef struct {
    imFileAccessRec8  fileinfo;
    void              *privatedata;
    csSDK_int32       reserved;
    PrFileOpenAccess  inReadWrite;
    csSDK_int32       inImporterID;
    csSDK_size_t      outExtraMemoryUsage;
    csSDK_int32       inStreamIdx;
  } imFileOpenRec8;

+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fileinfo``            | ``imFileAccessRec8`` describing the incoming file.                                                                                                  |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``privatedata``         | Instance data gathered from ``imGetInfo8`` or ``imGetPrefs8``.                                                                                      |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``reserved``            | Do not use.                                                                                                                                         |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inReadWrite``         | The file should be opened with the access mode specified:                                                                                           |
|                         |                                                                                                                                                     |
|                         | Either ``kPrOpenFileAccess_ReadOnly`` or ``kPrOpenFileAccess_ReadWrite``                                                                            |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inImporterID``        | Can be used as the ID for calls in the :ref:`universals/sweetpea-suites.ppix-cache-suite`.                                                          |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``outExtraMemoryUsage`` | New in CS5. If the importer uses memory just by being open, which cannot otherwise be registered in the cache, put the size in bytes in this field. |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inStreamIdx``         | New in CS6. If the clip has multiple streams (for stereoscopic video or otherwise), this ID differentiates between them.                            |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imFileRef:

imFileRef
================================================================================

Selectors:

- :ref:`importers/selector-descriptions.imAnalysis`,
- :ref:`importers/selector-descriptions.imDataRateAnalysis`,
- :ref:`importers/selector-descriptions.imOpenFile8`,
- :ref:`importers/selector-descriptions.imQuietFile`,
- :ref:`importers/selector-descriptions.imCloseFile`,
- :ref:`importers/selector-descriptions.imGetTimeInfo8`,
- :ref:`importers/selector-descriptions.imSetTimeInfo8`,
- :ref:`importers/selector-descriptions.imImportImage`,
- :ref:`importers/selector-descriptions.imImportAudio7`

A file HANDLE on Windows, or a void* on MacOS.

``imFileRef`` is also a member of ``imFileAccessRec``.

Use OS-specific functions, rather than ANSI file functions, when manipulating imFileRef.

----

.. _importers/structure-descriptions.imFrameFormat:

imFrameFormat
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetSourceVideo` (member of :ref:`importers/structure-descriptions.imSourceVideoRec`)

Describes the frame dimensions and pixel format.

::

  typedef struct {
    csSDK_int32    inFrameWidth;
    csSDK_int32    inFrameHeight;
    PrPixelFormat  inPixelFormat;
  } imFrameFormat;

+-------------------+------------------------------------------+
| ``inFrameWidth``  | The frame dimensions requested.          |
+-------------------+------------------------------------------+
| ``inFrameHeight`` |                                          |
+-------------------+------------------------------------------+
| ``inPixelFormat`` | The pixel format of the frame requested. |
+-------------------+------------------------------------------+

----

.. _importers/structure-descriptions.imGetAudioChannelLayoutRec:

imGetAudioChannelLayoutRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetAudioChannelLayout`

The importer should label each audio channel in the clip being imported.

If no labels are specified, the channel layout will be assumed to be discrete.

::

  typedef struct {
    void*                inPrivateData;
    PrAudioChannelLabel  outChannelLabels[kMaxAudioChannelCount];
  } imGetAudioChannelLayoutRec;

+----------------------+------------------------------------------------------------------------------+
| ``inPrivatedata``    | Instance data gathered from ``imGetInfo8`` or ``imGetPrefs8``.               |
+----------------------+------------------------------------------------------------------------------+
| ``outChannelLabels`` | A valid audio channel label should be assigned for each channel in the clip. |
|                      |                                                                              |
|                      | Labels are defined in the :ref:`universals/sweetpea-suites.audio-suite`.     |
+----------------------+------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imGetNextClosedCaptionRec:

imGetNextClosedCaptionRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetNextClosedCaption`

This structure provides private data allocated in ``imInitiateAsyncClosedCaptionScan``, and should be filled out to pass back a closed caption, it's time, format, size, and overall progress in the closed caption scan.

::

  typedef struct {
    void*                  inPrivateData;
    const void*            inPrefs;
    void*                  inAsyncCaptionScanPrivateData;
    float                  outProgress;
    csSDK_int64            outScale;
    csSDK_int64            outSampleSize;
    csSDK_int64            outPosition;
    PrClosedCaptionFormat  outClosedCaptionFormat;
    PrMemoryPtr            outCaptionData;
    prUTF8Char             outTTMLData[kTTMLBufferSize];
    csSDK_size_t           ioCaptionDataSize;
  } imGetNextClosedCaptionRec;

+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|         ``inPrivatedata``         |                                                                                                                                                                                              Instance data gathered from ``imGetInfo8`` or ``imGetPrefs8``.                                                                                                                                                                                              |
+===================================+==========================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| ``inPrefs``                       | Clip Source Settings gathered from ``imGetPrefs8`` (setup dialog info).                                                                                                                                                                                                                                                                                                                                                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``inAsyncCaptionScanPrivateData`` | This provides any private data that was allocated in ``imInitiateAsyncClosedCaptionScan``.                                                                                                                                                                                                                                                                                                                                                               |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``outProgress``                   | Update this value to denote the current progress iterating through all the captions. Valid values are between 0.0 and 1.0.                                                                                                                                                                                                                                                                                                                               |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``outScale``                      | The timebase of outPosition, represented as scale over sampleSize.                                                                                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``outSampleSize``                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``outPosition``                   | The position of the closed caption.                                                                                                                                                                                                                                                                                                                                                                                                                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``outClosedCaptionFormat``        | The format of the closed captions. One of the following:                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | - ``kPrClosedCaptionFormat_Undefined``                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                   | - ``kPrClosedCaptionFormat_CEA608`` - CEA-608 byte stream                                                                                                                                                                                                                                                                                                                                                                                                |
|                                   | - ``kPrClosedCaptionFormat_CEA708`` - CEA-708 byte stream (may contain 608 data wrapped in 708)                                                                                                                                                                                                                                                                                                                                                          |
|                                   | - ``kPrClosedCaptionFormat_TTML`` - W3C TTML string that conforms to the W3C Timed Text Markup Language (TTML) 1.0: `http://www.w3.org/TR/ttaf1-dfxp <http://www.w3.org/TR/ttaf1-dfxp/>`__ or optionally conforming to SMPTE ST 2052-1:2010: `hhttp://store.smpte.org/ <http://store.smpte.org/>`__, or optionally conforming to EBU Tech 3350 `http://tech.ebu.ch/webdav/site/tech/shared/tech/ <http://tech.ebu.ch/webdav/site/tech/shared/tech/>`__). |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | If the TTML string contains tunneled data (e.g. CEA-608 data), then it is preferred that the plug-in provide that through the appropriate byte stream format (e.g. ``kPrClosedCaptionFormat_CEA608``).                                                                                                                                                                                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``outCaptionData``                | Memory location to where the plug-in should write the closed caption bytes, if providing CEA-608 or CEA-708.                                                                                                                                                                                                                                                                                                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``outTTMLData``                   | UTF-8 String of valid W3C TTML data.                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                   | The entire string may be split into substrings (e.g. line by line) and the host will concatenate and decode them (only used when outCaptionData is kPrClosedCaptionFormat_TTML).                                                                                                                                                                                                                                                                         |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ioCaptionDataSize``             | ``Size`` of outCaptionData buffer (in bytes) allocated from the host. The importer should set this variable to the actual number of bytes that were written to outCaptionData, or the length of the string (characters, not bytes) pointed by outTTMLData.                                                                                                                                                                                               |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imGetPrefsRec:

imGetPrefsRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetPrefs8`

Contains settings/prefs data gathered from (or defaults to populate) a setup dialog.

If you are creating media, you can may generate a video preview that includes the background frame from the timeline.

::

  typedef struct {
    char            *prefs;
    csSDK_int32     prefsLength;
    char            firstTime;
    PrTimelineID    timelineData;
    void            *privatedata;
    TDB_TimeRecord  tdbTimelineLocation;
    csSDK_int32     sessionPluginID;
    csSDK_int32     imageWidth;
    csSDK_int32     imageHeight;
    csSDK_uint32    pixelAspectNum;
    csSDK_uint32    pixelAspectDen;
    csSDK_int32     vidScale;
    csSDK_int32     vidSampleSize;
    float           sampleRate;
  } imGetPrefsRec;

+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``prefs``               | A pointer to a private structure (which you allocate) for storing Clip Source Settings.                                                                                                                                                        |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``prefsLength``         | Prior to storing anything in the prefs member, set prefsLength to the size of your structure and return imNoErr; Premiere will re-size and call the plug-in again with ``imGetPrefs8``.                                                        |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``firstTime``           | If set, ``imGetPrefs8`` is being sent for the first time.                                                                                                                                                                                      |
|                         |                                                                                                                                                                                                                                                |
|                         | Instead, check to see if prefs has been allocated. If not, ``imGetPrefs8`` is being sent for the first time. Set up default values for the prefsLength buffer and present any setup dialog.                                                    |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``timelineData``        | ``Can`` be passed to getPreviewFrameEx callback along with tdbTimelineLocation to get a frame from the timeline beneath the current clip or timeline location. This is useful for titler plug-ins.                                             |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``privatedata``         | Private instance data.                                                                                                                                                                                                                         |
|                         |                                                                                                                                                                                                                                                |
|                         | Allocate a handle using Premiere's memory functions and store it here, if not already allocated in ``imGetInfo8``.                                                                                                                             |
|                         |                                                                                                                                                                                                                                                |
|                         | Premiere will return the handle with subsequent selectors.                                                                                                                                                                                     |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``tdbTimelineLocation`` | ``Can`` be passed to getPreviewFrameEx callback along with timelineData to get a frame from the timeline beneath the current clip or timeline location. This is useful for titler plug-ins.                                                    |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``sessionPluginID``     | This ID should be used in the :ref:`universals/sweetpea-suites.file-registration-suite` for registering external files (such as textures, logos, etc) that are used by a importer instance but do not appear as footage in the Project Window. |
|                         |                                                                                                                                                                                                                                                |
|                         | Registered files will be taken into account when trimming or copying a project using the Project Manager. The sessionPluginID is valid only for the call that it is passed on.                                                                 |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``imageWidth``          | New in CS5. The native resolution of the video.                                                                                                                                                                                                |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``imageHeight``         |                                                                                                                                                                                                                                                |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pixelAspectNum``      | New in CS5. The pixel aspect ratio of the video.                                                                                                                                                                                               |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pixelAspectDen``      |                                                                                                                                                                                                                                                |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vidScale``            | New in CS5. The frame rate of the video, represented as scale over sampleSize.                                                                                                                                                                 |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vidSampleSize``       |                                                                                                                                                                                                                                                |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``sampleRate``          | New in CS5. Audio sample rate.                                                                                                                                                                                                                 |
+-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imImageInfoRec:

imImageInfoRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetInfo8` (member of :ref:`importers/structure-descriptions.imFileInfoRec8`)

Describes the video to be imported.

::

  typedef struct {
    csSDK_int32   imageWidth;
    csSDK_int32   imageHeight;
    csSDK_uint16  pixelAspectV1;
    csSDK_uint16  depth;
    csSDK_int32   subType;
    char          fieldType;
    char          fieldsStacked;
    char          reserved_1;
    char          reserved_2;
    char          alphaType;
    matteColRec   matteColor;
    char          alphaInverted;
    char          isVectors;
    char          drawsExternal;
    char          canForceInternalDraw;
    char          dontObscure;
    char          isStill;
    char          noDuration;
    char          reserved_3;
    csSDK_uint32  pixelAspectNum;
    csSDK_uint32  pixelAspectDen;
    char          isRollCrawl;
    char          reservedc[3];
    csSDK_int32   importerID;
    csSDK_int32   supportsAsyncIO;
    csSDK_int32   supportsGetSourceVideo;
    csSDK_int32   hasPulldown;
    csSDK_int32   pulldownCadence;
    csSDK_int32   posterFrame;
    csSDK_int32   canTransform;
    csSDK_int32   interpretationUncertain;
    csSDK_int32   colorProfileSupport;
    PrSDKString   codecDescription;
    csSDK_int32   colorSpaceSupport;
    csSDK_int32   reserved[15];
  } imImageInfoRec;

Plug-in Info
********************************************************************************

+----------------------------+------------------------------------------------------------------------------------------------+
| ``importerID``             | ``Can`` be used as the ID for calls in the :ref:`universals/sweetpea-suites.ppix-cache-suite`. |
+----------------------------+------------------------------------------------------------------------------------------------+
| ``supportsAsyncIO``        | Set this to true if the importer supports ``imCreateAsyncImporter`` and ai* selectors.         |
+----------------------------+------------------------------------------------------------------------------------------------+
| ``supportsGetSourceVideo`` | Set this to true if the importer supports the ``imGetSourceVideo`` selector.                   |
+----------------------------+------------------------------------------------------------------------------------------------+

Bounds Info
********************************************************************************

+--------------------+-----------------------------------------------------------------------------------------------------+
| ``imageWidth``     | Frame width in pixels.                                                                              |
+--------------------+-----------------------------------------------------------------------------------------------------+
| ``imageHeight``    | Frame height in pixels.                                                                             |
+--------------------+-----------------------------------------------------------------------------------------------------+
| ``pixelAspectNum`` | The pixel aspect ratio numerator and denominator.                                                   |
|                    |                                                                                                     |
|                    | For synthetic importers, these are by default the PAR of the project.                               |
|                    |                                                                                                     |
|                    | Only set this if you need a specific PAR for the geometry of the synthesized footage to be correct. |
+--------------------+-----------------------------------------------------------------------------------------------------+
| ``pixelAspectDen`` |                                                                                                     |
+--------------------+-----------------------------------------------------------------------------------------------------+

Time Info
********************************************************************************

+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``isStill``         | If set, the file contains a single frame, so only one frame will be cached.                                                                        |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``noDuration``      | One of the following:                                                                                                                              |
|                     |                                                                                                                                                    |
|                     | - ``imNoDurationFalse``                                                                                                                            |
|                     | - ``imNoDurationNoDefault``                                                                                                                        |
|                     | - ``imNoDurationStillDefault`` - use the default duration for stills, as set by the user in the Preferences                                        |
|                     | - ``imNoDurationNoDefault`` - the importer will supply it's own duration                                                                           |
|                     |                                                                                                                                                    |
|                     | This is primarily for synthetic clips, but can be used for importing non-sequential still images.                                                  |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``isRollCrawl``     | Set to non-zero value to specify this clip is a rolling or crawling title.                                                                         |
|                     |                                                                                                                                                    |
|                     | This allows a player to optionally use the :ref:`universals/sweetpea-suites.rollcrawl-suite` to get sections of this title for real-time playback. |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``hasPulldown``     | Set this to true if the clip contains NTSC film footage with 3:2 pulldown.                                                                         |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pulldownCadence`` | Set this to the enumerated value that describes the pulldown of the clip:                                                                          |
|                     |                                                                                                                                                    |
|                     | ``importer_PulldownPhase_NO_PULLDOWN``                                                                                                             |
|                     |                                                                                                                                                    |
|                     | 2:3 cadences:                                                                                                                                      |
|                     |                                                                                                                                                    |
|                     | - ``importer_PulldownPhase_WSSWW``                                                                                                                 |
|                     | - ``importer_PulldownPhase_SSWWW``                                                                                                                 |
|                     | - ``importer_PulldownPhase_SWWWS``                                                                                                                 |
|                     | - ``importer_PulldownPhase_WWWSS``                                                                                                                 |
|                     | - ``importer_PulldownPhase_WWSSW``                                                                                                                 |
|                     |                                                                                                                                                    |
|                     | 24pa cadences:                                                                                                                                     |
|                     |                                                                                                                                                    |
|                     | - ``importer_PulldownPhase_WWWSW``                                                                                                                 |
|                     | - ``importer_PulldownPhase_WWSWW``                                                                                                                 |
|                     | - ``importer_PulldownPhase_WSWWW``                                                                                                                 |
|                     | - ``importer_PulldownPhase_SWWWW``                                                                                                                 |
|                     | - ``importer_PulldownPhase_WWWWS``                                                                                                                 |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``posterFrame``     | New in Premiere Pro CS3. Poster frame number to be displayed.                                                                                      |
|                     |                                                                                                                                                    |
|                     | If not specified, the poster frame will be the first frame of the clip.                                                                            |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

Format Info
********************************************************************************

+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``depth``                   | Bits per pixel. This currently has no effect and should be left unchanged.                                                                         |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``subType``                 | The four character code of the file's codec; associates files with MAL plug-ins. For uncompressed files, set to ``imUncompressed``.                |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fieldType``               | One of the following:                                                                                                                              |
|                             |                                                                                                                                                    |
|                             | - ``prFieldsNone``                                                                                                                                 |
|                             | - ``prFieldsUpperFirst``                                                                                                                           |
|                             | - ``prFieldsLowerFirst``                                                                                                                           |
|                             | - ``prFieldsUnknown``                                                                                                                              |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fieldsStacked``           | Fields are present, and not interlaced. Deprecated since Premiere Pro 7.0.                                                                         |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``alphaType``               | Used when depth is 32 or greater. One of the following:                                                                                            |
|                             |                                                                                                                                                    |
|                             | - ``alphaNone`` - no alpha channel (the default)                                                                                                   |
|                             | - ``alphaStraight`` - straight alpha channel                                                                                                       |
|                             | - ``alphaBlackMatte`` - premultiplied with black                                                                                                   |
|                             | - ``alphaWhiteMatte`` - premultiplied with white                                                                                                   |
|                             | - ``alphaArbitrary`` - premultiplied with the color specified in matteColor                                                                        |
|                             | - ``alphaOpaque`` - for video with alpha channel prefilled to opaque.                                                                              |
|                             |                                                                                                                                                    |
|                             | This gives Premiere the opportunity to make an optimization by skipping the fill to opaque that would otherwise be performed if alphaNone was set. |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``matteColor``              | ``Newly`` used in Premiere Pro CS3. Used to specify matte color if ``alphaType`` is set to ``alphaArbitrary``.                                     |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``alphaInverted``           | If non-zero, alpha is treated as inverted (e.g. black becomes transparent).                                                                        |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canTransform``            | Set to non-zero value to specify this importer handles resolution independent files and can apply a transform matrix.                              |
|                             |                                                                                                                                                    |
|                             | The matrix will be passed during the import request in ``imImportImageRec.transform``.                                                             |
|                             |                                                                                                                                                    |
|                             | This code path is currently not called by Premiere Pro. After Effects uses this call to import Flash video.                                        |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``interpretationUncertain`` | Use an 'or' operator to combine any of the following flags:                                                                                        |
|                             |                                                                                                                                                    |
|                             | - ``imPixelAspectRatioUncertain``                                                                                                                  |
|                             | - ``imFieldTypeUncertain``                                                                                                                         |
|                             | - ``imAlphaInfoUncertain``                                                                                                                         |
|                             | - ``imEmbeddedColorProfileUncertain``                                                                                                              |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``colorProfileSupport``     | Deprecated as of 13.0. New in CS5.5.                                                                                                               |
|                             |                                                                                                                                                    |
|                             | Set to ``imColorProfileSupport_Fixed`` to support color management.                                                                                |
|                             | If the importer is uncertain, it should use ``interpretationUncertain`` above instead.                                                             |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``codecDescription``        | Text description of the codec in use.                                                                                                              |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ColorProfileRec``         | New in 13.0; describes the color profile being used by the importer, with this media.                                                              |
+-----------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

Unused
********************************************************************************

+--------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``pixelAspectV1``        | Obsolete. Maintained for backwards compatability.                                                               |
|                          |                                                                                                                 |
|                          | Plug-ins written for the Premiere 6.x or Premiere Pro API should use ``pixelAspectNum`` and ``pixelAspectDen``. |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``isVectors``            | Use ``canTransform`` instead.                                                                                   |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``drawsExternal``        |                                                                                                                 |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``canForceInternalDraw`` |                                                                                                                 |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``dontObscure``          |                                                                                                                 |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imImportAudioRec7:

imImportAudioRec7
================================================================================

Selector: :ref:`importers/selector-descriptions.imImportAudio7`

Describes the audio samples to be returned, and contains an allocated buffer for the importer to fill in.

Provide the audio in 32-bit float, uninterleaved audio format.

::

  typedef struct {
    PrAudioSample  position;
    csSDK_uint32   size;
    float          **buffer;
    void           *privatedata;
    void           *prefs;
  } imImportAudioRec7;

+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``position``    | In point, in audio sample frames.                                                                                                                                                                                                                   |
|                 |                                                                                                                                                                                                                                                     |
|                 | The importer should save the out point of the request in privatedata, because if position is less than zero, then the audio request is sequential, which means the importer should return contiguous samples from the last ``imImportAudio7`` call. |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``size``        | The number of audio sample frames to import.                                                                                                                                                                                                        |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``buffer``      | An array of buffers, one buffer for each channel, with length specified in size.                                                                                                                                                                    |
|                 |                                                                                                                                                                                                                                                     |
|                 | These buffers are allocated by the host application, for the plug-in to fill in with audio data.                                                                                                                                                    |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``privatedata`` | Instance data gathered from ``imGetInfo8`` or ``imGetPrefs8``.                                                                                                                                                                                      |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``prefs``       | Clip Source Settings data gathered from ``imGetPrefs8`` (setup dialog info).                                                                                                                                                                        |
+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imImportImageRec:

imImportImageRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imImportImage`

Describes the frame to be returned.

::

  typedef struct {
    csSDK_int32    onscreen;
    csSDK_int32    dstWidth;
    csSDK_int32    dstHeight;
    csSDK_int32    dstOriginX;
    csSDK_int32    dstOriginY;
    csSDK_int32    srcWidth;
    csSDK_int32    srcHeight;
    csSDK_int32    srcOriginX;
    csSDK_int32    srcOriginY;
    csSDK_int32    unused2;
    csSDK_int32    unused3;
    csSDK_int32    rowbytes;
    char           *pix;
    csSDK_int32    pixsize;
    PrPixelFormat  pixformat;
    csSDK_int32    flags;
    prFieldType    fieldType;
    csSDK_int32    scale;
    csSDK_int32    sampleSize;
    csSDK_int32    in;
    csSDK_int32    out;
    csSDK_int32    pos;
    void           *privatedata;
    void           *prefs;
    prRect         alphaBounds;
    csSDK_int32    applyTransform;
    float          transform[3][3];
    prRect         destClipRect;
  } imImportImageRec;

Bounds Info
********************************************************************************

+----------------+------------------------------------------------------------+
| ``dstWidth``   | Width of the destination rectangle (in pixels).            |
+----------------+------------------------------------------------------------+
| ``dstHeight``  | Height of the destination rectangle (in pixels).           |
+----------------+------------------------------------------------------------+
| ``dstOriginX`` | Origin X point (0 indicates the frame is drawn offscreen). |
+----------------+------------------------------------------------------------+
| ``dstOriginY`` | Origin Y point (0 indicates the frame is drawn offscreen). |
+----------------+------------------------------------------------------------+
| ``srcWidth``   | The same number returned as dstWidth.                      |
+----------------+------------------------------------------------------------+
| ``srcHeight``  | The same number returned as dstHeight.                     |
+----------------+------------------------------------------------------------+
| ``srcOriginX`` | The same number returned as dstOriginX.                    |
+----------------+------------------------------------------------------------+
| ``srcOriginY`` | The same number returned as dstOriginY.                    |
+----------------+------------------------------------------------------------+

Frame Info
********************************************************************************

+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``rowbytes``       | The number of bytes in a single row of pixels.                                                                                                                                                                                        |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pix``            | Pointer to a buffer into which the importer should draw. Allocated based on information from the ``imGetInfo8``.                                                                                                                      |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pixsize``        | The number of pixels. rowbytes * height.                                                                                                                                                                                              |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pixformat``      | The pixel format Premiere requests.                                                                                                                                                                                                   |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``flags``          | ``imDraftMode`` - Draw quickly if possible, using a faster and possibly less accurate algorithm.                                                                                                                                      |
|                    |                                                                                                                                                                                                                                       |
|                    | This may be passed when playing from the timeline.                                                                                                                                                                                    |
|                    |                                                                                                                                                                                                                                       |
|                    | ``imSamplesAreFields`` - Most importers will ignore as Premiere already scales in/out/scale to account for fields, but if you need to know that this has occurred (because maybe you measure something in 'frames'), check this flag. |
|                    |                                                                                                                                                                                                                                       |
|                    | Also, may we suggest considering measuring in seconds instead of frames?                                                                                                                                                              |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fieldType``      | If the importer can swap fields, it should render the frame with the given field dominance: either ``imFieldsUpperFirst`` or ``imFieldsLowerFirst``.                                                                                  |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``scale``          | The frame rate of the video, represented as scale over sampleSize.                                                                                                                                                                    |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``sampleSize``     |                                                                                                                                                                                                                                       |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``in``             | In point, based on the timebase defined by scale over sampleSize..                                                                                                                                                                    |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``out``            | Out point, based on the timebase defined by scale over sampleSize..                                                                                                                                                                   |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pos``            | Import position, based on the above timebase.                                                                                                                                                                                         |
|                    |                                                                                                                                                                                                                                       |
|                    | **API bug**: Synthetic and custom importers will always receive zero.                                                                                                                                                                 |
|                    |                                                                                                                                                                                                                                       |
|                    | Thus, adjusting the in point on the timeline will not offset the in point.                                                                                                                                                            |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``privatedata``    | Instance data gathered during ``imGetInfo`` or ``imGetPrefs``.                                                                                                                                                                        |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``prefs``          | Clip Source Settings data gathered during ``imGetPrefs`` (setup dialog info).                                                                                                                                                         |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``alphaBounds``    | This is the rect outside of which the alpha is always 0. Simply do not alter this field if the alpha bounds match the destination bounds.                                                                                             |
|                    |                                                                                                                                                                                                                                       |
|                    | If set, the alpha bounds must be contained by the destination bounds. This is only currently used when a plug-in calls ``ppixGetAlphaBounds``, and not currently used by any native plug-ins.                                         |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``applyTransform`` | New in After Effects CS3. Not currently provided by Premiere.                                                                                                                                                                         |
|                    |                                                                                                                                                                                                                                       |
|                    | If non-zero, the host is requesting that the importer apply the transform specified in transform and destClipRect before returning the resulting image in pix.                                                                        |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``transform``      | New in After Effects CS3. Not currently provided by Premiere. The source to destination transform matrix.                                                                                                                             |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``destClipRect``   | New in After Effects CS3. Not currently provided by Premiere. Destination rect inside the bounds of the pix buffer.                                                                                                                   |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imImportInfoRec:

imImportInfoRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imInit`

Describes the importer's capabilities to Premiere.

::

  typedef struct {
    csSDK_uint32  importerType;
    csSDK_int32   canOpen;
    csSDK_int32   canSave;
    csSDK_int32   canDelete;
    csSDK_int32   canResize;
    csSDK_int32   canDoSubsize;
    csSDK_int32   canDoContinuousTime;
    csSDK_int32   noFile;
    csSDK_int32   addToMenu;
    csSDK_int32   hasSetup;
    csSDK_int32   dontCache;
    csSDK_int32   setupOnDblClk;
    csSDK_int32   keepLoaded;
    csSDK_int32   priority;
    csSDK_int32   canAsync;
    csSDK_int32   canCreate;
    csSDK_int32   canCalcSizes;
    csSDK_int32   canTrim;
    csSDK_int32   avoidAudioConform;
    prUTF16Char   *acceleratorFileExt;
    csSDK_int32   canCopy;
    csSDK_int32   canSupplyMetadataClipName;
    csSDK_int32   private;
    csSDK_int32   canProvidePeakAudio;
    csSDK_int32   canProvideFileList;
    csSDK_int32   canProvideClosedCaptions;
    prPluginID    fileInfoVersion;
  } imImportInfoRec;


Screen Info
********************************************************************************

+-------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``noFile``              | If set, this is a synthetic importer. The file reference will be zero.                                                    |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``addToMenu``           | If set to ``imMenuNew``, the importer will appear in the File > New menu.                                                 |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``canDoContinuousTime`` | If set, the importer can render frames at arbitrary times and there is no set timecode.                                   |
|                         | A color matte generator or a titler would set this flag.                                                                  |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``canCreate``           | If set, Premiere will treat this synthetic importer as if it creates files on disk to be referenced for frames and audio. |
|                         |                                                                                                                           |
|                         | See Additional Details for more information on custom importers.                                                          |
+-------------------------+---------------------------------------------------------------------------------------------------------------------------+

File Handling Flags
********************************************************************************

+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``canOpen``      | If set, the importer handles open and close operations.                                                                                 |
|                  | Set if the plug-in needs to be called to handle ``imOpenFile``, ``imQuietFile``, and ``imCloseFile``.                                   |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``canSave``      | If set, the importer handles File > Save and File > Save As after a clip has been captured and must handle the ``imSaveFile`` selector. |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``canDelete``    | If set, the importer can delete its own files.                                                                                          |
|                  |                                                                                                                                         |
|                  | The plug-in must handle the ``imDeleteFile`` selector.                                                                                  |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``canCalcSizes`` | If set, the importer can calculate the disk space used by a clip during imCalcSize.                                                     |
|                  |                                                                                                                                         |
|                  | An importer should support this call if it uses a tree of files represented as one top-level file to Premiere.                          |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``canTrim``      | If set, the importer can trim files during imTrimFile.                                                                                  |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``canCopy``      | Set this to true if the importer supports copying clips in the Project Manager.                                                         |
+------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

Setup Flags
********************************************************************************

+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``hasSetup``      | If set, the importer has a setup dialog. The dialog should be presented in response to ``imGetPrefs``                                        |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``setupOnDblClk`` | If set, the setup dialog should be opened whenever the user double clicks on a file imported by the plug-in the timeline or the project bin. |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

Memory Handling Flags
********************************************************************************

+----------------+--------------------------------------------------------------------------+
| ``dontCache``  | Unused.                                                                  |
+----------------+--------------------------------------------------------------------------+
| ``keepLoaded`` | If set, the importer plug-in should never be unloaded.                   |
|                |                                                                          |
|                | Don't set this flag unless it's absolutely necessary (it usually isn't). |
+----------------+--------------------------------------------------------------------------+

Other
********************************************************************************

+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``priority``                  | Determines priority levels for importers that handle the same filetype.                                                                     |
|                               |                                                                                                                                             |
|                               | Importers with higher numbers will override importers with lower numbers.                                                                   |
|                               |                                                                                                                                             |
|                               | For overriding importers that ship with Premiere, use a value of 100 or greater.                                                            |
|                               |                                                                                                                                             |
|                               | Higher-priority importers can defer files to lower-priority importers by returning ``imBadFile`` during ``imOpenFile8`` or ``imGetInfo8``.  |
+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``importType``                | Type identifier for the import module assigned based on the plug-in's IMPT resource.                                                        |
|                               |                                                                                                                                             |
|                               | Do not modify this field.                                                                                                                   |
+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``canProvideClosedCaptions``  | New in Premiere Pro CC. Set this to true if the importer supports media with embedded closed captioning.                                    |
+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``avoidAudioConform``         | Set this to true if the importer supports fast audio retrieval and does not need the audio clips it imports to be conformed.                |
+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``canProvidePeakAudio``       | New in Premiere Pro CS5.5. Set this to true if your non-synthetic importer wants to provide **peak audio data** using ``imGetPeakAudio``.   |
+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``acceleratorFileExt``        | Fill this prUTF16Char array of size 256 with the file extensions of accelerator files that the importer creates and uses.                   |
+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``canSupplyMetadataClipName`` | Allows file based importer to set clip name from metadata.                                                                                  |
|                               |                                                                                                                                             |
|                               | Set this in ``imFileInfoRec8.streamName``.                                                                                                  |
+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``canProvideFileList``        | New in CS6. Set this to true if the importer will provide a list of all files for a copy operation in response to ``imQueryInputFileList``. |
+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ``fileInfoVersion``           | New in CC 2014. This is used by an optimization in an internal importer. Do not use.                                                        |
+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

Unused
********************************************************************************

+------------------+
| ``canResize``    |
+------------------+
| ``canDoSubsize`` |
+------------------+
| ``canAsync``     |
+------------------+

----

.. _importers/structure-descriptions.imIndFormatRec:

imIndFormatRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetIndFormat`

Describes the format(s) supported by the importer. Synthetic files can only have one format.

::

  typedef struct {
    csSDK_int32  filetype;
    csSDK_int32  flags;
    csSDK_int32  canWriteTimecode;
    char         FormatName[256];
    char         FormatShortName[32];
    char         PlatformExtension[256];
    prBool       hasAlternateTypes;
    csSDK_int32  alternateTypes[kMaxAlternateTypes];
    csSDK_int32  canWriteMetaData;
  } imIndFormatRec;

+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``filetype``                           | Unique four character code (fourcc) of the file.                                                                            |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``flags``                              | Legacy mechanism for describing the importer capabilities.                                                                  |
|                                        |                                                                                                                             |
|                                        | Though the flags will still be honored for backward compatability, current and future importers should not use these flags. |
|                                        |                                                                                                                             |
|                                        | See table below for details.                                                                                                |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``canWriteTimecode``                   | If set, timecode can be written for this filetype.                                                                          |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``FormatName[256]``                    | The descriptive importer name.                                                                                              |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``FormatShortName[256]``               | The short name for the plug-in, appears in the format menu.                                                                 |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``PlatformExtension[256]``             | List of all the file extensions supported by this importer.                                                                 |
|                                        |                                                                                                                             |
|                                        | If there's more than one, separate with null characters.                                                                    |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``hasAlternateTypes``                  | Unused                                                                                                                      |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``alternateTypes[kMaxAlternateTypes]`` | Unused                                                                                                                      |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``canWriteMetaData``                   | New in 6.0. If set, imSetMetaData is supported for the filetype                                                             |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

The flags listed below are only for legacy plug-ins and should not be used.

+------------------------+---------------------------------------------------------------------------------------+
|        **Flag**        |                                       **Usage**                                       |
+========================+=======================================================================================+
| ``xfIsMovie``          | Unused                                                                                |
+------------------------+---------------------------------------------------------------------------------------+
| ``xfCanReplace``       | Unused                                                                                |
+------------------------+---------------------------------------------------------------------------------------+
| ``xfCanOpen``          | Unused: Use ``imImportInfoRec.canOpen`` instead.                                      |
+------------------------+---------------------------------------------------------------------------------------+
| ``xfCanImport``        | Unused: The PiPL resource describes the file as an importer.                          |
+------------------------+---------------------------------------------------------------------------------------+
| ``xfIsStill``          | Unused: Use ``imFileInfoRec.imImageInfoRec.isStill`` instead.                         |
+------------------------+---------------------------------------------------------------------------------------+
| ``xfIsSound``          | Unused: Use ``imFileInfoRec.hasAudio`` instead.                                       |
+------------------------+---------------------------------------------------------------------------------------+
| ``xfCanWriteTimecode`` | If set, the importer can respond to ``imGetTimecode`` and ``imSetTimecode``.          |
|                        |                                                                                       |
|                        | Obsolete: use ``imIndFormatRec.canWriteTimecode`` instead.                            |
+------------------------+---------------------------------------------------------------------------------------+
| ``xfCanWriteMetaData`` | Writes (and reads) metadata, specific to the importer's four character code filetype. |
|                        |                                                                                       |
|                        | Obsolete: use ``imIndFormatRec.canWriteMetaData`` instead.                            |
+------------------------+---------------------------------------------------------------------------------------+
| ``xfCantBatchProcess`` | Unused                                                                                |
+------------------------+---------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imIndPixelFormatRec:

imIndPixelFormatRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetIndPixelFormat`

Describes the pixel format(s) supported by the importer.

::

  typedef struct {
    void           *privatedata;
    PrPixelFormat  outPixelFormat;
    const void*    prefs;
  } imIndPixelFormatRec;

+--------------------+--------------------------------------------------------------------------------------+
| ``privatedata``    | Instance data from ``imGetInfo8`` or ``imGetPrefs8``.                                |
+--------------------+--------------------------------------------------------------------------------------+
| ``outPixelFormat`` | One of the pixel formats supported by the importer                                   |
+--------------------+--------------------------------------------------------------------------------------+
| ``prefs``          | New in CC. Clip Source Settings data gathered during ``imGetPrefs8`` (setup dialog). |
+--------------------+--------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imInitiateAsyncClosedCaptionScanRec:

imInitiateAsyncClosedCaptionScanRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imInitiateAsyncClosedCaptionScan`

Both ``imGetNextClosedCaption`` and ``imCompleteAsyncClosedCaptionScan`` may be called from a different thread from which imInitiateAsyncClosedCaptionScan was originally called.

To help facilitate this, outAsyncCaptionScanPrivateData can be allocated by the importer to be used for the upcoming closed caption scan calls, which should then be deallocated in ``imCompleteAsyncClosedCaptionScan``.

The estimated duration of all the closed captions can also be filled in.

This is useful for certain cases where the embedded captions contain many frames of empty data.

::

  typedef struct {
    void*        privatedata;
    void*        prefs;
    void*        outAsyncCaptionScanPrivateData;
    csSDK_int64  outScale;
    csSDK_int64  outSampleSize;
    csSDK_int64  outEstimatedDuration;
  } imInitiateAsyncClosedCaptionScanRec;

+------------------------------------+-------------------------------------------------------------------------------------------------+
| ``privatedata``                    | Instance data gathered during ``imGetInfo8`` or ``imGetPrefs8``.                                |
+------------------------------------+-------------------------------------------------------------------------------------------------+
| ``prefs``                          | Clip Source Settings data gathered during ``imGetPrefs8`` (setup dialog).                       |
+------------------------------------+-------------------------------------------------------------------------------------------------+
| ``outAsyncCaptionScanPrivateData`` | The importer can allocate instance data for this closed caption scan, and pass it back here.    |
+------------------------------------+-------------------------------------------------------------------------------------------------+
| ``outScale``                       | New in CC October 2013. The frame rate of the video clip, represented as scale over sampleSize. |
+------------------------------------+-------------------------------------------------------------------------------------------------+
| ``outSampleSize``                  |                                                                                                 |
+------------------------------------+-------------------------------------------------------------------------------------------------+
| ``outEstimatedDuration``           | New in CC October 2013. The estimated duration of all the captions, in the above timescale      |
+------------------------------------+-------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imMetaDataRec:

imMetaDataRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetMetaData` and :ref:`importers/selector-descriptions.imSetMetaData`

Describes the metadata specific to a given four character code.

::

  typedef struct {
    void          *privatedata;
    void          *prefs;
    csSDK_int32   fourCC;
    csSDK_uint32  buffersize;
    char          *buffer;
  } imMetaDataRec;

+-----------------+---------------------------------------------------------------------------+
| ``privatedata`` | Instance data gathered during ``imGetInfo8`` or ``imGetPrefs8``.          |
+-----------------+---------------------------------------------------------------------------+
| ``prefs``       | Clip Source Settings data gathered during ``imGetPrefs8`` (setup dialog). |
+-----------------+---------------------------------------------------------------------------+
| ``fourcc``      | Fourcc code of the metadata chunk.                                        |
+-----------------+---------------------------------------------------------------------------+
| ``buffersize``  | ``Size`` of the data in buffer.                                           |
+-----------------+---------------------------------------------------------------------------+
| ``buffer``      | The metadata.                                                             |
+-----------------+---------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imPeakAudioRec:

imPeakAudioRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetPeakAudio`

Describes the peak values of the audio at the specified position.

::

  typedef struct {
    void           *inPrivateData;
    void           *inPrefs;
    PrAudioSample  inPosition;
    float          inSampleRate;
    csSDK_int32    inNumSampleFrames;
    float          **outMaxima;
    float          **outMinima;
  } imPeakAudioRec;

+-----------------------+------------------------------------------------------------------+
| ``inPrivateData``     | Instance data gathered during ``imGetInfo8`` or ``imGetPrefs8``. |
+-----------------------+------------------------------------------------------------------+
| ``inPrefs``           | Instance data gathered during ``imGetPrefs8`` (setup dialog).    |
+-----------------------+------------------------------------------------------------------+
| ``inPosition``        | The starting audio sample frame of the peak data.                |
+-----------------------+------------------------------------------------------------------+
| ``inSampleRate``      | The sample rate at which to generate the peak data.              |
+-----------------------+------------------------------------------------------------------+
| ``inNumSampleFrames`` | The number of sample frames in each buffer.                      |
+-----------------------+------------------------------------------------------------------+
| ``outMaxima``         | An array of arrays to be filled with the maximum sample values.  |
+-----------------------+------------------------------------------------------------------+
| ``outMinima``         | An array of arrays to be filled with the minimum sample values.  |
+-----------------------+------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imPreferredFrameSizeRec:

imPreferredFrameSizeRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetPreferredFrameSize`

Describes a frame size preferred by the importer.

::

  typedef struct {
    void           *inPrivateData;
    void           *inPrefs;
    PrPixelFormat  inPixelFormat;
    csSDK_int32    inIndex;
    csSDK_int32    outWidth;
    csSDK_int32    outHeight;
  } imPreferredFrameSizeRec;

+-------------------+---------------------------------------------------------------------------+
| ``inPrivateData`` | Instance data gathered during ``imGetInfo8`` or ``imGetPrefs8``.          |
+-------------------+---------------------------------------------------------------------------+
| ``inPrefs``       | Clip Source Settings data gathered during ``imGetPrefs8`` (setup dialog). |
+-------------------+---------------------------------------------------------------------------+
| ``inPixelFormat`` | The pixel format for this preferred frame size.                           |
+-------------------+---------------------------------------------------------------------------+
| ``inIndex``       | The index of this preferred frame size.                                   |
+-------------------+---------------------------------------------------------------------------+
| ``outWidth``      | The dimensions of this preferred frame size.                              |
+-------------------+---------------------------------------------------------------------------+
| ``outHeight``     |                                                                           |
+-------------------+---------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imQueryContentStateRec:

imQueryContentStateRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imQueryContentState`

Fill in the outContentStateID, which should be a GUID calculated based on the content state of the clip at inSourcePath.

If the state hasn't changed since the last call, the GUID returned should be the same.

::

  typedef struct {
    const prUTF16Char*  inSourcePath;
    prPluginID          outContentStateID;
  } imQueryContentStateRec;

----

.. _importers/structure-descriptions.imQueryDestinationPathRec:

imQueryDestinationPathRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imQueryDestinationPath`

Fill in the desired ``outActualDestinationPath``, based on the ``inSourcePath`` and ``inSuggestedDestinationPath``.

::

  typedef struct {
    void               *inPrivateData;
    void               *inPrefs;
    const prUTF16Char  *inSourcePath;
    const prUTF16Char  *inSuggestedDestinationPath;
    prUTF16Char        *outActualDestinationPath;
  } imQueryDestinationPathRec;

+--------------------------------+------------------------------------------------------------------------------+
| ``inPrivateData``              | Instance data gathered during ``imGetInfo8`` or ``imGetPrefs8``.             |
+--------------------------------+------------------------------------------------------------------------------+
| ``inPrefs``                    | Clip Source Settings data gathered during ``imGetPrefs8`` (setup dialog).    |
+--------------------------------+------------------------------------------------------------------------------+
| ``inSourcePath``               | The path of the source file to be trimmed                                    |
+--------------------------------+------------------------------------------------------------------------------+
| ``inSuggestedDestinationPath`` | The path suggested by Premiere where the destination file should be created. |
+--------------------------------+------------------------------------------------------------------------------+
| ``outActualDestinationPath``   | The path where the importer wants the destination file to be created.        |
+--------------------------------+------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imQueryInputFileListRec:

imQueryInputFileListRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imQueryInputFileList`

Fill in the outContentStateID, which should be a GUID calculated based on the content state of the clip at ``inSourcePath``.

If the state hasn't changed since the last call, the GUID returned should be the same.

::

  typedef struct {
    void*        inPrivateData;
    void*        inPrefs;
    PrSDKString  inBasePath;
    csSDK_int32  outNumFilePaths;
    PrSDKString  *outFilePaths;
  } imQueryInputFileListRec;

+---------------------+-------------------------------------------------------------------------------------------------------------------+
| ``inPrivateData``   | Instance data gathered from ``imGetInfo8`` or ``imGetPrefs8``.                                                    |
+---------------------+-------------------------------------------------------------------------------------------------------------------+
| ``inPrefs``         | Clip Source Settings data gathered from ``imGetPrefs8`` (setup dialog info).                                      |
+---------------------+-------------------------------------------------------------------------------------------------------------------+
| ``inBasePath``      | Path of main file that was passed earlier in ``imOpenFile``.                                                      |
+---------------------+-------------------------------------------------------------------------------------------------------------------+
| ``outNumFilePaths`` | The first time ``imQueryInputFileList`` is sent, fill in the number of files that the media uses.                 |
+---------------------+-------------------------------------------------------------------------------------------------------------------+
| ``outFilePaths``    | The second time ``imQueryInputFileList`` is sent, this will be preallocated as an array of NULL strings.          |
|                     |                                                                                                                   |
|                     | Use the :ref:`universals/sweetpea-suites.string-suite` to fill the array with PrSDKStrings with the actual paths. |
+---------------------+-------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imQueryStreamLabelRec:

imQueryStreamLabelRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imQueryStreamLabel`

New in CS6. Based on the stream ID passed in, allocate and pass back a label for the stream.

For stereoscopic importers, use the predefined labels in PrSDKStreamLabel.h.

::

  typedef struct {
    void          *inPrivateData;
    csSDK_int32   *inPrefs;
    csSDK_int32   inStreamIdx;
    PrSDKString*  outStreamLabel;
  } imQueryStreamLabelRec;

+--------------------+---------------------------------------------------------------------------------------+
| ``privatedata``    | Instance data gathered from ``imGetInfo8`` or ``imGetPrefs8``.                        |
+--------------------+---------------------------------------------------------------------------------------+
| ``prefs``          | Clip Source Settings data gathered from ``imGetPrefs8`` (setup dialog info).          |
+--------------------+---------------------------------------------------------------------------------------+
| ``inStreamIdx``    | The ID of the stream that needs to be labeled.                                        |
+--------------------+---------------------------------------------------------------------------------------+
| ``outStreamLabel`` | The stream label, allocated using the :ref:`universals/sweetpea-suites.string-suite`. |
+--------------------+---------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imSaveFileRec8:

imSaveFileRec8
================================================================================

Selector: :ref:`importers/selector-descriptions.imSaveFile8`

Describes the file to be saved.

::

  typedef struct {
    void                *privatedata;
    csSDK_int32         *prefs;
    const prUTF16Char*  sourcePath;
    const prUTF16Char*  destPath;
    char                move;
    importProgressFunc  progressCallback;
    void                *progressCallbackID;
  } imSaveFileRec8;

+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``privatedata``        | Instance data gathered from ``imGetInfo8`` or ``imGetPrefs8``.                                                                                                     |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``prefs``              | Clip Source Settings data gathered from ``imGetPrefs8`` (setup dialog info).                                                                                       |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``sourcePath``         | Full path of the file to be saved.                                                                                                                                 |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``destPath``           | Full path the file should be saved to.                                                                                                                             |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``move``               | If non-zero, this is a move operation and the original file (the sourcePath) can be deleted after copying is complete.                                             |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``progressCallback``   | Function to call repeatedly to provide progress and to check for cancel by user. May be a NULL pointer, so make sure the function pointer is valid before calling. |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``progressCallbackID`` | Pass to ``progressCallback``.                                                                                                                                      |
+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imSourceVideoRec:

imSourceVideoRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetSourceVideo`, ``aiInitiateAsyncRead``, ``aiGetFrame``

Describes the requested frame, to be passed back in outFrame.

::

  typedef struct {
    void             *inPrivateData;
    csSDK_int32      currentStreamIdx;
    PrTime           inFrameTime;
    imFrameFormat    *inFrameFormats;
    csSDK_int32      inNumFrameFormats;
    bool             removePulldown;
    PPixHand         *outFrame;
    void             *prefs;
    csSDK_int32      prefsSize;
    PrSDKString      selectedColorProfileName;
    PrRenderQuality  inQuality;
  } imSourceVideoRec;

+------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``inPrivateData``            | Instance data gathered during ``imGetInfo8`` or ``imGetPrefs8``.                                                         |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``currentStreamIdx``         | New in CS6. If the clip has multiple streams (for stereoscopic video or otherwise), this ID differentiates between them. |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``inFrameTime``              | Time of frame requested.                                                                                                 |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``inFrameFormats``           | An array of requested frame formats, in order of preference. If NULL, then any format is acceptable.                     |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``inNumFrameFormats``        | The number of frame formats in the ``inFrameFormats``.                                                                   |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``removePulldown``           | If true, pulldown should be removed if the pixel format supports it.                                                     |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``outFrame``                 | Allocate memory to hold the requested frame, and pass it back here.                                                      |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``prefs``                    | New in Premiere Pro 4.1. prefs data from ``imGetPrefs8``                                                                 |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``prefsSize``                | New in Premiere Pro 4.1. Size of prefs data.                                                                             |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``selectedColorProfileName`` | New in Premiere Pro CS5.5. A string that specifies the color profile of the imported frame.                              |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``inQuality``                | New in Premiere Pro CC 2014.                                                                                             |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imSubTypeDescriptionRec:

imSubTypeDescriptionRec
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetSubTypeNames`

Added in Premiere Pro CS3. Describes the codec name associated with a given fourcc.

::

  typedef struct {
    csSDK_int32  subType;
    prUTF16Char  subTypeName[256];
  } imSubTypeDescriptionRec;

----

.. _importers/structure-descriptions.imTimeInfoRec8:

imTimeInfoRec8
================================================================================

Selector: :ref:`importers/selector-descriptions.imGetTimeInfo8` and :ref:`importers/selector-descriptions.imSetTimeInfo8`

Describes the timecode and timecode rate associated with a clip.

::

  typedef struct {
    void         *privatedata;
    void         *prefs;
    char         orgtime[18];
    csSDK_int32  orgScale;
    csSDK_int32  orgSampleSize;
    char         alttime[18];
    csSDK_int32  altScale;
    csSDK_int32  altSampleSize;
    char         orgreel[40];
    char         altreel[40];
    char         logcomment[256];
    csSDK_int32  dataType;
  } imTimeInfoRec;

+---------------------+----------------------------------------------------------------------------------------------+
| ``privatedata``     | Instance data gathered during ``imGetInfo8`` or ``imGetPrefs8``.                             |
+---------------------+----------------------------------------------------------------------------------------------+
| ``prefs``           | Clip Source Settings data gathered during ``imGetPrefs8`` (setup dialog).                    |
+---------------------+----------------------------------------------------------------------------------------------+
| ``orgtime[18]``     | The original time in hours;minutes;seconds;frames, as captured from the source reel.         |
|                     |                                                                                              |
|                     | The use of semi-colons indicates (to Premiere) drop-frame timecode, e.g. "00;00;00;00".      |
|                     |                                                                                              |
|                     | Use colons for non-drop-frame timecode, e.g. "00:00:00:00".                                  |
+---------------------+----------------------------------------------------------------------------------------------+
| ``orgScale``        | Timebase of the timecode in orgtime, represented as scale over sampleSize.                   |
+---------------------+----------------------------------------------------------------------------------------------+
| ``orgSampleSize``   |                                                                                              |
+---------------------+----------------------------------------------------------------------------------------------+
| ``alttime[18]``     | An alternative timecode (may differ from the source timecode), formatted as described above. |
+---------------------+----------------------------------------------------------------------------------------------+
| ``altScale``        | Timebase of the timecode in alttime.                                                         |
+---------------------+----------------------------------------------------------------------------------------------+
| ``altSampleSize``   |                                                                                              |
+---------------------+----------------------------------------------------------------------------------------------+
| ``orgreel[40]``     | Original reel name.                                                                          |
+---------------------+----------------------------------------------------------------------------------------------+
| ``altreel[40]``     | Alternate reel name.                                                                         |
+---------------------+----------------------------------------------------------------------------------------------+
| ``logcomment[256]`` | Comment string.                                                                              |
+---------------------+----------------------------------------------------------------------------------------------+
| ``dataType``        | Currently always set to 1, denoting SMPTE timecode. More values may be added in the future.  |
+---------------------+----------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.imTrimFileRec8:

imTrimFileRec8
================================================================================

Selector: ``imGetIndColorSpace``

Describes how to trim a clip, based on information returned by the importer during ``imCheckTrim8``.

Also provides a callback to update the progress bar and check if the user has cancelled.

::

  typedef struct {
    void                *privatedata;
    void                *prefs;
    csSDK_int32         trimIn;
    csSDK_int32         duration;
    csSDK_int32         keepAudio;
    csSDK_int32         keepVideo;
    const prUTF16Char   *destFilePath;
    csSDK_int32         scale;
    csSDK_int32         sampleSize;
    importProgressFunc  progressCallback;
    void                *progressCallbackID;
  } imTrimFileRec8;

+------------------------+------------------------------------------------------------------------------------------------------------------+
| ``privatedata``        | Instance data gathered during ``imGetInfo8`` or ``imGetPrefs8``.                                                 |
+------------------------+------------------------------------------------------------------------------------------------------------------+
| ``prefs``              | Clip settings data gathered during ``imGetPrefs8`` (setup dialog).                                               |
+------------------------+------------------------------------------------------------------------------------------------------------------+
| ``trimIn``             | In point of the trimmed clip, in the timebase specified by scale and sampleSize.                                 |
+------------------------+------------------------------------------------------------------------------------------------------------------+
| ``duration``           | Duration of the trimmed clip. If 0, then the request is to leave the clip untrimmed, and at the current duration |
+------------------------+------------------------------------------------------------------------------------------------------------------+
| ``keepAudio``          | If non-zero, the request is to keep the audio in the trimmed result.                                             |
+------------------------+------------------------------------------------------------------------------------------------------------------+
| ``keepVideo``          | If non-zero, the request is to keep the video in the trimmed result.                                             |
+------------------------+------------------------------------------------------------------------------------------------------------------+
| ``destFilePath``       | The unicode path and name of the file to create.                                                                 |
+------------------------+------------------------------------------------------------------------------------------------------------------+
| ``scale``              | The frame rate of the video, represented as scale over sampleSize.                                               |
+------------------------+------------------------------------------------------------------------------------------------------------------+
| ``sampleSize``         |                                                                                                                  |
+------------------------+------------------------------------------------------------------------------------------------------------------+
| ``progressCallback``   | ``importProgressFunc`` callback to call repeatedly to provide progress and to check for cancel by user.          |
|                        |                                                                                                                  |
|                        | May be a NULL pointer, so make sure the function pointer is valid before calling.                                |
+------------------------+------------------------------------------------------------------------------------------------------------------+
| ``progressCallbackID`` | Pass to ``progressCallback``.                                                                                    |
+------------------------+------------------------------------------------------------------------------------------------------------------+

----

.. _importers/structure-descriptions.ColorSpaceRec:

ColorSpaceRec
================================================================================

Selector: ``imGetIndColorSpace``

Describes the colorspace in use with the media.

::

  typedef struct {
    void                 *privatedata;
    PrSDKColorSpaceType  outColorSpaceType;
    RawColorProfileRec   ioProfileRec;
    prSEIColorCodesRec   outSEICodesRec;
  } ColorSpaceRec;

+-----------------------+----------------------------------------------------------------------------------------+
| ``privatedata``       | Private.                                                                               |
+-----------------------+----------------------------------------------------------------------------------------+
| ``outColorSpaceType`` | One of the following:                                                                  |
|                       |                                                                                        |
|                       | - ``kPrSDKColorSpaceType_Undefined``                                                   |
|                       | - ``kPrSDKColorSpaceType_ICC``                                                         |
|                       | - ``kPrSDKColorSpaceType_LUT``                                                         |
|                       | - ``kPrSDKColorSpaceType_SEITags``                                                     |
|                       | - ``kPrSDKColorSpaceType_MXFTags``                                                     |
+-----------------------+----------------------------------------------------------------------------------------+
| ioProfileRec          | A structure describing the color profile.                                              |
|                       |                                                                                        |
|                       | ::                                                                                     |
|                       |                                                                                        |
|                       |   csSDK_int32  ioBufferSize;                                                           |
|                       |   void*        inDestinationBuffer;                                                    |
|                       |   PrSDKString  outName;                                                                |
+-----------------------+----------------------------------------------------------------------------------------+
| ``outSEICodesRec``    | A structure describing the color profile; used with H.265, HEVC, AVC and ProRes media. |
|                       |                                                                                        |
|                       | ::                                                                                     |
|                       |                                                                                        |
|                       |   csSDK_int32  colorPrimariesCode;                                                     |
|                       |   csSDK_int32  transferCharacteristicCode;                                             |
|                       |   csSDK_int32  matrixEquationsCode;                                                    |
|                       |   csSDK_int32  bitDepth;                                                               |
|                       |   prBool       isFullRange;                                                            |
|                       |   prBool       isRGB;                                                                  |
+-----------------------+----------------------------------------------------------------------------------------+

