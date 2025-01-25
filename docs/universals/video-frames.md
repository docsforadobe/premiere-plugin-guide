.. _universals/video-frames:

Video Frames
################################################################################

Premiere stores each video frame in a PPix structure. A PPixHand is a handle to a PPix. This structure should not be accessed directly, but manipulated using various suites such as the :ref:`universals/sweetpea-suites.ppix-suite`, :ref:`universals/sweetpea-suites.ppix2-suite`, :ref:`universals/sweetpea-suites.ppix-creator-suite`, and :ref:`universals/sweetpea-suites.ppix-creator2-suite`.

Far from being just a boring buffer of RGB data, PPixes can contain a significant amount of information about a video frame, including: rectangle bounds (width, height), pixel aspect ratio, pixel format, field dominance, alpha interpretation, color space, gamma encoding, and more.

In the pixel buffer itself, there may be padding between neighboring horizontal rows of pixels. So when iterating through the pixels in the buffer, don't assume that the first pixel on the next line is stored immediately after the last pixel on the current line. Honor the rowbytes, which is a measure of the size in bytes of a row of pixels, including any extra padding.

Frames are guaranteed to be 16-byte aligned.
