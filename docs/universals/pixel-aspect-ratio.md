# Pixel Aspect Ratio

Pixel Aspect Ratio (PAR) is usually represented as a rational number, with a numerator and a denominator.

!!! note
    Several PAR values were changed in CS4 to match broadcast standards.

Here are some examples of pixel aspect ratios:

- NTSC DV 0.9091 PAR is (10, 11)
- NTSC DV Widescreen 1.2121 PAR is (40, 33)
- PAL DV 1.0940 PAR is (768, 702)
- PAL DV 1.4587 PAR is (1024, 702)
- Square 1.0 PAR is (1,1)

In certain legacy structures, PAR is represented as a single 32-bit integer, such as in `recCapInfoRec.pixelAspectRatio`.

This uses a representation where the numerator is bit-shifted 16 to the left, and OR'd with the denominator. For example NTSC DV 0.9091 PAR is `(10 << 16) \| 11`.
