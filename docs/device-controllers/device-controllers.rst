.. _device-controllers/device-controllers:

Device Controllers
################################################################################

Device controllers drive hardware devices, such as cameras and tape decks, enabling timecode-accurate, hardware-assisted video capture and output to tape. Device controllers are used when working in the Capture and Edit to Tape panels. A device controller can implement one or more communication protocols, and should gracefully handle differences across various hardware that support the same protocol.

Device controllers are usually called by Premiere when the user is in the Capture panel or Edit to Tape panel, for example, when using the VTR transport controls in either panel to navigate through video on a VTR. But device controllers can also be driven by recorder plug-ins during

capture. Especially when capturing video, the device controller's operation becomes deeply intertwined with the recorder. Device controllers work along with recorders to update Premiere with timecode information from the hardware.

If you've never developed a device controller before, you can skip the What's New section, and go directly to Getting Started.
