# tmModule Structures

## tmStdParms

This is passed to all calls. Most of it is allocated and filled in by the transmitter on Startup, and may be modified during SetupDialog.

```cpp
typedef struct {
  csSDK_int32   inPluginIndex;
  PrMemoryPtr   ioSerializedPluginData;
  csSDK_size_t  ioSerializedPluginDataSize;
  void*         ioPrivatePluginData;
  piSuitesPtr   piSuites;
} tmStdParms;
```

| `inPluginIndex`              | If the plugin has defined multiple transmitters in the same module, this index value tells them apart.                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ioSerializedPluginData`     | This data should contain user-selectable settings for the transmitter, that would be shown in the transmitter settings dialog, and need to persist so they can be saved and restored from one session to another.<br/><br/>When allocating this for the first time during Startup, this must be allocated using `NewPtr` so it can be disposed by the host on shutdown.<br/><br/>This must be flat memory that can be serialized by by the host and will be already filled in when Startup is called if previously available. |
| `ioSerializedPluginDataSize` | Size of the data above. Set this during Startup, if not already set.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `ioPrivatePluginData`        | This data should contain any memory needed for use across calls to the transmitter, except the settings data stored in `ioSerializedPluginData`.<br/><br/>Allocate this during Startup. Unlike `ioSerializedPluginData`, it does not need to be flat, and must be disposed of by the plugin on Shutdown.                                                                                                                                                                                                                      |

---

## tmPluginInfo

This is to be filled in by the transmitter on Startup.

```cpp
typedef struct {
  prPluginID    outIdentifier;
  unsigned int  outPriority;
  prBool        outAudioAvailable;
  prBool        outAudioDefaultEnabled;
  prBool        outClockAvailable;
  prBool        outVideoAvailable;
  prBool        outVideoDefaultEnabled;
  prUTF16Char   outDisplayName[256];
  prBool        outHideInUI;
  prBool        outHasSetup;
  csSDK_int32   outInterfaceVersion;
} tmPluginInfo;
```

| `outIdentifier`                                   | Persistent plugin identifier.                                                                                                                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `outPriority`                                     | 0 is default, higher priority wins.                                                                                                                                                                                                                                        |
| `outAudioAvailable`                               | Set this to `kPrTrue` if the transmitter supports audio.                                                                                                                                                                                                                   |
| `outAudioDefaultEnabled`                          | Set this to `kPrTrue` if you want to be turned on to handle audio by default.                                                                                                                                                                                              |
| `outClockAvailable`<br/><br/><br/><br/><br/><br/> | Set this to `kPrTrue` if providing plugin based audio.<br/><br/><br/><br/><br/>Currently, even if using host-based audio, a transmitter must provide a clock - please let us know if you would like to use host-based audio only, and we will log a bug on this.<br/><br/> |
| `outVideoAvailable`                               | Set this to `kPrTrue` if the transmitter supports video.                                                                                                                                                                                                                   |
| `outVideoDefaultEnabled`                          | Set this to `kPrTrue` if you want to be turned on to handle video by default.                                                                                                                                                                                              |
| `outDisplayName[256]`                             | Set the display name of the transmitter, up 256 UTF-16 characters, including NULL terminator.                                                                                                                                                                              |
| `outHideInUI`                                     | Set this to `kPrTrue` if you don't want this to show up as a user-selectable option in the transmitter choices.                                                                                                                                                            |
| `outHasSetup`                                     | Set this to `kPrTrue` if providing a setup dialog.                                                                                                                                                                                                                         |
| `outInterfaceVersion`                             | Set this to the `tmInterfaceVersion` that the transmitter is being compiled for.                                                                                                                                                                                           |
| `outPushAudioAvailable`                           | New in 24.0. Set this to `kPrTrue` if the transmitter supports push audio functionality. The device will be enabled for a 'secondary' mode where audio from the 'primary' or 'clock' device is pushed to this one.                                                         |
| `outHasStreaming`                                 | New in 24.0. Set this to `kPrTrue` if the transmitter streams audio or video (over a network).                                                                                                                                                                             |

the device will be
: \*\*      enabled for a "secondary" mode where audio from the "primary" or "clock"
  \*\*      device is pushed to this one.
  \*\*      This is especially useful for remote devices.
  \*\*      PushAudio APIs will only be used in this "mirror" case.
  \*\*      StartPushAudio() initializes the device for subsequent PushAudio() calls.
  \*\*      Unlike StartPlaybackClock, StartPushAudio() is only called
  \*\*      once until StopPushAudio() is called.
  \*\*      PushAudio() is called whenever the desired buffer size is

---

## tmInstance

This structure contains information for the transmitter to use for initializing an instance.

```cpp
typedef struct {
  csSDK_int32          inInstanceID;
  PrTimelineID         inTimelineID;
  PrPlayID             inPlayID;
  prBool               inHasAudio;
  csSDK_uint32         inNumChannels;
  PrAudioChannelLabel  inChannelLabels[16];
  PrAudioSampleType    inAudioSampleType;
  float                inAudioSampleRate;
  prBool               inHasVideo;
  csSDK_int32          inVideoWidth;
  csSDK_int32          inVideoHeight;
  csSDK_int32          inVideoPARNum;
  csSDK_int32          inVideoPARDen;
  PrTime               inVideoFrameRate;
  prFieldType          inVideoFieldType;
  void*                ioPrivateInstanceData;
} tmInstance;
```

| `inInstanceID`          | Instance identifier.                                                                                                      |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------|
| `inTimelineID`          | `TimelineID`, for use with various suite functions. May be 0.                                                             |
| `inPlayID`              | `PlayID`, for use with various suite functions. May be 0.                                                                 |
| `inHasAudio`            | True if the instance is handling a sequence with audio.                                                                   |
| `inNumChannels`         | The number of audio channels.                                                                                             |
| `inChannelLabels[16]`   | The identifiers for each audio channel.                                                                                   |
| `inAudioSampleType`     | The format of the audio data.                                                                                             |
| `inAudioSampleRate`     | The sample rate of the audio data.                                                                                        |
| `inHasVideo`            | True if the instance is handling a sequence with video.                                                                   |
| `inVideoWidth`          | The video resolution.                                                                                                     |
| `inVideoHeight`         |                                                                                                                           |
| `inVideoPARNum`         | The numerator and denominator of the video pixel aspect ratio.                                                            |
| `inVideoPARDen`         |                                                                                                                           |
| `inVideoFrameRate`      | The frame rate of the video.                                                                                              |
| `inVideoFieldType`      | The field dominance of the video.                                                                                         |
| `ioPrivateInstanceData` | May be written by plugin in `CreateInstance`, and disposed of by `DisposeInstance`. Need not be serializable by the host. |

---

## tmAudioMode

A full description of an audio mode that the transmitter will support.

The transmitter should fill in this information during `QueryAudioMode`.

```cpp
typedef struct {
  float                outAudioSampleRate;
  csSDK_uint32         outMaxBufferSize;
  csSDK_uint32         outNumChannels;
  PrAudioChannelLabel  outChannelLabels[16];
  PrTime               outLatency;
  PrSDKString          outAudioOutputNames[16]
} tmAudioMode;
```

| `outAudioSampleRate`      | The preferred audio sample rate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `outMaxBufferSize`        | The maximum audio buffer size needed if the transmitter uses plugin-based audio to request audio buffers using the [Playmod Audio Suite](suites.md#playmod-audio-suite).                                                                                                                                                                                                                                                                                                                                                                                |
| `outNumChannels`          | The maximum number of audio channels supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `outChannelLabels[16]`    | Set the audio channel configuration for the output hardware using the appropriate identifiers for each audio channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `outLatency`              | This value is only used for playback, not when scrubbing.<br/><br/>It specifies how early to send frames in advance when audio-only playback starts, and how many frames that will be sent prior to a `StartPlaybackClock` call. Use this value to get playback in sync between the Source/Program Monitors and external hardware output.<br/><br/>All modes must have the same latency.<br/><br/>Take care to not set this value any higher than necessary, since playback start will delayed by this amount. A value equivalent to 5 video frames or less is recommended. |
| `outAudioOutputNames[16]` | New in CS6.0.2. These must be displayable names of physical audio outputs like "XYZ HD Speaker 1"<br/><br/>The audio output names in tmAudioMode should be allocated by the plugin using the [String Suite](../universals/sweetpea-suites.md#string-suite) and NOT disposed by the plugin. The host will take care of disposing these strings.                                                                                                                                                                                                   |

---

## tmVideoMode

A full description of a video mode that the transmitter will support.

Transmitter should fill in this information during `QueryVideoMode`.

```cpp
typedef struct {
  csSDK_int32    outWidth;
  csSDK_int32    outHeight;
  csSDK_int32    outPARNum;
  csSDK_int32    outPARDen;
  prFieldType    outFieldType;
  PrPixelFormat  outPixelFormat;
  PrSDKString    outStreamLabel;
  PrTime         outLatency;
  ColorSpaceRec  outColorSpaceRec;
} tmVideoMode;
```

| `outWidth`         | The preferred video resolution.<br/><br/>Set to 0 if any resolution is supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `outHeight`        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `outPARNum`        | The preferred video pixel aspect ratio.<br/><br/>Set to 0 if any pixel aspect ratio is supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `outPARDen`        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `outFieldType`     | The supported video field type.<br/><br/>Set to prFieldsAny if any field dominance is supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `outPixelFormat`   | The preferred video pixel format.<br/><br/>Set to `PrPixelFormat_Any` if any format is acceptable.<br/><br/>If your transmitter would benefit from on-GPU frames, please let us know.                                                                                                                                                                                                                                                                                                                                                                               |
| `outStreamLabel`   | Leave this as 0 for now. Stream labels are not yet supported by transmitters (bug group BG127571)                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `outLatency`       | This value is only used for playback, not when scrubbing.<br/><br/>It specifies how early to send frames in advance when playback starts, and how many frames that will be sent prior to a `StartPlaybackClock` call.<br/><br/>Use this value to get playback in sync between the Source/Program Monitors and external hardware output.<br/><br/>All modes must have the same latency.<br/><br/>Take care to not set this value any higher than necessary, since playback start will delayed by this amount. A value equivalent to 5 frames or less is recommended. |
| `outColorSpaceRec` | New in 14.x. Definition of the colorspace in use; defaults to BT 709 full range 32f.<br/><br/>Transmitter can request host application to send frame in specific colorspace. See to `ColorSpaceRec` for detailed description.                                                                                                                                                                                                                                                                                                                                       |

---

## tmPlaybackClock

This structure is filled out by the host and sent to the transmitter to describe the playback clock to be managed by the transmitter.

The transmitter uses the callback here to update the host at regular intervals.

```cpp
typedef struct {
  tmClockCallback         inClockCallback;
  void*                   inCallbackContext;
  PrTime                  inStartTime;
  pmPlayMode              inPlayMode;
  float                   inSpeed;
  PrTime                  inInTime;
  PrTime                  inOutTime;
  prBool                  inLoop;
  tmDroppedFrameCallback  inDroppedFrameCallback;
} tmPlaybackClock;
```

| `tmClockCallback`        | A pointer to a call with the following signature:<br/><br/>```default<br/>void (*tmClockCallback)(<br/>  void*   inContext,<br/>  PrTime  inRelativeTimeAdjustment);<br/>```<br/><br/>Call this function when the time changes with a non-speed adjusted amount to increment the clock by.<br/><br/>This can be called once per frame in response to PushVideo.<br/><br/>Using a negative time should only be used to wait for device, not to achieve sync.<br/><br/>The transmitter will not receive any frames while using a negative time.<br/><br/>After the first positive valued clock callback, the time will be in `StartTime + inRelativeTimeAdjustment * inSpeed`.   |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `inCallbackContext`      | Pass this into the clock callback above.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `inStartTime`            | Start the clock at this time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `inPlayMode`             | Specifies whether the `StartPlaybackClock` was set for playback or scrubbing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `inSpeed`                | 1.0 is normal speed, -2.0 is double speed backwards.<br/><br/>Informational only.<br/><br/>This is useful for the built-in DV transmitter, which only writes DV captions if playing at regular speed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `inInTime`               | Informational only and will be handled by the host.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `inOutTime`              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `inLoop`                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `inDroppedFrameCallback` | A pointer to a call with the following signature:<br/><br/>```default<br/>void (*tmDroppedFrameCallback)(<br/>  void*        inContext,<br/>  csSDK_int64  inNewDroppedFrames);<br/>```<br/><br/>Use this call to report frames pushed to the transmit plugin on PushVideo but not delivered to the device.<br/><br/>If every frame pushed to the transmitter is sent out to hardware on time, then this should never need to be called as the host will count frames not pushed to the plugin.<br/><br/>`inNewDroppedFrames` should be the number of additional dropped frames since the last time `tmDroppedFrameCall` back was called.                                      |

---

## tmPushVideo

Describes a frame of video to be transmitted.

```cpp
typedef struct {
  PrTime                 inTime;
  pmPlayMode             inPlayMode;
  PrRenderQuality        inQuality;
  const tmLabeledFrame*  inFrames;
  csSDK_size_t           inFrameCount;
} tmPushVideo;
```

| `inTime`       | Describes which frame of the video is being passed in.<br/><br/>A negative value means the frame should be displayed immediately.<br/><br/>Use this value to determine the corresponding timecode for the frame being pushed.                                                                                                                          |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `inPlayMode`   | Pass this into the clock callback above.                                                                                                                                                                                                                                                                                                               |
| `inQuality`    | The quality of the render.                                                                                                                                                                                                                                                                                                                             |
| `inFrames`     | The frame or set of frames to transmit. As of CS6, this will always be a single frame.<br/><br/>`tmLabeledFrame` is defined as:<br/><br/>```default<br/>typedef struct {<br/>  PPixHand          inFrame;<br/>  PrSDKStreamLabel  inStreamLabel;<br/>} tmLabeledFrame;<br/>```<br/><br/>The frame(s) must be disposed of by the transmitter when done. |
| `inFrameCount` | The number of frames in inFrames.                                                                                                                                                                                                                                                                                                                      |

---

## tmPushAudio

Describes audio samples to be transmitted.

```cpp
typedef struct {
      PrTime          inTime;
      float**         inBuffers;
      csSDK_uint32    inNumSamples;
      csSDK_uint32    inNumChannels;
} tmPushAudio;
```

| `inTime`        | Describes which frame of the video is being passed in.<br/><br/>A negative value means the frame should be displayed immediately.<br/><br/>Use this value to determine the corresponding timecode for the frame being pushed.   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `inBuffers`     | The audio date to be transmitted.                                                                                                                                                                                               |
| `inNumSamples`  | Number of samples to process.                                                                                                                                                                                                   |
| `inNumChannels` | Number of channels to output.                                                                                                                                                                                                   |

---

## tmStopPushAudio

Sent when playback via PushAudio() ends.

```cpp
typedef struct {
      PrTime          inTime;
      float**         inBuffers;
      csSDK_uint32    inNumSamples;
      csSDK_uint32    inNumChannels;
} tmPushAudio;
```

| `inTime`        | Describes which frame of the video is being passed in.<br/><br/>A negative value means the frame should be displayed immediately.<br/><br/>Use this value to determine the corresponding timecode for the frame being pushed.   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `inBuffers`     | The audio date to be transmitted.                                                                                                                                                                                               |
| `inNumSamples`  | Number of samples to process.                                                                                                                                                                                                   |
| `inNumChannels` | Number of channels to output.                                                                                                                                                                                                   |
