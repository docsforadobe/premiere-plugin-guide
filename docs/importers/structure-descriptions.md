# Structure Descriptions

## imAcceleratorRec

Selector: [imRetargetAccelerator](selector-descriptions.md#imretargetaccelerator)

Describes the path to the new media and new accelerator created when the Project Manager copies media and its accelerator.

```cpp
typedef struct {
  const prUTF16Char *inOriginalPath;
  const prUTF16Char *inAcceleratorPath;
} imAcceleratorRec;
```

|       Member        |                     Description                      |
| ------------------- | ---------------------------------------------------- |
| `inOriginalPath`    | The unicode path and name of the copied media.       |
| `inAcceleratorPath` | The unicode path and name of the copied accelerator. |

---

## imAnalysisRec

Selector: [imAnalysis](selector-descriptions.md#imanalysis)

Sending back analysis data is a two step process. First, set buffersize to the size of your character buffer and return imNoErr.

Premiere will immediately send `imAnalysis` again; populate the buffer with text. Previously-stored preferences and privateData are returned in this structure.

```cpp
typedef struct {
  void         *privatedata;
  void         *prefs;
  csSDK_int32  buffersize;
  char         *buffer;
  csSDK_int32  *timecodeFormat;
} imAnalysisRec;
```

|      Member      |                                                              Description                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `privatedata`    | Instance data from `imGetInfo8` or `imGetPrefs8`.                                                                                     |
| `prefs`          | Clip Source Settings data from `imGetPrefs8` (setup dialog info).                                                                     |
| `buffersize`     | Set to the desired size and return imNoErr to Premiere, which will re-size and call the plugin again with the `imGetPrefs8` selector. |
| `buffer`         | Text buffer. Terminate lines with line endings (CR and LF).                                                                           |
| `timecodeFormat` | Preferred timecode format, sent by the host.                                                                                          |

---

## imAsyncImporterCreationRec

Selector: [imCreateAsyncImporter](selector-descriptions.md#imcreateasyncimporter)

Create an asynchronous importer object using the data provided, and store it here.

```cpp
typedef struct {
  void                *inPrivateData;
  void                *inPrefs;
  AsyncImporterEntry  outAsyncEntry;
  void                *outAsyncPrivateData;
}
```

|        Member         |                                      Description                                      |
| --------------------- | ------------------------------------------------------------------------------------- |
| `inPrivateData`       | Instance data from `imGetInfo8` or `imGetPrefs8`.                                     |
| `inPrefs`             | Clip Source Settings from `imGetPrefs8` (setup dialog info).                          |
| `outAsyncEntry`       | Provide the entry point for async selectors sent to the asynchronous importer object. |
| `outAsyncPrivateData` | `PrivateData` for the asynchronous importer object.                                   |

---

## imAudioInfoRec7

Selector: [imGetInfo8](selector-descriptions.md#imgetinfo8) (member of [imFileInfoRec8](#imfileinforec8))

Audio data properties of the file (or of the data you will generate, if synthetic).

```cpp
typedef struct {
  csSDK_int32        numChannels;
  float              sampleRate;
  PrAudioSampleType  sampleType;
}
```

|    Member     |                                                                                                                    Description                                                                                                                    |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `numChannels` | Number of audio channels in the audio stream.<br/><br/>Either 1, 2, or 6.                                                                                                                                                                         |
| `sampleRate`  | In hertz.                                                                                                                                                                                                                                         |
| `sampleType`  | This is for informational use only, to disclose the format of the audio on disk, before it is converted to 32-bit float, uninterleaved, by the importer.<br/><br/>The audio sample types are listed in [Universals](../universals/universals.md). |

---

## imCalcSizeRec

Selector: [imCalcSize8](selector-descriptions.md#imcalcsize8)

Asks the importer for an estimate of disk space used by the clip, given the provided trim boundaries.

```cpp
typedef struct {
  void         *privatedata;
  void         *prefs;
  csSDK_int32  trimIn;
  csSDK_int32  duration;
  prInt64      sizeInBytes;
  csSDK_int32  scale;
  csSDK_int32  sampleSize;
} imCalcSizeRec;
```

|    Member     |                                                                        Description                                                                         |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `privatedata` | Instance data gathered from `imGetInfo8` or `imGetPrefs8`.                                                                                                 |
| `prefs`       | Clip Source Settings gathered from `imGetPrefs8` (setup dialog info).                                                                                      |
| `trimIn`      | In point of the trimmed clip the importer should calculate the size for, in the timebase specified by scale over sampleSize.                               |
| `duration`    | Duration of the trimmed clip the importer should calculate the size for.<br/><br/>If 0, then the importer should calculate the size of the untrimmed clip. |
| `sizeInBytes` | Return the calculated size in bytes.                                                                                                                       |
| `scale`       | The frame rate of the video clip, represented as scale over sampleSize.                                                                                    |
| `sampleSize`  |                                                                                                                                                            |

---

## imCheckTrimRec

Selector: [imCheckTrim8](selector-descriptions.md#imchecktrim8)

Provides the requested trim boundaries to the importer, and allows adjusted trim boundaries to be passed back to Premiere.

```cpp
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
```

|    Member     |                                              Description                                               |
| ------------- | ------------------------------------------------------------------------------------------------------ |
| `privatedata` | Instance data gathered from `imGetInfo8` or `imGetPrefs8`.                                             |
| `prefs`       | Clip Source Settings gathered from `imGetPrefs8` (setup dialog info).                                  |
| `trimIn`      | Requested in point of the trimmed clip, in the timebase specified by scale over sampleSize.            |
| `duration`    | Requested duration. If 0, then the request is to leave the clip untrimmed, and at the current duration |
| `keepAudio`   | If non-zero, the request is to keep the audio in the trimmed result.                                   |
| `keepVideo`   | If non-zero, the request is to keep the video in the trimmed result.                                   |
| `newTrimIn`   | Return the acceptable in point of the trimmed clip. It must be at or before the requested in point.    |
| `newDuration` | Return the acceptable duration. newTrimIn + newDuration must be at or after the trimIn + duration.     |
| `scale`       | The frame rate of the video clip, represented as scale over sampleSize.                                |
| `sampleSize`  |                                                                                                        |

---

## imClipFrameDescriptorRec

Selector: [imSelectClipFrameDescriptor](selector-descriptions.md#imselectclipframedescriptor)

Based on the request in `inDesiredClipFrameDescriptor` and the importer's Source Settings, modify `outBestFrameDescriptor` as needed to describe what format the importer will provide.

```cpp
typedef struct {
  void*                inPrivateData;
  void*                inPrefs;
  ClipFrameDescriptor  inDesiredClipFrameDescriptor;
  ClipFrameDescriptor  outBestFrameDescriptor;
} imClipFrameDescriptorRec;
```

|             Member             |                                                             Description                                                              |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `inPrivatedata`                | Instance data gathered from `imGetInfo8` or `imGetPrefs8`.                                                                           |
| `inPrefs`                      | Clip Source Settings gathered from `imGetPrefs8` (setup dialog info).                                                                |
| `inDesiredClipFrameDescriptor` | Requested frame properties, as described by the host.<br/><br/>The `ClipFrameDescriptor` struct is defined in PrSDKImporterShared.h. |
| `outBestFrameDescriptor`       | Frame properties to be produced, filled in with initial guesses                                                                      |

---

## imCompleteAsyncClosedCaptionScanRec

Selector: [imCompleteAsyncClosedCaptionScan](selector-descriptions.md#imcompleteasyncclosedcaptionscan)

This structure is passed to provide one last chance to cleanup and dispose of `inAsyncCaptionScanPrivateData`, and to mark whether the closed caption scan completed without error.

```cpp
typedef struct {
  void*        inPrivateData;
  const void*  inPrefs;
  void*        inAsyncCaptionScanPrivateData;
  prBool       inScanCompletedWithoutError;
} imCompleteAsyncClosedCaptionScanRec;
```

|             Member              |                                                                                             Description                                                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `inPrivatedata`                 | Instance data gathered from `imGetInfo8` or `imGetPrefs8`.                                                                                                                                           |
| `inPrefs`                       | Clip Source Settings gathered from `imGetPrefs8` (setup dialog info).                                                                                                                                |
| `inAsyncCaptionScanPrivateData` | Cleanup and dispose of any data here that was allocated in `imInitiateAsyncClosedCaptionScan` or `imGetNextClosedCaption`.<br/><br/>This data should not be accessed after returning from this call. |
| `inScanCompletedWithoutError`   | Set to true if no error.                                                                                                                                                                             |

---

## imIndColorProfileRec

Selector: [imGetIndColorProfile](selector-descriptions.md#imgetindcolorprofile)

Deprecated as of 13.0. Describes a color profile supported by a clip.

The first time `imGetIndColorProfile` is sent, `inDestinationBuffer` will be NULL, and `ioBufferSize` will be 0.

Set `ioBufferSize` to the required size for the buffer, and the host will allocate the memory and call the importer again, with a valid `inDestinationBuffer`, and `ioBufferSize` set to the value just provided by the importer.

```cpp
typedef struct {
  void         *inPrivateData;
  csSDK_int32  ioBufferSize;
  void         *inDestinationBuffer;
  PrSDKString  outName;
} imIndColorProfileRec;
```

---

## imCopyFileRec

Selector: [imCopyFile](selector-descriptions.md#imcopyfile)

Describes how to copy a clip. Also provides a callback to update the progress bar and check if the user has cancelled.

```cpp
typedef struct {
  void                *inPrivateData;
  csSDK_int32         *inPrefs;
  const prUTF16Char   *inSourcePath;
  const prUTF16Char   *inDestPath;
  importProgressFunc  inProgressCallback;
  void                *inProgressCallbackID;
} imTrimFileRec;
```

|         Member         |                                                                                        Description                                                                                        |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `inPrivateData`        | Instance data gathered during `imGetInfo8` or `imGetPrefs8`.                                                                                                                              |
| `inPrefs`              | Clip Source Settings gathered during `imGetPrefs8` (setup dialog).                                                                                                                        |
| `inSourcePath`         | Full unicode path of the source file.                                                                                                                                                     |
| `inDestPath`           | Full unicode path of the destination file.                                                                                                                                                |
| `inProgressCallback`   | importProgressFunc callback to call repeatedly to provide progress and to check for cancel by user.<br/>May be a NULL pointer, so make sure the function pointer is valid before calling. |
| `inProgressCallbackID` | Pass to `progressCallback`.                                                                                                                                                               |

---

## imDataRateAnalysisRec

Selector: [imDataRateAnalysis](selector-descriptions.md#imdatarateanalysis)

Specify the desired buffersize, return to Premiere with `imNoErr`; upon the next call fill buffer with `imDataSamples`, and specify a base data rate for audio (if any).

This structure is used like `imAnalysisRec`.

```cpp
typedef struct {
  void         *privatedata;
  void         *prefs;
  csSDK_int32  buffersize;
  char         *buffer;
  csSDK_int32  baserate;
} imDataRateAnalysisRec;
```

|    Member     |                                         Description                                         |
| ------------- | ------------------------------------------------------------------------------------------- |
| `privatedata` | Instance data gathered from `imGetInfo8` or `imGetPrefs8`.                                  |
| `prefs`       | Clip Source Settings gathered from `imGetPrefs8` (setup dialog info).                       |
| `buffersize`  | The size of the buffer you request from Premiere prior to passing data back data in buffer. |
| `buffer`      | Pointer to the analysis buffer to be filled with `imDataSamples` (see structure below).     |
| `baserate`    | `Audio` data rate (bytes per second) of the file.                                           |

```cpp
typedef struct {
  csSDK_uint32  sampledur;
  csSDK_uint32  samplesize;
} imDataSample;
```

|    Member    |                                                 Description                                                 |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| `sampledur`  | Duration of one sample in video timebase, in samplesize increments; set the high bit if this is a keyframe. |
| `samplesize` | `Size` of this sample in bytes.                                                                             |

---

## imDeferredProcessingRec

Selector: [imDeferredProcessing](selector-descriptions.md#imdeferredprocessing)

Describes the current progress of the deferred processing on the clip referred to by inPrivateData.

```cpp
typedef struct {
  void   *inPrivateData;
  float  outProgress;
  char   outInvalidateFile;
  char   outCallAgain;
} imDeferredProcessingRec;
```

|       Member        |                                Description                                 |
| ------------------- | -------------------------------------------------------------------------- |
| `inPrivateData`     | Instance data gathered from `imGetInfo8` or `imGetPrefs8`.                 |
| `outProgress`       | Set this to the current progress, from 0.0 to 1.0.                         |
| `outInvalidateFile` | The importer has updated information about the file.                       |
| `outCallAgain`      | Set this to true to request that the importer be called again immediately. |

---

## imDeleteFileRec

Selector: [imDeleteFile](selector-descriptions.md#imdeletefile)

Describes the file to be deleted.

```cpp
typedef struct {
  csSDK_int32        filetype;
  const prUTF16Char  deleteFile;
} imDeleteFileRec;
```

|    Member    |                             Description                             |
| ------------ | ------------------------------------------------------------------- |
| `filetype`   | The file's unique four character code, defined in the IMPT resource |
| `deleteFile` | Specifies the name (and path) of the file to be deleted.            |

---

## imFileAccessRec8

Selectors: `imGetInfo8` and `imGetPrefs8`

Describes the file being imported.

```cpp
typedef struct {
  void               *importID;
  csSDK_int32        filetype;
  const prUTF16Char  *filepath;
  imFileRef          fileref;
  PrMemoryPtr        newfilename;
} imFileAccessRec;
```

|    Member     |                                                                                                     Description                                                                                                      |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `importID`    | Unique ID provided by Premiere. Do not modify!                                                                                                                                                                       |
| `filetype`    | The file's unique four character code, defined in the IMPT resource.                                                                                                                                                 |
| `filepath`    | The unicode file path and name.                                                                                                                                                                                      |
| `fileref`     | A Windows HANDLE. Premiere does not overload this value by using it internally, although setting it to the constant kBadFileRef may cause Premiere to think the file is closed.<br/><br/>This value is always valid. |
| `newfilename` | If the file is synthetic, the importer can specify the displayable name here as a prUTF16Char string during `imGetPrefs8`.                                                                                           |

---

## imFileAttributesRec

Selector: [imGetFileAttributes](selector-descriptions.md#imgetfileattributes)

New in Premiere Pro 3.1. Provide the clip creation date.

```cpp
typedef struct {
  prDateStamp  creationDateStamp;
  csSDK_int32  reserved[40];
} imFileAttributesRec;
```

|       Member        |                 Description                  |
| ------------------- | -------------------------------------------- |
| `creationDateStamp` | Structure to store when the clip was created |

---

## imFileInfoRec8

Selector: [imGetInfo8](selector-descriptions.md#imgetinfo8)

Describes the clip, or the stream with the ID streamIdx. Set the clip or stream attributes from the file header or data source. Create and store any privateData.

When a synthetic clip is created, and the user provides the desired resolution, frame rate, pixel aspect ratio, and audio sample rate in the New Synthetic dialog, these values will be pre-initialized by Premiere.

If importing stereoscopic footage, import the left-eye video channel for streamID 0, and the right-eye video channel for streamID 1.

```cpp
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
```

+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|        Member        |                                                                                                                                Description                                                                                                                                |
+======================+===========================================================================================================================================================================================================================================================================+
| `hasVideo`           | If non-zero, the file contains video.                                                                                                                                                                                                                                     |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `hasAudio`           | If non-zero, the file contains audio.                                                                                                                                                                                                                                     |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `vidInfo`            | If there is video in the file, fill out the `imImageInfoRec` structure (e.g. height, width, alpha info, etc.).                                                                                                                                                            |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `vidScale`           | The frame rate of the video, represented as scale over sampleSize.                                                                                                                                                                                                        |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `vidSampleSize`      |                                                                                                                                                                                                                                                                           |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `vidDuration`        | The total number of frames of video, in the video timebase.                                                                                                                                                                                                               |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `audInfo`            | If there is audio in the file, fill out the imAudioInfoRec7 structure.                                                                                                                                                                                                    |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `audDuration`        | The total number of audio sample frames.                                                                                                                                                                                                                                  |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `accessModes`        | The access mode of this file. Use one of the following constants:                                                                                                                                                                                                         |
|                      |                                                                                                                                                                                                                                                                           |
|                      | - `kRandomAccessImport` - This file can be read by random access (default)                                                                                                                                                                                                |
|                      | - `kSequentialAudioOnly` - When accessing audio, only sequential reads allowed (for variable bit rate files)                                                                                                                                                              |
|                      | - `kSequentialVideoOnly` - When accessing video, only sequential reads allowed                                                                                                                                                                                            |
|                      | - `kSequentialOnly` - Both sequential audio and video                                                                                                                                                                                                                     |
|                      | - `kSeparateSequentialAudio` - Both random access and sequential access.                                                                                                                                                                                                  |
|                      |                                                                                                                                                                                                                                                                           |
|                      | This setting allows audio to be retrieved for scrubbing or playback even during audio conforming.                                                                                                                                                                         |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `privatedata`        | Private instance data.                                                                                                                                                                                                                                                    |
|                      |                                                                                                                                                                                                                                                                           |
|                      | Allocate a handle using Premiere's memory functions and store it here.                                                                                                                                                                                                    |
|                      |                                                                                                                                                                                                                                                                           |
|                      | Premiere will return the handle with subsequent selectors.                                                                                                                                                                                                                |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `prefs`              | Clip Source Settings data gathered from `imGetPrefs8` (setup dialog info).                                                                                                                                                                                                |
|                      |                                                                                                                                                                                                                                                                           |
|                      | When a synthetic clip is created using File > New, `imGetPrefs8` is sent `beforeimGetInfo8` so this settings structure will already be valid.                                                                                                                             |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `hasDataRate`        | If set, the importer can read or generate data rate information for this file and will be sent `imDataRateAnalysis`.                                                                                                                                                      |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `streamIdx`          | The Premiere-specified stream index number.                                                                                                                                                                                                                               |
|                      |                                                                                                                                                                                                                                                                           |
|                      | Only useful if clip uses multiple streams.                                                                                                                                                                                                                                |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `streamsAsComp`      | If multiple streams and this is stream zero, indicate whether to import as a composition or multiple clips.                                                                                                                                                               |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `streamName`         | Optional. The unicode name of this stream if there are multiple streams.                                                                                                                                                                                                  |
|                      |                                                                                                                                                                                                                                                                           |
|                      | New in Premiere Pro 3.1, an importer may use this to set the clip name based on metadata rather than the filename.                                                                                                                                                        |
|                      |                                                                                                                                                                                                                                                                           |
|                      | The importer should set `imImportInfoRec.canSupplyMetadataClipName` to true, and fill out the name here.                                                                                                                                                                  |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `sessionPluginID`    | This ID should be used in the [File Registration Suite](../universals/sweetpea-suites.md#file-registration-suite) for registering external files (such as textures, logos, etc) that are used by an importer instance but do not appear as footage in the Project Window. |
|                      |                                                                                                                                                                                                                                                                           |
|                      | Registered files will be taken into account when trimming or copying a project using the Project Manager.                                                                                                                                                                 |
|                      |                                                                                                                                                                                                                                                                           |
|                      | The `sessionPluginID` is valid only for the call that it is passed on.                                                                                                                                                                                                    |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `alwaysUnquiet`      | Set to non-zero to tell Premiere if the clip should always be unquieted immediately when the application regains focus.                                                                                                                                                   |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `filepath`           | Added in Premiere Pro 4.1. For clips that have audio in files separate from the video file, set the filename here, so that UMIDs can properly be generated when exporting sequences to AAF.                                                                               |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `canProvidePeakData` | New in Premiere Pro CS6. This allows an importer to toggle whether or not it wants to provide peak audio data on a clip-by-clip basis.                                                                                                                                    |
|                      |                                                                                                                                                                                                                                                                           |
|                      | It defaults to the setting set in `imImportInfoRec.canProvidePeakAudio`.                                                                                                                                                                                                  |
|                      |                                                                                                                                                                                                                                                                           |
|                      | !!! warning                                                                                                                                                                                                                                                               |
|                      |      Do not attempt to use this setting with growing files.                                                                                                                                                                                                               |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `mayBeGrowing`       | New in Premiere Pro CS6.0.2. Set to non-zero if this clip is growing and should be refreshed at the interval set in the Media Preferences.                                                                                                                                |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

---

## imFileOpenRec8

Selector: [imOpenFile8](selector-descriptions.md#imopenfile8)

The file Premiere wants the importer to open.

```cpp
typedef struct {
  imFileAccessRec8  fileinfo;
  void              *privatedata;
  csSDK_int32       reserved;
  PrFileOpenAccess  inReadWrite;
  csSDK_int32       inImporterID;
  csSDK_size_t      outExtraMemoryUsage;
  csSDK_int32       inStreamIdx;
} imFileOpenRec8;
```

|        Member         |                                                                     Description                                                                     |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `fileinfo`            | `imFileAccessRec8` describing the incoming file.                                                                                                    |
| `privatedata`         | Instance data gathered from `imGetInfo8` or `imGetPrefs8`.                                                                                          |
| `reserved`            | Do not use.                                                                                                                                         |
| `inReadWrite`         | The file should be opened with the access mode specified:<br/><br/>Either `kPrOpenFileAccess_ReadOnly` or `kPrOpenFileAccess_ReadWrite`             |
| `inImporterID`        | Can be used as the ID for calls in the [PPix Cache Suite](../universals/sweetpea-suites.md#ppix-cache-suite).                                       |
| `outExtraMemoryUsage` | New in CS5. If the importer uses memory just by being open, which cannot otherwise be registered in the cache, put the size in bytes in this field. |
| `inStreamIdx`         | New in CS6. If the clip has multiple streams (for stereoscopic video or otherwise), this ID differentiates between them.                            |

---

## imFileRef

Selectors:

- [imAnalysis](selector-descriptions.md#imanalysis),
- [imDataRateAnalysis](selector-descriptions.md#imdatarateanalysis),
- [imOpenFile8](selector-descriptions.md#imopenfile8),
- [imQuietFile](selector-descriptions.md#imquietfile),
- [imCloseFile](selector-descriptions.md#imclosefile),
- [imGetTimeInfo8](selector-descriptions.md#imgettimeinfo8),
- [imSetTimeInfo8](selector-descriptions.md#imsettimeinfo8),
- [imImportImage](selector-descriptions.md#imimportimage),
- [imImportAudio7](selector-descriptions.md#imimportaudio7)

A file HANDLE on Windows, or a void\* on MacOS.

`imFileRef` is also a member of `imFileAccessRec`.

Use OS-specific functions, rather than ANSI file functions, when manipulating imFileRef.

---

## imFrameFormat

Selector: [imGetSourceVideo](selector-descriptions.md#imgetsourcevideo) (member of [imSourceVideoRec](#imsourcevideorec))

Describes the frame dimensions and pixel format.

```cpp
typedef struct {
  csSDK_int32    inFrameWidth;
  csSDK_int32    inFrameHeight;
  PrPixelFormat  inPixelFormat;
} imFrameFormat;
```

|     Member      |               Description                |
| --------------- | ---------------------------------------- |
| `inFrameWidth`  | The frame dimensions requested.          |
| `inFrameHeight` |                                          |
| `inPixelFormat` | The pixel format of the frame requested. |

---

## imGetAudioChannelLayoutRec

Selector: [imGetAudioChannelLayout](selector-descriptions.md#imgetaudiochannellayout)

The importer should label each audio channel in the clip being imported.

If no labels are specified, the channel layout will be assumed to be discrete.

```cpp
typedef struct {
  void*                inPrivateData;
  PrAudioChannelLabel  outChannelLabels[kMaxAudioChannelCount];
} imGetAudioChannelLayoutRec;
```

|       Member       |                                                                                 Description                                                                                  |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `inPrivatedata`    | Instance data gathered from `imGetInfo8` or `imGetPrefs8`.                                                                                                                   |
| `outChannelLabels` | A valid audio channel label should be assigned for each channel in the clip.<br/><br/>Labels are defined in the [Audio Suite](../universals/sweetpea-suites.md#audio-suite). |

---

## imGetNextClosedCaptionRec

Selector: [imGetNextClosedCaption](selector-descriptions.md#imgetnextclosedcaption)

This structure provides private data allocated in `imInitiateAsyncClosedCaptionScan`, and should be filled out to pass back a closed caption, it's time, format, size, and overall progress in the closed caption scan.

```cpp
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
```

+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|             Member              |                                                                                                                                                           Description                                                                                                                                                            |
+=================================+==================================================================================================================================================================================================================================================================================================================================+
| `inPrivatedata`                 | Instance data gathered from `imGetInfo8` or `imGetPrefs8`.                                                                                                                                                                                                                                                                       |
+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `inPrefs`                       | Clip Source Settings gathered from `imGetPrefs8` (setup dialog info).                                                                                                                                                                                                                                                            |
+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `inAsyncCaptionScanPrivateData` | This provides any private data that was allocated in `imInitiateAsyncClosedCaptionScan`.                                                                                                                                                                                                                                         |
+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `outProgress`                   | Update this value to denote the current progress iterating through all the captions. Valid values are between 0.0 and 1.0.                                                                                                                                                                                                       |
+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `outScale`                      | The timebase of outPosition, represented as scale over sampleSize.                                                                                                                                                                                                                                                               |
+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `outSampleSize`                 |                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `outPosition`                   | The position of the closed caption.                                                                                                                                                                                                                                                                                              |
+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `outClosedCaptionFormat`        | The format of the closed captions. One of the following:                                                                                                                                                                                                                                                                         |
|                                 |                                                                                                                                                                                                                                                                                                                                  |
|                                 | - `kPrClosedCaptionFormat_Undefined`                                                                                                                                                                                                                                                                                             |
|                                 | - `kPrClosedCaptionFormat_CEA608` - CEA-608 byte stream                                                                                                                                                                                                                                                                          |
|                                 | - `kPrClosedCaptionFormat_CEA708` - CEA-708 byte stream (may contain 608 data wrapped in 708)                                                                                                                                                                                                                                    |
|                                 | - `kPrClosedCaptionFormat_TTML` - W3C TTML string that conforms to the [W3C Timed Text Markup Language (TTML) 1.0](http://www.w3.org/TR/ttaf1-dfxp/) or optionally conforming to [SMPTE ST 2052-1:2010](http://store.smpte.org/), or optionally conforming to [EBU Tech 3350](http://tech.ebu.ch/webdav/site/tech/shared/tech/). |
|                                 |                                                                                                                                                                                                                                                                                                                                  |
|                                 | If the TTML string contains tunneled data (e.g. CEA-608 data), then it is preferred that the plugin provide that through the appropriate byte stream format (e.g. `kPrClosedCaptionFormat_CEA608`).                                                                                                                              |
+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `outCaptionData`                | Memory location to where the plugin should write the closed caption bytes, if providing CEA-608 or CEA-708.                                                                                                                                                                                                                      |
+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `outTTMLData`                   | UTF-8 String of valid W3C TTML data.                                                                                                                                                                                                                                                                                             |
|                                 | The entire string may be split into substrings (e.g. line by line) and the host will concatenate and decode them (only used when outCaptionData is kPrClosedCaptionFormat_TTML).                                                                                                                                                 |
+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `ioCaptionDataSize`             | `Size` of outCaptionData buffer (in bytes) allocated from the host. The importer should set this variable to the actual number of bytes that were written to outCaptionData, or the length of the string (characters, not bytes) pointed by outTTMLData.                                                                         |
+---------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

---

## imGetPrefsRec

Selector: [imGetPrefs8](selector-descriptions.md#imgetprefs8)

Contains settings/prefs data gathered from (or defaults to populate) a setup dialog.

If you are creating media, you can may generate a video preview that includes the background frame from the timeline.

```cpp
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
```

|        Member         |                                                                                                                                                                                                                           Description                                                                                                                                                                                                                            |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `prefs`               | A pointer to a private structure (which you allocate) for storing Clip Source Settings.                                                                                                                                                                                                                                                                                                                                                                          |
| `prefsLength`         | Prior to storing anything in the prefs member, set prefsLength to the size of your structure and return imNoErr; Premiere will re-size and call the plugin again with `imGetPrefs8`.                                                                                                                                                                                                                                                                             |
| `firstTime`           | If set, `imGetPrefs8` is being sent for the first time.<br/><br/>Instead, check to see if prefs has been allocated. If not, `imGetPrefs8` is being sent for the first time. Set up default values for the prefsLength buffer and present any setup dialog.                                                                                                                                                                                                       |
| `timelineData`        | `Can` be passed to getPreviewFrameEx callback along with tdbTimelineLocation to get a frame from the timeline beneath the current clip or timeline location. This is useful for titler plugins.                                                                                                                                                                                                                                                                  |
| `privatedata`         | Private instance data.<br/><br/>Allocate a handle using Premiere's memory functions and store it here, if not already allocated in `imGetInfo8`.<br/><br/>Premiere will return the handle with subsequent selectors.                                                                                                                                                                                                                                             |
| `tdbTimelineLocation` | `Can` be passed to getPreviewFrameEx callback along with timelineData to get a frame from the timeline beneath the current clip or timeline location. This is useful for titler plugins.                                                                                                                                                                                                                                                                         |
| `sessionPluginID`     | This ID should be used in the [File Registration Suite](../universals/sweetpea-suites.md#file-registration-suite) for registering external files (such as textures, logos, etc) that are used by a importer instance but do not appear as footage in the Project Window.<br/><br/>Registered files will be taken into account when trimming or copying a project using the Project Manager. The sessionPluginID is valid only for the call that it is passed on. |
| `imageWidth`          | New in CS5. The native resolution of the video.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `imageHeight`         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `pixelAspectNum`      | New in CS5. The pixel aspect ratio of the video.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `pixelAspectDen`      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `vidScale`            | New in CS5. The frame rate of the video, represented as scale over sampleSize.                                                                                                                                                                                                                                                                                                                                                                                   |
| `vidSampleSize`       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `sampleRate`          | New in CS5. Audio sample rate.                                                                                                                                                                                                                                                                                                                                                                                                                                   |

---

## imImageInfoRec

Selector: [imGetInfo8](selector-descriptions.md#imgetinfo8) (member of [imFileInfoRec8](#imfileinforec8))

Describes the video to be imported.

```cpp
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
  PrTime        frameRate;
  prBool        hasEmbeddedLUT;
  csSDK_int32   reserved[12];
} imImageInfoRec;
```

### Plug-in Info

|          Member          |                                                   Description                                                   |
| ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `importerID`             | `Can` be used as the ID for calls in the [PPix Cache Suite](../universals/sweetpea-suites.md#ppix-cache-suite). |
| `supportsAsyncIO`        | Set this to true if the importer supports `imCreateAsyncImporter` and ai\* selectors.                           |
| `supportsGetSourceVideo` | Set this to true if the importer supports the `imGetSourceVideo` selector.                                      |

### Bounds Info

|      Member      |                                                                                                                  Description                                                                                                                  |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `imageWidth`     | Frame width in pixels.                                                                                                                                                                                                                        |
| `imageHeight`    | Frame height in pixels.                                                                                                                                                                                                                       |
| `pixelAspectNum` | The pixel aspect ratio numerator and denominator.<br/><br/>For synthetic importers, these are by default the PAR of the project.<br/><br/>Only set this if you need a specific PAR for the geometry of the synthesized footage to be correct. |
| `pixelAspectDen` |                                                                                                                                                                                                                                               |

### Time Info

+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      Member       |                                                                             Description                                                                              |
+===================+======================================================================================================================================================================+
| `isStill`         | If set, the file contains a single frame, so only one frame will be cached.                                                                                          |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `noDuration`      | One of the following:                                                                                                                                                |
|                   |                                                                                                                                                                      |
|                   | - `imNoDurationFalse`                                                                                                                                                |
|                   | - `imNoDurationNoDefault`                                                                                                                                            |
|                   | - `imNoDurationStillDefault` - use the default duration for stills, as set by the user in the Preferences                                                            |
|                   | - `imNoDurationNoDefault` - the importer will supply it's own duration                                                                                               |
|                   |                                                                                                                                                                      |
|                   | This is primarily for synthetic clips, but can be used for importing non-sequential still images.                                                                    |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `isRollCrawl`     | Set to non-zero value to specify this clip is a rolling or crawling title.                                                                                           |
|                   |                                                                                                                                                                      |
|                   | This allows a player to optionally use the [RollCrawl Suite](../universals/sweetpea-suites.md#rollcrawl-suite) to get sections of this title for real-time playback. |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `hasPulldown`     | Set this to true if the clip contains NTSC film footage with 3:2 pulldown.                                                                                           |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pulldownCadence` | Set this to the enumerated value that describes the pulldown of the clip:                                                                                            |
|                   |                                                                                                                                                                      |
|                   | - `importer_PulldownPhase_NO_PULLDOWN`                                                                                                                               |
|                   |                                                                                                                                                                      |
|                   | **2:3 cadences:**                                                                                                                                                    |
|                   |                                                                                                                                                                      |
|                   | - `importer_PulldownPhase_WSSWW`                                                                                                                                     |
|                   | - `importer_PulldownPhase_SSWWW`                                                                                                                                     |
|                   | - `importer_PulldownPhase_SWWWS`                                                                                                                                     |
|                   | - `importer_PulldownPhase_WWWSS`                                                                                                                                     |
|                   | - `importer_PulldownPhase_WWSSW`                                                                                                                                     |
|                   |                                                                                                                                                                      |
|                   | **24pa cadences:**                                                                                                                                                   |
|                   |                                                                                                                                                                      |
|                   | - `importer_PulldownPhase_WWWSW`                                                                                                                                     |
|                   | - `importer_PulldownPhase_WWSWW`                                                                                                                                     |
|                   | - `importer_PulldownPhase_WSWWW`                                                                                                                                     |
|                   | - `importer_PulldownPhase_SWWWW`                                                                                                                                     |
|                   | - `importer_PulldownPhase_WWWWS`                                                                                                                                     |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `posterFrame`     | New in Premiere Pro CS3. Poster frame number to be displayed.                                                                                                        |
|                   | If not specified, the poster frame will be the first frame of the clip.                                                                                              |
+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Format Info

+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          Member           |                                                                                                                                                               Description                                                                                                                                                                |
+===========================+==========================================================================================================================================================================================================================================================================================================================================+
| `depth`                   | Bits per pixel. This currently has no effect and should be left unchanged.                                                                                                                                                                                                                                                               |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `subType`                 | The four character code of the file's codec; associates files with MAL plugins. For uncompressed files, set to `imUncompressed`.                                                                                                                                                                                                         |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `fieldType`               | One of the following:                                                                                                                                                                                                                                                                                                                    |
|                           |                                                                                                                                                                                                                                                                                                                                          |
|                           | - `prFieldsNone`                                                                                                                                                                                                                                                                                                                         |
|                           | - `prFieldsUpperFirst`                                                                                                                                                                                                                                                                                                                   |
|                           | - `prFieldsLowerFirst`                                                                                                                                                                                                                                                                                                                   |
|                           | - `prFieldsUnknown`                                                                                                                                                                                                                                                                                                                      |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `fieldsStacked`           | Fields are present, and not interlaced. Deprecated since Premiere Pro 7.0.                                                                                                                                                                                                                                                               |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `alphaType`               | Used when depth is 32 or greater. One of the following:                                                                                                                                                                                                                                                                                  |
|                           |                                                                                                                                                                                                                                                                                                                                          |
|                           | - `alphaNone` - no alpha channel (the default)                                                                                                                                                                                                                                                                                           |
|                           | - `alphaStraight` - straight alpha channel                                                                                                                                                                                                                                                                                               |
|                           | - `alphaBlackMatte` - premultiplied with black                                                                                                                                                                                                                                                                                           |
|                           | - `alphaWhiteMatte` - premultiplied with white                                                                                                                                                                                                                                                                                           |
|                           | - `alphaArbitrary` - premultiplied with the color specified in matteColor                                                                                                                                                                                                                                                                |
|                           | - `alphaOpaque` - for video with alpha channel prefilled to opaque.                                                                                                                                                                                                                                                                      |
|                           |                                                                                                                                                                                                                                                                                                                                          |
|                           | This gives Premiere the opportunity to make an optimization by skipping the fill to opaque that would otherwise be performed if alphaNone was set.                                                                                                                                                                                       |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `matteColor`              | `Newly` used in Premiere Pro CS3. Used to specify matte color if `alphaType` is set to `alphaArbitrary`.                                                                                                                                                                                                                                 |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `alphaInverted`           | If non-zero, alpha is treated as inverted (e.g. black becomes transparent).                                                                                                                                                                                                                                                              |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `canTransform`            | Set to non-zero value to specify this importer handles resolution independent files and can apply a transform matrix.<br/><br/>The matrix will be passed during the import request in `imImportImageRec.transform`.<br/><br/>This code path is currently not called by Premiere Pro. After Effects uses this call to import Flash video. |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `interpretationUncertain` | Use an 'or' operator to combine any of the following flags:                                                                                                                                                                                                                                                                              |
|                           |                                                                                                                                                                                                                                                                                                                                          |
|                           | - `imPixelAspectRatioUncertain`                                                                                                                                                                                                                                                                                                          |
|                           | - `imFieldTypeUncertain`                                                                                                                                                                                                                                                                                                                 |
|                           | - `imAlphaInfoUncertain`                                                                                                                                                                                                                                                                                                                 |
|                           | - `imEmbeddedColorProfileUncertain`                                                                                                                                                                                                                                                                                                      |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `colorProfileSupport`     | Deprecated as of 13.0. New in CS5.5.                                                                                                                                                                                                                                                                                                     |
|                           |                                                                                                                                                                                                                                                                                                                                          |
|                           | Set to `imColorProfileSupport_Fixed` to support color management.                                                                                                                                                                                                                                                                        |
|                           |                                                                                                                                                                                                                                                                                                                                          |
|                           | If the importer is uncertain, it should use `interpretationUncertain` above instead.                                                                                                                                                                                                                                                     |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `codecDescription`        | Text description of the codec in use.                                                                                                                                                                                                                                                                                                    |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `ColorProfileRec`         | New in 13.0; describes the color profile being used by the importer, with this media.                                                                                                                                                                                                                                                    |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `colorSpaceSupport`       | Set to `imColorSpaceSupport_Fixed` to support color management.                                                                                                                                                                                                                                                                          |
|                           |                                                                                                                                                                                                                                                                                                                                          |
|                           | If importer is uncertain, it should use `imColorSpaceSupport_None` above instead.                                                                                                                                                                                                                                                        |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `hasEmbeddedLUT`          | Set to `kPrTrue` if media contains embedded LUT. Else set to `kPrFalse`.                                                                                                                                                                                                                                                                 |
+---------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Unused

|         Member         |                                                                              Description                                                                              |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pixelAspectV1`        | Obsolete. Maintained for backwards compatability.<br/><br/>Plugins written for the Premiere 6.x or Premiere Pro API should use `pixelAspectNum` and `pixelAspectDen`. |
| `isVectors`            | Use `canTransform` instead.                                                                                                                                           |
| `drawsExternal`        |                                                                                                                                                                       |
| `canForceInternalDraw` |                                                                                                                                                                       |
| `dontObscure`          |                                                                                                                                                                       |

---

## imImportAudioRec7

Selector: [imImportAudio7](selector-descriptions.md#imimportaudio7)

Describes the audio samples to be returned, and contains an allocated buffer for the importer to fill in.

Provide the audio in 32-bit float, uninterleaved audio format.

```cpp
typedef struct {
  PrAudioSample  position;
  csSDK_uint32   size;
  float          **buffer;
  void           *privatedata;
  void           *prefs;
} imImportAudioRec7;
```

|    Member     |                                                                                                                                         Description                                                                                                                                          |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `position`    | In point, in audio sample frames.<br/><br/>The importer should save the out point of the request in privatedata, because if position is less than zero, then the audio request is sequential, which means the importer should return contiguous samples from the last `imImportAudio7` call. |
| `size`        | The number of audio sample frames to import.                                                                                                                                                                                                                                                 |
| `buffer`      | An array of buffers, one buffer for each channel, with length specified in size.<br/><br/>These buffers are allocated by the host application, for the plugin to fill in with audio data.                                                                                                    |
| `privatedata` | Instance data gathered from `imGetInfo8` or `imGetPrefs8`.                                                                                                                                                                                                                                   |
| `prefs`       | Clip Source Settings data gathered from `imGetPrefs8` (setup dialog info).                                                                                                                                                                                                                   |

---

## imImportImageRec

Selector: [imImportImage](selector-descriptions.md#imimportimage)

Describes the frame to be returned.

```cpp
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
```

### Bounds Info (for imImportImageRec)

|    Member    |                        Description                         |
| ------------ | ---------------------------------------------------------- |
| `dstWidth`   | Width of the destination rectangle (in pixels).            |
| `dstHeight`  | Height of the destination rectangle (in pixels).           |
| `dstOriginX` | Origin X point (0 indicates the frame is drawn offscreen). |
| `dstOriginY` | Origin Y point (0 indicates the frame is drawn offscreen). |
| `srcWidth`   | The same number returned as dstWidth.                      |
| `srcHeight`  | The same number returned as dstHeight.                     |
| `srcOriginX` | The same number returned as dstOriginX.                    |
| `srcOriginY` | The same number returned as dstOriginY.                    |

### Frame Info

|      Member      |                                                                                                                                                                                                                                        Description                                                                                                                                                                                                                                        |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rowbytes`       | The number of bytes in a single row of pixels.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `pix`            | Pointer to a buffer into which the importer should draw. Allocated based on information from the `imGetInfo8`.                                                                                                                                                                                                                                                                                                                                                                            |
| `pixsize`        | The number of pixels. rowbytes \* height.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `pixformat`      | The pixel format Premiere requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `flags`          | `imDraftMode` - Draw quickly if possible, using a faster and possibly less accurate algorithm.<br/><br/>This may be passed when playing from the timeline.<br/><br/>`imSamplesAreFields` - Most importers will ignore as Premiere already scales in/out/scale to account for fields, but if you need to know that this has occurred (because maybe you measure something in 'frames'), check this flag.<br/><br/>Also, may we suggest considering measuring in seconds instead of frames? |
| `fieldType`      | If the importer can swap fields, it should render the frame with the given field dominance: either `imFieldsUpperFirst` or `imFieldsLowerFirst`.                                                                                                                                                                                                                                                                                                                                          |
| `scale`          | The frame rate of the video, represented as scale over sampleSize.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `sampleSize`     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `in`             | In point, based on the timebase defined by scale over sampleSize.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `out`            | Out point, based on the timebase defined by scale over sampleSize.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `pos`            | Import position, based on the above timebase.<br/><br/>**API bug**: Synthetic and custom importers will always receive zero.<br/><br/>Thus, adjusting the in point on the timeline will not offset the in point.                                                                                                                                                                                                                                                                          |
| `privatedata`    | Instance data gathered during `imGetInfo` or `imGetPrefs`.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `prefs`          | Clip Source Settings data gathered during `imGetPrefs` (setup dialog info).                                                                                                                                                                                                                                                                                                                                                                                                               |
| `alphaBounds`    | This is the rect outside of which the alpha is always 0. Simply do not alter this field if the alpha bounds match the destination bounds.<br/><br/>If set, the alpha bounds must be contained by the destination bounds. This is only currently used when a plugin calls `ppixGetAlphaBounds`, and not currently used by any native plugins.                                                                                                                                              |
| `applyTransform` | New in After Effects CS3. Not currently provided by Premiere.<br/><br/>If non-zero, the host is requesting that the importer apply the transform specified in transform and destClipRect before returning the resulting image in pix.                                                                                                                                                                                                                                                     |
| `transform`      | New in After Effects CS3. Not currently provided by Premiere. The source to destination transform matrix.                                                                                                                                                                                                                                                                                                                                                                                 |
| `destClipRect`   | New in After Effects CS3. Not currently provided by Premiere. Destination rect inside the bounds of the pix buffer.                                                                                                                                                                                                                                                                                                                                                                       |

---

## imImportInfoRec

Selector: [imInit](selector-descriptions.md#iminit)

Describes the importer's capabilities to Premiere.

```cpp
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
```

### Screen Info

|        Member         |                                                                                             Description                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `noFile`              | If set, this is a synthetic importer. The file reference will be zero.                                                                                                                              |
| `addToMenu`           | If set to `imMenuNew`, the importer will appear in the File > New menu.                                                                                                                             |
| `canDoContinuousTime` | If set, the importer can render frames at arbitrary times and there is no set timecode.<br/>A color matte generator or a titler would set this flag.                                                |
| `canCreate`           | If set, Premiere will treat this synthetic importer as if it creates files on disk to be referenced for frames and audio.<br/><br/>See Additional Details for more information on custom importers. |

### File Handling Flags

|     Member     |                                                                                                 Description                                                                                                 |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `canOpen`      | If set, the importer handles open and close operations.<br/>Set if the plugin needs to be called to handle `imOpenFile`, `imQuietFile`, and `imCloseFile`.                                                  |
| `canSave`      | If set, the importer handles File > Save and File > Save As after a clip has been captured and must handle the `imSaveFile` selector.                                                                       |
| `canDelete`    | If set, the importer can delete its own files.<br/><br/>The plugin must handle the `imDeleteFile` selector.                                                                                                 |
| `canCalcSizes` | If set, the importer can calculate the disk space used by a clip during imCalcSize.<br/><br/>An importer should support this call if it uses a tree of files represented as one top-level file to Premiere. |
| `canTrim`      | If set, the importer can trim files during imTrimFile.                                                                                                                                                      |
| `canCopy`      | Set this to true if the importer supports copying clips in the Project Manager.                                                                                                                             |

### Setup Flags

|     Member      |                                                                 Description                                                                 |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `hasSetup`      | If set, the importer has a setup dialog. The dialog should be presented in response to `imGetPrefs`                                         |
| `setupOnDblClk` | If set, the setup dialog should be opened whenever the user double clicks on a file imported by the plugin the timeline or the project bin. |

### Memory Handling Flags

|    Member    |                                                               Description                                                               |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| `dontCache`  | Unused.                                                                                                                                 |
| `keepLoaded` | If set, the importer plugin should never be unloaded.<br/><br/>Don't set this flag unless it's absolutely necessary (it usually isn't). |

### Other

|           Member            |                                                                                                                                                                                            Description                                                                                                                                                                                             |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `priority`                  | Determines priority levels for importers that handle the same filetype.<br/><br/>Importers with higher numbers will override importers with lower numbers.<br/><br/>For overriding importers that ship with Premiere, use a value of 100 or greater.<br/><br/>Higher-priority importers can defer files to lower-priority importers by returning `imBadFile` during `imOpenFile8` or `imGetInfo8`. |
| `importType`                | Type identifier for the import module assigned based on the plugin's IMPT resource.<br/><br/>Do not modify this field.                                                                                                                                                                                                                                                                             |
| `canProvideClosedCaptions`  | New in Premiere Pro CC. Set this to true if the importer supports media with embedded closed captioning.                                                                                                                                                                                                                                                                                           |
| `avoidAudioConform`         | Set this to true if the importer supports fast audio retrieval and does not need the audio clips it imports to be conformed.                                                                                                                                                                                                                                                                       |
| `canProvidePeakAudio`       | New in Premiere Pro CS5.5. Set this to true if your non-synthetic importer wants to provide **peak audio data** using `imGetPeakAudio`.                                                                                                                                                                                                                                                            |
| `acceleratorFileExt`        | Fill this prUTF16Char array of size 256 with the file extensions of accelerator files that the importer creates and uses.                                                                                                                                                                                                                                                                          |
| `canSupplyMetadataClipName` | Allows file based importer to set clip name from metadata.<br/><br/>Set this in `imFileInfoRec8.streamName`.                                                                                                                                                                                                                                                                                       |
| `canProvideFileList`        | New in CS6. Set this to true if the importer will provide a list of all files for a copy operation in response to `imQueryInputFileList`.                                                                                                                                                                                                                                                          |
| `fileInfoVersion`           | New in CC 2014. This is used by an optimization in an internal importer. Do not use.                                                                                                                                                                                                                                                                                                               |

### Unused (in imImportInfoRec)

|     Member     | Description |
| -------------- | ----------- |
| `canResize`    |             |
| `canDoSubsize` |             |
| `canAsync`     |             |

---

## imIndFormatRec

Selector: [imGetIndFormat](selector-descriptions.md#imgetindformat)

Describes the format(s) supported by the importer. Synthetic files can only have one format.

```cpp
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
```

|                Member                |                                                                                                              Description                                                                                                              |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `filetype`                           | Unique four character code (fourcc) of the file.                                                                                                                                                                                      |
| `flags`                              | Legacy mechanism for describing the importer capabilities.<br/><br/>Though the flags will still be honored for backward compatability, current and future importers should not use these flags.<br/><br/>See table below for details. |
| `canWriteTimecode`                   | If set, timecode can be written for this filetype.                                                                                                                                                                                    |
| `FormatName[256]`                    | The descriptive importer name.                                                                                                                                                                                                        |
| `FormatShortName[256]`               | The short name for the plugin, appears in the format menu.                                                                                                                                                                            |
| `PlatformExtension[256]`             | List of all the file extensions supported by this importer.<br/><br/>If there's more than one, separate with null characters.                                                                                                         |
| `hasAlternateTypes`                  | Unused                                                                                                                                                                                                                                |
| `alternateTypes[kMaxAlternateTypes]` | Unused                                                                                                                                                                                                                                |
| `canWriteMetaData`                   | New in 6.0. If set, imSetMetaData is supported for the filetype                                                                                                                                                                       |

The flags listed below are only for legacy plugins and should not be used.

|        Member        |                                                                       Description                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Flag                 | Usage                                                                                                                                                   |
| `xfIsMovie`          | Unused                                                                                                                                                  |
| `xfCanReplace`       | Unused                                                                                                                                                  |
| `xfCanOpen`          | Unused: Use `imImportInfoRec.canOpen` instead.                                                                                                          |
| `xfCanImport`        | Unused: The PiPL resource describes the file as an importer.                                                                                            |
| `xfIsStill`          | Indicates that the importer handles still images.                                                                                                       |
| `xfIsSound`          | Unused: Use `imFileInfoRec.hasAudio` instead.                                                                                                           |
| `xfCanWriteTimecode` | If set, the importer can respond to `imGetTimecode` and `imSetTimecode`.<br/><br/>Obsolete: use `imIndFormatRec.canWriteTimecode` instead.              |
| `xfCanWriteMetaData` | Writes (and reads) metadata, specific to the importer's four character code filetype.<br/><br/>Obsolete: use `imIndFormatRec.canWriteMetaData` instead. |
| `xfCantBatchProcess` | Unused                                                                                                                                                  |

---

## imIndPixelFormatRec

Selector: [imGetIndPixelFormat](selector-descriptions.md#imgetindpixelformat)

Describes the pixel format(s) supported by the importer.

```cpp
typedef struct {
  void           *privatedata;
  PrPixelFormat  outPixelFormat;
  const void*    prefs;
} imIndPixelFormatRec;
```

|      Member      |                                    Description                                     |
| ---------------- | ---------------------------------------------------------------------------------- |
| `privatedata`    | Instance data from `imGetInfo8` or `imGetPrefs8`.                                  |
| `outPixelFormat` | One of the pixel formats supported by the importer                                 |
| `prefs`          | New in CC. Clip Source Settings data gathered during `imGetPrefs8` (setup dialog). |

---

## imInitiateAsyncClosedCaptionScanRec

Selector: [imInitiateAsyncClosedCaptionScan](selector-descriptions.md#iminitiateasyncclosedcaptionscan)

Both `imGetNextClosedCaption` and `imCompleteAsyncClosedCaptionScan` may be called from a different thread from which imInitiateAsyncClosedCaptionScan was originally called.

To help facilitate this, outAsyncCaptionScanPrivateData can be allocated by the importer to be used for the upcoming closed caption scan calls, which should then be deallocated in `imCompleteAsyncClosedCaptionScan`.

The estimated duration of all the closed captions can also be filled in.

This is useful for certain cases where the embedded captions contain many frames of empty data.

```cpp
typedef struct {
  void*        privatedata;
  void*        prefs;
  void*        outAsyncCaptionScanPrivateData;
  csSDK_int64  outScale;
  csSDK_int64  outSampleSize;
  csSDK_int64  outEstimatedDuration;
} imInitiateAsyncClosedCaptionScanRec;
```

|              Member              |                                           Description                                           |
| -------------------------------- | ----------------------------------------------------------------------------------------------- |
| `privatedata`                    | Instance data gathered during `imGetInfo8` or `imGetPrefs8`.                                    |
| `prefs`                          | Clip Source Settings data gathered during `imGetPrefs8` (setup dialog).                         |
| `outAsyncCaptionScanPrivateData` | The importer can allocate instance data for this closed caption scan, and pass it back here.    |
| `outScale`                       | New in CC October 2013. The frame rate of the video clip, represented as scale over sampleSize. |
| `outSampleSize`                  |                                                                                                 |
| `outEstimatedDuration`           | New in CC October 2013. The estimated duration of all the captions, in the above timescale      |

---

## imMetaDataRec

Selector: [imGetMetaData](selector-descriptions.md#imgetmetadata) and [imSetMetaData](selector-descriptions.md#imsetmetadata)

Describes the metadata specific to a given four character code.

```cpp
typedef struct {
  void          *privatedata;
  void          *prefs;
  csSDK_int32   fourCC;
  csSDK_uint32  buffersize;
  char          *buffer;
} imMetaDataRec;
```

|    Member     |                               Description                               |
| ------------- | ----------------------------------------------------------------------- |
| `privatedata` | Instance data gathered during `imGetInfo8` or `imGetPrefs8`.            |
| `prefs`       | Clip Source Settings data gathered during `imGetPrefs8` (setup dialog). |
| `fourcc`      | Fourcc code of the metadata chunk.                                      |
| `buffersize`  | `Size` of the data in buffer.                                           |
| `buffer`      | The metadata.                                                           |

---

## imPeakAudioRec

Selector: [imGetPeakAudio](selector-descriptions.md#imgetpeakaudio)

Describes the peak values of the audio at the specified position.

```cpp
typedef struct {
  void           *inPrivateData;
  void           *inPrefs;
  PrAudioSample  inPosition;
  float          inSampleRate;
  csSDK_int32    inNumSampleFrames;
  float          **outMaxima;
  float          **outMinima;
} imPeakAudioRec;
```

|       Member        |                           Description                           |
| ------------------- | --------------------------------------------------------------- |
| `inPrivateData`     | Instance data gathered during `imGetInfo8` or `imGetPrefs8`.    |
| `inPrefs`           | Instance data gathered during `imGetPrefs8` (setup dialog).     |
| `inPosition`        | The starting audio sample frame of the peak data.               |
| `inSampleRate`      | The sample rate at which to generate the peak data.             |
| `inNumSampleFrames` | The number of sample frames in each buffer.                     |
| `outMaxima`         | An array of arrays to be filled with the maximum sample values. |
| `outMinima`         | An array of arrays to be filled with the minimum sample values. |

---

## imPreferredFrameSizeRec

Selector: [imGetPreferredFrameSize](selector-descriptions.md#imgetpreferredframesize)

Describes a frame size preferred by the importer.

```cpp
typedef struct {
  void           *inPrivateData;
  void           *inPrefs;
  PrPixelFormat  inPixelFormat;
  csSDK_int32    inIndex;
  csSDK_int32    outWidth;
  csSDK_int32    outHeight;
} imPreferredFrameSizeRec;
```

|     Member      |                               Description                               |
| --------------- | ----------------------------------------------------------------------- |
| `inPrivateData` | Instance data gathered during `imGetInfo8` or `imGetPrefs8`.            |
| `inPrefs`       | Clip Source Settings data gathered during `imGetPrefs8` (setup dialog). |
| `inPixelFormat` | The pixel format for this preferred frame size.                         |
| `inIndex`       | The index of this preferred frame size.                                 |
| `outWidth`      | The dimensions of this preferred frame size.                            |
| `outHeight`     |                                                                         |

---

## imQueryContentStateRec

Selector: [imQueryContentState](selector-descriptions.md#imquerycontentstate)

Fill in the outContentStateID, which should be a GUID calculated based on the content state of the clip at inSourcePath.

If the state hasn't changed since the last call, the GUID returned should be the same.

```cpp
typedef struct {
  const prUTF16Char*  inSourcePath;
  prPluginID          outContentStateID;
} imQueryContentStateRec;
```

---

## imQueryDestinationPathRec

Selector: [imQueryDestinationPath](selector-descriptions.md#imquerydestinationpath)

Fill in the desired `outActualDestinationPath`, based on the `inSourcePath` and `inSuggestedDestinationPath`.

```cpp
typedef struct {
  void               *inPrivateData;
  void               *inPrefs;
  const prUTF16Char  *inSourcePath;
  const prUTF16Char  *inSuggestedDestinationPath;
  prUTF16Char        *outActualDestinationPath;
} imQueryDestinationPathRec;
```

|            Member            |                                 Description                                  |
| ---------------------------- | ---------------------------------------------------------------------------- |
| `inPrivateData`              | Instance data gathered during `imGetInfo8` or `imGetPrefs8`.                 |
| `inPrefs`                    | Clip Source Settings data gathered during `imGetPrefs8` (setup dialog).      |
| `inSourcePath`               | The path of the source file to be trimmed                                    |
| `inSuggestedDestinationPath` | The path suggested by Premiere where the destination file should be created. |
| `outActualDestinationPath`   | The path where the importer wants the destination file to be created.        |

---

## imQueryInputFileListRec

Selector: [imQueryInputFileList](selector-descriptions.md#imqueryinputfilelist)

Fill in the outContentStateID, which should be a GUID calculated based on the content state of the clip at `inSourcePath`.

If the state hasn't changed since the last call, the GUID returned should be the same.

```cpp
typedef struct {
  void*        inPrivateData;
  void*        inPrefs;
  PrSDKString  inBasePath;
  csSDK_int32  outNumFilePaths;
  PrSDKString  *outFilePaths;
} imQueryInputFileListRec;
```

|      Member       |                                                                                                                   Description                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `inPrivateData`   | Instance data gathered from `imGetInfo8` or `imGetPrefs8`.                                                                                                                                                                                       |
| `inPrefs`         | Clip Source Settings data gathered from `imGetPrefs8` (setup dialog info).                                                                                                                                                                       |
| `inBasePath`      | Path of main file that was passed earlier in `imOpenFile`.                                                                                                                                                                                       |
| `outNumFilePaths` | The first time `imQueryInputFileList` is sent, fill in the number of files that the media uses.                                                                                                                                                  |
| `outFilePaths`    | The second time `imQueryInputFileList` is sent, this will be preallocated as an array of NULL strings.<br/><br/>Use the [String Suite](../universals/sweetpea-suites.md#string-suite) to fill the array with PrSDKStrings with the actual paths. |

---

## imQueryStreamLabelRec

Selector: [imQueryStreamLabel](selector-descriptions.md#imquerystreamlabel)

New in CS6. Based on the stream ID passed in, allocate and pass back a label for the stream.

For stereoscopic importers, use the predefined labels in PrSDKStreamLabel.h.

```cpp
typedef struct {
  void          *inPrivateData;
  csSDK_int32   *inPrefs;
  csSDK_int32   inStreamIdx;
  PrSDKString*  outStreamLabel;
} imQueryStreamLabelRec;
```

|      Member      |                                             Description                                              |
| ---------------- | ---------------------------------------------------------------------------------------------------- |
| `privatedata`    | Instance data gathered from `imGetInfo8` or `imGetPrefs8`.                                           |
| `prefs`          | Clip Source Settings data gathered from `imGetPrefs8` (setup dialog info).                           |
| `inStreamIdx`    | The ID of the stream that needs to be labeled.                                                       |
| `outStreamLabel` | The stream label, allocated using the [String Suite](../universals/sweetpea-suites.md#string-suite). |

---

## imSaveFileRec8

Selector: [imSaveFile8](selector-descriptions.md#imsavefile8)

Describes the file to be saved.

```cpp
typedef struct {
  void                *privatedata;
  csSDK_int32         *prefs;
  const prUTF16Char*  sourcePath;
  const prUTF16Char*  destPath;
  char                move;
  importProgressFunc  progressCallback;
  void                *progressCallbackID;
} imSaveFileRec8;
```

|        Member        |                                                                            Description                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `privatedata`        | Instance data gathered from `imGetInfo8` or `imGetPrefs8`.                                                                                                         |
| `prefs`              | Clip Source Settings data gathered from `imGetPrefs8` (setup dialog info).                                                                                         |
| `sourcePath`         | Full path of the file to be saved.                                                                                                                                 |
| `destPath`           | Full path the file should be saved to.                                                                                                                             |
| `move`               | If non-zero, this is a move operation and the original file (the sourcePath) can be deleted after copying is complete.                                             |
| `progressCallback`   | Function to call repeatedly to provide progress and to check for cancel by user. May be a NULL pointer, so make sure the function pointer is valid before calling. |
| `progressCallbackID` | Pass to `progressCallback`.                                                                                                                                        |

---

## imSourceVideoRec

Selector: [imGetSourceVideo](selector-descriptions.md#imgetsourcevideo), `aiInitiateAsyncRead`, `aiGetFrame`

Describes the requested frame, to be passed back in outFrame.

```cpp
typedef struct {
  void              *inPrivateData;
  csSDK_int32       currentStreamIdx;
  PrTime            inFrameTime;
  imFrameFormat     *inFrameFormats;
  csSDK_int32       inNumFrameFormats;
  bool              removePulldown;
  PPixHand          *outFrame;
  void              *prefs;
  csSDK_int32       prefsSize;
  PrSDKString       selectedColorProfileName;
  PrRenderQuality   inQuality;
  imRenderContext   inRenderContext;
  PrSDKColorSpaceID   opaqueColorSpaceIdentifier;
} imSourceVideoRec;
```

|           Member           |                                                       Description                                                        |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `inPrivateData`            | Instance data gathered during `imGetInfo8` or `imGetPrefs8`.                                                             |
| `currentStreamIdx`         | New in CS6. If the clip has multiple streams (for stereoscopic video or otherwise), this ID differentiates between them. |
| `inFrameTime`              | Time of frame requested.                                                                                                 |
| `inFrameFormats`           | An array of requested frame formats, in order of preference. If NULL, then any format is acceptable.                     |
| `inNumFrameFormats`        | The number of frame formats in the `inFrameFormats`.                                                                     |
| `removePulldown`           | If true, pulldown should be removed if the pixel format supports it.                                                     |
| `outFrame`                 | Allocate memory to hold the requested frame, and pass it back here.                                                      |
| `prefs`                    | New in Premiere Pro 4.1. prefs data from `imGetPrefs8`                                                                   |
| `prefsSize`                | New in Premiere Pro 4.1. Size of prefs data.                                                                             |
| `selectedColorProfileName` | New in Premiere Pro CS5.5. A string that specifies the color profile of the imported frame.                              |
| `inQuality`                | New in Premiere Pro CC 2014.                                                                                             |
| `inQuality`                | New in Premiere Pro CC 2014.                                                                                             |
| `inQuality`                | New in Premiere Pro CC 2014.                                                                                             |

---

## imSubTypeDescriptionRec

Selector: [imGetSubTypeNames](selector-descriptions.md#imgetsubtypenames)

Added in Premiere Pro CS3. Describes the codec name associated with a given fourcc.

```cpp
typedef struct {
  csSDK_int32  subType;
  prUTF16Char  subTypeName[256];
} imSubTypeDescriptionRec;
```

---

## imTimeInfoRec8

Selector: [imGetTimeInfo8](selector-descriptions.md#imgettimeinfo8) and [imSetTimeInfo8](selector-descriptions.md#imsettimeinfo8)

Describes the timecode and timecode rate associated with a clip.

```cpp
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
```

|      Member       |                                                                                                                        Description                                                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `privatedata`     | Instance data gathered during `imGetInfo8` or `imGetPrefs8`.                                                                                                                                                                                               |
| `prefs`           | Clip Source Settings data gathered during `imGetPrefs8` (setup dialog).                                                                                                                                                                                    |
| `orgtime[18]`     | The original time in hours;minutes;seconds;frames, as captured from the source reel.<br/><br/>The use of semi-colons indicates (to Premiere) drop-frame timecode, e.g. "00;00;00;00".<br/><br/>Use colons for non-drop-frame timecode, e.g. "00:00:00:00". |
| `orgScale`        | Timebase of the timecode in orgtime, represented as scale over sampleSize.                                                                                                                                                                                 |
| `orgSampleSize`   |                                                                                                                                                                                                                                                            |
| `alttime[18]`     | An alternative timecode (may differ from the source timecode), formatted as described above.                                                                                                                                                               |
| `altScale`        | Timebase of the timecode in alttime.                                                                                                                                                                                                                       |
| `altSampleSize`   |                                                                                                                                                                                                                                                            |
| `orgreel[40]`     | Original reel name.                                                                                                                                                                                                                                        |
| `altreel[40]`     | Alternate reel name.                                                                                                                                                                                                                                       |
| `logcomment[256]` | Comment string.                                                                                                                                                                                                                                            |
| `dataType`        | Currently always set to 1, denoting SMPTE timecode. More values may be added in the future.                                                                                                                                                                |

---

## imTrimFileRec8

Selector: [imTrimFile8](selector-descriptions.md#imtrimfile8)

Describes how to trim a clip, based on information returned by the importer during `imCheckTrim8`.

Also provides a callback to update the progress bar and check if the user has cancelled.

```cpp
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
```

|        Member        |                                                                                           Description                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `privatedata`        | Instance data gathered during `imGetInfo8` or `imGetPrefs8`.                                                                                                                                     |
| `prefs`              | Clip settings data gathered during `imGetPrefs8` (setup dialog).                                                                                                                                 |
| `trimIn`             | In point of the trimmed clip, in the timebase specified by scale and sampleSize.                                                                                                                 |
| `duration`           | Duration of the trimmed clip. If 0, then the request is to leave the clip untrimmed, and at the current duration                                                                                 |
| `keepAudio`          | If non-zero, the request is to keep the audio in the trimmed result.                                                                                                                             |
| `keepVideo`          | If non-zero, the request is to keep the video in the trimmed result.                                                                                                                             |
| `destFilePath`       | The unicode path and name of the file to create.                                                                                                                                                 |
| `scale`              | The frame rate of the video, represented as scale over sampleSize.                                                                                                                               |
| `sampleSize`         |                                                                                                                                                                                                  |
| `progressCallback`   | `importProgressFunc` callback to call repeatedly to provide progress and to check for cancel by user.<br/><br/>May be a NULL pointer, so make sure the function pointer is valid before calling. |
| `progressCallbackID` | Pass to `progressCallback`.                                                                                                                                                                      |

---

## imIndColorSpaceRec

Selector: [imGetIndColorSpace](selector-descriptions.md#imgetindcolorspace)

Describes the colorspace of the media.

```cpp
typedef ColorSpaceRec imIndColorSpaceRec;

typedef struct {
  void                 *privatedata;
  PrSDKColorSpaceType  outColorSpaceType;
  RawColorProfileRec   ioProfileRec;
  prSEIColorCodesRec   outSEICodesRec;
} ColorSpaceRec;
```

+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|       Member        |                                                                                                        Description                                                                                                         |
+=====================+============================================================================================================================================================================================================================+
| `privatedata`       | Private.                                                                                                                                                                                                                   |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `outColorSpaceType` | One of the following:                                                                                                                                                                                                      |
|                     |                                                                                                                                                                                                                            |
|                     | - `kPrSDKColorSpaceType_Undefined`                                                                                                                                                                                         |
|                     | - `kPrSDKColorSpaceType_ICC`                                                                                                                                                                                               |
|                     | - `kPrSDKColorSpaceType_LUT` // DO NOT USE after 14.x.                                                                                                                                                                     |
|                     | - `kPrSDKColorSpaceType_SEITags`                                                                                                                                                                                           |
|                     | - `kPrSDKColorSpaceType_MXFTags` // DO NOT USE, Not supported.                                                                                                                                                             |
|                     | - `kPrSDKColorSpaceType_Predefined`                                                                                                                                                                                        |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `ioProfileRec`      | A structure describing the color profile.                                                                                                                                                                                  |
|                     |                                                                                                                                                                                                                            |
|                     | <pre lang="cpp">csSDK_int32  ioBufferSize;<br/>void*        inDestinationBuffer;<br/>PrSDKString  outName;</pre>                                                                                                           |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `outSEICodesRec`    | A structure describing the color space using codes; used with H.265, HEVC, AVC and ProRes media.                                                                                                                           |
|                     |                                                                                                                                                                                                                            |
|                     | <pre lang="cpp">csSDK_int32  colorPrimariesCode;<br/>csSDK_int32  transferCharacteristicCode;<br/>csSDK_int32  matrixEquationsCode;<br/>csSDK_int32  bitDepth;<br/>prBool       isFullRange;<br/>prBool       isRGB;</pre> |
+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

## RawColorSpaceRec

Selector: `imGetIndColorSpace`

Describes the colorspace in use with the media.

```cpp
typedef struct
{
        PrSDKColorSpaceType           colorSpaceType;
        RawColorProfileRec            profileRec;   // for ICC and Predefined Color Spaces
        prSEIColorCodesRec            seiCodesRec;  // H-265 codes for HEVC, AVC, ProRes
} RawColorSpaceRec;
```

+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      Member      |                                                                                                        Description                                                                                                         |
+==================+============================================================================================================================================================================================================================+
| `colorSpaceType` | One of the following:                                                                                                                                                                                                      |
|                  |                                                                                                                                                                                                                            |
|                  | - `kPrSDKColorSpaceType_Undefined`                                                                                                                                                                                         |
|                  | - `kPrSDKColorSpaceType_ICC`                                                                                                                                                                                               |
|                  | - `kPrSDKColorSpaceType_LUT` // DO NOT USE after 14.x.                                                                                                                                                                     |
|                  | - `kPrSDKColorSpaceType_SEITags`                                                                                                                                                                                           |
|                  | - `kPrSDKColorSpaceType_MXFTags` // DO NOT USE, Not supported.                                                                                                                                                             |
|                  | - `kPrSDKColorSpaceType_Predefined`                                                                                                                                                                                        |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `profileRec`     | A structure describing the color space.                                                                                                                                                                                    |
|                  |                                                                                                                                                                                                                            |
|                  | <pre lang="cpp">csSDK_int32  ioBufferSize;<br/>void*        inDestinationBuffer;<br/>PrSDKString  outName;</pre>                                                                                                           |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `seiCodesRec`    | A structure describing the color space; used with H.265, HEVC, AVC and ProRes media.                                                                                                                                       |
|                  |                                                                                                                                                                                                                            |
|                  | <pre lang="cpp">csSDK_int32  colorPrimariesCode;<br/>csSDK_int32  transferCharacteristicCode;<br/>csSDK_int32  matrixEquationsCode;<br/>csSDK_int32  bitDepth;<br/>prBool       isFullRange;<br/>prBool       isRGB;</pre> |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Colorspace can be described via multiple way, type depends on `colorSpaceType`.

If type is `kPrSDKColorSpaceType_Predefined` - Color space is specified via predefined strings from `PrSDKColorSpaces.h`.

If type is `kPrSDKColorSpaceType_ICC` - Color space is specified via ICC profile in `profileRec`.

If type is `kPrSDKColorSpaceType_SEITags` - Color space is specified via enums codes for color primaries (C), transfer characteristic (T),  matrix equation (M). Supported C-T-M enums are defined in `PrSDKColorSEICodes.h`.

---

## EmbeddedLUTRec

Selector: `imGetIndColorSpace`

Describes the LUT embedded with in the media.

```cpp
typedef struct
{
  void*               privateData;
  RawColorProfileRec  lutBlobRec;
  RawColorSpaceRec    lutInColorSpaceRec;
  RawColorSpaceRec    lutOutColorSpaceRec;
} EmbeddedLUTRec;
```

|        Member         |               Description                |
| --------------------- | ---------------------------------------- |
| `privatedata`         | Private.                                 |
| `lutBlobRec`          | Describes the embedded LUT.              |
| `lutInColorSpaceRec`  | Describes the LUT input colorspace rec.  |
| `lutOutColorSpaceRec` | Describes the LUT output colorspace rec. |

---

## imRenderContext

Selector: [imGetSourceVideo](selector-descriptions.md#imgetsourcevideo) (member of [imSourceVideoRec](#imsourcevideorec))

Describes the context of the render; why it's occurring, and what rate and ratio is in use.

```cpp
typedef struct
{
  imRenderIntent inIntent;
  double inPlaybackRatio;
  double inPlaybackRate;
} imRenderContext;
```

+-------------------+---------------------------------------------------------------------------+
|      Member       |                                Description                                |
+===================+===========================================================================+
| `inIntent`        | The intent of the render being requested.                                 |
|                   |                                                                           |
|                   | - `imRenderIntent_Unknown` (-1)                                           |
|                   | - `imRenderIntent_Export` 0                                               |
|                   | - `imRenderIntent_Stopped` // DO NOT USE after 14.x.                      |
|                   | - `imRenderIntent_Scrubbing`                                              |
|                   | - `imRenderIntent_Preroll`                                                |
|                   | - `imRenderIntent_Playing`                                                |
|                   | - `imRenderIntent_SpeculativePrefetch`                                    |
|                   | - `imRenderIntent_Thumbnail` // DO NOT USE after 14.x.                    |
|                   | - `imRenderIntent_Analysis`                                               |
|                   | - `imRenderIntent_ExportPreview`                                          |
|                   | - `imRenderIntent_ExportProxies`                                          |
+-------------------+---------------------------------------------------------------------------+
| `inPlaybackRatio` | `1.0` means full framerate, lower values indicate deteriorating playback. |
+-------------------+---------------------------------------------------------------------------+
| `inPlaybackRate`  | `1.0` means 1x forward, `-1.0` means 1x backward.                         |
+-------------------+---------------------------------------------------------------------------+
