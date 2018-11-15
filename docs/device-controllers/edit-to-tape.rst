.. _device-controllers/edit-to-tape:

Edit To Tape
################################################################################

Audio Channels
================================================================================

The device controller should specify how many audio channels are supported by the connected device, so that the Edit to Tape panel will only enable valid audio channel controls. During cmdGetFeatures, the device controller should set the bits corresponding to the audio channels available on the device in DeviceRec.exportAudioChannels.

Then later if performing an Insert Edit, during modeRecordInsert, if the device supports audio channel selection, the bits in exportAudioChannels will be set by the host corresponding to audio channels to export: A1 == bit 0, A2 == bit 1, etc.

----

Record
================================================================================

Starting in CC, the Edit to Tape panel provides three types of export modes: Insert, Assemble, and Print to Tape. The device controller should specify if it supports Assemble mode by setting fCa­ nAssembleEdit along with any other flags during dsExecute/cmdGetFeatures.

When the user presses the Record button in the Edit to Tape Panel, Premiere will send ``dsExecute`` / ``cmdNewMode`` with either modeRecord, modeRecordInsert, or modeRecordAssem­ ble, depending on the Export Type set in the Edit to Tape panel.

Hitting the Record button with Export Type set to Print to Tape sends modeRecord. This record mode is a simple crash record that has no preroll before the in point and causes noticable breaks in the video signal. Setting Assemble sends modeRecordAssemble. This mode uses a preroll before the in point for a smooth transition at the in point, but the out point ends the recording abruptly which will leave a noticable break if there is any subsequent video.

Setting Insert sends modeRecordInsert. This mode uses a preroll before the in point and also ends the recording at the outpoint without any breaks in the video signal. This is also the only mode that allows for selective replacement of specific video/audio channels.

DeviceRec.exportFlags will denote whether video and/or closed captioning should be exported or not, and DeviceRec.exportAudioChannels will denote which audio channels to export. DeviceRec.timecode provides the in point of the edit to tape operation, and DeviceRec.preroll provides the user-specified preroll.

Premiere will play the video output in the Edit to Tape panel. When the record is complete, the

device controller should return from ``dsExecute`` / ``cmdNewMode``.

----

Preview Edits
================================================================================

Starting in CC, the device controller should specify if it supports previewing edits by setting ``fCanPreviewEdit`` along with any other flags during dsExecute/cmdGetFeatures. If Preview is supported, the button will be activated in the Edit to Tape panel, and when pressed, the device controller will receive the same messaging as described above when pressing Record, except that previewEdit will be set in DeviceRec.exportFlags.

----

Abort on Dropped Frames
================================================================================

New in CC, when using the Edit to Tape panel, this is handled transparently to the device controller. If a transmit plug-in or renderer reports dropped frames, Premiere will stop playback and send ``dsExecute``/modeStop to the device controller.

In Premiere Pro CS6.0.1, or in CC if the device controller doesn't support the Edit to Tape panel, use the DroppedFrameProc callback to query the current number of frames dropped during an insert edit. A device controller can use this to provide the feature to abort an Export to Tape if frames are dropped. It can make the call regularly during Export to Tape, and if the value re- turned is non-zero, return dmExportToTapeFinished to abort playback.

----

Closed Captioning
================================================================================

When using the Edit to Tape panel, the device controller should specify if it supports Closed Captioning export by setting fCanUseCC along with any other flags during dsExecute/ cmdGetFeatures.

If the user checks the Insert Closed Captioning checkbox and chooses Record or Preview, the device controller should use the Captioning Suite to get the captions and send them out with the export.
