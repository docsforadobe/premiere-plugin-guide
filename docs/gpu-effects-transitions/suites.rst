.. _gpu-effects-transitions/suites:

Suites
################################################################################

For information on how to acquire and manage suites, see :ref:`universals/sweetpea-suites`.

----

.. _gpu-effects-transitions/suites.gpu-device-suite:

GPU Device Suite
================================================================================

This suite provides info on any GPU devices available. For example, GetDeviceInfo() allows an effect/transition to see if the device supports OpenCL or CUDA.

Use this suite to get exclusive access to a device using AcquireExclusiveDeviceAccess and ReleaseExclusiveDeviceAccess. If needed, you can reconcile devices using the outDeviceHandle passed back from GetDeviceInfo().

Device memory should ideally be allocated through this suite. In some cases you may find it more efficient to use a texture / image object as the source. With CUDA, you can bind a texture reference to an existing linear buffer. With OpenCL, you can create an image object from an existing 2D buffer object using image_2d_from_buffer. Temporary allocations are also fine but may be rather slow.

----

.. _gpu-effects-transitions/suites.opaque-effect-data-suite:

Opaque Effect Data Suite
================================================================================

This suite provides effects a way to share unflattened sequence data between instances of the same effect on a track item. The data is opaque to the host and effects are responsible for maintaining thread safety of the shared data. The host provides reference-counting that the effect can use to manage the lifetime of the shared data. Here's an overview of how this suite should be used:

When the effect is applied, in ``PF_Cmd_SEQUENCE_SETUP``, the effect plugin allocates and initializes the sequence data in PF_OutData->out_data. Then it calls

AcquireOpaqueEffectData(). The opaque effect data does not yet exist, so the plugin allocates it, and calls RegisterOpaqueEffectData, and then copies over the data from the sequence data. So both sequence data and opaque effect data are allocated.

Then ``PF_Cmd_SEQUENCE_RESETUP`` is called (multiple times) for clones of the effect used for rendering. The effect instance knows it's a clone because the PF_InData->sequence_data is NULL (there is a special case if the effect has Opaque Effect Data – in that case, its render clones will receive ``PF_Cmd_SEQUENCE_RESETUP`` with a NULL sequence_data pointer). It then calls AcquireOpaqueEffectData(). As a render clone, it relies on this opaque effect data, rather than sequence data, and does not try to copy the sequence data to opaque effect data.

When, on the other hand, ``SEQUENCE_RESETUP`` is called with valid sequence_data in PF_InData, this is not a render clone. The plugin unflattens this sequence data. It then calls AcquireOpaqueEffectData(), and if the opaque effect data does not yet exist (i.e. when reopening a saved project), the plugin allocates it, and calls RegisterOpaqueEffectData. It then copies the sequence data to opaque effect data.

On ``SEQUENCE_FLATTEN``, the plugin takes the unflattened data, flattens it, and disposes of the un-flat data.

When ``SEQUENCE_SETDOWN`` is called (it may be called multiple times to dispose of render clones), ReleaseOpaqueEffectData() is called.

instanceID
********************************************************************************

The :ref:`gpu-effects-transitions/suites.opaque-effect-data-suite` functions need the instanceID of the effect. For the software entry point, you can obtain this using GetFilterInstanceID() in PF_UtilitySuite, defined in PrSDKAESupport.h. For the GPU Render entry point, you can use the following code: csSDK_uint32 instanceID;

.. code-block:: cpp 

  GetProperty( kVideoSegmentProperty_Effect_RuntimeInstanceID, instanceID);

...where GetProperty() is defined in PrGPUFilterModule.h, and the ``kVideoSegmentProperty_`` IDs are defined in PrSDKVideoSegmentProperties.h.
