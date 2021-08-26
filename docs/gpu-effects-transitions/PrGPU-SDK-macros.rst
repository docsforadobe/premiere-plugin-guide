.. _gpu-effects-transitions/PrGPU-SDK-macros:

PrGPU SDK Macros
################################################################################

The PrGPU SDK macros and device functions allow you to write kernels that will compile on multiple GPU compute languages - CUDA, OpenCL, and Metal. These languages have an enormous overlap - a C98 language subset, and by using the porting macros and functions to abstract out the differences, you can write portable code. You can still access API specific features not covered by the porting set but you'll need to include an alternate code path for the other APIs.

Currently the SDK does not provide host side code to compile or launch arbitrary kernels, but there are SDK examples that show how to do this for the different APIs.

The macros are not part of the plugin API - they are provided as a utility if you would like to used them. This gives you broad latitude to fork them and make any changes you see fit without breaking plugin compatibility. On the Adobe end, we may expand and modify the SDK kernel porting set in future releases to cover other compute APIs or other enhancements.

----

External Dependencies
================================================================================

The macros do add one external source dependency - Boost (boost.org). We use the Boost preprocessor package to manipulate kernel definitions.

Depending on how you choose to compile and deploy your kernels, we also provide a small python script that may be useful (See "Preprocessing as a Separate Step")

----

Include Paths
================================================================================

You need to add some include paths to your kernel compilation environment:

- the path to PrGPU/KernelSupport/ (found in the SDK at Examples/Projects/GPUVideoFilter/ Utils/)
- the path to the Boost library

----

Defines
================================================================================

You will also need to define a symbol to tell the header file what API to process when compiling the kernel:

- Metal: -DGF_DEVICE_TARGET_METAL=1
- OpenCL:
  - DGF_DEVICE_TARGET_OPENCL=1
  - DGF_OPENCL_SUPPORTS_16F=1 or 0, depending on whether you will support half (16-bit float) access for this device. Some older cards are quite slow at half support, or just don't support it.
- CUDA: the KernelCore.h header will automatically sense the cuda compiler and will #define GF_DEVICE_TARGET_CUDA 1 for you.

Only one device target flag will be active in any given compilation. The header the define the device target macros to 0 for the inactive APIs. Feel free to use these macros in your code for any API specializations. Outside of the header, we don't need to do this much.

----

Header Files
================================================================================

- KernelCore.h - basic header macros. You'll certainly want these
- KernelMemory.h - global device memory access abstractions for float and half
- FloatingPoint.h - common floating point routines. These mostly hide naming differences across APIs.

..

You'll want to include them like this in your kernel:

.. code-block:: cpp

  #include "PrGPU/KernelSupport/KernelCore.h"

The folder contains additional files used by the above files.

One thing to watch out for is whether your projects are tracking header dependencies properly. If not, you'll need to manually recompile kernels when include files change. This is true whether or not you use the SDK porting set, so you've likely already sorted this out.

----

Top Level Kernel Files
================================================================================

You can organize your code and projects as you like, but we find it convenient to have separate top level kernel files for each API (.cl, .cu, and .metal) that just include shared code and are otherwise nearly empty. This makes build rules much easier.

----

Preprocessing as a Separate Step
================================================================================

If you compile the kernel source on the customer machine, you may wish to preprocess the kernel at plugin compile time, and store the kernel source in your plugin. A python script is provided that will convert preprocessed source to a character array. The script is in Examples/Projects/GPUVideoFilter/Utils/CreateCString.py. See the ProcAmp example for usage.

You can also compile kernels (which is always the case for CUDA) at plugin compile time, in which case you don't need the python script, or a separate preprocessing run. You will need to package the compiled kernel in your plugin if you go this route.

The ProcAmp plugin example uses a preprocessing step for OpenCL and Metal.

----

Declaring Kernels
================================================================================

Metal kernels require syntax that is quite different than CUDA, and the PrGPU macros use the Boost preprocessing package to express parameters. This is by far the most complicated part of the package, so grab a fresh cup of coffee and sit back for a read.

The GF_KERNEL_FUNCTION macro is used to pass values as parameters (CUDA) or in a struct (metal). The macro will create an API-specific kernel entry point which will call a

function that it defines, leaving you to fill in the body. The macro uses Boost preprocessor sequences to express a type/name pair:

.. code-block:: cpp

  (float)(inValue)

These pairs are then nested into a sequence of parameters:

.. code-block:: cpp

  ((float)(inAge))((int)(inMarbles))

There are different categories of parameters, such as buffers, values, and kernel position. Each category sequence is a separate macro parameter. Example usage:

.. code-block:: cpp

  GF_KERNEL_FUNCTION(RemoveFlicker,

  //kernel name, then comma, ((GF_PTR(float4))(inSrc))

  //all buffers and textures go after the first comma
  ((GF_PTR(float4))(outDest)),
  ((int)(inDestPitch))

  //After the second comma, all values to be passed ((DevicePixelFormat)(inDeviceFormat))
  ((int)(inWidth))
  ((int)(inHeight)),
  ((uint2)(inXY)(KERNEL_XY))

  //After the third comma, the position arguments.
  ((uint2)(inBlockID)(BLOCK_ID)))
  {
    <do something interesting here>
  }

In the example above, the host does not pass the position values when invoking the kernel.

Position values are filled in automatically by the unmarshalling code generated by the GF_KERNEL_FUNCTION macro. The code you write will actually end up in a device function that the unmarshalling code will call. See the ProcAmp example plugin for usage.

Kernels that use statically sized shared memory use a different macro, ``GF_KERNEL_FUNCTION_SHARED``. Please see the header for details.

----

Declaring Device Functions
================================================================================

By comparison, device functions are a snap to write:

.. code-block:: cpp

  GF_DEVICE_FUNCTION float Average(float a, float b) {...

----

Other Macros and Functions
================================================================================

There's a variety of other macros and functions in the KernelSupport headers. Please see the Headers and examples for details.
