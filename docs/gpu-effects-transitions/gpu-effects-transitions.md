# GPU Effects & Transitions

This chapter describes the additional capabilities available to effects and transitions for GPU interoperability with Premiere Pro. The GPU extensions allow these plugins to have full access to GPU-resident frames without readback to system memory, when using the Mercury Playback Engine in a GPU-accelerated mode. Effects and transitions can also optionally tell the host that they support real-time processing, so that they will not be flagged as non-realtime.

The GPU extensions work on top of effects and transitions built using the After Effects SDK. The extensions are designed to supplement a regular software effect or transition, which defines the software rendering path, parameters, custom UI drawing, and other standard interaction. The GPU effect exists as a new entry point for rendering using the GPU if possible. The software render path will be used otherwise.

---

## System Requirements

The system requirements for developing GPU effects & transitions are higher than developing other plugins. You'll need a video card that supports Mercury Playback Engine GPU acceleration. Make sure your video card supports the type of video acceleration you are developing, on the platform you are developing on. See this page for the latest supported video cards: [https://helpx.adobe.com/premiere-pro/system-requirements.html](https://helpx.adobe.com/premiere-pro/system-requirements.html)

The CUDA SDK is also needed for CUDA rendering development.

---

## Compilation notes

### CUDA

To compile GPU effects in Premiere SDK, we highly recommend using CUDA SDK 11.8.

Caution: GPU Effects built using CUDA SDK 11.8 will not work with NVIDIA Kepler generation cards. The minimum CUDA Compute Capability has been increased to sm_50.

### CUDA Runtime API vs. Driver API

1. Utilize CUDA Driver API
   - For best compatibility, we highly recommend utilizing CUDA Driver API only. Unlike the runtime API, the driver API is directly backwards compatible with future drivers. Please note that the CUDA Runtime API is built to handle/automate some of the housekeeping that is exposed and needs to be handled in the Driver APIs, so there might be some new steps/code you would need to learn and implement for migrating from Runtime API to Driver API.
2. Statically Link to CUDA Runtime
  - If you must stick to CUDA Runtime API, we recommend you statically link to the CUDA Runtime. That's an alternative way for leveraging the backwards compatibility of the driver into the future. This can be done by linking cudart_static.lib.
3. Dynamically Link to CUDA Runtime
  - This also works but would be prone to compatibility issues. A compatible CUDA Runtime DLL needs to be available on users' systems so that driver can understand and be backward compatible. Currently Premiere Pro ships a copy of CUDA Runtime DLL of our recommended CUDA SDK version. This may change in future. If you must dynamically link to CUDA Runtime, we recommend you ship a copy of the CUDA Runtime DLL with your plugin and leverage dlopen/LoadLibrary to explicitly load the desired runtimes. For more details, see the CUDA Compatibility section of NVIDIA's GPU Management and Deployment guide: [https://docs.nvidia.com/deploy/cuda-compatibility/](https://docs.nvidia.com/deploy/cuda-compatibility/)

---

## DirectX

We would like to announce that we have been working on introducing support for DirectX 12 in our rendering pipeline. We will soon be sharing unlock instructions to enable DirectX in your application.

### Why?

- Performance - DirectX 12 is a thin wrapper over the hardware which would provide us with more control than OpenCL/CUDA over the execution of our shaders. This translates to a higher ceiling for performance
- Stability/Error Handling - DirectX 12 supports TDR detection and recovery which can help us recover from hardware problems. It is actively supported by Microsoft i.e., proactive fixes for bugs in drivers
- Interoperability - Seamless interoperability with our display module which already uses DirectX12

### Direction

Adding a new rendering engine to Premiere is a massive undertaking. Although we have made significant progress, it is still under development and will have an update for you soon.

### Feedback & Support

We will be happy to receive any thoughts regarding DirectX or answer any questions. I am reachable at, [pusingha@adobe.com](mailto:pusingha@adobe.com) or you can post them on [ae_api_nda@adobe.com](mailto:ae_api_nda@adobe.com)
