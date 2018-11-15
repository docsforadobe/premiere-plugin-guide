.. _video-filters/selector-descriptions:

Selector Descriptions
################################################################################

fsInitSpec
================================================================================

Responding to this selector is optional. This selector is sent when the filter is applied to a clip and the plug-in is called for the first time. This call can be used to initialize the plug-in parameters with default values in order to achieve an initial "silent setup", in which ``fsSetup`` is skipped when the filter is applied to a clip, to avoid popping the modal dialog that may be needed in ``fsSetup``.

Allocate and pass back a handle to a structure containing the parameter values in specsHandle. The filter is given the total duration (in samples), and number of the first sample in the source buffer.

----

fsHasSetupDialog
================================================================================

New for Premiere Pro CS3. Optional. Specify whether or not the filter has a setup dialog, by ``returning`` fsHasNoSetupDialog or fsNoErr.

----

fsSetup
================================================================================

Optional. Sent when the filter is applied, if *fsInitSpec* doesn't allocate a valid specsHandle. Also sent when the user clicks on the setup link in the Effect Controls Panel. The filter can optionally display a (platform-dependent) modal dialog to get new parameter values from the user. First, check VideoHandle.specsHandle. If NULL, the plug-in is being called for the first time.

Initialize the parameters to their default values. If non-NULL, load the parameter values from specsHandle. Now use the parameter values to display a modal setup dialog to get new values. Return a handle to a structure containing the parameter values in specsHandle.

In order to properly store parameter values between calls to the plug-in, describe the structure of your specsHandle data in your PiPL's ANIM properties. Premiere interpolates animatable parameter values as appropriate before sending ``fsExecute``.

The filter is given the total duration in samples and the sample number of the first sample in the source buffer.

During ``fsSetup``, the frames passed to VideoRecord.source will almost always be 320x240. The exception is if the plug-in is receiving the fsSetup selector when the effect is initially applied, in which case it will receive a full height frame, with the width adjusted to make the frame square pixel aspect ratio. For example, a filter applied in a 1440x1080 HDV sequence will receive a full 1920x1080 buffer. The frame is the layer the filter is applied to at the current time indicator. If the CTI is not on the clip the filter is applied to, the frame is transparent black.

If the filter has a setup dialog, the VFilterCallbackProcPtr should be used to get source frames for previews. ``getPreviewFrameEx`` can be used to get rendered frames, although if this call is used, the video filter should be ready to be called reentrantly with ``fsExecute``.

----

fsExecute
================================================================================

This is really the only required selector for a video filter, and it's where the rendering happens. Take the input frame in VideoHandle.source, render the effect and return the frame to Premiere in VideoHandle.destination. The specsHandle contains your parameter settings (already interpolated if animatable). You can store a handle to any additional non-parameter data in VideoHandle.InstanceData. If you do so, deallocate the handle in response to *fsDisposeData*, or your plug-in will leak memory.

The video your filter receives may be interlaced, in the field order determined by the project settings. If interlaced, your plug-in will be called twice for each frame of video, and each PPix will be half the frame height.

----

fsDisposeData
================================================================================

Optional. Called when the project closes. Dispose of any instance data created during ``fsExecute``. See VideoHandle->InstanceData.

----

fsCanHandlePAR
================================================================================

Optional. Indicate how your filter wants to handle pixel aspect ratio by returning a combination of the following flags.

This selector is only sent if several conditions are met.

The pixel aspect ratio of the clip to which the filter is applied must be known, and not be square (1.0).

The clip must not be a solid color.

The PiPL bits ``anyPixelAspectRatio`` and ``unityPixelAspectRatio`` must not be set.

+-----------------------------+-----------------------------------------------------------------------------------+
|          **Flag**           |                                  **Description**                                  |
+=============================+===================================================================================+
| ``prEffectCanHandlePAR``    | Premiere should not make any adjustment to the source image to compensate for PAR |
+-----------------------------+-----------------------------------------------------------------------------------+
| ``prEffectUnityPARSetup``   | Premiere should render the source image to square pixels during ``fsSetup``       |
+-----------------------------+-----------------------------------------------------------------------------------+
| ``prEffectUnityPARExecute`` | Premiere should render the source image to square pixels during ``fsExecute``     |
+-----------------------------+-----------------------------------------------------------------------------------+

----

fsGetPixelFormatsSupported
================================================================================

Optional. Gets pixel formats supported. Called iteratively until all formats have been given. Set (*theData)->pixelFormatSupported to a supported pixel format, and return fsNo­ Err. When all formats have been described, return fsBadFormatIndex. See the field-aware video filter sample for an example.

----

fsCacheOnLoad
================================================================================

Optional. Return ``fsDoNotCacheOnLoad`` to disable plug-in caching for this filter.
