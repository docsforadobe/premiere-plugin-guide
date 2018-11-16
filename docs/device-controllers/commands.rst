.. _device-controllers/commands:

Commands
################################################################################

When the plug-in receives ``dsExecute``, DeviceRec.command indicates the behavior requested.

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
|            **Command**            |                                                                   **Description**                                                                    |
+===================================+======================================================================================================================================================+
| ``cmdGetFeatures``                | Fill in the features field with the device's features.                                                                                               |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cmdStatus``                     | Return the deck mode and current timecode position.                                                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cmdNewMode``                    | Change the deck's mode.                                                                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cmdGoto``                       | Move asynchronously to a particular time and return in pause mode.                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cmdLocate``                     | Move synchronously to a particular time and return in play mode.                                                                                     |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cmdShuttle``                    | Shuttle the deck at a specified rate.                                                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cmdEject``                      | Eject media.                                                                                                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cmdInsertEdit``                 | No longer needed in CC and later, if the Edit to Tape panel is supported.                                                                            |
|                                   |                                                                                                                                                      |
|                                   | In previous versions this was sent for Export To Tape. This has been left in for backwards-compatibility.                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cmdGetDeviceDisplayName``       | Provide the device display name for display in the Capture Panel.                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cmdSetDropness``                | Tells the device controller whether the current timecode is drop-frame or non-drop-frame.                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cmdGetCurrentDeviceIdentifier`` | For internal use only.                                                                                                                               |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``cmdSetDeviceHandler``           | New in CC October 2013. Optional. Tells the plug-in which panel is using the device controller -- either the Capture panel, or Export to Tape panel. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

----

cmdGetFeatures
================================================================================

Populate DeviceRec.features with the features of your device controller, using the following flags OR'd together in a bit-field:

+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|        **Flag**         |                                                                                            **Description**                                                                                            |
+=========================+=======================================================================================================================================================================================================+
| ``fExportDialog``       | The device controller has an export dialog and wishes to control the edit.                                                                                                                            |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fCanInsertEdit``      | No longer needed in CC. In previous versions, this flag would tell Premiere that Insert Edit mode ws supported.                                                                                       |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fDrvrQuiet``          | Quiet mode is supported.                                                                                                                                                                              |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fHasJogMode``         | Jog is supported.                                                                                                                                                                                     |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fCanEject``           | Media ejection is supported.                                                                                                                                                                          |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fStepFwd``            | Stepping the device forward one frame is supported.                                                                                                                                                   |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fStepBack``           | Stepping the device backward one frame is supported.                                                                                                                                                  |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fRecord``             | Your device can record.                                                                                                                                                                               |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fPositionInfo``       | Your device can retrieve position information.                                                                                                                                                        |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fGoto``               | Your device can seek to a particular frame. You must also set ``fPositionInfo``, and respond to *cmdGoto*.                                                                                            |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``f1_5``                | Your device can play at one-fifth speed.                                                                                                                                                              |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fBasic``              | Your device supports the basic five deck control operations: stop, play, pause, fast-forward, and rewind.                                                                                             |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fReversePlay``        | Your device can play in reverse.                                                                                                                                                                      |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fCanLocate``          | Your device can accurately locate a particular timecode and supports ``cmdLocate``. Please do so; cmdLocate is more accurate than *cmdGoto*.                                                          |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fCanShuttle``         | Your device is capable of variable-speed shuttle operations, forward and backward.                                                                                                                    |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fNoTransport``        | Device supports no transport modes (play, stop, etc).                                                                                                                                                 |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fCanAssembleEdit``    | New in CC. Set if the device controller supports ``modeRecordAssemble``.                                                                                                                              |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fCanPreviewEdit``     | New in CC. Set if modePreviewRecord is supported for the Edit to Tape panel.                                                                                                                          |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fCanInsertNoUI``      | New in CC. Set if new Edit to Tape panel is supported. Otherwise, legacy device controllers can continue to function as previously built for CS6 and earlier.                                         |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fCanUseCC``           | New in CC. Set if Closed Captioning is supported. This will enable the Insert Closed Captioning Data checkbox in the Edit to Tape panel.                                                              |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fCanPrintToTape``     | New in CC July 2013. Set to tell Premiere Pro that the device controller supports the "Print to Tape" option in the Export Type popup of the Edit to Tape panel.                                      |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fCanDelayMovieStart`` | New in CC July 2013. Set this flag to specify that the device controller wants to handle Delay Movie Start on its own.                                                                                |
|                         |                                                                                                                                                                                                       |
|                         | If the flag is set, the value as set by the user (in frames) in the Edit to Tape panel will be passed in ``DeviceRec.delayFrames``, and Premiere Pro will let the device controller handle the delay. |
+-------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

cmdStatus
================================================================================

Premiere sends ``cmdStatus`` to obtain the deck's current mode (play, pause, etc.) and the current timecode position. Store the device's current mode in mode, and the current timecode value in timecode. Be sure to set timerate and timeformat as described in DeviceRec.

The values of mode and timecode persist. If you only know one of the two pieces of information, store it, and ignore the other. If your device controller makes two calls to determine these values, alternately request one and return the other.

----

cmdNewMode
================================================================================

Puts the device into a new operating mode, specified in mode.

+---------------------------+--------------------------------------------------------------------------------------------------+
|         **Mode**          |                                         **Description**                                          |
+===========================+==================================================================================================+
| ``modeStop``              | Stop.                                                                                            |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modePlay``              | Play.                                                                                            |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modePlay1_5``           | Play at 1/5 speed.                                                                               |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modePlay1_10``          | Play at 1/10 speed.                                                                              |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modePause``             | Pause.                                                                                           |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modeFastFwd``           | Fast forward.                                                                                    |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modeRewind``            | Rewind.                                                                                          |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modeRecord``            | Record. This is the original record mode for Print to Tape.                                      |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modeGoto``              | Go to time specified in DeviceRec.timecode.                                                      |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modeStepFwd``           | Step one frame forward.                                                                          |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modeStepBack``          | Step one frame backward.                                                                         |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modePlayRev``           | Play backward at full speed.                                                                     |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modePlayRev1_5``        | Play backward at 1/5 speed.                                                                      |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modePlayRev1_10``       | Play backward at 1/10 speed.                                                                     |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modeTapeOut``           | No tape is in device.                                                                            |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modeLocal``             | Device is unavailable.                                                                           |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modeRecordPause``       | Pause in record mode.                                                                            |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modeRecordPlayFastFwd`` | Fast forward in play mode.                                                                       |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modeRecordPlayRewind``  | Rewind in play mode.                                                                             |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modeRecordAssemble``    | New in CC. This is selected by the user in the Edit to Tape panel, in the Export Type drop-down. |
+---------------------------+--------------------------------------------------------------------------------------------------+
| ``modeRecordInsert``      | New in CC. This is selected by the user in the Edit to Tape panel, in the Export Type drop-down. |
+---------------------------+--------------------------------------------------------------------------------------------------+

----

cmdGoto
================================================================================

This is sent, for example, when typing in a new timecode value into the current timecode hot-text control in the lower left hand corner of the Capture panel. It can also be sent when the user chooses Capture In/Out, if the device controller does not support ``cmdLocate``.

Begin seeking to the timecode specified by timecode. Set up an asynchronous seek, save off the desired timecode in private data, and return immediately with mode set to modeGoto.

Premiere will then send ``cmdStatus`` repeatedly, so that you can continue to query the timecode of the device as it moves toward the desired timecode. In modeGoto, Premiere will put "Searching..." in the status panel. Later, when the device arrives at the desired timecode, place

the device in modePause (if you were able to complete the seek) or modeStop (if there was an error).

----

cmdLocate
================================================================================

This is sent, for example, when the user chooses Capture In/Out, if the device controller has set ``fCanLocate`` during *cmdGetFeatures*.

Seek to an exact frame specified in DeviceRec.timecode, minus any amount specified by the Preroll Time, and return immediately with the device in modePlay. Unlike *cmdGoto*, which is asynchronous, this is a synchronous operation. Do not return until the operation is complete or an error occurs.

----

cmdShuttle
================================================================================

Sent when the user moves the shuttle control; mode is the shuttle speed:

Use intermediate speeds if the device supports them. If it doesn't implement shuttling but does support multiple play speeds, Premiere will simulate shuttling by playing at different rates, based on the shuttle control position. Better results can be obtained by directly supporting shuttling with the *cmdShuttle* command.

----

cmdInsertEdit
================================================================================

No longer needed starting in CC, if the Edit to Tape panel is supported. Otherwise, this was sent if the device controller supports insert mode and wants to control the edit (set ``fExportDialog`` and fCanInsertEdit during *cmdGetFeatures* to do so).

When the user invokes Export To Tape, Premiere prepares to play the chosen clip and sets the following in the DeviceHand:

::

  command = *cmdInsertEdit*
  mode = modeRecord
  xTimecode = duration of the movie

Premiere then enters a loop, calling the device controller with the above DeviceHand. When the device controller returns, Premiere sends the PrintProc specified in ``DeviceHand.setupWaitProc``. Premiere will have already performed the preroll; everything is ready to play.

When the device controller returns, Premiere plays the clip, sending idle to PrintProc once per frame. Premiere again calls the plug-in's entry point with the DeviceHand, allowing the device controller to perform any cue operations. Premiere calls PrintProc with complete when finished. If *cmdInsertEdit* is proceeding correctly PrintProc should always return 0.

----

cmdGetDeviceDisplayName
================================================================================

Sent so the device controller can provide the device display name for display in the Capture Panel. The device controller fills in DeviceRec.displayName.

----

cmdSetDropness
================================================================================

Sent only if DeviceRec.autoDetectDropness is set to true. This selector tells the device controller whether the current timecode is drop-frame or non-drop-frame, as determined by the active recorder. The timecode information is passed in videoStreamIsDrop in DeviceRec. Sent when recorder determines drop-frame attribute and calls FormatChangedFunc.

----

cmdSetDeviceHandler
================================================================================

New in CC October 2013. Optional. Tells the plug-in which panel is using the device controller -- either the Capture panel, or Export to Tape panel. DeviceRec.mode will contain either handlerCapture or handlerEditToTape.
