# Time

There are two different representations of time: `scale over sampleSize`, and `ticks`.

---

## scale over sampleSize

The first representation of time uses value/scale/`sampleSize` components, either separated, or combined in a TDB_TimeRecord structure. scale over `sampleSize` defines the timebase. For example, to represent the NTSC standard of 29.97 frames per second, `scale` / `sampleSize = 30000` / 1001. To represent the PAL standard of 25 frames per second, 25 / 1.

To represent the 24p standard of 23.976, 23976 / 1000, or 24000 / 1001. To represent most other timebases, use `sampleSize = 1`, and scale is the frame rate (e.g. 15, 24, 30 fps, etc). Another way of thinking about scale and `sampleSize` is that `sampleSize` is the duration of a frame of video, and scale is that duration of a second of video.

`value` is the time in the timebase given by `scale` over `sampleSize`. So, for example, 30 frames with a sampleSize of 1001 have a value of 30030.

To convert `value` to seconds, divide by scale. To convert `value` to frames, divide by `sampleSize`.

Sometimes, as when handling audio-only media, `sampleSize` refers to a sample of audio, and `sampleSize = 1`. In this case, scale is the audio sampling rate (22050, 32000, 44100, 48000 Hz, etc).

---

## PrTime

Most newer areas of the API use a tick-based time value that is stored in a signed 64-bit integer. Variables that use this new format are of type PrTime. When a frame rate is represented as a PrTime, the frame rate is the number of ticks in a frame duration.

The current number of ticks per second must be retrieved using the callback in the [Time Suite](sweetpea-suites.md#universals-sweetpea-suites-time-suite). This rate is guaranteed to be constant for the duration of the application’s run-time.
