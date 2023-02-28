.. _device-controllers/capture:

Capture
################################################################################

Timecode
================================================================================

Since the device controller and recorder sample plugins both only simulate hardware, they will return different timecode values to the app. You can set the Capture panel to only display device controller timecode by going to Preferences > Capture, and check "Use device control timecode". On the other hand, leaving this box unchecked and observing the different timecodes returned is a good way to get a feel for when the device controller timecode is used, and when the recorder timecode is used.

----

Preroll Time
================================================================================

The Preroll Time value is set in the Capture panel, in the Settings tab. The value defaults to zero seconds, but it may be set to any positive value chosen by the user. Adjusting the Preroll Time setting will have an effect on the DeviceRec.preroll value sent during *dsExecute/cmdLocate*. The value with be converted from seconds into frames for the device controller.

----

Timecode Offset
================================================================================

The Timecode Offset value is set in the Capture panel, in the Settings tab. The value defaults to zero frames, but it may be set to any value chosen by the user when they calibrate their VTR to account for any latencies. So when using the same tape in two separate VTRs, to capture the same timecode span, the Timecode Offset may be used to account for any differences in the way the VTRs report timecode back to Premiere. Using the Timecode Offset, the in point sent to the device controller can be shifted earlier or later, while the timecode embedded in the clip after the capture will remain the same.

Adjusting the Timecode Offset setting will be transparent to the device controller, but will have an effect on the DeviceRec.timecode value sent during *dsExecute/cmdLocate*. Starting in

CS5.5, a negative Timecode Offset value is acceptable. Note that for In/Out capture, the earliest allowable time for the in point is 2 seconds. If the provided in point is earlier than that, it will be automatically adjusted to start at 2 seconds.
