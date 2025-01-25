# PrGPUFilter Function Table

PrGPUFilter is a structure consisting of the following functions that a effect/transition can implement.

| **Selector**                                                                                                        | **Optional**   | **Description**                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------|
| [CreateInstance](function-descriptions.md#createinstance)             | No             | Allocate and initialize any GPU resources.                                                                        |
| [DisposeInstance](function-descriptions.md#disposeinstance)           | No             | Release GPU resources.                                                                                            |
| [GetFrameDependencies](function-descriptions.md#getframedependencies) | Yes            | If the rendered result of the effect/transition depends on frames other than the input frame, specify these here. |
| [PreCompute](function-descriptions.md#precompute)                     | Yes            | Precompute.                                                                                                       |
| [Render](function-descriptions.md#render)                             | No             | Render.                                                                                                           |
