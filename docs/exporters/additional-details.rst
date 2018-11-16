.. _exporters/additional-details:

Additional Details
################################################################################

Multiplexer Tab Ordering
================================================================================

If your exporter provides a Multiplexer tab like some of the built-in exporters do, you may find that it appears after the Video and Audio tab, rather than before those tabs as in the case of our exporters. The key is to use the following define as the parameter identifer for the multiplexer tab group:

::

  #define ADBEMultiplexerTabGroup "ADBEAudienceTabGroup"

----

Creating a Non-Editable String in the Parameter UI
================================================================================

During ``exSelGenerateDefaultParams``, add a parameter with ``exNewParamInfo.flags = exParamFlag_none``.

Then during ``exSelPostProcessParams``, call ``AddConstrainedValuePair()`` in the :ref:`exporters/suites.export-param-suite`.

If you only add one value pair, then the parameter will be a non-editable string.

In the case of the SDK Exporter sample, it adds two, which appear as a pair of radio buttons side-by-side.

----

.. _exporters/additional-details.guidelines-for-exporters-in-encore:

Guidelines for Exporters in Encore
================================================================================

Starting in CS5, third-party exporters can now be used to transcode assets to MPEG-2 or Blu-ray compliant files. Currently, the option to choose a third-party exporter is only available on a per-clip basis, not on a project-wide basis. The user will need to right-click on an asset in the Project panel, choose Transcode Settings, and choose the third-party preset from the Quality Preset drop-down.

Prior to CS6, Encore was a 32-bit application. So if you are developing plug-ins for Encore CS5, use the CS5 headers to create 32-bit plug-ins. We have left the 32-bit configurations in the

sample projects to facilitate this. Install the exporter in the Encore application folder at Plug-ins/ Common/. Note that on Mac OS, this subfolder is in within the application package.

Naming Your Exporter
********************************************************************************

Encore only uses the MPEG2-DVD and MPEG2 Blu-ray formats for transcoding to MPEG2-DVD and MPEG2 Blu-ray formats, respectively. Currently it looks for the substrings "MPEG2-DVD", "MPEG2 Blu-ray" and "H.264 Blu-ray" in the exporter name to identify the video format of the exporter, and to enable it within the Encore UI. So the format name returned from exporter plug-in should contain one of these as a substring, in order for it to be usable within Encore.

For example "My MPEG2 Blu-ray", "Accelerated MPEG2-DVD", etc. Please avoid using the exact same names as the built-in formats to avoid conflict.

Naming Your Output
********************************************************************************

Encore uses the exporters to create elementary video and audio streams (muxing is switched to off during transcoding). The output file extensions should be standard ones: .m2v for MPEG2-DVD, MPEG2 Blu-ray video formats, .m4v for H.264 Blu-ray; .ac3 for Dolby audio, .wav for PCM, .mpa for MPEG-1 Layer 2.

Parameters
********************************************************************************

Please refer to the built-in MPEG2-DVD and MPEG2 Blu-ray formats present in Encore to get familiar with the typical exporter user interface in Encore. Having UI properties similar to the built-in formats in Encore will make it easier to integrate a third-party exporter.

The audio formats available in an exporter should correspond to the same choices as available in Encore for a DVD or Blu-ray project. In an MPEG-2 DVD exporter, the audio formats should be either Dolby Digital 2.0 (stereo), MPEG-1 Layer 2 audio in stereo or PCM audio (48kHz). For an MPEG2 Blu-ray exporter, only the Dolby and the PCM formats should be available. For more details regarding audio formats supported in Encore, please refer to the Encore help documentation. Allowing audio formats other than these for encoding will not work in Encore due to the constraints of the DVD/Blu-ray disc specifications.

Encore will need to access many of the exporter's encoding parameters. It may even modify some of the encoding parameters during the transcoding to MPEG-2 DVD and Blu-ray formats, so that the encoding stays within the bit-budget constraints of the project. So a third-party exporter must use specific property identifiers and property types. If these parameters are not used, then there

is little guarantee of the correctness of the encoded file and the size of the final disc, since Encore will not be able to control the settings of the exporter to apply the size constraints to the output files. Below is a list of the properties with their identifiers and types that an exporter plugin must support:

+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+
| **Property Identifier**            | **Required**                           | **Property type**              | **Description**                                                               |
+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+
| ``ADBEVideoWidth``                 | Yes                                    | ``exParamType_int``            | Frame width                                                                   |
+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+
| ``ADBEVideoHeight``                | Yes                                    | ``exParamType_int``            | Frame height                                                                  |
+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+
| ``ADBEVideoVBR``                   | No                                     | ``exParamType_int``            | Type of encoding (constant/variable bitrate, 1 / 2 passes)                    |
|                                    |                                        | Constrained value list         |                                                                               |
|                                    |                                        |                                | - 0 = CBR                                                                     |
|                                    |                                        |                                | - 1 = VBR, 1 Pass                                                             |
|                                    |                                        |                                | - 2 = VBR, 2 Pass                                                             |
+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+
| - ``ADBEVideoBitRate``             | No                                     | ``exParamType_float``          | Video bitrate(s) (Mbps)                                                       |
| - ``ADBEVideoMaxBitRate``          |                                        |                                |                                                                               |
| - ``ADBEVideoAvgBitRate``          |                                        |                                | For CBR encoding use the first parameter.                                     |
| - ``ADBEVideoMinBitRate``          |                                        |                                |                                                                               |
|                                    |                                        |                                | For VBR encoding use parameters 2-4                                           |
+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+
| ``ADBEVideoFPS``                   | Yes                                    | ``exParamType_ticksFrameRate`` | Frame rate                                                                    |
+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+
| ``ADBEMPEGCodecBroadcastStandard`` | Yes                                    | ``exParamType_int``            | - 0 = NTSC                                                                    |
|                                    |                                        | Constrained value list         | - 1 = PAL                                                                     |
|                                    |                                        |                                | - 2 = SECAM                                                                   |
+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+
| ``ADBEVideoAspect``                | No                                     | ``exParamType_int``            | Frame aspect ratio                                                            |
|                                    |                                        | Constrained value list         |                                                                               |
|                                    |                                        |                                | - 1 = Square 1:1                                                              |
|                                    |                                        |                                | - 2 = Standard 4:3                                                            |
|                                    |                                        |                                | - 3 = Widescreen16:9                                                          |
+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+
| ``ADBEVMCMux_Type``                | No                                     | ``exParamType_int``            | Encore needs a way to switch off muxing as it creates only elementary streams |
|                                    |                                        | Constrained value list         |                                                                               |
|                                    |                                        |                                | - 0 = MPEG-1                                                                  |
|                                    |                                        |                                | - 1 = VCD                                                                     |
|                                    |                                        |                                | - 2 = MPEG-2                                                                  |
|                                    |                                        |                                | - 3 = SVCD                                                                    |
|                                    |                                        |                                | - 4 = DVD                                                                     |
|                                    |                                        |                                | - 5 = TS                                                                      |
|                                    |                                        |                                | - 6 = None                                                                    |
+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+
| ``ADBEVideoFieldType``             | No                                     | ``exParamType_int``            | - 0 = Progressive                                                             |
|                                    |                                        | Constrained value list         | - 1 = Upper field first                                                       |
|                                    |                                        |                                | - 2 = Lower field first                                                       |
+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+
| ``ADBEAudioCodec``                 | Yes                                    | ``exParamType_int``            | Use these 4CCs for values                                                     |
|                                    |                                        | Constrained value list         | - 'dlby' – Dolby                                                              |
|                                    |                                        |                                | - 'PCMA' – PCM                                                                |
|                                    |                                        |                                | - 'mpa ' – MPEG-1 Layer 2                                                     |
+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+
| ``ADBEAudio_Endianness``           | Optional                               | ``exParamType_int``            | If using Dolby audio; Encore will set to big endian for AC3 files             |
|                                    |                                        | Constrained value list         |                                                                               |
|                                    |                                        |                                | - 0 = little endian                                                           |
|                                    |                                        |                                | - 1 = big endian                                                              |
+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+
| ``ADBEAudioBitrate``               | Yes, for Dolby and MPEG-2 audio codecs | ``exParamType_int``            | Audio codec bitrate (kbps)                                                    |
+------------------------------------+----------------------------------------+--------------------------------+-------------------------------------------------------------------------------+

----

.. _exporters/additional-details.guidelines-for-exporters-in-premiere-elements:

Guidelines for Exporters in Premiere Elements
================================================================================

First, make sure you are building the exporter using the right SDK. Premiere Elements 8 requires the Premiere Pro CS4 SDK. The next version of Premiere Elements will likely use the CS5 SDK.

Exporter Preset
********************************************************************************

For an exporter to show up in the Premiere Elements UI, you'll need to create and install a preset in a specific location:

1) Create a folder named "OTHERS" in [App installation folder]/sharingcenter/Presets/pc/
2) Create a sub-folder with your name (e.g. MyCompany) under OTHERS and place the preset file (.epr) in it. The final path of the preset file should be something like [App installation folder]/ sharingcenter/Presets/pc/OTHERS/MyCompany/MyPreset.epr
3) Relaunch Premiere Elements.

a. Add a clip to the timeline
b. Goto the "Share" tab
c. Under that choose "Personal Computer"
d. You should see the "Others – 3rd Party Plug-ins" in the list of formats. Select this.
e. Your preset should be seen in the drop-down.

Return Values
********************************************************************************

Premiere Elements 8 uses a slightly different definition of the return values. Use the following definition instead:

::

  enum {
    exportReturn_ErrNone = 0,
    exportReturn_Abort,
    exportReturn_Done,
    exportReturn_InternalError,
    exportReturn_OutputFormatAccept,
    exportReturn_OutputFormatDecline,
    exportReturn_OutOfDiskSpace,
    exportReturn_BufferFull,
    exportReturn_ErrOther,
    exportReturn_ErrMemory,
    exportReturn_ErrFileNotFound,
    exportReturn_ErrTooManyOpenFiles,
    exportReturn_ErrPermErr,
    exportReturn_ErrOpenErr,
    exportReturn_ErrInvalidDrive,
    exportReturn_ErrDupFile,
    exportReturn_ErrIo,
    exportReturn_ErrInUse,
    exportReturn_IterateExporter,
    exportReturn_IterateExporterDone,
    exportReturn_InternalErrorSilent,
    exportReturn_ErrCodecBadInput,
    exportReturn_ErrLastErrorSet,
    exportReturn_ErrLastWarningSet,
    exportReturn_ErrLastInfoSet,
    exportReturn_ErrExceedsMaxFormatDuration,
    exportReturn_VideoCodecNeedsActivation,
    exportReturn_AudioCodecNeedsActivation,
    exportReturn_IncompatibleAudioChannelType,
    exportReturn_Unsupported = -100
  };

The red values are unique to Premiere Elements 8, and shifted the subsequent return values 2 values higher than their definition in the Premiere Pro SDK.
