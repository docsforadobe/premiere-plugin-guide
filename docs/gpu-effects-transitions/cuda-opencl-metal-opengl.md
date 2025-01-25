.. _gpu-effects-transitions/cuda-opencl-metal-opengl:

CUDA, OpenCL, Metal, or OpenGL?
################################################################################

As of Summer 2021, Premiere Pro will no longer support OpenCL. The GPU architecture of Premiere Pro is entirely CUDA/Metal, and this is what is exposed through the GPU extensions to the effect/transition APIs.

Premiere Pro plugins have the ability to transfer frames from CUDA to OpenGL (though not always efficiently). Read more about that here.
