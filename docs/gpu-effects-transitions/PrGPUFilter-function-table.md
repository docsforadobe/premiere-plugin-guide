<a id="gpu-effects-transitions-prgpufilter-function-table"></a>

# PrGPUFilter Function Table

PrGPUFilter is a structure consisting of the following functions that a effect/transition can implement.

| **Selector**                                                                                                        | **Optional**   | **Description**                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------|
| [CreateInstance](function-descriptions.md#gpu-effects-transitions-function-descriptions-createinstance)             | No             | Allocate and initialize any GPU resources.                                                                        |
| [DisposeInstance](function-descriptions.md#gpu-effects-transitions-function-descriptions-disposeinstance)           | No             | Release GPU resources.                                                                                            |
| [GetFrameDependencies](function-descriptions.md#gpu-effects-transitions-function-descriptions-getframedependencies) | Yes            | If the rendered result of the effect/transition depends on frames other than the input frame, specify these here. |
| [PreCompute](function-descriptions.md#gpu-effects-transitions-function-descriptions-precompute)                     | Yes            | Precompute.                                                                                                       |
| [Render](function-descriptions.md#gpu-effects-transitions-function-descriptions-render)                             | No             | Render.                                                                                                           |
