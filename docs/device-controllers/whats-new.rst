.. _device-controllers/whats-new:

Whats New
################################################################################

What's New in CC October 2013
================================================================================

The new command *cmdSetDeviceHandler* was added. This command tells the device controller which panel is using the device controller -- either the Capture panel, or Export to Tape panel.

----

What's New in CC July 2013?
================================================================================

In the July 2013 release of CC, the new capability flag fCanPrintToTape was added for a device controller supporting Edit to Tape using the new panel to specify whether or not it supports Print to Tape mode. fCanDelayMovieStart was added for a device controller to optionally specify that it wants to handle Delay Movie Start on its own. If the flag is set, the value as set by

the user will be passed in DeviceRec.delayFrames during an Edit to Tape. The DeviceRec. version has been incremented to kDeviceControlAPIVersion13 for plug-ins to distinguish which version they are running in.

----

What's New in CC?
================================================================================

In CC, the new Edit to Tape panel provides an integrated UI with settings and controls for exporting a clip or sequence to tape. The device controller can optionally support various common settings in the Edit to Tape panel. Three types of record modes are now natively supported: Print to Tape, Insert, and Assemble modes. Although a device controller can still provide a custom setup dialog for any additional settings, the panel eliminates much of the need for custom UI. It also allows for integrated device presets, and some bonus capabilities like adding Bars and Tone / Black Video / Universal Counting Leader to the start of the edit to tape. To update your device controller to use the new panel, set fCanInsertNoUI along with any other flags during dsExecute/ cmdGetFeatures. Then take your *cmdInsertEdit* implementation and integrate your logic to respond to the new record modes sent in *cmdNewMode*.

----

What's New in CS6.0.1?
================================================================================

In CS6.0.1, DroppedFrameProc was added to give device controllers a way to get the number of frames dropped during an insert edit. A device controller can use this to provide the feature to abort an Export to Tape if frames are dropped. This method is already superceded by the new Edit to Tape panel functionality in CC.
