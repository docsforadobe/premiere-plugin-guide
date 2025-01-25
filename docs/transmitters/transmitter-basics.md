# Transmitter Basics

## Basic Organization

A transmitter module can define multiple plugins. Each plugin can appear in the Playback Preferences as an option for video playback and/or audio playback. Only one transmitter can be used for audio, since the transmitter used for audio drives the clock. Multiple transmitters may be selected for video simultaneously.

When active, multiple instances of a single plugin can be created. An instance is created to display a clip or sequence. Hardware access is regulated through ActivateDeactivate. Only an active instance should access the hardware.

---

## Video Formats

Specify which video format(s) you wish to receive during QueryVideoMode. To simplify your plugin, be as specific as possible, and allow the host to perform the conversion asynchronously ahead of time. Packed and compressed formats are also supported. If multiple formats are specified, the closest will be selected at render time. If your transmitter would benefit from on-GPU frames, please let us know.

When sent QueryVideoMode, the transmitter is informed about the clip/sequence video attributes by being passed a tmInstance pointer. So, for example, if the transmitter instance is constructed to support a 1920x1080 timeline, it can report that same size back to the host application, so that it will not have to handle any scaling. If, for example, it does handle scaling, and it is constructed to handle a 1440x1080 timeline, it can report 1440x1080 and handle the scaling itself. In this way you can choose a single fixed size depending on the timeline.

When video frames are pushed to the transmitter, properties like pixel format may change on a segment-by-segment basis depending on the source footage. Other properties like size may change based on the current fractional resolution, which may differ between scrubbing and stopped.

---

## Fractional Resolution

In the Premiere Pro Source and Program Monitors, the user can choose independent resolutions for rendering during playback and paused modes. For example, it is common to have the playback resolution set to half, and paused resolution set to full.

If an output card has a hardware scaler, the transmit plugin can declare support for fractional resolutions. For example, for a 1920x1080 instance, it could declare support for not only

1920x1080, but also 960x540, 480x270, etc. This will allow the renderer to skip the step of rescaling back up to full resolution after rendering at a fractional resolution. If however, the plugin only declares support for full resolution, the renderer will scale the video back up before pushing it to the transmitter.

---

## Audio Format

During QueryAudioMode, a transmitter will be told how many channels the instance has. The transmitter should change that value based on what it can support and then make sure the buffers it provides match that. Although Premiere Pro can support 32 channels of audio, transmitters can only support up to 16 channels of audio.

As of CS6, sequences will currently always report audio available in CreateInstance, even if empty. An example of somewhere that a transmitter will be called with no audio is for video output from the RED settings dialog, which is video only.

A transmitter should call GetNextAudioBuffer only when inAudioActive is passed as true to ActivateDeactivate.

---

## Frame Rate

For framerate, video will be pushed to you at the rate of the timeline. This was chosen because of the wide variety in conversion policies, including pulldown, frame duplication, etc.

---

## Dropped Frames

If the host cannot keep up rendering, it will send duplicate frames with PushVideo. If you receive a frame that cannot be sent out to hardware on time, notify the host using inDroppedFrame Callback in tmPlaybackClock. In Premiere Pro, the user can turn on the Dropped Frame Indicator to see the total number of frames that were dropped either because the host couldn't keep up, or the hardware couldn't keep up.

---

## Sync Between Application UI and Hardware Output

Naturally there is some latency between the time the host sends frames to be displayed on the output, and the time it can actually be displayed. Use tmVideoMode.outLatency to specify the latency. For example, if a transmitter specifies 5 frames of latency, when the user starts playback, the host will send 5 frames of video to the transmitter before sending StartPlaybackClock. This allows time for the transmitter to send frames to the hardware output in advance, so that the hardware output will be in sync with the monitor in the host application UI.

When the user is scrubbing in the timeline, send the video frames as fast as possible to the output. The host application UI will not wait for the hardware output to catch up, and currently as of

6.0.1 there may be a noticable latency. To reduce the scrubbing latency as much as possible, when scrubbing or stopped the transmitter should cancel any frames it has pending to immediately display the new one.

---

## Dog Ears

Turn on dog ears to view statistics about the frames being sent to the transmitter. This is useful to view information such as pixel formats and much more.

!!! note
    This mode may result in duplicate PushVideo calls made for a single frame.

---

## Closed Captioning

This captioning data is attached to a sequence by the user via menu items in the Sequence menu. In the Program Monitor, the Closed Captioning Display options in the fly-out menu give the user control over the display. The hardware should always transmit any Closed Captioning data, and the user can go through the hardware monitor's on-screen display menu to choose which caption track to view. The closed captioning data is accessible using the new [Captioning Suite](../universals/sweetpea-suites.md#universals-sweetpea-suites-captioning-suite). Use this data for the hardware output.

---

## Driving Transmitters from Other Plugins

Transmitters can be driven by many areas of the Premiere Pro interface. Currently, they are called to show frames from the Program Monitor and Source Monitor. But other types of plugins can use the [Transmit Invocation Suite](suites.md#transmitters-suites-transmit-invocation-suite) to push frames to transmitters. For example, an effect or titler with a modal setup dialog could push frames to the output.

---

## Entry Point

This entry point function will be called once on load, and once on unload.

```cpp
tmResult (*tmEntryFunc)(
  csSDK_int32  inInterfaceVersion,
  prBool       inLoadModule,
  piSuitesPtr  piSuites,
  tmModule*    outModule)
```

A tmModule is a structure of function pointers, which the transmitter implements.
