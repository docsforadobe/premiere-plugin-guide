.. _exporters/additional-details:

Additional Details
################################################################################

Multiplexer Tab Ordering
================================================================================

If your exporter provides a Multiplexer tab like some of the built-in exporters do, you may find that it appears after the Video and Audio tab, rather than before those tabs as in the case of our exporters. The key is to use the following define as the parameter identifer for the multiplexer tab group:

.. code-block:: cpp

  #define ADBEMultiplexerTabGroup "ADBEAudienceTabGroup"

----

Creating a Non-Editable String in the Parameter UI
================================================================================

During ``exSelGenerateDefaultParams``, add a parameter with ``exNewParamInfo.flags = exParamFlag_none``.

Then during ``exSelPostProcessParams``, call ``AddConstrainedValuePair()`` in the :ref:`exporters/suites.export-param-suite`.

If you only add one value pair, then the parameter will be a non-editable string.

In the case of the SDK Exporter sample, it adds two, which appear as a pair of radio buttons side-by-side.

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
d. You should see the "Others – 3rd Party Plugins" in the list of formats. Select this.
e. Your preset should be seen in the drop-down.

Return Values
********************************************************************************

Premiere Elements 8 uses a slightly different definition of the return values. Use the following definition instead:

.. code-block:: cpp

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
