.. _universals/audio:

Audio
################################################################################

----

32-bit Float, Uninterleaved Format
================================================================================

All audio calls to and from Premiere use arrays of buffers of 32-bit floats to pass audio. Audio is not interleaved, rather separate channels are stored in separate buffers. So the structure for stereo audio looks like this:

::

  float\* audio[2];

where audio[0] is the address of a buffer N samples long, and audio[1] is the address of a second buffer N samples long. audio[0] contains the left channel, and audio[1] contains the right channel. N is the number of sample frames in the buffer.

Since Premiere uses 32-bit floats for each audio sample, it can represent values above 0 dB. 0 dB corresponds to +/- 1.0 in floating point. A floating point sample can be converted to a 16-bit short integer by multiplying by 32767.0 and casting the result to a short.

E.g.:

::

  sample16bit[n] = (short int) (sample32bit[n] * 32767.0)

The plug-in is responsible for converting to and from the 32-bit uninterleaved format when reading a file that uses a different format. There are calls to convert between formats in the Audio Suite. For symmetry in the int <--> float conversions, we recommend you use the utility functions provided.

----

Audio Sample Types
================================================================================

Since 32-bit floats are the only audio format ever passed, there is no option of sample type or bit depth. However, file formats do use a variety of sample types and bit depths, so ``AudioSampleTypes`` define a variety of possible formats.

These formats are used to set members in structures passed to Premiere to define the user interface, and do not affect the format of the audio passed to and from Premiere.

+--------------------------------------------+-----------------------------------------------+
|           **PrAudioSampleType**            |                **Description**                |
+============================================+===============================================+
| ``kPrAudioSampleType_8BitInt``             | 8-bit integer                                 |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_8BitTwosInt``         | 8-bit integer, two's complement               |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_16BitInt``            | 16-bit integer                                |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_24BitInt``            | 24-bit integer                                |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_32BitInt``            | 32-bit integer                                |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_32BitFloat``          | 32-bit floating point                         |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_64BitFloat``          | 64-bit floating point                         |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_16BitIntBigEndian``   | 16-bit integer, big endian                    |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_24BitIntBigEndian``   | 24-bit integer, big endian                    |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_32BitIntBigEndian``   | 32-bit integer, big endian                    |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_32BitFloatBigEndian`` | 32-bit floating point, big endian             |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_Compressed``          | Any non-PCM format                            |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_Packed``              | Any PCM format with mixed sample types        |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_Other``               | A sample type not in this list                |
+--------------------------------------------+-----------------------------------------------+
| ``kPrAudioSampleType_Any``                 | Any available sample type (used by exporters) |
+--------------------------------------------+-----------------------------------------------+

----

Audio Sample Frames
================================================================================

A sample frame is a unit of measurement for audio. One audio sample frame describes all channels of one sample of audio. Each sample is a 32-bit float. Thus, the storage requirement of an audio sample frame in bytes is equal to ``4 * number of channels``.

----

Audio Sample Rate
================================================================================

``PrAudioSample`` is a ``prInt64``

----

Audio Channel Types
================================================================================

Premiere currently supports four different audio channel types: mono, stereo, 5.1, and max channel.

Greater than 5.1 channel support was originally added in Premiere Pro 4.0.1, with partial support for a 16 channel master audio track, only for importing OMFs and playing out to hardware.

In CS6, 16-channel audio export was added.

Starting in CC, the audio channel support is increased to 32 channels.

+------------------------------------+-------------------------------------------------------------+
|       **PrAudioChannelType**       |                       **Description**                       |
+====================================+=============================================================+
| ``kPrAudioChannelType_Mono``       | Mono                                                        |
+------------------------------------+-------------------------------------------------------------+
| ``kPrAudioChannelType_Stereo``     | Stereo. The order of the stereo channels is:                |
|                                    |                                                             |
|                                    | - ``kPrAudioChannelLabel_FrontLeft``,                       |
|                                    | - ``kPrAudioChannelLabel_FrontRight``.                      |
+------------------------------------+-------------------------------------------------------------+
| ``kPrAudioChannelType_51``         | 5.1 audio.                                                  |
|                                    |                                                             |
|                                    | The order of the 5.1 channels is:                           |
|                                    |                                                             |
|                                    | - ``kPrAudioChannelLabel_FrontLeft``,                       |
|                                    | - ``kPrAudioChannelLabel_FrontRight``,                      |
|                                    | - ``kPrAudioChannelLabel_BackLeft``,                        |
|                                    | - ``kPrAudioChannelLabel_BackRight``,                       |
|                                    | - ``kPrAudioChannelLabel_FrontCenter``,                     |
|                                    | - ``kPrAudioChannelLabel_LowFrequency``                     |
+------------------------------------+-------------------------------------------------------------+
| ``kPrAudioChannelType_MaxChannel`` | New in CC.                                                  |
|                                    |                                                             |
|                                    | ``kMaxAudioChannelCount``, defined as 32 channels as of CC. |
|                                    |                                                             |
|                                    | All channels use ``kPrAudioChannelLabel_Discrete``.         |
+------------------------------------+-------------------------------------------------------------+
