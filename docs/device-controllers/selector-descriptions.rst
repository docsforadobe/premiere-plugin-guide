.. _device-controllers/selector-descriptions:

Selector Descriptions
################################################################################

dsInit
================================================================================

This will be sent when the device controller is selected in the UI for the first time, because no device controller private data is stored in the application preferences. When there is already existing private data in the preferences, *dsRestart* will be sent instead. To delete the preferences, hold down Ctrl-Alt-Shift on Win and Ctrl-Opt-Shift on MacOS when launching the app.

Allocate a memory handle to private data, and store the handle in DeviceRec.deviceData.

Initialize the hardware connection, and choose a default operating mode if more than one is available.

A dialog can be presented to prompt the user for settings.

If the connection fails, return dmDeviceNotFound.

Keep in mind, though, that the host will still send messages to the device controller, in case the hardware comes on-line later.

----

dsRestart
================================================================================

Reestablish connections to hardware devices.

This selector is similar to ``dsInit``, but the private instance data, deviceData, is already populated.

If you have just modified the definition of the private data structure, you can run into problems unless you provide some version checking here.

``dsInit`` can fall into the ``dsRestart`` case.

----

dsSetup
================================================================================

This selector is sent when the user hits the Device Settings button in the Edit to Tape panel, the Options button in the Device Control area of the Capture panel, or the Options button in the Device Control area of the Preferences.

Display a modal dialog with any user settings and info the device controller wishes to show the user. If your device controller doesn't require user input, this selector can be safely ignored, but should return dmNoErr. To specify that the Setup button in the device control options should not be shown, respond to *dsHasOptions*.

----

dsExecute
================================================================================

Perform a device control operation based on the command in the DeviceRec. See the Commands section below for detailed descriptions.

----

dsCleanup
================================================================================

Disconnect from hardware and dispose of the plug-in's private instance data (stored in ``deviceData``).

----

dsQuiet
================================================================================

Like ``dsCleanup``; disconnect from the device, but don't dispose of private instance data.

``dsRestart`` will be sent to reconnect the device.

----

dsHasOptions
================================================================================

Return dmHasNoOptions to disable the device controller options button.
