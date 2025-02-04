# Getting Started

## Setting up the Sample Projects

If you are developing an effect, begin with one of the two GPU effect sample projects, progressively replacing its functionality with your own. Refer to [Introduction](../index.md) for general instructions on how to build the SDK projects.

In addition to those general instructions, the sample project is also dependent on the After Effects plugin SDK. On Windows, create an environment variable pointing to it named AE_SDK_BASE_PATH, so that the compiler will find the AE headers that the project includes. On macOS, in *Xcode > Preferences > Locations > Custom Paths*, specify AE_SDK_BASE_PATH to be the root folder of the AE plugin SDK you have downloaded and unzipped.

The samples also use Boost, which may be downloaded at boost.org. Download that, and create a variable named BOOST_BASE_PATH just as you did with AE_SDK_BASE_PATH above.

Finally, install Python (version 3.6 or greater), if you do not have it already. It may be downloaded at python.org. The sample projects use this as part of the custom build steps.

Depending on whether your effect will use CUDA, you'll need to download the CUDA SDK. On Windows, create an environment variable pointing to it named CUDA_SDK_BASE_PATH, so that the linker will find the right libraries.

---

## Querying for Parameters and other Attributes of a Effect or Transition

You'll notice that PrGPUFilterRenderParams has some attributes about an effect or transition, but many things, such as the parameters or duration of the clip to which the plugin is applied, are not found in that structure. These attributes will need to be queried using the GetParam() and GetProperty() helper functions in PrGPUFilterModule.h. For example:

```cpp
GetProperty(kVideoSegmentProperty_Effect_EffectDuration, duration);
GetProperty(kVideoSegmentProperty_Transition_TransitionDuration, duration);
```

---

## Lifetime of a GPU Effect / Transition

A new GPU effect instance is created when an effect/transition is applied in the timeline, or when an effect parameter is changed. When rendering a series of frames it won't needlessly be recreated. The [Opaque Effect Data Suite](suites.md#opaque-effect-data-suite) should be used to share unflattened sequence data between instances of the same effect on a track item.

---

## Fallback to Software Rendering

When a new GPU effect instance is created, the instance has the option of opting-in or out of providing GPU rendering. The GPU effect should be reasonably sure it has sufficient resources to complete the render if it opts-in, because there is no API support to fall back to software rendering in the middle of a render.

Calling GetDeviceInfo() in the [GPU Device Suite](suites.md#gpu-device-suite), and checking `outDeviceInfo.outMeetsMinimumRequirementsForAcceleration`, you can see if supports the minimum system requirements for acceleration. Do not proceed with

AcquireExclusiveDeviceAccess(), if the minimum requirements are not met.

In emergency situations, when there is not enough GPU memory available to complete a render, an effect may call PurgeDeviceMemory in the [GPU Device Suite](suites.md#gpu-device-suite) to free up memory not initially available. This will impact performance, and should be used only if absolutely necessary.

---

## OpenGL Interoperability

If you want, you have the ability to transfer frames from CUDA to OpenGL (though not always efficiently).

For CUDA interoperability with OpenGL:

### CUDA -> OpenGL

- Create an OpenGL buffer
- map it into CUDA with `cuGraphicsMapResources`
- get the mapped address with `cuGraphicsResourceGetMappedPointer`
- copy from the CUDA address to the mapped address with `cuMemcpyDtoDAsync`
- unmap with `cuGraphicsUnmapResources`

### OpenGL -> CUDA

- Map the OpenGL buffer into CUDA with `cuGraphicsMapResources`
- get the mapped address with `cuGraphicsResourceGetMappedPointer`
- copy from the mapped address to CUDA with `cuMemcpyDtoDAsync`
- unmap with `cuGraphicsUnmapResources`

!!! note
    On the Mac there is no real OpenGL/CUDA interoperability, and these calls will go through system memory.

---

## Entry Point

The GPU entry point function will only be called if the current project is using GPU acceleration. Otherwise, the normal entry point function will be called as described in the After Effects SDK, or [GPU Effects & Transitions](gpu-effects-transitions.md) or [Video Filters](../video-filters/video-filters.md) in this SDK Guide.

Make sure GPU acceleration is activated in File > Project Settings > General > Video Rendering and Playback > Renderer. If a GPU option is not available, then you will need to install a suitable video card in your system.

```cpp
prSuiteError xGPUFilterEntry (
  csSDK_uint32      inHostInterfaceVersion,
  csSDK_int32*      ioIndex,
  prBool            inStartup,
  piSuitesPtr       piSuites,
  PrGPUFilter*      outFilter,
  PrGPUFilterInfo*  outFilterInfo)
```

If `inStartup` is non-zero, the effect/transition should startup and initialize the functions needed to implement PrGPUFilter, as well as the info in PrGPUFilterInfo.

If `inStartup` is false, then the effect/transition should shutdown, unloading any resources it loaded on startup.

As of CC, inHostInterfaceVersion is `PrSDKGPUFilterInterfaceVersion1 == 1`

If a single plugin supports multiple effects, increment ioIndex to the next value before returning, in order to be called again to describe the next effect.
