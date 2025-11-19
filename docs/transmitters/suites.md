# Suites

For information on how to acquire and manage suites, as well as information on more suites that are available to other plugin types beyond just transmitters, see [SweetPea Suites](../universals/sweetpea-suites.md).

---

## Playmod Audio Suite

This suite is used to play audio during playback. There are many more functions that were used by players, still documented in the players chapter. Here we will only consider the single call in the suite that is relevant to transmitters.

### Host-Based, or Plugin Based Audio?

A transmitter has two choices for playing audio: it can ask the host to play the audio through the audio device selected by the user, or it can get audio buffers from the host and handle its own playback of audio.

### GetNextAudioBuffer

Retrieves from the host the next contiguous requested number of audio sample frames, specified in `inNumSampleFrames`, in `inInBuffers` as arrays of uninterleaved floats.

The plugin must manage the memory allocation of `inInBuffers`, which must point to n buffers of floating point values of length `inNumSampleFrames`, where n is the number of channels. This call is only available if `InitPluginAudio` was used.

Returns:

- `suiteError_NoError`,
- `suiteError_PlayModuleAudioNotInitialized`, or
- `suiteError_PlayModuleAudioNotStarted`

```cpp
prSuiteError (*GetNextAudioBuffer)(
  csSDK_int32   inPlayID,
  float**       inInBuffers,
  float**       outOutBuffers,
  unsigned int  inNumSampleFrames);
```

+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
|      Parameter      |                                                                       Description                                                                       |
+=====================+=========================================================================================================================================================+
| `inInBuffers`       | Currently unused in CS6.                                                                                                                               |
|                     |                                                                                                                                                         |
|                     | A pointer to an array of buffers holding `inNumSampleFrames` input audio in each buffer, corresponding to the total number of available input channels. |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| `outOutBuffers`     | A pointer to an array of buffers `inNumSampleFrames` long into which the host will write the output audio.                                             |
|                     |                                                                                                                                                         |
|                     | There must be N buffers, where N is the number of output channels for the output channel type specified in `InitPluginAudio`.                          |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| `inNumSampleFrames` | The size of each of the buffers in the array in both `inInBuffers` and `outOutBuffers`.                                                                |
+---------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

---

## Transmit Invocation Suite

This suite can be used by other types of plugins to push frames to transmitters.

For example, an effect or titler with a modal setup dialog could push frames to the output.
