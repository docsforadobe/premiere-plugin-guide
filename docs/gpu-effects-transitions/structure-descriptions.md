# Structure Descriptions

## PrGPUFilterInfo

This structure contains some basic info about a GPU filter. It provides access to various suites, and access to private data where the instance can allocate memory and store data which will be passed to subsequent functions.

```cpp
typedef struct {
  csSDK_uint32  outInterfaceVersion;
  PrSDKString   outMatchName;
} PrGPUFilterInfo;
```

| Member            | Description                                                                                        |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| `outInterfaceVersion` | Set to the GPU API version corresponding to the version defined in the SDK you are using.              |
| `outMatchName`        | outMatchName must be equal to a registered software filter, if NULL will default to the module's PiPL. |

---

## PrGPUFilterInstance

This structure contains some basic info about a GPU filter. It provides access to various suites, and access to private data where the instance can allocate memory and store data which will be passed to subsequent functions.

```cpp
typedef struct {
  piSuitesPtr   piSuites;
  csSDK_uint32  inDeviceIndex;
  PrTimelineID  inTimelineID;
  csSDK_int32   inNodeID;
  void*         ioPrivatePluginData;
  prBool        outIsRealtime;
} PrGPUFilterInstance;
```

| Member            | Description                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `piSuites`            | Standard suites.                                                                                                                         |
| `inDeviceIndex`       | For use with `PrSDKGPUDeviceSuite`.                                                                                                      |
| `inTimelineID`        | For use with `PrSDKVideoSegmentSuite`.                                                                                                   |
| `inNodeID`            | For use with `PrSDKVideoSegmentSuite`.                                                                                                   |
| `ioPrivatePluginData` | Used by a plugin to store instance data, never touched by the host.                                                                      |
| `outIsRealtime`       | Specify if the plugin is likely to play in real-time, used to determine whether the segment is red, yellow, or unmarked in the timeline. |

---

## PrGPUFilterRenderParams

This structure describes the current render request.

```cpp
typedef struct {
  PrTime  inClipTime;
  PrTime  inSequenceTime;

  // Render properties
  PrRenderQuality  inQuality;
  float            inDownsampleFactorX;
  float            inDownsampleFactorY;

  // Frame properties
  csSDK_uint32    inRenderWidth;
  csSDK_uint32    inRenderHeight;
  csSDK_uint32    inRenderPARNum;
  csSDK_uint32    inRenderPARDen;
  prFieldType     inRenderFieldType;
  PrTime          inRenderTicksPerFrame;
  pmFieldDisplay  inRenderField;
} PrGPUFilterRenderParams;
```

| Member              | Description                                                                                                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `inClipTime`            | The time of the current render, relative to clip start                                                                                                                                                 |
| `inSequenceTime`        | The time of the current render, relative to sequence start                                                                                                                                             |
| `inQuality`             | Render quality; one of the PrRenderQuality enum values                                                                                                                                                 |
| `inDownsampleFactorX`   | Horizontal downsample factor                                                                                                                                                                           |
| `inDownsampleFactorY`   | Vertical downsample factor                                                                                                                                                                             |
| `inRenderWidth`         | Video resolution                                                                                                                                                                                       |
| `inRenderHeight`        |                                                                                                                                                                                                        |
| `inRenderPARNum`        | Video pixel aspect ratio, described as a fractional number with separate values for numerator and denominator.                                                                                         |
| `inRenderPARDen`        |                                                                                                                                                                                                        |
| `inRenderFieldType`     | Render field type                                                                                                                                                                                      |
| `inRenderTicksPerFrame` | Video frame rate                                                                                                                                                                                       |
| `inRenderField`         | GPU rendering is always done on full-height progressive frames unless `PrGPUFilterFrameDependency.outNeedsFieldSeparation` is false.<br/><br/>`inRenderField` indicates which field is being rendered. |

---

## PrGPUFilterFrameDependency

This structure describes any dependencies for a rendered frame.

```cpp
typedef struct {
  PrGPUFilterFrameDependencyType  outDependencyType;

  // Dependence on other frame times
  csSDK_int32  outTrackID;
  PrTime       outSequenceTime;

  // Dependence on precomputation phase
  PrPixelFormat  outPrecomputePixelFormat;
  csSDK_uint32   outPrecomputeFrameWidth;
  csSDK_uint32   outPrecomputeFrameHeight;
  csSDK_uint32   outPrecomputeFramePARNumerator;
  csSDK_uint32   outPrecomputeFramePARDenominator;
  prFieldType    outPrecomputeFrameFieldType;
  csSDK_size_t   outPrecomputeCustomDataSize;
  prBool         outNeedsFieldSeparation;
} PrGPUFilterFrameDependency;
```

| Member                         | Description                                                                                                                                                     |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `outDependencyType`                | The dependency type.<br/><br/>Could be either:<br/><br/>- `PrGPUDependency_InputFrame`,<br/>- `PrGPUDependency_Precompute`,<br/>- `PrGPUDependency_FieldSeparation` |
| `outTrackID`                       | Specify which track is a dependency. Set to 0 for the current track                                                                                                 |
| `outSequenceTime`                  | Set the sequence time which is a dependency.                                                                                                                        |
| `outPrecomputePixelFormat`         | Dependence on precomputation phase                                                                                                                                  |
| `outPrecomputeFrameWidth`          |                                                                                                                                                                     |
| `outPrecomputeFrameHeight`         |                                                                                                                                                                     |
| `outPrecomputeFramePARNumerator`   |                                                                                                                                                                     |
| `outPrecomputeFramePARDenominator` |                                                                                                                                                                     |
| `outPrecomputeFrameFieldType`      |                                                                                                                                                                     |
| `outPrecomputeCustomDataSize`      | Only needed if `outPrecomputePixelFormat` is custom                                                                                                                 |
| `outNeedsFieldSeparation`          | Indicates the plugin may operate on both fields simultaneously (eg non-spatial and non-time varying)                                                                |
