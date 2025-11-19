# What's New

## What's New in Premiere Pro CC 2019 (13.0)

We've begun adding colorspace support to Premiere Pro's APIs, beginning with Importers.

Adding APIs `AddFrameToCacheWithColorSpace()` and `GetFrameFromCacheWithColorSpace()` which will deprecate `AddFrameToCacheWithColorProfile2()` and `GetFrameFromCacheWithColorProfile2()`.

---

## What's New in Premiere Pro CC 2014

Importers can now choose the format they are rendering in, which allows importers to change pixel formats and quality based on criteria like enabled hardware and other Clip Source Settings, such as HDR. To handle the negotiation, implement `imSelectClipFrameDescriptor`.

`imSourceVideoRec` now includes a quality attribute. [PPix Cache Suite](../universals/sweetpea-suites.md#ppix-cache-suite) is now at version 6, adding `AddFrameToCacheWithColorProfile2()` and `GetFrameFromCacheWithColorProfile2()`, which are the same as the ones added in version 5 with the addition of a PrRenderQuality parameter.

`imFileInfoRec8.highMemUsage` is no longer supported.

---

## What's New in Premiere Pro CC October 2013 release?

`imInitiateAsyncClosedCaptionScanRec` now provides extra fields for the importer to fill in the estimated duration of all the captions. This is useful for certain cases where the embedded captions contain many frames of empty data.

---

## What's New in Premiere Pro CC?

Starting in CC, importers can support closed captioning that is embedded in the source media. Note that Premiere Pro can also import and export captions in a sidecar file (e.g. .mcc, .scc, or

.xml) alongside any media file, regardless of the media file format. This does not require any specific work on the importer side. The importer only needs to add support if it will support embedded closed captions.

Importers can now support audio beyond basic mono, stereo, and 5.1, without implementing multiple streams (existing importers do not need to be updated). The importer specifies a channel layout by implementing the new `imGetAudioChannelLayout` selector. Otherwise the channel layout will be assumed to be discrete.

The clip preferences are now passed with `imIndPixelFormatRec`, so that an importer can choose to return varying pixel formats depending on the Clip Source Settings.

---

## What's New in Premiere Pro CS6.0.2?

This release adds more support for growing files by adding a new flag, `imFileInfoRec8.mayBeGrowing`.

---

## What's New in Premiere Pro CS6?

Importers can now bring in stereoscopic footage as a single clip with separate left and right channels.

With some additional work, importers can now support growing files. The refresh rate for growing files is set by the user in Preferences > Media > Growing Files. The importer should get the refresh rate using the new call `GetGrowingFileRefreshInterval()` in the Importer File Manager Suite. Call `RefreshFileAsync()` to refresh the file.

A new selector, `imQueryInputFileList`, was added to support Collect Files in After Effects for file types that use more than a single file. In imImportInfoRec, a new member, `canProvideFileList`, specifies whether the importer can provide a list of all files for a copy operation. If the importer does not implement this selector, the host will assume the media just uses a single file at the original imported media path.

The Media Accelerator Suite is now at version 4. `FindPathInDatabaseAndValidateContentState` provides a new way to find existing media accelerators, making sure they are up-to-date.

Importers can now choose whether or not they want to provide peak audio data on a clip-by-clip basis.

The importer-wide setting still remains in `imImportInfoRec.canProvidePeakAudio`, but an importer can override the general setting by setting `imFileInfoRec8.canProvidePeakAudio` appropriately.

---

## What's New in Premiere Pro CS5.5?

Importers can now support color management, when running in After Effects. The importer should set `imImageInfoRec.colorProfileSupport` to `imColorProfileSupport_Fixed`, and then describe the color profiles supported by the clip using the new `imGetIndColorProfile` selector. When importing the frame, specify the color profile in `imSourceVideoRec. selectedColorProfileName`. The [PPix Cache Suite](../universals/sweetpea-suites.md#ppix-cache-suite) has been updated to differentiate between color profiles as well.

New `canProvidePeakAudio` flag to allow an importer to provide peak audio data by responding to `imGetPeakAudio`.

The new return value, `imRequiresProtectedContent`, allows an importer to be disabled if a library it depends on has not been activated.

---

## What's New in Premiere Pro CS5?

When an importer's settings dialog is opened, the importer now has access to the resolution, pixel aspect ratio, timebase, and audio sample rate of the source clip, in `imGetPrefsRec`.

Custom importers can now use a new call in the Importer File Manager Suite, `RefreshFileAsync()`, to be able to update a clip after it is modified in `imGetPrefs8`.

Two new selectors have been added.

- `imQueryDestinationPath` allows importers that trim or copy files to be able to change the destination path of the trimmed or copy file.
- `imQueryContentState` gives the host an alternate way of checking the state of a clip, for clips that have multiple source files.

A new return value, `inFileNotAvailable` can be returned from `imQueryContentState` if the clip is no longer available because it is offline or has been deleted.

As a convenience, when a file is opened, an importer can tell Premiere Pro how much memory to reserve for the importer's usage, rather than calling ReserveMemory in the [Memory Manager Suite](../universals/sweetpea-suites.md#memory-manager-suite). The importer should pass back this value in `imFileOpenRec8.outExtraMemoryUsage`.

Several new return values are available for more descriptive error reporting:

- `imBadHeader`,
- `imUnsupportedCompression`,
- `imFileOpenFailed`,
- `imFileHasNoImportableStreams`,
- `imFileReadFailed`,
- `imUnsupportedAudioFormat`,
- `imUnsupportedVideoBitDepth`,
- `imDecompressionError`, and
- `imInvalidPreferences`

---

## What's New in Premiere Pro CS4?

For CS4 only, importers are loaded and called from a separate process. As a result of being in a separate process, (1) all importers must do their own file handling, (2) privateData is no

longer accessible from `imGetPrefs8`, and (3) the compressed frame selectors such as `imGetCompressedFrame` are no longer supported (this may now be achieved using custom pixel formats and a renderer plugin).

To debug importers, attach to the `ImporterProcessServer` process. There is also a separate Importer Process Plugin Loading.log.

All legacy selectors have been removed, and are now longer supported. All structures used only in these legacy selectors have been removed as well.

There are built-in XMP metadata handlers for known filetypes. These handlers write and read metadata to and from the file, without going through the importer. `imSetTimeInfo8` is no longer called, since this is set by the XMP handler for that filetype.

All file-based importers (which does not include synthetics) are required to do their own file handling now, rather than having Premiere Pro open the files. The `imCallbackFuncs`: `OpenFileFunc` and `ReleaseFileFunc` are no longer supported.

Due to the out-of-process importing, `privateData` is not accessible during `imGetPrefs8`, and has been removed from `imGetPrefsRec`.

`imGetFrameInfo`, `imDisposeFrameInfo`, `imGetCompressedFrame`, and `imDisposeCompressedFrame` are no longer supported. Supporting a custom pixel format in an importer, a renderer, and an exporter is the new way to implement smart rendering, by passing custom compressed data from input to output.

New `imFrameNotFound` return code. Returned if an importer could not find the requested frame (typically used with async importers).

New in Premiere Pro 4.1, importer prefs are now part of imSourceVideoRec, passed to both `imGetSourceVideo` and the async import calls

New in Premiere Pro 4.1, there is a new filepath member in imFileInfoRec8. For clips that have audio in files separate from the video file, set the filename here, so that UMIDs can properly be generated for AAFs.

---

## What's New in Premiere Pro CS3?

Importers can specify an initial poster frame for a clip in imImageInfoRec.

Importers can specify subtype names during the new `imGetSubTypeNames` selector. This selector is sent after each `imGetIndFormat`, which gives an importer the opportunity to enumerate all the fourCCs and display names (e.g. "Cinepak") of their known compression types for a specific filetype. The importer can return imUnsupported, or create an array of `imSubTypeDescriptionRec` records (pairs of fourCCs and codec name strings) for all the codecs/subtypes it knows about.

Importers that open their own files should specify how many files they keep open between `imOpenFile8` and `imQuietFile` using the new Importer File Manager Suite, if the number is not equal to one. Importers that don't open their own files, or importers that only open a single file should not use this suite. Premiere's File Manager now keeps track of the number of files held open by importers, and limits the number open at a time by closing the least recently used files when too many are open. On Windows, this helps memory usage, but on MacOS this addresses a whole class of bugs that may occur when too many files are open.

Importers can also specify that certain files have very high memory usage, by setting `imFileInfoRec8.highMemUsage`. The number of files allowed to be open with this flag set to true is currently capped at 5.

Importers can now specify an arbitrary matte color for premultiplied alpha channels in `imImageInfoRec.matteColor`. Importers can state that they are uncertain about a clip's pixel aspect ratio, field type, or alpha info in imImageInfoRec.interpretationUncertain.

The imInvalidHandleValue is now -1 for MacOS.

Importers can specify a transform matrix for frames by setting `imImageInfoRec.canTransform = kPrTrue`, and then during `imImportImage`, when `imImportImageRec.applyTransform` is non-zero, use `imImportImageRec.transform`, and `destClipRect` to calculate the transform - This code path is currently not called by Premiere Pro. After Effects uses this call to import Flash video.

New in Premiere Pro 3.1, the new capability flag, `imImportInfoRec.canSupplyMetadataClipName`, allows an importer to set the clip name from metadata, rather than the filename. The clip name should be set in `imFileInfoRec8.streamName`. This is useful for clips recorded by some new file-based cameras.

New in Premiere Pro 3.1, the new `imGetFileAttributes` selector allows an importer to provide the clip creation date in the new imFileAttributesRec.
