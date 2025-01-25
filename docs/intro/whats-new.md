# Whats New

## What’s New in 24.0

With the removal of Capture functionality from Premiere Pro, support for Record modules and Device Control plug-ins have been removed from the SDK.

## What’s New in 15.4

We’ve updated the `PrSetEnv.h` header, to allow building ARM-native plugins.

## What’s New in 14.2

Cleared the dust and debris off of the SDK source files. ;) The primary motivation for this new SDK release is to provided updated headers. Example code utilizing those new headers, as well as documentation of their new contents, will (regrettably) need to wait for another day.

## What’s New in 13.1

Removed “CC” from the product name.

---

## What’s New in 13.0

The only significant change to Premiere Pro’s C++ APIs for 13.0 is the addition of color-space specifiers to the Importer API. The ColorProfileRec structure is deprecated; instead, Importers will describe supported colorspaces (in response to imGetIndColorSpace ) using a ColorSpaceRec.

---

## What’s New in 12.0

### Effects and Transitions

[GPU Effects & Transitions](../gpu-effects-transitions/gpu-effects-transitions.md#gpu-effects-transitions-gpu-effects-transitions) built using this SDK are now compatible with After Effects 15.0 and later. The sample GPU effect projects have been updated so that they load in both Premiere Pro and After Effects.

The newly provided [PrGPU SDK Macros](../gpu-effects-transitions/PrGPU-SDK-macros.md#gpu-effects-transitions-prgpu-sdk-macros) and device functions allow you to write kernels that will compile on CUDA, and Metal.

Multiple effects and transitions can now be implemented in a single plugin binary, by defining multiple entry points in software at runtime. The new method for registering entry points will be a replacement for the PiPL resource, and is currently only supported in Premiere Pro. The sample effects and transitions demonstrate this new method, while [Plug-In Property Lists (PiPL) Resource](../resources/pipl-resource.md#resources-pipl-resource) remains, for backwards-compatibility in PPro, and compatibility with AE.

[Sequence Info Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-sequence-info-suite) is now at version 5, adding the new call GetImmersiveVideoVRConfiguration(), which returns the VR video settings of the specified sequence.

New selector available for [Export Info Suite](../exporters/suites.md#exporters-suites-export-info-suite): kExportInfo_SourceBitrate. This returns the source’s bitrate in kbps, and is not available for all source types. exParamType can now be of type exParamType_thumbnail. A new flag exParamFlag_verticalAlignment can now be set so that property name and value controls are displayed vertically rather than side-by-side.

---

## What’s New in CC 2017.1

### Importers

Importers that support captions can make use of the mayHaveCaptions flag in `imFileInfoRec8`, for better performance. Also, a `imImageInfoRec` is now added to `imInitiateAsyncClosedCaptionScanRec`, just for the width and height parameters.

### Exporters

Exporters can advertise whether they support color profile embedding. There are also APIs to set color profile in the exporter, and a flag that controls whether profile is to be embedded. The color profile is passed to an exporter via exDoExportRec, for it to embed in the output media according to format standards. This is currently used for exports from After Effects through Media Encoder.

### Transmit

New 10-bit and 12-bit RGB HLG formats have been added for expanded HDR support.

In [App Info Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-app-info-suite), a new identifier has been added for Character Animator, which now supports transmit plugins.

### VR Video Support

The Playmod Immersive Video Suite can be used to query whether or not ambisonics monitoring is on or not, in the VR Video Settings.

---

## What’s New in CC 2017

### VR Video Support added

Transmit plugins can have the VR perspective in the desktop Monitor driven by the Head-Mounted Display, so when the person with the Head-Mounted Display looks in a different direction, the desktop Monitor shows that same perspective. To do this, the transmit plugin can use the new Playmod Immersive Video Suite to indicate that it supports tracking.

Once Premiere sees the transmitter supports tracking, when the user activates the VR viewer, the new menu item, “Track Head-Mounted Display” will become active, and can be toggled to begin tracking. The transmitter should call NotifyDirection() as frequently it wants with updated info. Premiere will pick up the new position on the next frame draw.

For importers, imFileInfoRec8 has now been expanded so that if an importer detects that a clip contains VR video, it can inform Premiere.

### New Sample Projects

This SDK includes a new render path for the ProcAmp sample for Metal. This sample requires macOS 10.11.4 and later.

We’ve also added a sample GPU effect called Vignette, donated by Bart Walczak. This effect has OpenCL, CUDA, and software render paths. Software rendering in Premiere Pro includes

8-bit/32-bit RGB/YUV software render paths. Software rendering in After Effects includes 8-bit and 32-bit smart rendering.

And lastly, the Control Surface sample is now cross-platform.

### New Panel/Scripting Capabilities

Scripting, the processing underlying HTML5 panels, is consistently being improved upon. In this release, we’ve added scripting functions to add/modify effect keyframes. See the sample panel code on GitHub:

[https://github.com/Adobe-CEP/Samples/tree/master/PProPanel](https://github.com/Adobe-CEP/Samples/tree/master/PProPanel)

In particular, see the function onPlayWithKeyframes() in jsx/Premiere.jsx

### Miscellaneous

In [Video Segment Render Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-video-segment-render-suite), new versions of various calls have been added with an additional boolean value that allows renders to skip rendering of non-intrinsic effects.

---

## What’s New in CC 2024.0

The Transmit API has been expanded to enable multiple audio outputs, and plug-ins which stream video and audio information.

## What’s New in CC 2015.4

### Metal rendering for Effects and Transitions

GPU-accelerated rendering using Metal is now supported for third-party effects and transitions. PrGPUDeviceFramework_Metal has been added as one of the enum values in PrGPUDeviceFramework.

---

## What’s New in CC 2015.3?

### Control Surfaces

New suites have been added for Control Surfaces to support the Lumetri Color panel. Most controls are supported, including the color wheels, but not including the Curves controls.

There is now a shared location for Control Surface plugins. On Mac:

/Library/Application Support/Adobe/Common/Plugins/ControlSurface, and

~/Library/Application Support/Adobe/Common/Plugins/ControlSurface

On Win:

C:Program FilesAdobeCommonPluginsControlSurface

### Importers

Video duration can now be reported as a 64-bit integer, using the new imFileInfoRec8. vidDurationInFrames, to support longer file lengths. There is also a new suite function, SetImporterInstanceStreamFileCount(), for importers to specify how many files they open.

### Exporters

New flags can be set in exExporterInfoRec.flags, to restrict an exporter from being used in a way that doesn’t make sense. Now, an exporter can specify that video-only export is not supported. Also, an exporter can turn off the Publish tab if it chooses to.

### Effects

Source settings effects should use the updated Source Settings suite with new

SetIsSourceSettingsEffect() function. They should make this call during *PF_Cmd*

*GLOBAL_SETUP*. This function was added to handle the case when the effect is applied to proxy video.

### Misc

Using the [Sequence Info Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-sequence-info-suite), a new call has been added, GetProxyFlag(), for a plugin to know whether the proxy mode is on or off.

---

## What’s New in CC 2015.1?

### Transmit

Native support for 12-bit Dolby PQ pixel formats, with Rec. 709, P3, and Rec. 2020 primaries, have been added.

---

## What’s New in CC 2015?

### After Effects-Style Transitions

AE-style Transitions can now get and set transition start and end percentages. The user can change the start and end parameters in the Effect Controls panel. To allow a plugin to be informed of changes to these values, there are two new functions in the PF TransitionSuite: RegisterTransitionStartParam() and RegisterTransitionEndParam(), which register these parameters with the plugin as float parameters. Once registered, the plugin will receive *PF_Cmd_USER_CHANGED_PARAM* when these params change, as well as when the transition is first applied, so the plugin can initialize them to the desired value.

AE-style Transitions can now retrieve GPU frames from arbitrary locations in the underlying clips. There is a new PrGPUDependency_TransitionInputFrame, and PrGPUFilterFrameDependency has a new member to specify whether frames from the incoming or outgoing clips are needed.

### Source Settings = Effect + Importer

Source Settings for clips can now be implemented using effects that are tied to importers. This has the advantage of providing settings in the Effect Controls panel, rather than in a modal dialog. Editors can adjust Source Settings for multiple clips this way. These effects are used for the DPX source settings, CinemaDNG, etc.

To implement this, an importer should set `imImportInfoRec.hasSourceSettingsEffect` to true. Then in imFileInfoRec8, it should set sourceSettingsMatchName to the match name of the effect to be used for the Source Settings.

On the effects side, a new PF Source Settings Suite has been added to PrSDKAESupport.h, for effects using the After Effects API. This is how an effect registers a function to handle the Source Settings command.

A source settings effect is used primarily for the parameter UI and management. A source settings effect doesn’t provide the actual frames. In fact, the effect isn’t even called with *PF_Cmd_RENDER*. The frames come directly from the importer, which provides frames based on the settings as passed to the importer via prefs data.

When a clip is first imported, the effect is called with *PF_Cmd_SEQUENCE_SETUP*. It should call PerformSourceSettingsCommand() in the Source Settings Suite, to initialize the prefs. This causes the importer to get called with *imPerformSourceSettingsCommand*, where it can read the file and set the default prefs. param1 of that function is imFileAccessRec8\*, and param2 is imSourceSettingsCommandRec\*.

When the source settings effect parameters are changed, the effect gets called with *PF_Cmd_TRANSLATE_PARAMS_TO_PREFS*. The function signature is:

```cpp
PF_Err TranslateParamsToPrefs(
  PF_InData*                      in_data,
  PF_OutData*                     out_data,
  PF_ParamDef*                    params[],
  PF_TranslateParamsToPrefsExtra  *extra)
```

With the new prefs, the importer will be sent *imOpenFile8, imGetInfo8, imGetIndPixelFormat, imGetPreferredFrameSize, imGetSourceVideo*, etc.

imSourceSettingsCommandRec and PF Source Settings Suite allow the effect to communicate directly with the importer, so that it can initialize its parameters properly, based on the source media. In the DPX source settings effect, for example, in *PF_Cmd_SEQUENCE_SETUP*, it calls PF_SourceSettingsSuite->PerformSourceSettingsCommand(), which calls through to the importer with the selector *imPerformSourceSettingsCommand*. Here, the importer opens the media, looks at the header and initializes the prefs based on the media. For

DPX, the initial parameters and default prefs are based on the bit depth of the video. These default prefs are passed back to the effect, which sets the initial param values and stashes a copy of them in sequence_data to use again for future calls to *PF_Cmd_SEQUENCE_RESETUP*.

### Importers

For any importers that are using imClipFrameDescriptorRec, note that the structure definition has changed. Any importers that use this in both CC 2014 and CC 2015 or later will need to do a runtime check before accessing the members of this structure.

### Exporters

Exporters can now use standard parameters for audio channel configuration, as used with the built-in QuickTime exporter. The new exporter parameters ADBEAudioChannelConfigurationGroup and ADBEAudioChannelConfiguration supercede ADBEAudioNumChannels. The new Export Audio Param Suite can be used to query/change the audio channel configuration.

The [Sequence Audio Suite](../exporters/suites.md#exporters-suites-sequence-audio-suite) is now at version 2, revising `MakeAudioRenderer()` to take `PrAudioChannelLabel*` as a parameter.

### Transmitters

Transmitters can get a few new bits of information to aid with A/V sync. In the [Playmod Audio Suite](../transmitters/suites.md#transmitters-suites-playmod-audio-suite), the new function GetNextAudioBuffer2() returns the actual time the rendered buffer is from.

Also, in `tmPlaybackClock`, the new members `inAudioOffset` and `inVideoOffset` have been added to specify the offset chosen by the user in the preferences.

The host accounts for these offsets automatically by sending frames early, but if a transmitter is manually trying to line up audio and video times, it can use this to know how far apart from each other they are supposed to be.

### Miscellaneous

Legacy callbacks bottlenecks->ConvolvePtr() and IndexMapPtr() have had their parameter types updated to fix a bug. Any plugins that use these in both previous versions and CC 2015 will need to do a runtime check before calling this function.

Starting in CC 2015, we now provide installer hints for Mac. You’ll find a new plist file “com. Adobe.Premiere Pro.paths.plist” at “/Library/Preferences”. This contains hints for your Mac installer to know where to install plugins, and is similar to the registry entries we have been providing on Win.

### New Sample Projects

This SDK includes updated GPU effect and transition samples that demonstrate GPU rendering. Thanks to Rama Hoetzlein from nVidia for the CUDA render path provided for the SDK_CrossDissolve sample!

A barebones Control Surface sample is now provided, too.

---

## What’s New in CC 2014 (8.2)?

Importers now have more visibility into the player’s intent on a given async request, since the render context info is now passed in imSourceVideoRec.inRenderContext. Async importers can implement *aiSelectEfficientRenderTime* to specify if a frame request would be more efficient at another frame time, for example at I-frame boundaries. The [Video Segment Render Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-video-segment-render-suite) has been updated to version 4, adding new calls that include imRenderContext as a parameter.

---

## What’s New in CC 2014 (8.1)?

Importers that support growing files now get a hint if the host knows the file has stopped growing:

imFileInfoRec8.ignoreGrowing.

Exporters can now get the list of source pixel formats used by the clips in a sequence that is being smart rendered. GetExportSourceInfo(…, kExportInfo_SourcePixelFormat, …) provides this information.

---

## What’s New in CC 2014 (8.0.1)?

Importers can fill in imImageInfoRec.codecDescription to provide a string that will be displayed for clips in the Video Codec column of the Project panel.

---

## What’s New in CC 2014?

Importers can now choose the format they are rendering in, which allows importers to change pixel formats and quality based on criteria like enabled hardware and other source settings, such as HDR. To handle the negotiation, implement *imSelectClipFrameDescriptor*.

imSourceVideoRec now includes a quality attribute. [PPix Cache Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-ppix-cache-suite) is now at version 6, adding AddFrameToCacheWithColorProfile2() and

GetFrameFromCacheWithColorProfile2(), which are the same as the ones added in version 5 with the addition of a PrRenderQuality parameter.

imFileInfoRec8.highMemUsage is no longer supported.

A new recorder return code was added, rmRequiresRoyaltyContent. Return this from

recmod_Startup8 or recmod_StartRecord, if the codec used is unlicensed.

OpenCL rendering now also uses the half-precision 16-bit floating point pixel format for rendering. GPU effects and transitions that support OpenCL should implement both 16f and 32f rendering.

A new plugin API has been introduced for hardware Control Surfaces. This is the API that allows support for EUCON and Mackie devices to control audio mixing and basic transport controls. The API supports two-way communication with Premiere Pro, so that hardware faders, VU meters, etc are in sync with the application.

Premiere Pro is now localized in Russian and Brazilian Portugese.

---

## What’s New in CC October 2013?

We’ve extended the After Effects API to support native transitions in Premiere Pro.

For device controllers, the new command *cmdSetDeviceHandler* was added. This command tells the device controller which panel is using the device controller – either the Capture panel, or Export to Tape panel.

For importers, imInitiateAsyncClosedCaptionScanRec now provides extra fields for the importer to fill in the estimated duration of all the captions. This is useful for certain cases where the embedded captions contain many frames of empty data.

We added version 2 of the [Export File Suite](../exporters/suites.md#exporters-suites-export-file-suite) to resolve a mismatch in seek modes.

---

## What’s New in CC July 2013?

The only significant additions made in the July 2013 update to version CC are in the device controller API.

---

## What’s New in CC?

### New Edit to Tape Panel

You can think of this as the Export to Tape equivalent of the Capture panel for capturing, which provides a video preview and various settings in the PPro UI. Among the benefits are more seamless integration, a more familiar UI for users, integrated device presets, and some new capabilities like adding Bars and Tone / Black Video / Universal Counting Leader to the start of your layoff to tape. To use this new feature, read more about what’s new in the device controller API.

### New GPU Extensions for Effects and Transitions

New GPU Extensions to existing APIs allow effects and transitions to access video frames in GPU memory, when using the Mercury Playback Engine in a GPU-accelerated mode. See [GPU Effects & Transitions](../gpu-effects-transitions/gpu-effects-transitions.md#gpu-effects-transitions-gpu-effects-transitions) for more information.

### Closed Captioning Support in Importer and Exporter APIs

The importer and exporter APIs have been extended to support closed captioning embedded in media. Note that Premiere Pro can also import and export captions in a sidecar file (e.g. .mcc,

.scc, or .xml) alongside any media file, regardless of the media file format.

### Miscellaneous Improvements

- A new pixel format for native 10-bit RGB support - PrPixelFormat_RGB_444_10u, as well as `PrPixelFormat_UYVY_422_32f_*` formats
- VST 3 support allows many more audio plugins to run in Premiere Pro
- Windows installer improvements, by adding new registry values for preset and settings locations.
- Get the current build number via the [App Info Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-app-info-suite)
- Importers can now support audio beyond basic mono, stereo, and 5.1, without implementing multiple streams, and importers can return varying pixel formats depending on the clip settings. Read more about what’s new for importers.
- Exporters can get the number of audio channels in the source, and check if the user has checked “Use Previews” in the Export Settings dialog. They can also move an existing settings parameter to a different location. Read more about what’s new for exporters.
- The [Sequence Info Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-sequence-info-suite) can retrieve the field type, zero point, and whether or not the timecode is drop-frame
- New flags to the transition API as a hint to optimize rendering when a transition only has an input on one side
- The [Video Segment Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-video-segment-suite) provides access to a new property: Effect_ClipName

Premiere Pro is now localized in Chinese.

---

## What’s New in CS6.0.x?

CS6.0.2 adds more support for growing files in importers. A transmitter can now label its audio channels for the Audio Output Mapping preferences.

CS6.0.1 gives device controllers a way to get the number of frames dropped during an insert edit, to abort an Export to Tape if desired. This method is already superceded by the new Edit to Tape panel functionality in CC.

---

## What’s New in CS6?

### Transmit API

We are introducing the Transmit API as the preferred means for external hardware monitoring. This new API provides vastly simplified support for monitoring on external hardware. Transmit plugins offer more flexible usage, since they are not tied to the sequence Editing Mode, which cannot be changed once a sequence has been edited. Transmitters can be specified by the user in Preferences > Playback. Other plugins such as importers and effects with settings preview dialogs can send video out to the active transmitter, opening up new possibilities for hardware monitoring. See [Transmitters](../transmitters/transmitters.md#transmitters-transmitters) for more details.

### Exporter Enhancements

Exporters can now use “push” model compression. This can simplify export code and improve performance. The “pull” model is still supported, and required for legacy versions and Encore.

We’ve added the [Export Standard Param Suite](../exporters/suites.md#exporters-suites-export-standard-param-suite), which provides the standard parameters used in many built-in exporters. This can greatly reduce the amount of code needed to manage standard parameters for a typical exporter, and guarantee consistency with built-in exporters.

Exporters can now set tooltip strings for parameters. Multiple exporters are now supported in a single plugin. And the Maximum Render Precision flag is now queried from the exporter, rather than being handled without the exporter’s knowledge.

Exporters can now set events (error, warning, or info) for a specific encode in progress in the Adobe Media Encoder render queue, using the new [Exporter Utility Suite](../exporters/suites.md#exporters-suites-exporter-utility-suite). These events are displayed in the application UI, and are also added to the AME encoding log.

Make sure your presets go in the right location in the new AME Preset Browser. Read additional details of what’s new in [Exporters](../exporters/exporters.md#exporters-exporters).

### Stereoscopic Video Pipeline

We are also adding API support for stereoscopic video throughout the render pipeline. This affects importers, effects built using the After Effects API, and exporters.

### Other Changes

**Importers** can now support growing files in Premiere Pro. We have also added a way for importers to specify all their source files to be copied by Collect Files in After Effects. There is also a new function in the Media Accelerator Suite to validate the content state of a media accelerator. See additional details of what’s new in [Importers](../importers/importers.md#importers-importers).

For **Recorders**, the parent window handle is now properly passed in during *recmod_ShowOptions*

when a recorder should display its modal setup dialog.

For **Players**, pmPlayerSettings has a new member, mPrimaryDisplayFullScreen, which indicates whether or not the player should display fullscreen.

**Device controllers** have a new callback, DroppedFrameProc, to provide the feature to abort and Export to Tape if frames are dropped.

New video segment properties were added:

- `kVideoSegmentProperty_MediaClipScaleToFramePolicy`,
- `kVideoSegmentProperty_AdjustmentAdjustmentMediaIsOpaque`,
- `kVideoSegmentProperty_AdjustmentOperatorsHash`,
- `kVideoSegmentProperty_Media_InPointMediaTimeAsTicks`,
- `kVideoSegmentProperty_Media_OutPointMediaTimeAsTicks`,
- `kVideoSegmentProperty_Clip_TrackItemStartAsTicks`,
- `kVideoSegmentProperty_Clip_TrackItemEndAsTicks`,
- `kVideoSegmentProperty_Clip_EffectiveTrackItemStartAsTicks`,
- `kVideoSegmentProperty_Clip_EffectiveTrackItemEndAsTicks`

The [Memory Manager Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-memory-manager-suite) is now at version 4. AdjustReservedMemorySize provides a way to adjust the reserved memory size relative to the current size. This may be easier for the plugin, rather than maintaining the absolute memory usage and updating it using the older ReserveMemory call.

MPEG-4 pixel formats and full-range Rec. 709 MPEG-2 and MPEG-4 formats have now been added for native support in the render pipeline.

---

## What’s New in CS5.5?

**Importers** can now support color management, when running in After Effects. Now, even nonsynthetic importers can explicitly provide peak audio data. And a new return value allows an importer to specify that it is dependent on a library that needs to be activated. See additional details of what’s new in [Importers](../importers/importers.md#importers-importers).

**Players** can now support closed captioning. See additional details of what’s new in the players chapter.

**Exporters** now have a call to request a rendered frame and then conform it to a specific pixel format. See additional details of what’s new in [Exporters](../exporters/exporters.md#exporters-exporters).

We have opened up a new **Export Controller** API that can drive any exporter to output a file in any format and perform custom post-processing operations. Developers wanting to integrate Premiere Pro with an asset management system will want to use this API instead of the exporter API. See [Export Controllers](../export-controllers/export-controllers.md#export-controllers-export-controllers) for more details.

A new pair of pixel formats was added to natively support full-range Rec. 601 4:2:0 YUV planar video, both progressive and interlaced: PrPixelFormat_YUV_420_MPEG2_FRAME_PICTURE_PLANAR_8u_601_FullRange and PrPixelFormat_YUV_420_MPEG2_FIELD_PICTURE_PLANAR_8u_601_FullRange.

The [Video Segment Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-video-segment-suite) now provides a new call to retrieve a segment node for a requested time. There are also a few new properties for media nodes:

StreamIsContinuousTime, ColorProfileName, ColorProfileData, and

ScanlineOffsetToImproveVerticalCentering.

The [Sequence Info Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-sequence-info-suite) now provides a call to get the sequence frame rate, which may be useful for effects.

The [Image Processing Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-image-processing-suite) has a new call to set the aspect ratio flag of a DV frame.

---

## What’s New in CS5?

**Importers** now have access to the resolution, pixel aspect ratio, timebase, and audio sample rate of the source clip from a setup dialog. Custom importers can use a new call to update a clip after it has modified by the user in the setup dialog. Please refer to [Importers](../importers/importers.md#importers-importers) for more info on what’s new.

**Recorders** can now provide audio metering during preview and capture.

**Exporters** and **players** can automatically take advantage of GPU acceleration, if available on the end-user’s system. Each project now has a setting for the renderer that the user can choose in the project settings dialog. When renders occur through the [Sequence Render Suite](../exporters/suites.md#exporters-suites-sequence-render-suite) or the Playmod Render Suite, they now go through the renderer chosen for the current project. This allows third-party exporters and players to use the built-in GPU acceleration available in the new Mercury Playback Engine.

Exporters and players can now handle any pixel format, with the new [Image Processing Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-image-processing-suite). Exporters and players that parse segments and perform their own rendering can now call the host for subtree rendering. See the [Video Segment Render Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-video-segment-render-suite) for details.

If you provide an installer for an exporter, note that custom presets created in Premiere Pro are now visible in AME and vice-versa.

### Mac 64-Bit and Cocoa

It is invalid to unload any bundle that uses Cocoa because of restrictions in the Objective-C runtime which do not support unregistering classes. If a plugin uses Cocoa, it must call CFRetain on its own bundle, otherwise it will cause a crash when the application is closing and tries to unload the plugins.

---

## What’s New in CS4?

### New Renderer API and Custom Pixel Formats

The new renderer API provides a way to take over and accelerate rendering of segments. Just as a player can choose which segments to accelerate, so a renderer can choose which segments to accelerate. Renderers may accelerate any segment, in any sequence, in any project.

Renderers also provide a way to add completely custom pixel formats to the render pipeline. Supporting a custom pixel format in an importer, a renderer, and an exporter is the new way to implement smart rendering, by passing custom compressed data from input to output.

### Sequence Preview Formats

Sequence preview file formats are now defined by Sequence encoder preset files. Without any presets installed, you will not be able to create a new sequence using your custom editing mode.

### Separate Processes During Export

When choosing export settings, the settings UI is displayed by Premiere Pro. When the user confirms the settings, the clip or sequence is passed to Media Encoder. From Media Encoder, frames from the clip or sequence can be retrieved and rendered without further participation from Premiere Pro. For a clip export, Media Encoder uses any installed importers to get source frames. For sequence export, Media Encoder uses a process called PProHeadless, to import and render frames to be exported.

Since there are so many processes involved during export, it is important that plugins be accessible to all processes, by being installed in the common plugins folder. PProHeadless Plugin Loading.log provides information on the PProHeadless process. PProHeadless is also used when the user creates a dynamic link to a .prproj that is not opened in Premiere Pro.

### XMP metadata

There are built-in XMP metadata handlers for known filetypes. These handlers write and read metadata to and from the file, without going through the importer. *imSetTimeInfo8* is no longer called, since this is set by the XMP handler for that filetype.

### More Pixel Format Flexibility

Effects, transitions, and exporters no longer need to support 8-bit RGB at a minimum. So, for example, an effect can be written to process floating point YUV only. If necessary, Premiere will make an intermediate conversion so that the effect will receive the pixel format it supports.

---

## Legacy API

Legacy API features, such as selectors and callbacks that are superceded by new ones, are deprecated, but are supported, unless indicated.
