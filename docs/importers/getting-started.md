# Getting Started

## The Basics of Import

For each clip, importers can tell Premiere Pro the resolutions and pixel formats they can decode video frames to.

Premiere will request video frames as needed during scrubbing, playback, or export.

Audio will be requested right when the clip is imported, if audio conforming or peak file generation is necessary.

If audio conforming is not necessary, audio frames will be requested as needed during scrubbing, playback, or export.

Premiere requests audio in arrays of 32-bit float, uninterleaved format.

---

## Try the Sample Importer Plugins

Choose which one of the three sample importers matches closest with your desired functionality.

Build that one, or if you are still not sure, build all three! Step through the code in your debugger to learn order of events.

Start your importer by modifying one of the SDK samples.

---

## `imGetSourceVideo` versus `imImportImage`

For synchronous import, there are two different selectors an importer can use to provide frames to the host.

Why? *imGetSourceVideo* is best for media that has specific resolutions.

Importers that support *imGetSourceVideo* can import frames at their native resolution or specify preferred resolutions, rather than having to scale the frames to an arbitrary size.

*imImportImage* is only useful for resolution-independent video, such as vector-based graphics.

Choose the one that fits the media your importer will support.

The SDK importer demonstrates *imGetSourceVideo* because resolution dependent video is much more common.

The synthetic importer sample demonstrates *imImportImage* because it generates video on-the-fly and doesn't have a preference as to video resolution.

`imImageInfoRec.supportsGetSourceVideo` should be set to true if the importer wants to support *imGetSourceVideo*.

---

## Asynchronous Import

Importers can optionally support asynchronous calls to read frames for better performance. imImageInfoRec.supportsAsyncIO should be set to true if the importer wants to support asynchronous import. The importer can implement *imCreateAsyncImporter*, which tells the importer to create an asynchronous importer object using the data provided, and store it in `imAsyncImporterCreationRec`.

This async importer object must implement a separate entry point from a standard importer because it does not follow the same rules as a standard importer.

All calls to AsyncImporterEntry are reentrant, except for the *aiClose* selector. *aiClose* will only be called once, but may be called while other calls are still executing. No calls will be made after *aiClose* is called.

Here is an overview of the lifetime of an async importer:

1. The host calls *imOpenFile* and *imGetInfo* on the standard importer.
2. The host calls *imCreateAsyncImporter* on the standard importer. At this time, the standard importer creates the private data for the async importer. The async importer MUST NOT contain a link to the standard importer, as their lifetimes are now decoupled. The async importer, therefore, must contain copies of all relevant private data from the creator importer. The importer preferences are also guaranteed to not change during the lifetime of the async importer.
3. The host uses the async importer to perform i/o.
4. The host closes the async importer, forgetting about it. This will happen whenever the app loses focus, or when the async importer is no longer needed.

---

## privateData

Don't use global variables to store data. Use privateData instead. Each clip can have its own privateData. The host application will automatically pass the correct privateData to the appropriate importer instance.

For privateData, create a handle to the custom structure you wish to store (during `imGetInfo8` or `imGetPrefs8`.) and save the handle to the privateData member of the structure passed in.

The importer is responsible for allocating and deallocating the memory for privateData using Premiere's memory functions.

Free the allocated privateData during *imCloseFile or imShutdown*, as appropriate.

---

## Clip Source Settings

This data is unique to each clip instance, and can be used to store clip-wide data that affects the appearance of video and/or audio in the clip, usually user-modifiable.

For example, Clip Source Settings for a titler/graphics importer could contain all the data describing the text and shapes for that clip.

For a raw video clip, it could contain metadata that affects how the video is developed prior to import.

Starting in Premiere Pro CC 2014, importers can now choose the format they are rendering in, which allows importers to change pixel formats and quality based on criteria like enabled hardware and other Clip Source Settings, such as HDR.

To handle the negotiation, implement `imSelectClipFrameDescriptor`.

Clip Source Settings can be shown on file creation (for synthetic or custom importers) or when a clip is double-clicked.

Settings data should be stored in a disk-safe prefs structure, which is defined by the importer.

Premiere will allocate the prefs based on the prefsLength re turned from the first call to *imGetPrefs8*.

Premiere will deallocate the prefs when it is no longer needed.

Once prefs has been allocated, the importer should show its setup dialog during all subsequent calls to *imGetPrefs8*, and store any setup dialog settings in prefs.

Like privateData, each clip has its own prefs, and the host application automatically passes the correct prefs to the appropriate importer instance.

If the user changes the Clip Source Settings in a way such that the frames should be reimported, then the importer should use the Importer File Manager Suite to call RefreshFileAsync() on the main file.

This is demonstrated in the SDK Custom Importer sample code.

### Showing a Video Preview in the Settings Dialog

If a clip is placed in the timeline, and its settings dialog is opened by double-clicking in the timeline, then the import can get frames from the timeline of the settings dialog. Only the rendered frames on layers beneath the current clip or timeline location are available. Use the `getPreviewFrameEx` callback with the time given by tdbTimelocation in imGetPrefsRec. timelineData is also valid during *imGetPrefs8*.

---

## File Handling

Basic importers that bring in media from a single file can rely on the host to provide basic file handling. If a clip has child files or a custom file system, an importer can provide its own file handling. Set canOpen, canSave, and canDelete to true during `imInit`, and respond to `imOpenFile8`, *imQuietFile*, *imCloseFile*, *imSaveFile8*, *imDeleteFile8*.

Use the [Async File Reader Suite](suites.md#async-file-reader-suite) for cross-platform file operations.

### Quieting versus Closing a File

When the application loses focus, importers receive *imQuietFile* for each file it has been asked to open. Update any PrivateData and close the file. If the project is closed, *imCloseFile* is sent, telling the importer to free any PrivateData. If the importer didn't store any PrivateData, it will not receive *imCloseFile*.

### Growing Files

When Premiere Pro attempts to refresh a growing file (after N seconds, as determined by the preferences value), it quiets the existing importer instance, and opens a new one pointing to the same file. In response, the Importer should report the current (new) duration and, once it's determined whether the file is still growing, set  `imFileInfoRec.mayBeGrowing` appropriately.

### Importing from Streaming Sources

For importing video from a streaming source, in order to pretend that the file is a local file or available on the network, create a placeholder file like video_proxy.abc.

Inside this file, include info that lets your importer know it is your own type, and the http path, like this:

"MyCompany ABC streaming format placeholder file [https://myurl.com/video.abc](https://myurl.com/video.abc)"

Your importer would open the local video_proxy.abc file, check the header and find it is your own placeholder file, and then access the real contents at the http location included. To create the local

.abc files, you could use a custom importer that presents a OS dialog to choose the remote file, or a Premiere panel to do so. The Panel SDK can be found here:

[https://github.com/Adobe-CEP/Samples/tree/master/PProPanel](https://github.com/Adobe-CEP/Samples/tree/master/PProPanel)

If the filetype is an existing filetype supported by Premiere Pro, then set a high value in `imImportInfoRec.priority` to give your importer the first opportunity to handle the file.

For your filetype to be visible in the Proxy > Attach Proxies window, set imIndFormatRec. flags |= xfIsMovie (this flag is labeled obsolete, but still needed for this case)

If your importer supports different fractional resolutions and decode qualities, the fractional resolutions can be enumerated in response to the selector *imGetPreferredFrameSize*, and the decode quality hint is sent on import requests to your importer (for example in imSourceVideoRec.inQuality).

---

## Audio Conforming and Peak File Generation

When a clip that contains audio is imported into Premiere, one or two types of files may be generated:

First, a separate .pek file is always created. This contains peak audio samples for quick access when Premiere needs to draw the audio waveform, for example in the Source Monitor or Timeline panel.

Second, the audio may be conformed into a separate .cfa file. The conformed audio is in an interleaved 32-bit floating point format that matches the sequence audio sample rate, to maximize the speed at which Premiere can render audio effects and mix it without sacrificing quality.

Both of these files can be generated through sequential calls for audio using *imImportAudio7*. Audio conforming cannot be disabled through the Premiere menus or API. However, if an importer can provide random-access, uncompressed audio of the clip, Premiere will not conform the audio. All compressed audio data must be conformed.

Specifically, it is important to set these flags to avoid conforming: imImportInfoRec.avoidAudioConform = kPrTrue; imFileInfoRec8.accessModes |= kRandomAccessImport;

Starting in CS5.5, peak audio data can also optionally be provided by the importer, if the importer implements a faster way to read the peak audio data from the clip. By setting imImportInfoRec. canProvidePeakAudio to non-zero, the importer will be sent *imGetPeakAudio* whenever this data is requested. Starting in CS6, if an importer wants to provide peak audio data on a clip-by-clip basis, it can set imFileInfoRec8.canProvidePeakData accordingly.

The location of the .cfa and .pek files is determined by the user-specified path in Edit > Preferences > Media > Media Cache Files. When the project is closed, the files will be cleaned up. If the source clip is not saved in the project, the associated conformed audio files will be deleted.

Importers can get audio for scrubbing, playing and other timeline operations before conforming has completed, resulting in responsive audio feedback during conforming. To do this, they must support both random access and sequential access audio importing. The `kSeparateSequentialAudio` access mode should be set in imFileInfoRec8.accessModes.

---

## Quality Levels

Importers can optionally support two different quality modes, with the imDraftMode flag that is used in imImportImageRec.

---

## Closed Captioning

Starting in CC, importers can support closed captioning that is embedded in the source media. The built-in QuickTime importer provides this capability.

!!! note
    Premiere Pro can also import and export captions in a sidecar file (e.g. .mcc, .scc, or .xml) alongside any media file, regardless of the media file format. This does not require any specific work on the importer side.

To support embedded closed captioning, set `imImportInfoRec.canSupportClosedCaptions` to true. The importer should handle the following selectors: `imInitiateAsyncClosedCaptionScan`, `imGetNextClosedCaption`, and *imCompleteAsyncClosedCaptionScan*.

*imInitiateAsyncClosedCaptionScan* will be called for every file that is imported through an importer that sets canSupportClosedCaptions to true. The plugin should at this point determine whether or not there is closed captioning data for this file. If not, then the plugin should simply return imNoCaptions, and everything is done. If the plugin didn't report an error for that call, then *imGetNextClosedCaption* will be called until the plugin returns imNoCaptions. After which, *imCompleteAsyncClosedCaptionScan* will be called informing the importer that the host is done requesting captions.

Both *imGetNextClosedCaption* and *imCompleteAsyncClosedCaptionScan* may be called from a different thread from which `imInitiateAsyncClosedCaptionScan` was originally called. To help facilitate this, `outAsyncCaptionScanPrivateData` during `imInitiateAsyncClosedCaptionScan` can be allocated by the importer to be used for the upcoming calls, which can be deallocated

in *imCompleteAsyncClosedCaptionScan*.

---

## N-Channel Audio

Starting in CC, for audio configurations beyond mono, stereo, and 5.1, an importer can specify a channel layout by implementing the new *imGetAudioChannelLayout* selector. Otherwise the channel layout will be assumed to be discrete. For support prior to CC, the importer needs to import them as multiple streams.

---

## Multiple Streams

Importers can support multiple streams of audio and/or video. For most filetypes with a single video and a simple audio configuration (mono, stereo, or 5.1), only a single stream is necessary. Multiple streams can be useful for stereoscopic footage, layered file types (like Photoshop PSD files), or clips with complex audio configuration (such as 4 mono audio channels). The following describes the general case of multiple streams. For stereoscopic importers, please refer to the description further down.

An importer describes each stream one-by-one during iterative calls to *imGetInfo8*. In response to each call, the importer describes one stream, and returns imIterateStreams, until it reaches the last stream, and then it returns imBadStreamIndex. Set imFileInfoRec8->streamsAsComp = kPrFalse, so that the set of streams appear as a single clip within Premiere Pro.

In *imGetInfo8*, save streamIdx in privateData, to have access to it later. That way, when called in *imImportAudio7*, the importer will know which stream of audio to pass back.

See the sample code in the SDK File Importer, which can be turned on by uncommenting back in the MULTISTREAM_AUDIO_TESTING define in SDK_File_Import.h.

### Stereoscopic Video

First, an importer must advertise multiple video streams. During *imGetInfo8*, the host passes in the stream index in imFileInfoRec8.streamIdx. If the clip has a second stream, then on index 0 the importer should return imIterateStreams and it will be called again for the second stream. On the second one you return imNoErr, as before. The nice thing is that this works in Premiere Pro CS5.5 and earlier - when two video streams are present, on import, they will just appear as two different project items.

Prior to CS6, an importer would need to have a prefs structure and on *imGetInfo8* it would need to store the stream index in that structure. With CS6 this is a lot simpler. Now, in the `imSourceVideoRec` (passed in *imGetSourceVideo*, and part of the *aiFrameRequest* for async importers), the host application passes in the currentStreamIndex (in the value formerly

known as unused1). This makes it much easier to just check when providing a PPix and differentiate the two streams.

Now, obviously, it is not desirable to have two project items. In order to get them merged, an importer needs to label the streams (the logic here is pretty simple, if there are multiple labeled video streams, it will appear as a single project item, and all views on that item will show the first stream). For this there is a new selector: *imQueryStreamLabel*. The struct passed to the importer has its privateData, prefs data, and the stream index, and the label needs to be passed back in a PrSDKString. If you're not familiar with PrSDKStringSuite, it's fairly obvious how to use. In this case you'll be allocating a string, passing either UTF-8 data, or UTF-16 data.

In PrSDKStreamLabel.h we define two labels: kPrSDK_StreamLabelStereoscopicLeft and kPrSDKStreamLabel_Stereoscopic_Right. By convention, we expect Left to be stream 0 and Right to be stream 1. This is purely for consistency - if we have multiple stereo clips from multiple importers, we would want the thumbnails to all be consistent. If we stick to this convention, then the thumbnails will all be Left.

To integrate well with other third-parties, we strongly encourage using these labels for stereoscopic importers. However, the entire StreamLabel mechanism is intentionally left quite general. You could use whatever labels you want in your importers and effects, and when you request the video segments you can pass whatever label you would like. If you have other uses for this, we would be interested to hear about them, and we would welcome any bug reports.

---

## Project Manager Support

The Project Manager in Premiere Pro allows users to archive projects, trim out unused media, or collect all source files to a single location. Importers are the most knowledgable about the sources they work with. So Premiere Pro doesn't make any assumptions about the source media, but instead relies on the importers to handle the trimming and file size estimates. Only importers that specifically support trimming will trim and not copy when the Project Manager trims projects.

To support trimming, importers will want to set the canCalcSizes and canTrim flags during *imInit*, and support *imCalcSize8*, *imCheckTrim8*, and *imTrimFile8*.

If the each clip has more than one source file (such as audio channels in separate files), the importer should also set canCopy and support *imCopyFile*. Otherwise, the Project Manager will not know about the other source files.

External files, such as textures, logos, etc. that are used by an importer instance but do not appear as footage in Project panel, should be registered with Premiere Pro using the [File Registration Suite](../universals/sweetpea-suites.md#file-registration-suite) during *imGetInfo8* or *imGetPrefs8*. Registered files will be taken into account when trimming or copying a project using the Project Manager.

---

## Creating a Custom Importer

This variant of the importer API allows importers to dynamically create disk-based media while working within Premiere. A titler plugin or similar should use this API. Once your clip is created, it is treated like any other standard file and will receive all standard missing file handling.

A Custom Importer **must** do the following:

- Set the following flags true in imImportInfoRec; canCreate, canOpen, addToMenu, noFile. This tells Premiere your plugin will create a clip on disk at *imGetPrefs8* time.
- To determine when you need to create a new clip vs. modify an existing clip, check the `imFileAccessRec` filename. If it's identical to the plugin display name (as set in the PiPL), create a new clip; otherwise modify the clip.
- If the user cancels from your dialog when creating a new clip, return imCancel.
- If the clip is modified, the importer needs to do a few things for Premiere to pick up the changes. Put your file access information in the supplied `imFileAccessRec`. Premiere will use this data to reference your clip from now on. Close the file handle after you create it. Return imSetFile after creating a file handle in *imGetPrefs8*., and call RefreshFileAsync() in the Importer

File Manager Suite to notify Premiere that the clip has been modified. Premiere will immediately call you to open the file and return a valid imFileRef. Respond to *imOpenFile8*, *imQuietFile*, *imCloseFile* at a minimum.

---

## Real-Time Rolling and Crawling Titles

For RT rolls and crawls, a player and importer must be specially designed to work together. An importer can implement the appropriate functionality, but it is up to the player to take advantage of it.

Importers can make image data available for rolling and crawling titles, using `imImageInfoRec.isRollCrawl`. If the importer sets it to non-zero, this declares that the image is a title or other image that does roll/crawl, and that the importer supports the *imGetRollCrawlInfo* and *imRollCrawlRenderPage* selectors. *imGetRollCrawlInfo* is used to get info on the roll/crawl from the importer, and *imRollCrawlRenderPage* is used to get a rendered page of the roll/crawl.

---

## Troubleshooting

### How to Get First Crack at a File

To get the first opportunity to import a filetype also supported by a built-in importer (e.g. MPEG, AVI, QuickTime, etc), provide a different subtype and classID in order for your importer to be called for the types of files you support. imImportInfoRec.priority must be higher than any of the other importers for that filetype. Set this value to 100 or higher to override all built-in importers. Premiere Pro has more than one type of AVI importer and MPEG importer, which use this same prioritization mechanism. So your importer can override all of them and get the first shot at a filetype.

Just because you want to take over handling some files of a given filetype, it doesn't mean you have to handle all of them. To defer an unsupported subtype to a lower priority importer, return imBadFile during *imOpenFile8* or *imGetInfo8*. See the Media Abstraction chapter for more information on filetypes, subtypes, and classIDs.

### Format repeated in menu?

To avoid having your importer appear multiple times in the file formats supported pop-up list, fill out the formatName, formatShortName and platform extension once and only once during your *imGetIndFormat*.

---

## Resources

Importers must contain a IMPT resource. Premiere uses this to identify the plugin as an importer. Also, depending on the type of importer (standard, synthetic, or custom), a PiPL may be required.

---

## Entry Point

```cpp
csSDK_int32 xImportEntry (
  csSDK_int32  selector,
  imStdParms   *stdParms,
  void         *param1,
  void         *param2)
```

*selector* is the action Premiere wants the importer to perform. stdParms provides callbacks to obtain additional information from Premiere or to have Premiere perform tasks.

`param1` and `param2` vary with the selector; they may contain a specific value or a pointer to a structure. Return imNoErr if successful, or an appropriate return code.

---

## Standard Parameters

A pointer to this structure is sent from the host application to the plugin with every selector.

```cpp
typedef struct {
  csSDK_int32      imInterfaceVer;
  imCallbackFuncs  *funcs;
  piSuitesPtr      piSuites;
} imStdParms;
```

+------------------+-------------------------------------------------+
|      Member      |                   Description                   |
+==================+=================================================+
| `imInterfaceVer` | Importer API version                            |
|                  |                                                 |
|                  | - Premiere Pro CC 2014 - `IMPORTMOD_VERSION_15` |
|                  | - Premiere Pro CC - `IMPORTMOD_VERSION_14`      |
|                  | - Premiere Pro CS6.0.2 - `IMPORTMOD_VERSION_13` |
|                  | - Premiere Pro CS6 - `IMPORTMOD_VERSION_12`     |
|                  | - Premiere Pro CS5.5 - `IMPORTMOD_VERSION_11`   |
|                  | - Premiere Pro CS5 - `IMPORTMOD_VERSION_10`     |
|                  | - Premiere Pro CS4 - `IMPORTMOD_VERSION_9`      |
+------------------+-------------------------------------------------+
| `funcs`          | Pointers to callbacks for importers             |
+------------------+-------------------------------------------------+
| `piSuites`       | Pointer to universal callback suites            |
+------------------+-------------------------------------------------+

---

## Importer-Specific Callbacks

```cpp
typedef struct {
  ClassDataFuncsPtr  classFuncs;
  csSDK_int32        unused1;
  csSDK_int32        unused2;
} imCallbackFuncs;

typedef csSDK_int32 (*importProgressFunc){
  csSDK_int32  partDone;
  csSDK_int32  totalToDo;
void *trimCallbackID};
```

+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|       Function       |                                                                     Description                                                                      |
+======================+======================================================================================================================================================+
| `classFuncs`         | See [ClassData functions](../hardware/classdata-functions.md).                                                                                      |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| `importProgressFunc` | Available in `imSaveFileRec` and `imTrimFileRec` during *imSaveFile8* and *imTrimFile8*.                                                            |
|                      |                                                                                                                                                      |
|                      | Callback function pointer for use during project archiving or trimming to call into Premiere and update the progress bar and check for cancellation. |
|                      |                                                                                                                                                      |
|                      | Either `imProgressAbort` or `imProgressCon` tinue will be returned.                                                                                 |
|                      |                                                                                                                                                      |
|                      | The trimCallbackID parameter is passed in the same structures.                                                                                      |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
