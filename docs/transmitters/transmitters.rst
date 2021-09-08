.. _transmitters/transmitters:

Transmitters
################################################################################

This API provides support for pushing video, audio, and closed captions to external hardware. Transmitters can be specified by the user in Preferences > Playback. Other plugins such as importers and effects with settings preview dialogs can send video out to the active transmitter, opening up new possibilities for hardware monitoring. Transmit plugins are supported in Premiere Pro, After Effects (starting in CC 2014), SpeedGrade, Encore, Prelude, and Character Animator.

When a new transmitter instance is created, it is asked to describe the format(s) it wishes to receive the rendered video in. A transmitter plugin can request different formats depending on the source clip or timeline format. The host application will handle all the conversions to the desired video format. As an example, a transmitter instance may specify that it can only handle a fixed width and height, but any pixel format. Besides video conversions, the host handles scheduling for prefetching the media and asynchronous rendering.

A transmitter may leave the audio to be played by the host, through the system's sound drivers (ASIO or CoreAudio). Or, if a transmitter wants to handle the audio itself to send it to the external hardware, it can request audio using GetNextAudioBuffer in the :ref:`transmitters/suites.playmod-audio-suite`.

On playback, the host provides the transmitter with a clock callback, which the transmitter must call to update the host with the new time every frame. This allows the transmitter to orchestrate the audio/video sync.

Transmitters can use the :ref:`universals/sweetpea-suites.captioning-suite` to get any closed captions for the sequence.

Transmitters do not need to call the Playmod Device Controller suite to handle Export to Tape. This is handled at the player level.

----

What's New in Premiere Pro CS6.0.2?
================================================================================

A transmitter can now provide strings to label its audio channels, in ``tmAudioMode.outOutputAudioNames``. These strings will be used for the Audio Output Mapping preferences, rather than the default strings.
