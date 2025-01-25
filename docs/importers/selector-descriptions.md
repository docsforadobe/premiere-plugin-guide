# Selector Descriptions

This section provides a brief overview of each selector and highlights implementation issues.

Additional implementation details are at the end of the chapter.

## imInit

- param1 - [imImportInfoRec\*](structure-descriptions.md#importers-structure-descriptions-imimportinforec)
- param2 - `unused`

Sent during application startup.

Describe the importer’s capabilities in the imImportInfoRec; all options are false by default.

The similarly named flags in imIndFormatRec.flags are obsolete and should not be used.

Set hasSetup to kPrTrue if the importer has a setup dialog, and setupOnDblClk to kPrTrue to have that dialog display when the user double-clicks a file in the Project Panel; Premiere throws away any preview files generated for a file imported with this setting, even if no setup dialog is displayed.

Return imIsCacheable from *imInit* if a plugin does not need to be called to initialize every time Premiere launched.

This will help reduce the time to launch the application.

### Synthetic Importers

Setting `noFile` to `kPrTrue` indicates that the importer is synthetic.

Set `addToMenu` to `kPrTrue` to add the importer to the File > New menu.

### Custom Importers

To create a custom importer, the following capabilities must be set.

See Additional Details for more info on custom importers.

```cpp
noFile    = kPrTrue;
hasSetup  = kPrTrue;
canOpen   = kPrTrue;
canCreate = kPrTrue;
addToMenu = imMenuNew;
```

---

## imShutdown

- param1 - `unused`
- param2 - `unused`

Release all resources and perform any other necessary clean-up; sent when Premiere quits.

---

## imGetIndFormat

- param1 - `(int) index`
- param2 - [imIndFormatRec\*](structure-descriptions.md#importers-structure-descriptions-imindformatrec)

Sent repeatedly, immediately after imInit; enumerate the filetypes the plugin supports by populating the imIndFormatRec.

When finished, return imBadFormatIndex.

imIndFormatRec.flags are obsolete and should not be used.

### Synthetic Importer selectors

Because they have no file, synthetic importers only need to respond with the filetype established in their resource.

Create a separate plugin for each synthetic file type.

---

## imGetSupports8

- param1 - `unused`
- param2 - `unused`

A plugin that supports the Premiere Pro 2.0 API (and beyond) must return `malSupports8`.

---

## imGetSupports7

- param1 - `unused`
- param2 - `unused`

A plugin that supports the Premiere Pro 1.0 API (and beyond) must return `malSupports7`.

---

## imGetInfo8

- param1 - [imFileAccessRec8\*](structure-descriptions.md#importers-structure-descriptions-imfileaccessrec8)
- param2 - [imFileInfoRec8\*](structure-descriptions.md#importers-structure-descriptions-imfileinforec8)

Describe a clip, or a single stream of a clip if the clip has multiple streams.

Called when a specific file is instantiated.

Importer checks file validity, optionally allocates file instance data, and describes the properties of the file being imported by populating the imFileInfoRec8.

### Synthetic Importers

You can create a still frame, a movie of a set duration, or an ‘infinite’ length movie, but cannot change the properties of a synthetic file once imported.

---

## imCloseFile

- param1 - [imFileRef\*](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - `(void*) PrivateData**`

The specified file is no longer required; dispose of `privateData`.

Only sent if privateData was allocated during `imGetInfo8`.

---

## imGetIndPixelFormat

- param1 - `(int) index`
- param2 - [imIndPixelFormatRec\*](structure-descriptions.md#importers-structure-descriptions-imindpixelformatrec)

New optional selector called to enumerate the pixel formats available for a specific file.

This message will be sent repeatedly until all formats have been returned.

Pixel formats should be returned in the preferred order that the importer supports.

The Importer should return imBadFormatIndex after all formats have been enumerated.

imUnsupported should be returned on the first call if only *yawn* BGRA_4444_8u is supported.

What pixel formats should you support? Keep it real.

Just return the pixel format that most closely matches the data stored in your file.

If decoding to two or more formats can be done at about the same speed, declare support for both, but favor any pixel formats that are more compact, to save on memory and bandwidth.

---

## imGetPreferredFrameSize

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imPreferredFrameSizeRec\*](structure-descriptions.md#importers-structure-descriptions-impreferredframesizerec)

Provide the frame sizes preferred by the importer.

---

## imSelectClipFrameDescriptor

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imClipFrameDescriptorRec\*](structure-descriptions.md#importers-structure-descriptions-imclipframedescriptorrec)

New in Premiere Pro CC 2014.

If the importer can provide multiple formats, describe the format it will provide here.

This allows importers to change pixel formats based on criteria like enabled hardware and other source settings, such as HDR.

---

## imGetSourceVideo

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imSourceVideoRec\*](structure-descriptions.md#importers-structure-descriptions-imsourcevideorec)

Get the host an unscaled frame of video.

This selector will be sent instead of `imImportImage` if supportsGetSourceVideo is set to true during `imGetInfo8`.

---

## imCreateAsyncImporter

- param1 - [imAsyncImporterCreationRec\*](structure-descriptions.md#importers-structure-descriptions-imasyncimportercreationrec)
- param2 - `unused`

Create an asynchronous importer object using the data provided, and store it in `imAsyncImporterCreationRec`.

---

## imImportImage

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imImportImageRec\*](structure-descriptions.md#importers-structure-descriptions-imimportimagerec)

!!! note
    In most cases, `imGetSourceVideo` is the better choice.

Before going down this route, read the discussion here.

Give the host a frame of video; populate the imImportImageRec buffer with pixel data, or (if you’ve set canDraw to true during `imInit`) draw to the screen in the provided window using platform-specific calls to do so.

You must scale the image data to fit the window; Premiere relies on the import module for properly scaled frames.

---

## imImportAudio7

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imImportAudioRec7\*](structure-descriptions.md#importers-structure-descriptions-imimportaudiorec7)

Replacement for `imImportAudio` that uses new `imAudioInfoRec7`.

Called to import audio using the new 32-bit float, uninterleaved audio format.

Fill `imImportAudioRec7->buffer` with the number of sample frames specified in `imImportAudioRec7->size`, starting from `imImportAudioRec7->position`.

Always return 32-bit float, uninterleaved samples as described in [Universals](../universals/universals.md#universals-universals).

You may use the calls in the [Audio Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-audio-suite) to do some common conversions.

---

## imGetPrefs8

- param1 - [imFileAccessRec8\*](structure-descriptions.md#importers-structure-descriptions-imfileaccessrec8)
- param2 - [imGetPrefsRec\*](structure-descriptions.md#importers-structure-descriptions-imgetprefsrec)

Only sent if clip filetype uses a setup dialog within Premiere.

Premiere sends this selector when the user imports (or creates, if synthetic) a file of your type, or when double-clicking on an existing clip.

You must have set `hasSetup = true` during `imInit` to receive this selector.

Storing preferences is a two step process.

If the pointer in `imGetPrefsRec.prefs` is `NULL`, set prefsLength to the size of your preferences structure and return `imNoErr`.

Premiere sends `imGetPrefs` again; display your dialog, and pass the preferences pointer back in `imGetPrefsRec.prefs`.

Starting in Premiere Pro 1.5, the importer can get a frame from the timeline beneath the current clip or timeline location.

This is useful for titler plugins.

Use the `getPreviewFrameEx` callback with the time given by `TDB_TimeRecord` `tdbTimelocation` in `imGetPrefsRec`.

### Synthetic Importers

Synthetic importers can specify the displayable name by changing the `newfilename` member of `imFileAccessRec8`.

The first time this selector is sent, the `imGetPrefsRec.timelineData`, though non-null, contains garbage and should not be used.

It will only contain valid information once the user has put the clip into the timeline, and is double-clicking on it.

### Custom Importers

Custom importers should return imSetFile after successfully creating a new file, storing the file access information in imFileAccessRec8.

Premiere will use this data to then ask the importer to open the file it created.

See Additional Details for more information on custom importers.

---

## imOpenFile8

- param1 - [imFileRef\*](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imFileOpenRec8\*](structure-descriptions.md#importers-structure-descriptions-imfileopenrec8)

Open a file and give Premiere its handle.

This selector is sent only if canOpen was set to true during `imInit`; do so if you generate child files, you need to have read and write access during the Premiere session, or use a custom file system.

If you respond to this selector, you must also respond to `imQuietFile` and `imCloseFile`.

You may additionally need to respond to `imDeleteFile` and `imSaveFile`; see Additional Details.

Close any child files during `imCloseFile`.

Importers that open their own files should specify how many files they keep open between `imOpenFile8` and `imQuietFile` using the new Importer File Manager Suite, if the number is not equal to one.

Importers that don’t open their own files, or importers that only open a single file should not use this suite.

Premiere’s File Manager now keeps track of the number of files held open by importers, and limits the number open at a time by closing the least recently used files when too many are open.

On Windows, this helps memory usage, but on Mac OS this addresses a whole class of bugs that may occur when too many files are open.

---

## imQuietFile

- param1 - [imFileRef\*](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - `(void*) PrivateData**`

Close the file in `imFileRef`, and release any hardware resources associated with it.

Respond to this selector only if `canOpen` was set to true during imInit.

A quieted file is closed (at the OS level), but associated privateData is maintained by Premiere.

Do not deallocate `privateData` in response to `imQuietFile`; do so during `imCloseFile`.

---

## imSaveFile8

- param1 - [imSaveFileRec8\*](structure-descriptions.md#importers-structure-descriptions-imsavefilerec8)
- param2 - `unused`

Save the file specified in `imSaveFileRec8`.

Only sent if canOpen was set to true during `imInit`.

---

## imDeleteFile

- param1 - [imDeleteFileRec\*](structure-descriptions.md#importers-structure-descriptions-imdeletefilerec)
- param2 - `unused`

Request this selector (by setting canDelete to true during `imInit`) only if you have child files or related files associated with your file.

If you have only a single file per clip you do not need to delete your own files.

Numbered still file importers do not need to respond to this selector; each file is handled individually.

---

## imCalcSize8

- param1 - [imCalcSizeRec\*](structure-descriptions.md#importers-structure-descriptions-imcalcsizerec)
- param2 - [imFileAccessRec8\*](structure-descriptions.md#importers-structure-descriptions-imfileaccessrec8)

Called before Premiere trims a clip, to get the disk size used by a clip.

This selector is called if the importer sets imImportInfoRec.canCalcSizes to non-zero.

An importer should support this call if it uses a tree of files represented as one top-level file to Premiere.

The importer should calculate either the trimmed or current size of the file and return it.

If the `trimIn` and `duration` are set to zero, Premiere is asking for the current size of the file.

If the `trimIn` and `duration` are valid values, Premiere is asking for the trimmed size.

---

## imCheckTrim8

- param1 - [imCheckTrimRec\*](structure-descriptions.md#importers-structure-descriptions-imchecktrimrec)
- param2 - [imFileAccessRec8\*](structure-descriptions.md#importers-structure-descriptions-imfileaccessrec8)

Called before Premiere trims a clip, to check if a clip can be trimmed at the specified boundaries.

`imCheckTrimRec` and `imFileAccessRec` are passed in.

The importer examines the proposed trimmed size of the file, and can change the requested in point and duration to new values if the file can only be trimmed at certain locations (for example, at GOP boundaries in MPEG files).

If the importer changes the in and duration, the new values must include all the material requested in the original trim request.

If an importer does not need to change the in and duration, it may either return imUnsupported, or imNoErr and simply not change the in/duration fields.

If the importer does not want the file trimmed (perhaps because the audio or video would be degraded if trimmed at all) it can return imCantTrim and the trim operation will fail and the file will be copied instead.

For a file with both audio and video, the selector will be sent several times.

The first time, `imCheckTrimRec` will have both `keepAudio` and `keepVideo` set to a non-zero value, and the trim boundaries will represent the entire file, and Premiere is asking if the file can be trimmed at all.

If the importer returns an error, it will not be called again.

The second time, `imCheckTrimRec` will have keepAudio set to a non-zero value, and the trim boundaries will represent the audio in and out points in the audio timebase, and Premiere is asking if the audio can be trimmed on these boundaries.

The third time, `imCheckTrimRec` will have keepVideo set to a non-zero value, and the trim boundaries will represent the video in and out points in the video timebase, and Premiere is asking if the video can be trimmed on these boundaries.

If either the video or audio boundaries extend further than the other boundaries, Premiere will trim the file at the furthest boundary.

---

## imTrimFile8

- param1 - [imFileAccessRec8\*](structure-descriptions.md#importers-structure-descriptions-imfileaccessrec8)
- param2 - [imTrimFileRec8\*](structure-descriptions.md#importers-structure-descriptions-imtrimfilerec8)

Called when Premiere trims a clip.

`imFileAccessRec8` and `imTrimFileRec8` are passed in.

`imDiskFull` or `imDiskErr` may be returned if there is an error while trimming.

The current file, inPoint, and new duration are given and a destination file path.

If a file has video and audio, the trim time is in the video’s timebase.

For audio only, the trim times are in the audio timebase.

A simple callback and `callbackID` is passed to `imTrimFile8` and `imSaveFile8` that allows plugins to query whether or not the user has cancelled the operation.

If non-zero (and they can be nil), the callback pointer should be called to check for cancellation.

The callback function will return `imProgressAbort` or `imProgressContinue`.

---

## imCopyFile

- param1 - [imCopyFileRec\*](structure-descriptions.md#importers-structure-descriptions-imcopyfilerec)
- param2 - `unused`

`imCopyFile` is sent rather than `imSaveFile` to importers that have set `imImportInfoRec` can Copy when doing a copy operation using the Project Manager.

The importer should maintain data on the original file rather than the copy when it returns from the selector.

---

## imRetargetAccelerator

- param1 - [imAcceleratorRec\*](structure-descriptions.md#importers-structure-descriptions-imacceleratorrec)
- param2 - `unused`

When the Project Manager copies media and its accelerator, this selector gives an opportunity to update the accelerator to refer to the copied media.

---

## imQueryDestinationPath

- param1 - [imQueryDestinationPathRec\*](structure-descriptions.md#importers-structure-descriptions-imquerydestinationpathrec)
- param2 - `unused`

New in CS5.

This allows the plugin to modify the path that will be used for a trimmed clip, so the trimmed project is written with the correct path.

---

## imInitiateAsyncClosedCaptionScan

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imInitiateAsyncClosedCaptionScanRec\*](structure-descriptions.md#importers-structure-descriptions-iminitiateasyncclosedcaptionscanrec)

New in CC.

Gives a chance for the importer to allocate private data to be used during the scan for any closed captions embedded in the clip.

If there are no captions, return imNoCaptions.

---

## imGetNextClosedCaption

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imGetNextClosedCaptionRec\*](structure-descriptions.md#importers-structure-descriptions-imgetnextclosedcaptionrec)

New in CC.

Called iteratively, each time asking the importer for a single closed caption embedded in the clip.

After returning the last caption, return imNoCaptions to signal the end of the scan.

---

## imCompleteAsyncClosedCaptionScan

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imCompleteAsyncClosedCaptionScanRec\*](structure-descriptions.md#importers-structure-descriptions-imcompleteasyncclosedcaptionscanrec)

New in CC.

Called to cleanup any temporary data used while getting closed captions embedded in the clip, and to see if the scan completed without error.

---

## imAnalysis

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imAnalysisRec\*](structure-descriptions.md#importers-structure-descriptions-imanalysisrec)

Provide information about the file in the imAnalysisRec; this is sent when the user views the Properties dialog for your file.

Premiere displays a dialog with information about the file, including the text you provide.

---

## imDataRateAnalysis

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imDataRateAnalysisRec\*](structure-descriptions.md#importers-structure-descriptions-imdatarateanalysisrec)

Give Premiere a data rate analysis of the file.

Sent when the user presses the Data Rate button in the Properties dialog, and is enabled only if hasDataRate was true in the imFileInfoRec returned during *imGetInfo*.

Premiere generates a data rate analysis graph from the data provided.

---

## imGetTimeInfo8

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imTimeInfoRec8\*](structure-descriptions.md#importers-structure-descriptions-imtimeinforec8)

Read any embedded timecode data in the file.

Supercedes `imGetTimeInfo`.

---

## imSetTimeInfo8

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imTimeInfoRec8\*](structure-descriptions.md#importers-structure-descriptions-imtimeinforec8)

Sent after a capture completes, where timecode was provided by the recorder or device controller.

Use this to write timecode data and timecode rate to your file.

See [Universals](../universals/universals.md#universals-universals) for more information on time in Premiere.

Supercedes `imSetTimeInfo`.

Timecode rate is important for files that have timecode, but not an implicit frame rate, or where the sampling rate might differ from the timecode rate.

For example, audio captured from a tape uses the video’s frame rate for timecode, although its sampling rate is not equal to the timecode rate.

Another example is capturing a still from tape, which could be stamped with timecode, yet not have a media frame rate.

---

## imGetFileAttributes

- param1 - [imFileAttributesRec\*](structure-descriptions.md#importers-structure-descriptions-imfileattributesrec)

Optional.

`Pass back the creation date stamp in imFileAttributesRec.`

---

## imGetMetaData

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imMetaDataRec\*](structure-descriptions.md#importers-structure-descriptions-immetadatarec)

Called to get a metadata chunk specified by a fourcc code.

If imMetaDataRec->buffer is null, the plugin should set buffersize to the required buffer size and return imNoErr.

Premiere will then call again with the appropriate buffer already allocated.

---

## imSetMetaData

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imMetaDataRec\*](structure-descriptions.md#importers-structure-descriptions-immetadatarec)

Called to add a metadata chunk specified by a fourcc code.

---

## imDeferredProcessing

- param1 - [imDeferredProcessingRec\*](structure-descriptions.md#importers-structure-descriptions-imdeferredprocessingrec)
- param2 - `unused`

Describe the current progress of the deferred processing on the clip.

---

## imGetAudioChannelLayout

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imGetAudioChannelLayoutRec\*](structure-descriptions.md#importers-structure-descriptions-imgetaudiochannellayoutrec)

New in CC.

Called to get the audio channel layout in the file.

---

## imGetPeakAudio

- param1 - [imFileRef](structure-descriptions.md#importers-structure-descriptions-imfileref)
- param2 - [imPeakAudioRec\*](structure-descriptions.md#importers-structure-descriptions-impeakaudiorec)

Optional selector allows Premiere to get audio peak data directly from the importer.

This is used for synthetic clips longer than five minutes.

Providing peak data can significantly improve waveform rendering performance when the user views audio waveform of the clip in the Source Monitor.

The values provided are `floats`, in the range 0.0 to 1.0 in amplitude. There is an array which has an array of `float *` for each audio channel the importer reported for this stream. The `float *` point to `float[inNumSampleFrames]` which needs to be filled in by the importer. The `inSampleRate` is the sample rate of the returned data; in the case that `inNumSampleFrame = 1000` and `inSampleRate = 10`, the importer would fill in 1000 min values and 1000 max values per channel, with 10 values per second of original audio.

---

## imQueryContentState

- param1 - [imQueryContentStateRec\*](structure-descriptions.md#importers-structure-descriptions-imquerycontentstaterec)
- param2 - `unused`

New in CS5.

This is used by streaming importers and folder based importers (P2, XDCAM, etc) that have multiple files that comprise the content.

If an importer doesn’t support the selector then the host checks the last modification time for the main file.

---

## imQueryStreamLabel

- param1 - [imQueryStreamLabelRec\*](structure-descriptions.md#importers-structure-descriptions-imquerystreamlabelrec)
- param2 - `unused`

New in CS6.

This is used by stereoscopic importers to specify which stream IDs represent the left and right eyes.

---

## imGetSubTypeNames

- param1 - `(csSDK_int32) fileType`
- param2 - [imSubTypeDescriptionRec\*](structure-descriptions.md#importers-structure-descriptions-imsubtypedescriptionrec)

New optional selector added for After Effects CS3.

As of CS4, this info still isn’t used in Premiere Pro, but is used in After Effects to display the codec name in the Project Panel.

The importer should fill in the codec name for the specific subtype fourcc provided.

This selector will be sent repeatedly until names for all subtypes have been requested.

The `imSubTypeDescriptionRec` must be allocated by the importer, and will be released by the plugin host.

---

## imGetIndColorProfile

- param1 - `(int) index`
- param2 - [imIndColorProfileRec\*](structure-descriptions.md#importers-structure-descriptions-imindcolorprofilerec)

Only sent if the importer has set `imImageInfoRec.colorProfileSupport` to `imColorProfileSupport_Fixed`.

This selector is sent iteratively for the importer to provide a description of each color profile supported by the clip.

After all color profiles have been described, return a non-zero value.

---

## imGetIndColorSpace

- param1 - `(int) index`
- param2 - [imIndColorSpaceRec\*](structure-descriptions.md#importers-structure-descriptions-imindcolorspacerec)

This is new selector for enumerating color spaces of media.

Only sent if the importer has set `imImageInfoRec.colorSpaceSupport` to `imColorSpaceSupport_Fixed`.

This selector is sent iteratively for the importer to provide a description of each color space supported by the clip.

After all color spaces have been described, return a non-zero value.

---

## imQueryInputFileList

- param1 - [imQueryInputFileListRec\*](structure-descriptions.md#importers-structure-descriptions-imqueryinputfilelistrec)
- param2 - `unused`

New for After Effects CS6; not used in Premiere Pro.

If an importer supports media that uses more than a single file (i.e.

a file structure with seperate files for metadata, or separate video and audio files), this is the way the importer can specify all of its source files, in order to support Collect Files in After Effects.

In `imImportInfoRec`, a new member, `canProvideFileList`, specifies whether the importer can provide a list of all files for a copy operation.

If the importer does not implement this selector, the host will assume the media just uses a single file at the original imported media path.

---

## imGetEmbeddedLUT

This is a selector for enumerating the LUTs embedded in the media.

- param1 - `(int) index`.
- param2 - [EmbeddedLUTRec\*](structure-descriptions.md#importers-structure-descriptions-embeddedlutrec)

Sent if Importer reported that it has embedded LUT. The first time it is called, the inDestinationBuffer will be NULL. Fill in the required size for the buffer, set the correct space type, and Premiere Pro will call your importer back with enough memory.
