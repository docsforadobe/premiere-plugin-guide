.. _gpu-effects-transitions/function-descriptions:

Function Descriptions
################################################################################

CreateInstance
================================================================================

::

  prSuiteError (*CreateInstance)(
    PrGPUFilterInstance*  ioInstanceData);

Creates a GPU filter instance representing an effect or transition on a track item.

Returning an error from CreateInstance will cause this node to be rendered in software for the current set of parameters.

Unlike software instances of effects and transitions, GPU instances are created and disposed whenever an effect parameter changes.

This allows an effect have more flexibility about opting-in for GPU rendering, depending on the parameters. Separate instances may be called concurrently.

----

DisposeInstance
================================================================================

::

  prSuiteError (*DisposeInstance)(
    PrGPUFilterInstance*  ioInstanceData);

Cleanup any resources allocated during CreateInstance.

----

GetFrameDependencies
================================================================================

::

  prSuiteError (*GetFrameDependencies)(
    PrGPUFilterInstance*            inInstanceData,
    const PrGPUFilterRenderParams*  inRenderParams,
    csSDK_int32*                    ioQueryIndex,
    PrGPUFilterFrameDependency*     outFrameDependencies);

Return dependency information about a render, or nothing if only the current frame is required.

Increment ``ioQueryIndex`` for additional dependencies.

----

PreCompute
================================================================================

::

  prSuiteError (*Precompute)(
    PrGPUFilterInstance*            inInstanceData,
    const PrGPUFilterRenderParams*  inRenderParams,
    csSDK_int32                     inIndex,
    PPixHand                        inFrame);

Precompute a result into preallocated uninitialized host (pinned) memory.

Will only be called if ``PrGPUDependency_Precompute`` was returned from ``GetFrameDependencies``.

Precomputation may be called ahead of render time.

Results will be uploaded to the GPU by the host.

If outPrecomputePixelFormat is not custom, frames will be converted to the GPU pixel format.

----

Render
================================================================================

::

  prSuiteError (*Render)(
    PrGPUFilterInstance*            inInstanceData,
    const PrGPUFilterRenderParams*  inRenderParams,
    const PPixHand*                 inFrames,
    csSDK_size_t                    inFrameCount,
    PPixHand*                       outFrame);

Render into an allocated outFrame allocated with ``PrSDKGPUDeviceSuite`` or operate in place.

Result must be in the same pixel format as the input. If the effect grows or shrinks the output area (e.g. rendering a drop shadow), it is allowable for the effect to allocate and return a different sized outFrame.

For effects, inFrames[0] will always be the frame at the current time, other input frames will be in the same order as returned from GetFrameDependencies. For transitions in­ Frames[0] will be the incoming frame and inFrames[1] the outgoing frame. Transitions may not have other frame dependencies.

Use the utility function GetParam to retrieve the parameter values at the current time.
