# Premiere Pro plugin Types

+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                        Type                                        |                                                                        Description                                                                        |
+====================================================================================+===========================================================================================================================================================+
| [Importers](../importers/importers.md)                                             | Import video and audio media into Premiere.                                                                                                              |
|                                                                                    |                                                                                                                                                           |
|                                                                                    | Synthetic importers, a subset, dynamically synthesize media without creating an actual file on disk.                                                     |
|                                                                                    |                                                                                                                                                           |
|                                                                                    | Custom importers, dynamically synthesize media to disk.                                                                                                  |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Export Controllers](../export-controllers/export-controllers.md)                  | Can drive any exporter to generate a file in any format and perform custom post-processing operations.                                                   |
|                                                                                    |                                                                                                                                                           |
|                                                                                    | Developers wanting to integrate Premiere Pro with an asset management system will want to use this API instead of the exporter API.                      |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Exporters](../exporters/exporters.md)                                             | Allows the user to output media to disk.                                                                                                                 |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Transmitters](../transmitters/transmitters.md)                                    | Sends video, audio, and closed captioning to any external device during playback and editing.                                                            |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Video Filters](../video-filters/video-filters.md)                                 | **We strongly recommend using the After Effects SDK to develop effects plugins. Most of the effects included in Premiere Pro are After Effects plugins.** |
|                                                                                    |                                                                                                                                                           |
|                                                                                    | Process a series of video frames with parameters that can be animated over time.                                                                         |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [GPU Effects & Transitions](../gpu-effects-transitions/gpu-effects-transitions.md) | Process two video sources into a single destination over time.                                                                                           |
|                                                                                    |                                                                                                                                                           |
|                                                                                    | This API is based on the After Effects API, with certain functions to enable transition functionality in Premiere Pro.                                   |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Control Surfaces](../control-surfaces/control-surfaces.md)                        | Interface with a hardware control surface to support audio mixing, basic transport controls, and the Lumetri Color panel.                                |
|                                                                                    |                                                                                                                                                           |
|                                                                                    | The API supports two-way communication with Premiere Pro, so that motorized hardware faders, VU meters, etc can be in sync with the application.         |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

## Other Supported plugin Standards

+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          Type           |                                                                                        Description                                                                                        |
+=========================+===========================================================================================================================================================================================+
| Adobe After Effects API | Premiere Pro supports a portion of the AE API.                                                                                                                                           |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                         |                                                                                                                                                                                           |
|                         | The After Effects SDK is not included in the Premiere Pro SDK.                                                                                                                           |
|                         |                                                                                                                                                                                           |
|                         | The last chapter in the After Effects SDK Guide.pdf, included in the After Effects SDK, contains information on known differences with how Premiere Pro supports the AE API.             |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VST                     | Starting in CC, Premiere supports version 3 of the VST specification for audio effects.                                                                                                  |
|                         |                                                                                                                                                                                           |
|                         | In CS6.x and previous versions, support was limited to version 2.4.                                                                                                                      |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ASIO                    | An ASIO driver is often provided in addition to a transmit plugin, to provide audio output during editing, playback, and Export To Tape.                                                 |
|                         |                                                                                                                                                                                           |
|                         | Prior to CS6, an ASIO driver was required to support audio input for voiceover recording in the audio mixer. On macOS, a Core Audio component may be provided rather than an ASIO driver. |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Core Audio              | macOS only. May be provided instead of an ASIO driver.                                                                                                                                   |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

---

### Plugin Support Across Adobe Video and Audio Applications

This chart shows which third-party plugins are supported by the various Video and Audio applications.

|                             | Premiere Pro | After Effects | Media Encoder | Audition | Character Animator | Prelude |
| --------------------------- | ------------ | ------------- | ------------- | -------- | ------------------ | ------- |
| After Effects AEGPs         |              | X             |               |          |                    |         |
| After Effects effects       | X            | X             |               |          |                    |         |
| After Effects transitions   | X            |               |               |          |                    |         |
| ASIO                        | X            | X             |               | X        |                    | X       |
| Control Surfaces            | X            |               |               | X        |                    |         |
| CoreAudio                   | X            | X             |               | X        |                    | X       |
| Premiere device controllers | X            |               |               |          |                    |         |
| Premiere export controllers | X            |               |               |          |                    |         |
| Premiere exporters          | X            | X             | X             | X        |                    |         |
| Premiere importers          | X            | X             | X             | X        |                    | X       |
| Premiere recorders          | X            |               |               |          |                    |         |
| Premiere transmitters       | X            | X             |               |          | X                  | X       |
| Premiere video filters      | X            |               |               |          |                    |         |
| QuickTime codecs            | X            | X             | X             | X        |                    | X       |
| Transitions                 | X            |               |               |          |                    |         |
| VfW codecs                  | X            | X             | X             | X        |                    | X       |
| VST audio effects           | X            |               |               | X        |                    |         |

---

### Premiere Elements Plugin Support

Premiere Elements uses the same core libraries for plugin support that Premiere Pro does, although Premiere Elements is 32-bit, whereas Premiere Pro is 64-bit starting with CS5.

| Premiere Elements version | Equivalent Premiere Pro API version |
| ------------------------- | ----------------------------------- |
| 12                        | CS6                                 |
| 11                        | CS5.5                               |
| 10                        | CS5.5                               |
| 9                         | CS5                                 |
| 8                         | CS4                                 |

It's always important to test the plugin fully in each application before advertising compatibility.

Check out [Guidelines for Exporters in Premiere Elements](../exporters/additional-details.md#guidelines-for-exporters-in-premiere-elements) for instructions on how to set up your exporter to be used in Premiere Elements.

---

### What Exactly Is a Premiere Pro Plugin?

Premiere plugins contain a single entry point of a type specific to each API.

Plugins are DLLs on Windows, and Carbon or Cocoa Bundles on macOS.

Plugins in the \\Plugins[language] folder, and any of its subfolders, will be loaded at launch.

Plugins can have private resources.

Only one plugin per file is parsed, unlike After Effects and Photoshop plugins, which can contain multiple entry points.
