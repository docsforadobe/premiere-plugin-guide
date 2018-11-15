.. _recorders/whats-new:

Whats New
################################################################################

What's New in Premiere Pro CC 2014?
================================================================================

A new return code was added, rmRequiresRoyaltyContent. Return this from recmod_Startup8 or recmod_StartRecord, if the codec used is unlicensed.

----

What's New in Premiere Pro CS6?
================================================================================

The parent window handle is now properly passed in, during ``recmod_ShowOptions`` when a re- corder should display its modal setup dialog.

----

What's New in Premiere Pro CS5?
================================================================================

Recorders can now display audio meters in the Audio Master Meters panel while previewing and capturing. Just use the new AudioPeakDataFunc callback passed in recOpenParms with ``recmod_Open``.

----

What's New in Premiere Pro CS4?
================================================================================

Audio settings in the Capture Settings window are no longer supported. Any audio settings should be in the custom dialog shown by the recorder during ``recmod_ShowOptions``. Recorders should no longer set the acceptsAudioSettings flag in recInfoRec8.

No More Project Presets
********************************************************************************

Since Premiere Pro CS4 support sequence-specific settings, project presets have been replaced by sequence presets. The difference from project presets are that sequence presets do not contain information to initialize capture settings. This means that users will have to initialize capture set- tings manually the first time they use a recorder with custom settings.

When the Capture Panel is invoked, if the capture settings are invalid or uninitialized, the Capture Settings dialog is invoked. In the Capture Settings dialog: If the recorder requires private data, the user cannot continue past the Capture Settings dialog until they have opened the current recorder's settings dialog.

----

What's New in Premiere Pro CS3?
================================================================================

A new function, GetDeviceTimecodeFunc, can be used to ask the device controller for its current timecode.

A new return value, rmRequiresCustomPrefsError, should be returned on ``recmod_SetActive`` if there are no valid capture prefs.
