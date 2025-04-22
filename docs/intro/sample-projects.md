# Sample Projects

## Descriptions

+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|       Name        |                                                                                                               Description                                                                                                               |
+===================+=========================================================================================================================================================================================================================================+
| SDK File Importer | This importer supports .sdk media files.                                                                                                                                                                                                |
|                   |                                                                                                                                                                                                                                         |
|                   | To use the importer, choose File > Import, and select an .sdk file. Such files may be created using the SDK Exporter.                                                                                                                   |
|                   |                                                                                                                                                                                                                                         |
|                   | It supports uncompressed 8-bit RGB with or without alpha, and packed 10-bit YUV (v410).                                                                                                                                                 |
|                   |                                                                                                                                                                                                                                         |
|                   | It supports mono, stereo, and 5.1 audio at arbitrary sample rates and 32-bit float.                                                                                                                                                     |
|                   |                                                                                                                                                                                                                                         |
|                   | It supports trimming using the Project Manager, Properties and Data Rate Analysis, Unicode filenames, the avoidAudioConform flag, and can read video frames asynchronously.                                                             |
|                   |                                                                                                                                                                                                                                         |
|                   | It also features a test harness for multistream audio, which can be turned on by uncommenting the `MULTISTREAM_AUDIO_TESTING` define in the header.                                                                                     |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Synth Import      | This synthetic importer generates 8-bit YUV and RGB, video only.                                                                                                                                                                        |
|                   |                                                                                                                                                                                                                                         |
|                   | To use it, choose File > New > SDK Synthetic Importer.                                                                                                                                                                                  |
|                   |                                                                                                                                                                                                                                         |
|                   | When the clip is created, it demonstrates a sample settings dialog, which can be displayed again by double-clicking the clip in the Project Panel or Timeline Panel.                                                                    |
|                   |                                                                                                                                                                                                                                         |
|                   | Every time the settings dialog is displayed, it creates new footage in memory. It creates ten seconds of footage at 24 fps. The video consists of horizontal lines of random colors.                                                    |
|                   |                                                                                                                                                                                                                                         |
|                   | No file is created on disk for an example of that, see the Custom Importer.                                                                                                                                                             |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SDK Custom Import | This custom importer creates a clip similar to the Synth Import sample, but generates it to disk, rather than memory.                                                                                                                   |
|                   |                                                                                                                                                                                                                                         |
|                   | To use it, choose File > New > SDK Custom Importer.                                                                                                                                                                                     |
|                   |                                                                                                                                                                                                                                         |
|                   | Or, import an existing .sdkc clip from the File > Import dialog.                                                                                                                                                                        |
|                   |                                                                                                                                                                                                                                         |
|                   | On Windows, newly generated files with .sdkc file extensions are created in C:WindowsTemp. On macOS, they are created on the Desktop.                                                                                                   |
|                   |                                                                                                                                                                                                                                         |
|                   | After the sample settings dialog, it optionally displays a background frame from the timeline (useful for titlers).                                                                                                                     |
|                   |                                                                                                                                                                                                                                         |
|                   | The generated footage is between 2 and 30 frames at 24 fps, with a random resolution between 32 and 720 pixels wide and between 32 and 480 high, at DV NTSC pixel aspect ratio.                                                         |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ExportController  | Adds a new menu item to File > Export > SDK Export Controller.                                                                                                                                                                          |
|                   |                                                                                                                                                                                                                                         |
|                   | When selected, it displays a simple message box on Windows, takes the DV NTSC widescreen preset, and exports a file to `C:\Windows\Temp` on Windows, or to the Desktop on macOS.                                                        |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SDK Exporter      | This exporter writes .sdk files.                                                                                                                                                                                                        |
|                   |                                                                                                                                                                                                                                         |
|                   | To use it, choose File > Export > Media, and in the Export Settings choose File Type: SDK File.                                                                                                                                         |
|                   |                                                                                                                                                                                                                                         |
|                   | It supports uncompressed 8-bit RGB with or without alpha, and packed 10-bit YUV (v410).                                                                                                                                                 |
|                   |                                                                                                                                                                                                                                         |
|                   | It supports mono, stereo, and 5.1 audio at arbitrary sample rates and 32-bit float.                                                                                                                                                     |
|                   |                                                                                                                                                                                                                                         |
|                   | It demonstrates custom parameters, including a custom settings button.                                                                                                                                                                  |
|                   |                                                                                                                                                                                                                                         |
|                   | It also writes marker data to an .html file with the same filename.                                                                                                                                                                     |
|                   |                                                                                                                                                                                                                                         |
|                   | To write files with v410 compression using 8-bit RGB sources, this sample uses routines to convert the 8-bit RGB data to 32-bit RGB, then to 32-bit YUV, and finally to v410.                                                           |
|                   |                                                                                                                                                                                                                                         |
|                   | These same routines may be adapted for transitions, filters, and other plugin types.                                                                                                                                                    |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Transmitter       | The sample transmit plugin does not output to any hardware, but can be used to step through interactions between the host and plugin in the debugger.                                                                                   |
|                   |                                                                                                                                                                                                                                         |
|                   | To use it, go the the Preferences > Playback, and choose the SDK Transmitter as the Audio Device, and as a Video Device.                                                                                                                |
|                   |                                                                                                                                                                                                                                         |
|                   | This transmit plugin provides the basic structure, separating concepts of plugin and instance. For video, it declares support for any pixel format and resolution.                                                                      |
|                   |                                                                                                                                                                                                                                         |
|                   | For audio, it declares support for 2 channels. It also declares a small latency value for demonstrative purposes.                                                                                                                       |
|                   |                                                                                                                                                                                                                                         |
|                   | On Windows, there is some basic debug logging.                                                                                                                                                                                          |
|                   |                                                                                                                                                                                                                                         |
|                   | It does not actually provide it's own clock at this time, but on playback it simply pretends to step forward a frame with every frame received.                                                                                         |
|                   |                                                                                                                                                                                                                                         |
|                   | This may result in some bug behavior such as playing back at speeds faster or slower than normal, depending on how fast the host can push frames.                                                                                       |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SDK_ProcAmp       | This GPU-accelerated effect demonstrates a simple ProcAmp effect using the After Effects API with the Premiere Pro GPU extensions.                                                                                                      |
|                   |                                                                                                                                                                                                                                         |
|                   | The effect is found in the SDK folder of the Video Effects in the Effects Control panel.                                                                                                                                                |
|                   |                                                                                                                                                                                                                                         |
|                   | It supports Metal acceleration.                                                                                                                                                                                                         |
|                   |                                                                                                                                                                                                                                         |
|                   | **This sample requires macOS 10.11.4 and later.**                                                                                                                                                                                       |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Vignette          | This effect creates a vignette on video using the After Effects API with the Premiere Pro GPU extensions.                                                                                                                               |
|                   |                                                                                                                                                                                                                                         |
|                   | Has CUDA and software render paths.                                                                                                                                                                                                     |
|                   |                                                                                                                                                                                                                                         |
|                   | Software rendering in Premiere Pro includes 8-bit/32-bit RGB/ YUV software render paths.                                                                                                                                                |
|                   |                                                                                                                                                                                                                                         |
|                   | Software rendering in After Effects includes 8-bit and 32-bit smart rendering.                                                                                                                                                          |
|                   |                                                                                                                                                                                                                                         |
|                   | Thanks to Bart Walczak for donating this sample.                                                                                                                                                                                        |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SDK_CrossDissolve | This GPU-accelerated transition demonstrates a simple cross dissolve transition using the After Effects API with the transition extensions.                                                                                             |
|                   |                                                                                                                                                                                                                                         |
|                   | The transition is found in the SDK folder of the Video Transitions in the Effects Control panel.                                                                                                                                        |
|                   |                                                                                                                                                                                                                                         |
|                   | It supports CUDA acceleration.                                                                                                                                                                                                          |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ControlSurface    | You should see the plugin in the PPro UI in Preferences > Control Surface, when you hit the Add button, as one of the options in the Device Class drop-down next to Mackie and EUCON (currently shows as "SDK Control Surface Sample"). |
|                   |                                                                                                                                                                                                                                         |
|                   | Just a starting point for you to add your functionality.                                                                                                                                                                                |
+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

---

## How To Build the SDK Sample Projects

The required development environment is described in [SDK Audience](sdk-audience.md).

See a quickstart video on building an effect using a similar SDK (on macOS) [here](https://assets.adobe.com/public/08c43fb7-4633-4007-5201-b3b77405d770?scid=social_20180227_75678337).

We've combined the sample projects into a single master project, stored in the Examples folder of the SDK.

For macOS it is BuildAll.xcodeproj; for Windows, it is \_BuildAll.sln.

You'll need to specify some settings so that the plugins are built into a folder where they will be loaded by the application you are developing for.

We recommend plugins be built into the following folder for macOS: `/Library/Application Support/Adobe/Common/Plugins/[version]/MediaCore/`

Version is locked at 7.0 for all CC versions, or CSx for earlier versions.

For example: `/Library/Application Support/Adobe/Common/Plugins/7.0/MediaCore/`

or: `/Library/Application Support/Adobe/Common/Plugins/CS6/MediaCore/`

and the following path for Windows:

`[Program Files]\Adobe\Common\Plugins\[version]\MediaCore\\`

for example: `C:\Program Files\Adobe\Common\Plugins\7.0\MediaCore\\`

or: `C:\Program Files\Adobe\Common\Plugins\CS6\MediaCore\\`

!!! note
    This Windows path is only recommended for development purposes.

In Xcode, set the build location for the project in File > Project Settings. Press the Advanced button. Under Build Location choose Custom, select Absolute, and set the Products path.

In Visual Studio, for convenience, we have set the Output File for all sample projects to use the base path set by the environment variable PREMSDKBUILDPATH. You'll need to set this as a user environment variable for your system, and shown in the screenshot below.

![Setting Environment Variables](../_static/env-vars.png "Setting Environment Variables")
*Setting Environment Variables*

1. On Windows, right-click *My Computer > Properties*, and in the left sidebar choose *Advanced System Settings*.
2. In the dialog that appears, hit the *Environment Variables* button.
3. In the *User variables*, create a new variable named PREMSDKBUILDPATH, with the path as described above. (e.g. "C:Program FilesAdobeCommonPlugins[version]MediaCore").
4. Log out of Windows, and log back in so that the variable will be set.

When compiling the plugins, if you see a link error such as:

"Cannot open file "[MediaCore plugins path]plugin.prm", make sure to launch Visual Studio in administrator mode. In your Visual Studio installation, right-click devenv.exe, Properties > Compatibility > Privilege Level, click "Run this program as an administrator".

It's not recommended to copy plugins into the plugin folder after you've built them, because that won't allow you to debug the plugins while the host application is running.
