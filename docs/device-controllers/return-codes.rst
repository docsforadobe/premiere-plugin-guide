.. _device-controllers/return-codes:

Return Codes
################################################################################

+----------------------------+-----------------------------------------------------------------------------------+
|      **Return Code**       |                                    **Reason**                                     |
+============================+===================================================================================+
| ``dmNoErr``                | Operation has completed without error.                                            |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmDeviceNotFound``       | The device is not available.                                                      |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmTimecodeNotFound``     | The device cannot read the timecode from the media, or there is none to be read.  |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmBadTimecode``          | The device has timecode but it doesn't trust it.                                  |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmCantRecord``           | The device is unable to record to the media.                                      |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmUserAborted``          | The operation has stopped because the user cancelled.                             |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmLastErrorSet``         | The device controller set the last error string using the Error Suite.            |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmExportToTapeFinished`` | The device controller is signaling the end of the export to tape operation.       |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmTapeWriteProtected``   | Return value during Export To Tape if tape is write pro- tected.                  |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmNoTape``               | Return value during Export To Tape if there is no tape in the deck.               |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmLastInfoSet``          | The device controller set the last info string using the SweetPea Error Suite.    |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmLastWarningSet``       | The device controller set the last warning string using the SweetPea Error Suite. |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmHasNoOptions``         | Return during ``dsHasOptions`` to disable the device controller options button..  |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmUnknownError``         | The device controller set the last error string using the Error Suite.            |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmUnsupported``          | The selector is not recognized, or unsupported.                                   |
+----------------------------+-----------------------------------------------------------------------------------+
| ``dmGeneralError``         | Unspecified error.                                                                |
+----------------------------+-----------------------------------------------------------------------------------+
