.. _device-controllers/getting-started:

Getting Started
################################################################################

You'll need a thorough understanding of the device(s) you hope to control before developing a device control plug-in. Begin with the sample project, progressively replacing its functions with your own.

Will your device controller be used for the capture process, or for output to tape, or both? Below are notes describing how to support these in your plug-in.

----

Resources
================================================================================

Device controllers use a basic PiPL to specify their name and the match name that Premiere uses to identify them. When making changes to the PiPL resource, rebuild the plug-in each time, so that the PiPL will be recompiled.

----

Entry Point
================================================================================

::

  short xDevice (
    short       selector,
    DeviceHand  theData)

*selector* is the action Premiere wants the device controller to perform. DeviceHand is a handle to DeviceRec, which provides all pertinent information.

Return ``dmNoError`` if successful, or an appropriate return code.
