.. _device-controllers/selector-table:

Selector Table
################################################################################

This table summarizes the various selector commands a device controller can receive.

+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
|                         **Selector**                         |                                                                  **Description**                                                                  |
+==============================================================+===================================================================================================================================================+
| :ref:`device-controllers/selector-descriptions.dsInit`       | Create private instance data, and initialize hardware connection.                                                                                 |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`device-controllers/selector-descriptions.dsRestart`    | Restart device controller – used at startup to reconnect to a device.                                                                             |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`device-controllers/selector-descriptions.dsSetup`      | Display a modal dialog with any user settings and info the device controller wishes to show the user.                                             |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`device-controllers/selector-descriptions.dsExecute`    | Execute a specified device control command.                                                                                                       |
|                                                              |                                                                                                                                                   |
|                                                              | One a device controller has been initialized, most of the various user-driven interactions will be sent as dsExecute selectors with a subcommand. |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`device-controllers/selector-descriptions.dsCleanup`    | Dispose of any allocated data structures.                                                                                                         |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`device-controllers/selector-descriptions.dsQuiet`      | Disconnect from the device, but don't dispose of allocated structures.                                                                            |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`device-controllers/selector-descriptions.dsHasOptions` | Return dmHasNoOptions to disable the device controller options button.                                                                            |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
