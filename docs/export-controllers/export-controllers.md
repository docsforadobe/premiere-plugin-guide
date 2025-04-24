# Export Controllers

An export controller can drive any exporter to generate a file in any format and perform custom post-processing operations. 

An export controller adds its own custom menu item to the File > Export submenu. When the user chooses the menu item, the plugin is called with a TimelineID, which represents the current sequence. Although details on the current sequence are not passed in, the export controller can use the [Sequence Info Suite](../universals/sweetpea-suites.md#sequence-info-suite) to query for various properties. The export controller can then optionally display any custom modal UI to allow the user to set any parameters for the export.

The Export Controller must provide its own UI, calling ExportFile in the Export Controller Suite, which takes the TimelineID, a path to an exporter preset, and a path for the output. This tells Premiere Pro to handle the export, displaying progress. The call will return either a success value, an error, or that the user canceled. During the export, the UI will be blocked, just as when doing a standard export that doesn't use the Adobe Media Encoder Render Queue.

Once Premiere Pro completes the export, the call will return to the export controller. The plugin can then perform any post-processing operations, such as transferring the newly exported file over the network, or registering the file in an asset management system.
