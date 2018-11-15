.. _ae-transition-extensions/getting-started:

Getting Started
################################################################################

Setting up the Sample Project
================================================================================

If you are developing an transition, begin with the sample project, named SDK_CrossDissolve, progressively replacing its functionality with your own. Refer to chapter 1 for general instructions on how to build the SDK projects.

In addition to those general instructions, the sample project is also dependent on the After Effects SDK. Download it here. On Windows, create an environment variable pointing to it named "AE_SDK_BASE_PATH", so that the compiler will find the AE headers that the project includes. On

MacOS, in XCode > Preferences > Locations > Source Trees, specify AE_SDK_BASE_PATH to be the root folder of the AE SDK you have downloaded and unzipped.

Depending on whether your transition will use OpenCL or CUDA or both, you'll need to download the CUDA SDK. On Windows, create an environment variable pointing to it named "CUDA_SDK_BASE_PATH", so that the linker will find the right libraries.

----

Compatibility Considerations
================================================================================

For compatibility with plug-in hosts that doesn't support the AE Transition Extensions, a plug-in should check first for the existence of the suite. If it isn't available, the plug-in should act as a normal effect. This is demonstrated in the SDK_CrossDissolve sample project.
