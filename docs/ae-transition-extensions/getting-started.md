<a id="ae-transition-extensions-getting-started"></a>

# Getting Started

## Setting up the Sample Project

If you are developing an transition, begin with the SDK_CrossDissolve sample project, progressively replacing its functionality with your own. Refer to [Introduction](../intro/intro.md#intro-intro) for general instructions on how to build sample projects.

In addition to those general instructions, the sample project is also dependent on the After Effects SDK. Download it here. On Windows, create an environment variable pointing to it named “AE_SDK_BASE_PATH”, so that the compiler will find the AE headers that the project includes. On

MacOS, in XCode > Preferences > Locations > Custom Paths, specify AE_SDK_BASE_PATH to be the root folder of the AE SDK you have downloaded and unzipped.

As of version 15.4, Premiere Pro no longer supports OpenCL.

If your transition uses CUDA, you’ll need to download the CUDA SDK. On Windows, create an environment variable pointing to it named “CUDA_SDK_BASE_PATH”, so that the linker will find the right libraries.

---

## Compatibility Considerations

For compatibility with plugin hosts that doesn’t support the AE Transition Extensions, a plugin should check first for the existence of the PF_TransitionSuite suite. If it isn’t available, the plugin should act as a normal effect. This is demonstrated in the SDK_CrossDissolve sample project.
