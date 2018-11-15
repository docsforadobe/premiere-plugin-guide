.. _recorders/recorders:

Recorders
################################################################################

Recorders interface directly with capture hardware, and capture video and/or audio to any file format. The recorder is responsible for displaying any video preview in the Capture panel, playing any audio preview to the system sound or hardware output, driving the meters in the Audio Master Meters panel, providing any settings in a custom dialog, and digitizing the video and audio to a file (or multiple files) on disk. A recorder can optionally provide source timecode information to Premiere, and notify Premiere when the video format changes so that the capture preview area can be resized. The recorder does not communicate anything about the audio to Premiere. When recording is complete, Premiere imports the file using any available importers that support that filetype.

A recorder can only capture to a single filetype. To capture to several filetypes, provide several recorders.

If you've never developed a recorder before, you can skip the What's New sections, and go directly to Getting Started.
