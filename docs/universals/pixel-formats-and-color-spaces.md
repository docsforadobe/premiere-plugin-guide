# Pixel Formats And Color Spaces

As of CC, Premiere supports 69 different pixel formats, not including raw and custom formats.

Why so many? Each pixel format has it's unique advantages and disadvantages. 8-bit formats are compact, but lack quality. 32-bit ones are more accurate, but overkill in some situations.

Compressed formats are great for storing raw frames, but bad for effects processing. And so on… In summary, choose wisely!

---

## What Format Should I Use?

Starting in CS4, plugins no longer need to support 8-bit BGRA at a minimum. If required, Premiere can make intermediate format conversions in the render pipeline, although these intermediate conversions will be avoided if possible.

Previously in CS3 and earlier, all plugins except importers needed to support 8-bit per channel BGRA, even if they supported other formats.

When choosing which pixel formats to support, there are different factors to consider, depending on the plugin type.

### Importers

Importers typically should provide frames in a format closest to the source format.

If needed, Premiere can convert any compressed format to a 8-bit or 32-bit uncompressed format. Keeping the format compressed as long as possible as it passes through the render pipeline will save memory and bandwidth.

Starting in Premiere Pro CC 2014, importers can now choose the format they are rendering in. This allows importers to change pixel formats and quality based on criteria like enabled hardware and other source settings, such as HDR. To handle the negotiation, implement *imSelectClipFrameDescriptor*.

### Effects

Effects should support the uncompressed format(s) that works best with the effect's pixel processing algorithm.

If the algorithm is based on RGB pixel calculations, provide a fast render path using 8-bit BGRA, and optionally a high-quality render path using 32-bit BGRA. If the algorithm is Y'UV-based, use the VUYA pixel formats.

### Exporters and Transmitters

Exporters and transmitters should request frames in a format closest to the output format. New in CS5, PrPixelFormat_Any can be used in exporter render requests.

Any render function that takes a list of pixel formats can now be called with just two formats - the desired 4:4:4:4 pixel format, and PrPixelFormat_Any. This allows the host to avoid frame conversions and decompressions in many very common cases. The best part is that the plugin doesn't need to

understand all the possible pixel formats to make use of this. It can use the [Image Processing Suite](sweetpea-suites.md#image-processing-suite) to copy/convert from any a PPix of any format to a separate memory buffer, which is a copy that would likely need to be done anyway.

After the request is made, Premiere analyzes the preferred format of all importers and effects that are used to produce a single rendered frame, as well as the list of requested formats, and chooses the best format to use on a per-segment basis.

If the requestor supports more than one format, and the importers and effects used for various clips in the sequence support different formats, the render may use different formats for each segment.

Premiere Pro's built-in Rec. 601 to 709 color space conversion can be slow. So if the majority of the sources and effects use the Rec 601 color space, and if the exporter or transmitter can handle the 601 to 709 conversion quickly on its own, it may be faster to do the color space conversion in the exporter or transmitter.

### Other Considerations

For high-bit depth support, the 32f formats are the recommended route, rather than the 16u formats. For example, an exporter that supports 10-bit Y'UV should ask for frames in 32f Y'UV format, and then convert the 32f to 10u.

The ARGB formats can be natively used in the After Effects render pipeline, and are used by After Effects effect plugins that do not specifically support any other pixel format. However, in Premiere Pro, these ARGB formats will require byte-swapping, and shouldn't be used.

---

## Byte Order

BGRA, ARGB, and VUYA are written in order of increasing memory address from left to right. Uncompressed formats have a lower-left origin, meaning the first pixel in the buffer describes the pixel in the lower-left corner of the image. Compressed formats have format-specific origins. Use calls in the [Image Processing Suite](sweetpea-suites.md#image-processing-suite) to get details on any format.

8-bit and 16-bit BGRA formats do not contain super whites or super blacks.

The 16-bit formats use channels that go from black at 0 to white at 32768, like After Effects and Photoshop 16-bit formats.

### Unpacked, Uncompressed

|   PrPixelFormat   | Bits / Channel | Format / FourCC |               Additional Details               |
| ----------------- | -------------- | --------------- | ---------------------------------------------- |
| BGRA_4444_8u      | 8              | RGB             |                                                |
| VUYA_4444_8u      | 8              | Y'UV            |                                                |
| VUYA_4444_8u_709  | 8              | Y'UV            | Rec. 709 color space. New in Premiere Pro 4.1. |
| BGRA_4444_16u     | 16             | RGB             |                                                |
| BGRA_4444_32f     | 32             | RGB             |                                                |
| VUYA_4444_32f     | 32             | Y'UV            |                                                |
| VUYA_4444_32f_709 | 32             | Y'UV            | Rec. 709 color space. New in Premiere Pro 4.1. |

### Unpacked, Uncompressed, native After Effects support only

| PrPixelFormat | Bits / Channel | Format / FourCC |                              Additional Details                              |
| ------------- | -------------- | --------------- | ---------------------------------------------------------------------------- |
| ARGB_4444_8u  | 8              | RGB             | For native After Effects support. For native Premiere Pro support, use BGRA. |
| ARGB_4444_16u | 16             | RGB             |                                                                              |
| ARGB_4444_32f | 32             | RGB             |                                                                              |

### Unpacked, Uncompressed, with implicit alpha

|   PrPixelFormat   | Bits / Channel | Format / FourCC |                                                                                                        Additional Details                                                                                                         |
| ----------------- | -------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BGRX_4444_8u      | 8              | RGB             | Implicitly opaque alpha channel. The actual data may be left filled with garbage, which allows optimized processing by both the plugin and host, with the understanding the the alpha channel is opaque. New in Premiere Pro CS5. |
| VUYX_4444_8u      | 8              | Y'UV            |                                                                                                                                                                                                                                   |
| VUYX_4444_8u_709  | 8              | Y'UV            |                                                                                                                                                                                                                                   |
| XRGB_4444_8u      | 8              | RGB             |                                                                                                                                                                                                                                   |
| BGRX_4444_16u     | 16             | RGB             |                                                                                                                                                                                                                                   |
| XRGB_4444_16u     | 16             | RGB             |                                                                                                                                                                                                                                   |
| BGRX_4444_32f     | 32             | RGB             |                                                                                                                                                                                                                                   |
| VUYX_4444_32f     | 32             | Y'UV            |                                                                                                                                                                                                                                   |
| VUYX_4444_32f_709 | 32             | Y'UV            |                                                                                                                                                                                                                                   |
| XRGB_4444_32f     | 32             | RGB             |                                                                                                                                                                                                                                   |
| BGRP_4444_8u      | 8              | RGB             | Premultiplied alpha. New in Premiere Pro CS5.                                                                                                                                                                                    |
| VUYP_4444_8u      | 8              | Y'UV            |                                                                                                                                                                                                                                   |
| VUYP_4444_8u_709  | 8              | Y'UV            |                                                                                                                                                                                                                                   |
| PRGB_4444_8u      | 8              | RGB             |                                                                                                                                                                                                                                   |
| BGRP_4444_16u     | 16             | RGB             |                                                                                                                                                                                                                                   |
| PRGB_4444_16u     | 16             | RGB             |                                                                                                                                                                                                                                   |
| BGRP_4444_32f     | 32             | RGB             |                                                                                                                                                                                                                                   |
| VUYP_4444_32f     | 32             | Y'UV            |                                                                                                                                                                                                                                   |
| VUYP_4444_32f_709 | 32             | Y'UV            |                                                                                                                                                                                                                                   |
| PRGB_4444_32f     | 32             | RGB             |                                                                                                                                                                                                                                   |

### Linear RGB

|    PrPixelFormat     | Bits / Channel | Format / FourCC |                                     Additional Details                                      |
| -------------------- | -------------- | --------------- | ------------------------------------------------------------------------------------------- |
| BGRA_4444_32f_Linear | 32             | RGB             | These RGB formats have a gamma of 1, rather than the standard 2.2. New in Premiere Pro CS5. |
| BGRP_4444_32f_Linear | 32             | RGB             |                                                                                             |
| BGRX_4444_32f_Linear | 32             | RGB             |                                                                                             |
| ARGB_4444_32f_Linear | 32             | RGB             |                                                                                             |
| PRGB_4444_32f_Linear | 32             | RGB             |                                                                                             |
| XRGB_4444_32f_Linear | 32             | RGB             |                                                                                             |

### Packed, Uncompressed formats

|  PrPixelFormat   | Bits / Channel | Format / FourCC |                       Additional Details                        |
| ---------------- | -------------- | --------------- | --------------------------------------------------------------- |
| RGB_444_10u      |                |                 | New in Premiere Pro CC. Full range 10-bit 444 RGB little-endian |
| YUYV_422_8u_601  | 8              | 'YUY2'          | New in Premiere Pro CS4.                                       |
| YUYV_422_8u_709  | 8              | 'YUY2'          | Rec. 709 color space. New in Premiere Pro CS4.                 |
| UYVY_422_8u_601  | 8              | 'UYVY'          | New in Premiere Pro CS4.                                       |
| UYVY_422_8u_709  | 8              | 'UYVY'          | Rec. 709 color space. New in Premiere Pro CS4.                 |
| V210_422_10u_601 | 10             | 'v210'          | New in Premiere Pro CS4.                                       |
| V210_422_10u_709 | 10             | 'v210'          | Rec. 709 color space. New in Premiere Pro CS4.                 |
| UYVY_422_32f_601 | 32             | 'UYVY'          | New in Premiere Pro CC.                                        |
| UYVY_422_32f_709 | 32             | 'UYVY'          | New in Premiere Pro CC.                                        |

### Compressed Y'UV

|                           PrPixelFormat                           | Bits / Channel |   Format / FourCC    |                                                                                  Additional Details                                                                                   |
| ----------------------------------------------------------------- | -------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NTSCDV25                                                          | 8              | DV25 / 'dvsd'        |                                                                                                                                                                                       |
| PALDV25                                                           | 8              | DV25 / 'dvsd'        |                                                                                                                                                                                       |
| NTSCDV50                                                          | 8              | DV50 / 'dv50'        |                                                                                                                                                                                       |
| PALDV50                                                           | 8              | DV50 / 'dv50'        |                                                                                                                                                                                       |
| NTSCDV100_720p                                                    | 8              | DV100 720p / 'dvh1'  |                                                                                                                                                                                       |
| PALDV100_720p                                                     | 8              | DV100 720p / 'dvh1'  |                                                                                                                                                                                       |
| NTSCDV100_1080i                                                   | 8              | DV100 1080i / 'dvh1' |                                                                                                                                                                                       |
| PALDV100_1080i                                                    | 8              | DV100 1080i / 'dvh1' |                                                                                                                                                                                       |
| YUV_420_MPEG2_FRAME_PICTURE_PLANAR_8u_601                         | 8              | Y'UV 4:2:0 / 'YV12'  | Progressive Rec. 601 color space                                                                                                                                                      |
| YUV_420_MPEG2_FIELD_PICTURE_PLANAR_8u_601                         | 8              | Y'UV 4:2:0 / 'YV12'  | Interlaced Rec. 601 color space                                                                                                                                                       |
| YUV_420_MPEG2_FRAME_PICTURE_PLANAR_8u_601_FullRange               | 8              | Y'UV 4:2:0 / 'YV12'  | New in Premiere Pro CS5.5. Progressive Rec. 601 color space, full range Y'UV                                                                                                          |
| YUV_420_MPEG2_FIELD_PICTURE_PLANAR_8u_601_FullRange               | 8              | Y'UV 4:2:0 / 'YV12'  | New in Premiere Pro CS5.5. Interlaced Rec. 601 color space, full range Y'UV                                                                                                           |
| YUV_420_MPEG2_FRAME_PICTURE_PLANAR_8u_709                         | 8              | Y'UV 4:2:0 / 'YV12'  | Progressive Rec. 709 color space                                                                                                                                                      |
| YUV_420_MPEG2_FIELD_PICTURE_PLANAR_8u_709                         | 8              | Y'UV 4:2:0 / 'YV12'  | Interlaced Rec. 709 color space                                                                                                                                                       |
| YUV_420_MPEG2_FRAME_PICTURE_PLANAR_8u_709_FullRange               | 8              | Y'UV 4:2:0 / 'YV12'  | New in Premiere Pro CS6. Progressive Rec. 709 color space, full range Y'UV. Matricies scaled from 709 by each component's excursion (Y is scaled by 219/255 and UV scaled by 224/256) |
| YUV_420_MPEG2_FIELD_PICTURE_PLANAR_8u_709_FullRange               | 8              | Y'UV 4:2:0 / 'YV12'  | New in Premiere Pro CS6. Interlaced Rec. 709 color space, full range Y'UV                                                                                                             |
| YUV_420_MPEG4_FRAME_PICTURE_PLANAR_8u_601                         | 8              | Y'UV 4:2:0 / 'YV12'  | New in Premiere Pro CS6. Progressive Rec. 601 color space                                                                                                                             |
| YUV_420_MPEG4_FIELD_PICTURE_PLANAR_8u_601                         | 8              | Y'UV 4:2:0 / 'YV12'  | New in Premiere Pro CS6. Interlaced Rec. 601 color space                                                                                                                              |
| YUV_420_MPEG4_FRAME_PICTURE_PLANAR_8u_601_FullRange               | 8              | Y'UV 4:2:0 / 'YV12'  | New in Premiere Pro CS6. Progressive Rec. 601 color space, full range Y'UV                                                                                                            |
| YUV_420_MPEG4_FIELD_PICTURE_PLANAR_8u_601_FullRange               | 8              | Y'UV 4:2:0 / 'YV12'  | New in Premiere Pro CS6. Interlaced Rec. 601 color space, full range Y'UV                                                                                                             |
| YUV_420_MPEG4_FRAME_PICTURE_PLANAR_8u_709                         | 8              | Y'UV 4:2:0 / 'YV12'  | New in Premiere Pro CS6. Progressive Rec. 709 color space                                                                                                                             |
| YUV_420_MPEG4_FIELD_PICTURE_PLANAR_8u_709                         | 8              | Y'UV 4:2:0 / 'YV12'  | New in Premiere Pro CS6. Interlaced Rec. 709 color space                                                                                                                              |
| YUV_420_MPEG4_FRAME_PICTURE_PLANAR_8u_709_FullRange               | 8              | Y'UV 4:2:0 / 'YV12'  | New in Premiere Pro CS6. Progressive Rec. 709 color space, full range Y'UV. Matricies scaled from 709 by each component's excursion (Y is scaled by 219/255 and UV scaled by 224/256) |
| PrPixelFormat_YUV_420_MPEG4_FIELD_PICTURE_PLANAR_8u_709_FullRange | 8              | Y'UV 4:2:0 / 'YV12'  | New in Premiere Pro CS6. Interlaced Rec. 709 color space, full range Y'UV                                                                                                             |

### Miscellaneous

| PrPixelFormat | Bits / Channel | Format / FourCC |              Additional Details              |
| ------------- | -------------- | --------------- | -------------------------------------------- |
| Raw           | ?              | ?               | Raw, opaque data, with no rowbytes or height |

---

## Custom Pixel Formats

New in CS4, custom pixel formats are supported. Plugins can define a pixel format which can pass through various aspects of our pipeline, but remain completely opaque to the built-in renderers. Use the macro MAKE_THIRD_PARTY_CUSTOM_PIXEL_FORMAT_FOURCC in the [Pixel Format Suite](sweetpea-suites.md#pixel-format-suite). Please use a unique name to avoid collisions.

The format doesn't need to be registered in any sense. They can just be used in the same way the current pixel formats are used, though in many cases they will be ignored.

The first place the new pixel formats can appear in the render pipeline is at the importer level. Importers can advertise the availability of these pixel formats during *imGetIndPixelFormat*, just as they would for any other format.

!!! note
    Importers must also support a non-custom pixel format, for the case where the built-in renderer is used, which would not be prepared to handle an opaque pixel format added by a third-party.

In the importer, use the new CreateCustomPPix call in the [PPix Creator 2 Suite](sweetpea-suites.md#ppix-creator-2-suite), and specify a custom pixel format and a memory buffer size, and the call will pass back a PPix of the requested format. These PPixes can then be returned from an importer, like any other. The memory for the PPix will be allocated by MediaCore, and must be a flat data structure as they will need to be copied between processes.

However, because the data itself is completely opaque, it can easily be a reference to another pixel buffer, as long as the reference can be copied. For example, the buffer could be a constant 16 bytes, containing a GUID which can be used to access a memory buffer by name in another process.

To query for available custom pixel formats from the player, use the GetNumCustomPixelFormats and GetCustomPixelFormat calls in the [Clip Render Suite](sweetpea-suites.md#clip-render-suite). The custom pixel formats will not returned by the regular calls to get the supported frame formats, mostly to prevent them from being used.

The other [Clip Render Suite](sweetpea-suites.md#clip-render-suite) functions will accept requests for custom pixel formats and will return these custom PPixes like any others.

With the [Clip Render Suite](sweetpea-suites.md#clip-render-suite), a third-party player can directly access these custom PPixes from a matched importer.

### Smart Rendering

Smart rendering involves passing compressed frames from the importer to the exporter, to bypass any unnecessary decompression and recompression, which reduces quality and performance.

The way to implement this is by passing custom PPixes between an importer, exporter, and usually a renderer.

In the rare case of exporting a single clip, using the [Clip Render Suite](sweetpea-suites.md#clip-render-suite) in the exporter to request custom PPixes from the importer is sufficient. But in the more common case of exporting a sequence, a renderer that supports the custom pixel format is required.

When an exporter running in Media Encoder parses the segments in the sequence, it only has a very high-level view. It sees the entire sequence as a single clip (which is actually a temporary project file that has been opened using a Dynamic Link to the PProHeadless process), and it sees any optional cropping or filters as applied effects.

So when the exporter parses that simple, high-level sequence, if there are no effects, it should use the MediaNode's ClipID with the [Clip Render Suite](sweetpea-suites.md#clip-render-suite) to get frames directly from the PProHeadless process. In the PProHeadless process, the renderer can step in and parse the real sequence in all its glory.

It can use the [Clip Render Suite](sweetpea-suites.md#clip-render-suite) to get the frames in the custom pixel format directly from the importer, and then set the custom PPix as the render result. This custom PPix then is available to the exporter, in a pristine, compressed PPix.
