# Getting Started

Start your plugin by modifying the SDK sample. Step through the code in your debugger to learn the order of events.

---

## Media Encoder as a Test Harness

It may be faster to developing exporters using Media Encoder, since it is a lighter-weight application. However, you will want to test your exporter in Premiere Pro, to make sure the behavior is the same as when running in Media Encoder.

---

## Adding Parameters

Starting in CS6, the [Export Standard Param Suite](suites.md#export-standard-param-suite) provides a way to add several basic sets of parameters, whether for video, audio, still sequences, etc. Beyond the standard parameters, custom defined parameters can be added using the [Export Param Suite](suites.md#export-param-suite).

First register the parameters during `exSelGenerateDefaultParams`. Then provide the localized strings and min/max parameter values during `exSelPostProcessParams`. When the exporter is sent `exSelExport` to export, get the user-specified parameter values using the [Export Param Suite](suites.md#export-param-suite).

---

## Updating Parameters Dynamically

Parameters can be updated dynamically based on user interaction with any related parameter. The time to update is during the `exSelValidateParamChanged` selector. Use ChangeParam in the [Export Param Suite](suites.md#export-param-suite) to make the change. Then, set `exParamChangedRec.rebuildAllParams` to true before returning. If you don't set that flag, parameters may appear out of order after a change.

---

## Supporting "Match Source"

The exporter must set `exExporterInfoRec.canMatchSource` to true. This will add the Match Source button to the Video tab in the Export Settings.

Next, if the Match Source button is pressed in the Export Settings, `exPostProcessParamsRec.doConformToMatchParams` will be true. The exporter should respond by updating any parameter values it can to match the source settings.

---

## Get Video Frames and Audio Samples

Starting in CS6, exporters can use the new push model, or the legacy pull model for obtaining frames. The new push model is supported starting in CS6, and the pull model is still supported.

Push Model

---

Using the push model, the exporter host can simply push frames to a thread-safe exporter-specified callback. Use DoMultiPassExportLoop in the [Exporter Utility Suite](suites.md#exporter-utility-suite) to register the callback.

Compared with the pull model, this will cut down on the code previously required for render loop management. It should also yield substantial performance increases for exporters that haven't finely tuned their multithreaded rendering.

### Pull Model

Using the pull model to get video and audio data involves making calls to the host to ask for this data. Use the [Sequence Render Suite](suites.md#sequence-render-suite) to get individual video frames, and the [Sequence Audio Suite](suites.md#sequence-audio-suite) to get buffers of audio samples.

Video frames can be requested synchronously or asynchronously. The asynchronous method can yield better performance, but it is up to the exporter to provide its asynchronous render loop.

---

## Handling a Pause or Cancel by the User (Pull Model only)

Push model export does not require any special code to handle pause or cancel by the user. For pull model export, the way to check if the user has paused or cancelled the export is to call UpdateProgressPercent in the [Export Progress Suite](suites.md#export-progress-suite), and check the return value. If the return value is suiteError_ExporterSuspended, the user has hit the pause button, which is only available in the Media Encoder UI. If the return value is `exportReturn_Abort`, then the export has been cancelled by the user.

If UpdateProgressPercent returns `suiteError_ExporterSuspended`, then the exporter should next call `WaitForResume`, which will block until the user has unpaused the export.

If UpdateProgressPercent returns `exportReturn_Abort`, the exporter should take steps to abort the export and clean up. Note that the exporter can still continue to ask for video frames and audio samples after a cancel has been received, which is useful in certain circumstances, such as if an exporter needs a few more frames to complete an MPEG GOP, or if it wants to include the audio for the video exported up to the point of cancel. This allows the exporter to generate well-formed output files, even in the case of a cancel.

---

## Creating Presets

Create your own presets using the Export Settings UI, either from within Premiere Pro, or Media Encoder. Just modify the parameters the way you want, and hit the Save icon to save the preset to disk. The presets are saved with the extension '.epr'.

Starting in CS5, all the presets are saved to the same location, regardless of whether saved from Premiere Pro or Media Encoder:

On Windows 7, presets are saved here: `[User folder]\AppData\Roaming\Adobe\Common\AME\[version]\Presets\\`

On Mac OS: `~/Library/Preferences/Adobe/Common/AME/[version]/Presets/`

In CS4, where the files are saved depends on whether you've opened the Export Settings UI in Premiere Pro or Media Encoder:

### Media Encoder presets

On Windows Vista, presets are saved here: `[User folder]\AppData\Roaming\Adobe\Adobe Media Encoder\[version]\Presets\\`

On Windows XP: `[Documents and Settings folder]\[user name]\Application Data\\ Adobe\Adobe Media Encoder\[version]\Presets\\`

On Mac OS: `~/Library/Preferences/Adobe/Adobe Media Encoder/[version]/ Presets/`

### Premiere Pro presets

On Windows Vista, presets are saved here: `[User folder]\AppData\Roaming\Adobe\Premiere Pro\[version]\\ Presets\\`

On Windows XP: `[Documents and Settings folder]\[user name]\Application Data\\ Adobe\Premiere Pro\[version]\Presets\\`

On Mac OS: `~/Library/Preferences/Adobe/Adobe Premiere Pro/[version]/Presets/`

#### AME Preset Browser

Starting in CS6, Adobe Media Encoder has a Preset Browser with provides a structured organization of presets. Third-party presets can be added to any folder or subfolder within the main categories. Once you have created a preset, it will default to the Other folder. You can set the desired folder location in the `<FolderDisplayPath>` tag in the preset XML.

For example, if you set it to: `<FolderDisplayPath>System Presets/Image Sequence/PNG</ FolderDisplayPath>` then AME will display the preset in the `System Presets > Image Sequence > PNG folder`.

It is essential to use: "System Presets/xxx/" where the xxx must be any of the existing main categories (use the English name for this). Only one level below can you can create a custom-named folder. If the folder doesn't already exist, it will be created.

The Preset Browser data is cached in a file at: `[User Folder]\AppData\Roaming\Adobe\Common\AME\[version]\Presets\\ PresetTree.xml`

If you want to force a refresh of the Preset Browser data, just quit AME, delete this file, and re-launch AME.

### Installation in CS4

For better performance, in CS4, we recommend you install any presets for your exporter in the application folder for Premiere Pro and Media Encoder.

For both Windows and Mac OS: `[App installation path]\MediaIO\systempresets\[exporter subfolder]`

The subfolder must be named based on the hexadecimal fourCCs of the ClassID and filetype of the exporter. For example, the SDK exporter has a ClassID of 'DTEK' or 0x4454454B, and a filetype of `SDK` or 0x53444B5F. So the subfolder must be named '4454454B_53444B5F'. For convenience, you can find the ClassID and filetype fourCCs in the preset file itself, in a decimal representation.

---

## Parameter Caching

During development, when you modify parameters in your exporter and reload the plugin into the host, the Settings UI may continue to show stale parameter data. New parameters that you have added may not appear, or old ones may continue to appear. Or if you have changed the UI for an existing parameter, it may not take effect.

At a minimum, any old presets must be deleted. This includes Media Encoder presets and Premiere Pro presets. After deleting the old presets, there are two options, depending on whether the an older version of the exporter has already been distributed and is in use.

### Increment the Parameter Version

If an older version of the exporter is already being used by customers, you'll need to use parameter versioning. During `exSelGenerateDefaultParams`, you should call SetParamsVersion() in the [Export Param Suite](suites.md#export-param-suite) and increment the version number.

After that, create new presets and sequence encoder presets (if needed) using the new set of parameters. Make sure your installer removes the old presets, and installs the new ones.

### Flush the Parameter Cache

If you don't increment the parameter version, you can manually flush the parameter cache in a few steps. After you've deleted the old presets, do the following:

1. Delete hidden presets that were created by the hosts for the most recently used parameter settings. Look for a file called Placeholder Preset.epr in both the folders above the Media Encoder presets and the Premiere Pro presets.
2. Delete batch.xml, used by Media Encoder. This is also in the folder above the Media Encoder presets. Deleting this is equivalent to deleting the items out of the Media Encoder render queue.
3. Delete Premiere Pro sequence encoder presets that use the exporter, if any
4. Even after deleting all the old presets, Media Encoder may initially show old cached parameter UI. In the Settings UI, just switch to a different format and then back to yours.

---

## Multichannel Audio Layouts

To support multichannel audio layouts, kPrAudioChannelType_MaxChannel should be the type requested in MakeAudioRenderer().

The audio buffers you use for GetAudio() should likewise be an array of kPrAudioChannelType_MaxChannel channels, and yes, this means you may be allocating more space than actually used.

In the exporter's Audio tab UI, you can provide a parameter to choose between various multi-channel audio layouts. You can compare your settings to what we have with the built-in formats, QuickTime and MXF (such as MXF OP1a and DNxHD). From the user selection in your audio export settings (e.g., 2x stereo, etc), you will know how many of those channels passed back in GetAudio() should actually be written to the file.

Here's a helpful video on audio track mapping: [http://www.video2brain.com/en/lessons/changes-in-audio-tracks-and-merged-clip-audio](http://www.video2brain.com/en/lessons/changes-in-audio-tracks-and-merged-clip-audio)

---

## Closed Captioning

Starting in CC, the Export Settings includes a new Captions tab, for Closed Captioning export. For all formats, a sidecar file containing the captions can be exported. Additionally, exporters can optionally embed Closed Captioning directly in the output file. First, the exporter must set exExporterInfoRec.canEmbedCaptions to true. This will add the option to embed the captions in the output file, from the Export Options drop-down in the Captions tab. If this option is selected during export, exDoExportRec.embedCaptions will be true. The exporter should retrieve the captions using the [Captioning Suite](../universals/sweetpea-suites.md#captioning-suite).

---

## Multiple File Formats

To support more than one file format in a single exporter, describe one format at a time during `exSelStartup`. After describing the first one, return exportReturn_IterateExporter from `exSelStartup`, and the exporter will be called again to describe the second format, and so on. After describing the last format, return exportReturn_IterateExporter, and the exporter will be called yet again. This time, return exportReturn_IterateExporterDone.

Use a unique fileType for each format. When you are later sent `exSelGenerateDefaultParams`, `exSelPostProcessParams`, etc, you'll want to pay attention to the fileType, and respond according to the format.

---

## Exporters Used for Editing Modes

An exporter that is used in an editing mode must have a codec parameter, and that parameter ID must be ADBEVideoCodec. If Premiere Pro cannot find this parameter, it will not be able to reopen projects in the custom editing mode, and will revert the project to Desktop mode.

### Sequence Encoder Presets

Sequence preview presets are now required for editing modes. These contain the exporter parameters to generate preview files. This makes preview file formats much easier to define, by using the Media Encoder or Premiere Pro UI to create presets, rather than directly editing XML.

To create a sequence encoder preset:

1. Create a preset. The name that you give it will be the name that will be used in the Sequence Settings > General > Preview File Format drop-down.
2. Make sure this preset is installed in the application folder for Premiere Pro, along with the other sequence presets:

On Windows, they should be installed here: `[App installation path]\Settings\EncoderPresets\SequencePreview\[editing mode GUID]*.epr`

On MacOS, it is basically the same (inside the application package): `[App installation path]/[Premiere Pro package]/Contents/Settings/EncoderPresets/ SequencePreview/[editing mode GUID]/*.epr`

As you can see by the installation paths above, Premiere Pro associates the sequence preview presets with the editing mode they go with, by using the presets in the folder that matches the GUID of the editing mode. The editing mode GUID is defined in the editing mode XML file, using the `<EditingMode.ID>` tag.

### Adding new Preview File Formats to Existing Editing Modes

You can not only provide sequence preview presets for your own editing mode, but you could even add additional sequence preview presets for one of the built-in editing modes. Editing mode GUIDs for built-in editing modes can be found in the Adobe Editing Modes. xml file. For example, the Desktop editing mode on Windows has the GUID 9678AF98A7B7-4bdb-B477-7AC9C8DF4A4E. On Mac OS it is 795454D9-D3C2-429d-9474- 923AB13B7018.

You can additionally restrict the list and specify which one is chosen by default, by editing the `<PresetComments>` tag in the preset file.

If the value of the tag starts with "IsConstrained,", then a comma delimited list of 4ccs follows that dictates which codecs are available, and the first one is chosen by default.

For example, QuickTime DV NTSC.epr for the Mac DV NTSC editing mode has this: `<PresetComments>IsConstrained,dvc </PresetComments>`

Which restricts the codec selection of the exporter to be only the single codec choice.

---

## Stereoscopic Video

!!! note
    Currently stereoscopic exporters must use the old "pull" model, and only receive stereoscopic video when exporting directly from Premiere Pro. In other words, when exports are queued to run in Adobe Media Encoder, they will not get stereoscopic video.

To get rendered frames for both left and right eye, use the [Video Segment Suite](../universals/sweetpea-suites.md#video-segment-suite) to request the left and right cutlists, and render frames from both. An exporter can tell if segments in both of them are identical (implying that they have nothing stereoscopic about them) by looking at the segment hashes, and you can tell if two frames are identical (by looking at the request identifiers).

---

## Timeline Segments in Exporters

The timeline segments available to exporters do not always fully describe the sequence being exported. To consistently get timeline segments that fully describe the sequence, an exporter needs to work along with a renderer plugin.

During a sequence export, Premiere Pro makes a copy of the project file and passes it to Media Encoder. Media Encoder takes that project and uses the PProHeadless process to generate rendered frames. So when an exporter, which is running in Media Encoder, parses the sequence, it only has a very high-level view. It sees the entire sequence as a single clip, and sees any optional cropping or filters as applied effects. So when parsing that simple, high-level sequence, if there are no effects, an exporter can just use the MediaNode's ClipID with the [Clip Render Suite](../universals/sweetpea-suites.md#clip-render-suite) to get frames directly from the PProHeadless process. In the PProHeadless process, a renderer plugin can step in, parse the real sequence in all its glory, and optionally provide frames in a custom pixel format.

When rendering preview files, Premiere Pro does the rendering without Media Encoder, so an exporter can get the individual segments for each clip, similar to before.

---

## Smart Rendering

Under very specific circumstances, an exporter can request compressed frames, avoiding unnecessary de/recompression.

This would be done by providing both exporter and renderer plugins that parse timeline segments.

If the source can be copied over to the destination, the compressed frames can be passed in a custom pixel format.

These compressed frames are not guaranteed, however, so the exporter should be prepared to handle uncompressed frames.

---

## Entry Point

```cpp
DllExport PREMPLUGENTRY xSDKExport (
  csSDK_int32      selector,
  exportStdParms*  stdParmsP,
  void*            param1,
  void*            param2)
```

- `selector` is the action the host wants the exporter to perform.
- `stdParms` provides callbacks to obtain additional information from the host or to have the host perform tasks.
- Parameters 1 and 2 vary with the selector; they may contain a specific value or a pointer to a structure.

Return `exportReturn_ErrNone` if successful, or an appropriate return code.

---

## Standard Parameters

A pointer to this structure is sent from the host to the plugin with every selector.

```cpp
typedef struct {
  csSDK_int32               interfaceVer;
  plugGetSPBasicSuiteFunc*  getSPBasicSuite;
} exportStdParms;
```

+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
|      Member       |                                                                          Description                                                                          |
+===================+===============================================================================================================================================================+
| `interfaceVer`    | Exporter API version, one of :                                                                                                                                |
|                   |                                                                                                                                                               |
|                   | - Premiere Pro CC - `prExportVersion400`                                                                                                                      |
|                   | - Premiere Pro CS6 - `prExportVersion300`                                                                                                                     |
|                   | - Premiere Pro CS5.5 - `prExportVersion250`                                                                                                                   |
|                   | - Premiere Pro CS5 - `prExportVersion200`                                                                                                                     |
|                   | - Premiere Pro 4.0.1 through 4.2.1 - `prExportVersion101`                                                                                                     |
|                   | - Premiere Pro CS4 - `prExportVersion100`                                                                                                                     |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `getSPBasicSuite` | This very important call returns the SweetPea suite that allows plugins to acquire and release all other [SweetPea Suites](../universals/sweetpea-suites.md). |
|                   |                                                                                                                                                               |
|                   | ```SPBasicSuite* getSPBasicSuite();```                                                                                                                        |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
