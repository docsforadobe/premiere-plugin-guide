.. _universals/sweetpea-suites:

SweetPea Suites
################################################################################

Overview
================================================================================

Suites common to more than one plug-in type are documented in this chapter below.

Suites that are only used by one plug-in type are documented in the chapter on that plug-in type.

Below is a table of all suites available in Premiere Pro:

+-------------------------------------+---------------------------------------------+
|           **Suite Name**            |        **Relevant to Plug-in Type**         |
+=====================================+=============================================+
| Accelerated Render Invocation Suite | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| App Info Suite                      | All                                         |
+-------------------------------------+---------------------------------------------+
| Application Settings Suite          | All                                         |
+-------------------------------------+---------------------------------------------+
| Async File Reader Suite             | Importers                                   |
+-------------------------------------+---------------------------------------------+
| Async Operation Suite               | All                                         |
+-------------------------------------+---------------------------------------------+
| Audio Suite                         | Importers, Exporters                        |
+-------------------------------------+---------------------------------------------+
| Captioning Suite                    | Device Controllers, Exporters, Transmitters |
+-------------------------------------+---------------------------------------------+
| Clip Render Suite                   | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| Deferred Processing Suite           | Importers                                   |
+-------------------------------------+---------------------------------------------+
| Error Suite                         | All except Exporters starting in CS6        |
+-------------------------------------+---------------------------------------------+
| Export File Suite                   | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| Export Info Suite                   | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| Export Param Suite                  | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| Export Progress Suite               | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| Export Standard Param Suite         | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| Exporter Utility Suite              | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| File Registration Suite             | Importers, Transitions, Video Filters       |
+-------------------------------------+---------------------------------------------+
| Flash Cue Marker Data Suite         | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| GPU Device Suite                    | GPU Effects and Transitions                 |
+-------------------------------------+---------------------------------------------+
| Image Processing Suite              | All                                         |
+-------------------------------------+---------------------------------------------+
| Importer File Manager Suite         | Importers                                   |
+-------------------------------------+---------------------------------------------+
| Legacy Suite                        | All                                         |
+-------------------------------------+---------------------------------------------+
| Marker Suite                        | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| Media Accelerator Suite             | Importers                                   |
+-------------------------------------+---------------------------------------------+
| Memory Manager Suite                | All                                         |
+-------------------------------------+---------------------------------------------+
| Palette Suite                       | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| Pixel Format Suite                  | All                                         |
+-------------------------------------+---------------------------------------------+
| Playmod Audio Suite                 | Transmitters                                |
+-------------------------------------+---------------------------------------------+
| Playmod Device Control Suite        | None (Deprecated)                           |
+-------------------------------------+---------------------------------------------+
| Playmod Overlay Suite               | Transmitters                                |
+-------------------------------------+---------------------------------------------+
| Playmod Render Suite                | None (Deprecated)                           |
+-------------------------------------+---------------------------------------------+
| PPix Cache Suite                    | Importers                                   |
+-------------------------------------+---------------------------------------------+
| PPix Creator Suite                  | All                                         |
+-------------------------------------+---------------------------------------------+
| PPix Creator 2 Suite                | All                                         |
+-------------------------------------+---------------------------------------------+
| PPix Suite                          | All                                         |
+-------------------------------------+---------------------------------------------+
| PPix 2 Suite                        | All                                         |
+-------------------------------------+---------------------------------------------+
| Quality Suite                       | None (Deprecated)                           |
+-------------------------------------+---------------------------------------------+
| RollCrawl Suite                     | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| Scope Render Suite                  | None (Deprecated)                           |
+-------------------------------------+---------------------------------------------+
| Sequence Audio Suite                | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| Sequence Info Suite                 | Importers, Transitions, Video Filters       |
+-------------------------------------+---------------------------------------------+
| Sequence Render Suite               | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| Stock Image Suite                   | None (Deprecated)                           |
+-------------------------------------+---------------------------------------------+
| String Suite                        | All                                         |
+-------------------------------------+---------------------------------------------+
| Threaded Work Suite                 | All                                         |
+-------------------------------------+---------------------------------------------+
| Time Suite                          | All                                         |
+-------------------------------------+---------------------------------------------+
| Transmit Invocation Suite           | All                                         |
+-------------------------------------+---------------------------------------------+
| Video Segment Render Suite          | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| Video Segment Suite                 | Exporters                                   |
+-------------------------------------+---------------------------------------------+
| Window Suite                        | All                                         |
+-------------------------------------+---------------------------------------------+

----

Acquiring and Releasing the Suites
================================================================================

All SweetPea suites are accessed through the Utilities Suite. Plug-ins can acquire the suites like so:

::

  SPBasicSuite *SPBasic = NULL;
  PrSDKPixelFormatSuite *PixelFormatSuite = NULL;

  SPBasic = stdParmsP->piSuites->utilFuncs->getSPBasicSuite();

  if (SPBasic)
  {
  SPBasic->AcquireSuite ( kPrSDKPixelFormatSuite,
                          kPrSDKPixelFormatSuiteVersion,
                          (const void**)&PixelFormatSuite);
  }

Don't forget to release the suites when finished!

::

  if (SPBasic && PixelFormatSuite)
  {
    SPBasic->ReleaseSuite ( kPrSDKPixelFormatSuite,
                            kPrSDKPixelFormatSuiteVersion);
  }

Versioning
********************************************************************************

Generally from version to version, the changes made to a suite are additive, so it is recommended to work with the most recent version of a suite if possible. However the latest version of a suite may not be supported by older versions of Premiere Pro or other host applications. Attempting to acquire suites that are unsupported by the host application will result in a NULL pointer being returned from AcquireSuite.

For a plug-in to support multiple versions, it may choose to use a specific older version of the suite that is supported across those multiple versions. Alternatively, it may check the version of the host application (using the App Info Suite below), and use the new suites where available, or the older suites when running in an older version. To acquire a specific older version of a suite, rather than requesting kPrSDKPixelFormatSuiteVersion in the example above, use a specific version number instead.

----

App Info Suite
================================================================================

Useful for plug-i that are shared between different applications, such as After Effects plug-ins, Premiere exporters, transmitters, and importers, where it may be important to know which host, version, or language the plug-in is currently running in. Note that this suite is not available to AE effects running in AE.

This suite provides the host application and version number. For a version such as 6.0.3, it will return major = 6, minor = 0, and patch = 3. See PrSDKAppInfoSuite.h.

Starting in version 2 of the suite, introduced in CC, the suite has a new selector to retrieve the build number. SpeedGrade CC supports this suite starting with the July 2013 update.

In version 3, starting in CC 2014, the suite has a new selector to retrieve the language as a NULL-terminated string identifying the locale used in the host application. For example: "en_US", "ja_JP", "zh_CN".

----

Application Settings Suite
================================================================================

New in CS4. This suite provides calls to get the scratch disk folder paths defined in the current project, where the captured files and preview files are created. It also provides a call to get the project file path. All paths are passed back as PrSDKStrings. Use the new String Suite to extract the strings to UTF-8 or UTF-16. See PrSDKApplicationSettingsSuite.h.

----

Audio Suite
================================================================================

Calls to convert to and from the native audio format used by the Premiere API, at various bit depths. See PrSDKAudioSuite.h.

----

Captioning Suite
================================================================================

This suite enables a device controller, exporter, player, or transmitter to get the closed captioning data attached to a sequence. This suite provides the data in either Scenarist (CEA-608, \*.scc) and MacCaption (CEA-708, \*.mcc) formats. In the case of CEA-708, it includes not just the text to display, but it's also the position information, and background, font, etc. If the transmitter or player just wants to overlay the captioning data on a frame, it can use the Playmod Overlay Suite instead.

----

Clip Render Suite
================================================================================

New in 2.0. Use this suite in the player or renderer, to request source frames directly from the importer. There are calls to find the supported frame sizes and pixel formats, so that the caller can make an informed decision about what format to request. Frames can be retrieved synchronously or asynchronously. Asynchronous requests can be cancelled, for example if the frames have passed their window of playback. See PrSDKClipRenderSuite.h.

Starting in CS4, this suite includes calls to find any custom pixel format supported by a clip, and to get frames in those custom pixel formats.

An exporter can use this suite to request frames from the renderer in a compressed pixel format.

----

Error Suite
================================================================================

Uses a single callback for errors, warnings, and info. This callback will activate a flashing icon in the lower left-hand corner of the main application window, which when clicked, will open up the new Events Window containing the error information. See PrSDKErrorSuite.h.

Starting in version 3 of the suite, introduced in CS4, the suite supports UTF-16 strings. Starting in CS6, exporters should use the Exporter Utility Suite to report events.

----

File Registration Suite
================================================================================

Used for registering external files (such as textures, logos, etc) that are used by a plug-in instance but do not appear as footage in the Project Window. Registered files will be taken into account when trimming or copying a project using the Project Manager. See PrSDKFileRegistrationSuite.h.

----

Flash Cue Marker Data Suite
================================================================================

New in CS4. Specific utilities to read Flash cue points. Use in conjunction with the Marker Suite. See PrSDKFlashCueMarkerDataSuite.h.

----

Image Processing Suite
================================================================================

New in CS5. Various calls to get information on pixel formats and process frames. The ScaleConvert() call is the way to copy-convert from a buffer of any supported pixel format to a separate memory buffer.

In version 2, new in CS5.5, we have added StampDVFrameAspect(), which allows a plug-in to set the aspect ratio of a DV frame. This was added to supplement ScaleConvert(), which doesn't have an aspect ratio parameter.

----

Marker Suite
================================================================================

New in CS4. New way to read markers of all types. See PrSDKMarkerSuite.h.

----

Memory Manager Suite
================================================================================

New in Premiere Pro 2.0. Calls to allocate and deallocate memory, and to reserve an amount of memory so that it is not used by the host. See PrSDKMemoryManagerSuite.h.

In CS6, the suite is now at version 4. AdjustReservedMemorySize provides a way to adjust the reserved memory size relative to the current size. This may be easier for the plug-in, rather than maintaining the absolute memory usage and updating it using the older ReserveMemory call.

ReserveMemory
********************************************************************************

A plug-in instance can call ReserveMemory as a request to reserve space so that Premiere's media cache does not use it. Each time ReserveMemory is called, it updates Premiere Pro on how many bytes the plug-in instance is currently reserving. The amount specified is absolute, rather than cumulative. So to release any reserved memory to be made available to Premiere Pro's media cache, call it with a size of 0. However, it's not needed to reset this when exporters are destructed on *exSDK_EndInstance*, since the media manager will be deleting all the references anyways.

ReserveMemory changes the maximum size of Premiere's Media Cache. So if the cache size starts at 10 GB, and you reserve 1 GB, then the cache will not grow beyond 9 GB. ReserveMemory will reserve a different amount of memory, depending on the amount of available memory in the system, and what other plug-in instances have already reserved. The media cache needs a minimum amount of memory to play audio, render, etc.

Starting in version 2 of the suite, introduced in CS4, there are calls to allocate/deallocate memory. This is necessary for exporters, which are not passed the legacy memFuncs.

----

Pixel Format Suite
================================================================================

See the table of supported pixel formats. GetBlackForPixelFormat returns the minimum (black) value for a given pixel format. GetWhiteForPixelFormat returns the maximum (white) value for a given pixel format. Pixel types like YUYV actually contain a group of two pixels to specify a color completely, so the data size returned in this case will be 4 bytes (rather than 2). This call does not support MPEG-2 planar formats.

ConvertColorToPixelFormattedData converts an BGRA/ARGB value into a value of a different pixel type. These functions are not meant to convert entire frames from one colorspace to another, but may be used to convert a single color value from a filter color picker or transition border. To convert frames between pixel formats, see the Image Processing Suite.

New in Premiere Pro 4.0.1, ``MAKE_THIRD_PARTY_CUSTOM_PIXEL_FORMAT_FOURCC()`` defines a custom pixel format.

----

Playmod Overlay Suite
================================================================================

New in CS5.5. A transmitter can ask Premiere Pro to render the overlay for a specific time. As of CS6, this is only used for closed captioning.

To render the closed captioning overlay, it is not necessary to know anything about the closed captioning data, whether it is CEA-608 or CEA-708. RenderImage will simply produce a PPixHand.

The reason why it's not called Closed Captioning Overlay Suite is because going forward we want to use it as a general suite that provides all kinds of overlays. That way, when we add more overlay types in the future, you don't need to worry about updating your player each time to mirror the implementation on your side. In the future, we will likely use this same suite to render static overlays, such as safe areas. To support those, even if VariesOverTime returns false, you can call HasVisibleRegions at time 0.

Version 2 in CC 2014 removes ``CalculateVisibleRegions()``.

RenderImage
********************************************************************************

Render the overlay into an optionally provided BGRA PPixHand. RenderImage does not composite the overlay onto an existing frame, it just renders the overlay into the visible regions. After rendering the overlay at the player's display size, you will then need to composite that result over the frame.

If the user has zoomed the video, it could be wasteful to render a full-sized overlay image and then scale it. For better performance, the overlay can be rendered at the actual display size. The inDisplayWidth, inDisplayHeight and inLogicalRegion parameters provide this extra information needed to optimize for scaling in the UI.

As an example, let's say the sequence is 720x480 at 0.9091 PAR, and the Sequence Monitor is set to show the full frame at square PAR. Set inLogicalRegion to (0, 0, 720, 480), and inDis­ playWidth to 654 and inDisplayHeight to 480.

If the Monitor zoom level was set to 50%, then the inLogicalRegion should stay the same, but display width and height should be set to 327x240. If zoomed to 200%, display width and height should be set to 1308x960. To pan around (as opposed to showing the entire frame), the logical region should be adjusted to represent the part of the sequence frame currently being displayed.

::

  prSuiteError (*RenderImage)(
    PrPlayID       inPlayID,
    PrTime         inTime,
    const prRect*  inLogicalRegion,
    int            inDisplayWidth,
    int            inDisplayHeight,
    prBool         inClearToTransparentBlack,
    PPixHand*      ioPPix);

+-------------------------------+---------------------------------------------------------------------------------------------------------------+
|         **Parameter**         |                                                **Description**                                                |
+===============================+===============================================================================================================+
| ``inLogicalRegion``           | The non-scaled region of the source PPix to overlay                                                           |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``inDisplayWidth``            | Width and height of PPix, if provided in ioPPix, scaled to account for Monitor zoom and PAR                   |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``inDisplayHeight``           |                                                                                                               |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``inClearToTransparentBlack`` | If ``kPrTrue``, the frame will first be cleared to transparent black before render                            |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``ioPPix``                    | The frame into which to draw the overlay. If NULL, the host will allocate the PPix.                           |
|                               |                                                                                                               |
|                               | If provided, the PPix must be BGRA, square pixel aspect ratio, and sized to inDisplayWidth & inDisplayHeight. |
+-------------------------------+---------------------------------------------------------------------------------------------------------------+

GetIdentifier
********************************************************************************

::

  prSuiteError (*GetIdentifier)(
    PrPlayID       inPlayID,
    PrTime         inTime,
    const prRect*  inLogicalRegion,
    int            inDisplayWidth,
    int            inDisplayHeight,
    prBool         inClearToTransparentBlack,
    prPluginID*    outIdentifier);

HasVisibleRegions
********************************************************************************

::

  prSuiteError (*HasVisibleRegions)(
    PrPlayID       inPlayID,
    PrTime         inTime,
    const prRect*  inLogicalRegion,
    int            inDisplayWidth,
    int            inDisplayHeight,
    prBool*        outHasVisibleRegions);


VariesOverTime
********************************************************************************

::

  prSuiteError (*VariesOverTime)(
    PrPlayID  inPlayID,
    prBool*   outVariesOverTime);

----

PPix Cache Suite
================================================================================

Used by an importer, player, or renderer to take advantage of the host application's PPix cache. See PrSDKPPixCacheSuite.h.

Starting in version 2 of this suite, introduced in Premiere Pro 4.1, AddFrameToCache and GetFrameFromCache now have two extra parameters, inPreferences and inPrefer­ encesLength. Now frames are differentiated within the cache, based on the importer preferences, so when the preferences change, the host will not use the old frame when it gets a frame request.

Version 4, new in CS5.0.3, adds ExpireNamedPPixFromCache() and ExpireAllPPixesFromCache(), which allow a plug-in to remove one or all PPixes from the Media Cache, which can be useful if the media is changing due to being edited in a separate application.

To expire an individual frames expired using ExpireNamedPPixFromCache(), the identifier must be known. The plug-in may specify an identifier using AddNamedPPixToCache(). If a frame is in the cache with multiple names, and you expire any one of those names, then the frame will be expired. Alternatively, for rendered frames, the identifier may be retrieved using GetIdentifierForProduceFrameAsync() in the Video Segment Render Suite.

Clearing the cache will not interfere with any outstanding requests, because each request holds dependencies on the needed frames.

Version 5, new in CS5.5, adds the new color profile-aware calls AddFrameToCacheWithColorProfile() and GetFrameFromCacheWithColorProfile().

Version 6, new in CC 2014, adds AddFrameToCacheWithColorProfile2() and GetFrameFromCacheWithColorProfile2(), which are the same as the ones added in version 5 with the addition of a PrRenderQuality parameter.

----

PPix Creator Suite
================================================================================

Includes callbacks to create and copy PPixs. See also the PPix Creator 2 Suite.

CreatePPix
********************************************************************************

Creates a new PPix. The advantage of using this callback is that frames allocated are accounted for in the media cache, and are 16-byte aligned.

``ppixNew`` and ``newPtr`` don't allocate memory in the media cache, or perform any alignment.

::

  prSuiteError (*CreatePPix)(
    PPixHand*           outPPixHand,
    PrPPixBufferAccess  inRequestedAccess,
    PrPixelFormat       inPixelFormat,
    const prRect*       inBoundingRect);

+------------------------------------------+------------------------------------------------------------------------+
|              **Parameter**               |                            **Description**                             |
+==========================================+========================================================================+
| ``PPixHand *outPPixHand``                | The new PPix handle if the creation was successful.                    |
|                                          |                                                                        |
|                                          | NULL otherwise.                                                        |
+------------------------------------------+------------------------------------------------------------------------+
| ``PrPPixBufferAccess inRequestedAccess`` | Requested pixel access. Read-only is not allowed (doesn't make sense). |
|                                          |                                                                        |
|                                          | ``PrPPixBufferAccess`` values are defined in PPix Suite.               |
+------------------------------------------+------------------------------------------------------------------------+
| ``PrPixelFormat inPixelFormat``          | The pixel format of this PPix                                          |
+------------------------------------------+------------------------------------------------------------------------+

ClonePPix
********************************************************************************

Clones an existing PPix.

It will ref-count the PPix if only read access is requested and the PPix to copy from is read-only as well, otherwise it will create a new one and copy.

::

  prSuiteError (*ClonePPix)(
    PPixHand            inPPixToClone,
    PPixHand*           outPPixHand,
    PrPPixBufferAccess  inRequestedAccess);

+------------------------------------------+----------------------------------------------------------+
|              **Parameter**               |                     **Description**                      |
+==========================================+==========================================================+
| ``PPixHand inPPixToClone``               | The PPix to clone from.                                  |
+------------------------------------------+----------------------------------------------------------+
| ``PPixHand *outPPixHand``                | The new PPix handle if the creation was successful.      |
|                                          |                                                          |
|                                          | NULL otherwise.                                          |
+------------------------------------------+----------------------------------------------------------+
| ``PrPPixBufferAccess inRequestedAccess`` | Requested pixel access.                                  |
|                                          |                                                          |
|                                          | Only read-only is allowed right now.                     |
|                                          |                                                          |
|                                          | ``PrPPixBufferAccess`` values are defined in PPix Suite. |
+------------------------------------------+----------------------------------------------------------+

----

PPix Creator 2 Suite
================================================================================

More callbacks to create PPixs, including raw PPixs.

Starting in version 2 of this suite, introduced in Premiere Pro 4.0.1, there is a new CreateCustomPPix call to create a PPix in a custom pixel format. See PrSDKPPixCreator2Suite.h.

----

PPix Suite
================================================================================

Callbacks and enums pertaining to PPixs. See also PPix 2 Suite.

PrPPixBufferAccess
********************************************************************************

Can be either:

- ``PrPPixBufferAccess_ReadOnly``,
- ``PrPPixBufferAccess_WriteOnly``,
- ``PrPPixBufferAccess_ReadWrite``

Dispose
********************************************************************************

This will free this PPix. The PPix is no longer valid after this function is called.

::

  prSuiteError (*Dispose)(
    PPixHand  inPPixHand);

+-------------------------+-----------------------------+
|      **Parameter**      |       **Description**       |
+=========================+=============================+
| ``PPixHand inPPixHand`` | The PPix handle to dispose. |
+-------------------------+-----------------------------+

GetPixels
********************************************************************************

This will return a pointer to the pixel buffer.

::

  prSuiteError (*GetPixels)(
    PPixHand            inPPixHand,
    PrPPixBufferAccess  inRequestedAccess,
    char**              outPixelAddress);

+-----------------------------------------------+-------------------------------------------------------------+
|                 **Parameter**                 |                       **Description**                       |
+===============================================+=============================================================+
| ``PPixHand inPPixHand``                       | The PPix handle to operate on.                              |
+-----------------------------------------------+-------------------------------------------------------------+
| ``PrPPixBufferAccess inRequestedAccess``      | Requested pixel access.                                     |
|                                               |                                                             |
|                                               |                                                             |
| Most PPixs do not support write access modes. |                                                             |
+-----------------------------------------------+-------------------------------------------------------------+
| ``char** outPixelAddress``                    | The output pixel buffer address.                            |
|                                               |                                                             |
|                                               | May be NULL if the requested pixel access is not supported. |
+-----------------------------------------------+-------------------------------------------------------------+

GetBounds
********************************************************************************

This will return the bounding rect.

::

  prSuiteError (*GetBounds)(
    PPixHand  inPPixHand,
    prRect*   inoutBoundingRect);

+-------------------------------+-------------------------------------------------+
|         **Parameter**         |                 **Description**                 |
+===============================+=================================================+
| ``PPixHand inPPixHand``       | The PPix handle to operate on.                  |
+-------------------------------+-------------------------------------------------+
| ``prRect* inoutBoundingRect`` | The address of a bounding rect to be filled in. |
+-------------------------------+-------------------------------------------------+

GetRowBytes
********************************************************************************

This will return the row bytes of the PPix.

::

  prSuiteError (*GetRowBytes)(
    PPixHand      inPPixHand,
    csSDK_int32*  outRowBytes);

+------------------------------+-------------------------------------------------------------------------------------------+
|        **Parameter**         |                                      **Description**                                      |
+==============================+===========================================================================================+
| ``PPixHand inPPixHand``      | The PPix handle to operate on.                                                            |
+------------------------------+-------------------------------------------------------------------------------------------+
| ``csSDK_int32* outRowBytes`` | Returns how many bytes must be added to the pixel buffer address to get to the next line. |
+------------------------------+-------------------------------------------------------------------------------------------+

GetPixelAspectRatio
********************************************************************************

This will return the pixel aspect ratio of this PPix.

::

  prSuiteError (*GetPixelAspectRatio)(
    PPixHand       inPPixHand,
    csSDK_uint32*  outPixelAspectRatioNumerator,
    csSDK_uint32*  outPixelAspectRatioDenominator);

+-----------------------------------+---------------------------------------+
|           **Parameter**           |            **Description**            |
+===================================+=======================================+
| ``PPixHand inPPixHand``           | The PPix handle to operate on.        |
+-----------------------------------+---------------------------------------+
| ``PrPixelFormat* outPixelFormat`` | Returns the pixel format of this PPix |
+-----------------------------------+---------------------------------------+

GetUniqueKey
********************************************************************************

This will return the unique key for this PPix.

+-------------+----------------------------------------------------------------------------------+
| **Returns** |                                      **If**                                      |
+=============+==================================================================================+
| error       | the buffer size is too small (call ``GetUniqueKeySize`` to get the correct size) |
+-------------+----------------------------------------------------------------------------------+
| error       | the key is not available                                                         |
+-------------+----------------------------------------------------------------------------------+
| success     | the key data was filled in                                                       |
+-------------+----------------------------------------------------------------------------------+

::

  prSuiteError (*GetUniqueKey)(
    PPixHand        inPPixHand,
    unsigned char*  inoutKeyBuffer,
    size_t          inKeyBufferSize);

+-----------------------------------+-------------------------------------+
|           **Parameter**           |           **Description**           |
+===================================+=====================================+
| ``PPixHand inPPixHand``           | The PPix handle to operate on.      |
+-----------------------------------+-------------------------------------+
| ``unsigned char* inoutKeyBuffer`` | Storage for the key to be returned. |
+-----------------------------------+-------------------------------------+
| ``size_t inKeyBufferSize``        | Size of buffer                      |
+-----------------------------------+-------------------------------------+

GetUniqueKeySize
********************************************************************************

This will return the unique key size. This will not change for the entire run of the application.

::

  prSuiteError (*GetUniqueKeySize)(
    size_t*  outKeyBufferSize);

+------------------------------+------------------------------------------+
|        **Parameter**         |             **Description**              |
+==============================+==========================================+
| ``size_t* outKeyBufferSize`` | Returns the size of the PPix unique key. |
+------------------------------+------------------------------------------+

GetRenderTime
********************************************************************************

This will return the render time for this PPix.

::

  prSuiteError (*GetRenderTime)(
    PPixHand      inPPixHand,
    csSDK_int32*  outRenderMilliseconds);

+-----------------------------------------+-------------------------------------------------+
|              **Parameter**              |                 **Description**                 |
+=========================================+=================================================+
| ``PPixHand inPPixHand``                 | The PPix handle to operate on.                  |
+-----------------------------------------+-------------------------------------------------+
| ``csSDK_int32* outRenderMillisec­onds`` | Returns the render time in milliseconds.        |
|                                         |                                                 |
|                                         | If the frame was cached, the time will be zero. |
+-----------------------------------------+-------------------------------------------------+

----

PPix 2 Suite
================================================================================

A call to get the size of a PPix. Starting in version 2 of this suite, introduced in CS4, there is a new GetYUV420PlanarBuffers call to get buffer offsets and rowbytes of YUV_420_MPEG2 pixel formats. See PrSDKPPix2Suite.h.

----

RollCrawl Suite
================================================================================

Used by a player or renderer to obtain the pixels for a roll/crawl. The player or render can then move and composite it using accelerated algorithms or hardware. See PrSDKRollCrawlSuite.h.

----

Sequence Info Suite
================================================================================

New in CS4. Calls to get the frame size and pixel aspect ratio of a sequence. This is use-

ful for importers, transitions, or video filters, that provide a custom setup dialog with a preview of the video, so that the preview frame can be rendered at the right dimensions. See PrSDKSequenceInfoSuite.h.

Version 2, new in CS5.5, adds ``GetFrameRate()``.

Version 3, new in CC, adds ``GetFieldType()``, ``GetZeroPoint()``, and ``GetTimecodeDropFrame()``.

----

String Suite
================================================================================

New in CS4. Calls to allocate, copy, and dispose of PrSDKStrings. See PrSDKStringSuite.h.

----

Threaded Work Suite
================================================================================

New in CS4. Calls to register and queue up a threaded work callback for processing on a render thread. If you queue multiple times, it is possible for multiple threads to call your callback. If this is a problem, you'll need to handle this on your end.

----

Time Suite
================================================================================

A SweetPea suite that includes the following structure, callbacks, and enum:

pmPlayTimebase
********************************************************************************

+------------------------------+---------------------------+
|          **Member**          |      **Description**      |
+==============================+===========================+
| ``csSDK_uint32 scale``       | rate of the timebase      |
+------------------------------+---------------------------+
| ``csSDK_int32 sampleSize``   | size of one sample        |
+------------------------------+---------------------------+
| ``csSDK_int32 fileDuration`` | number of samples in file |
+------------------------------+---------------------------+

PrVideoFrameRates
********************************************************************************

+-----------------------------+-----------------+
|         **Member**          | **Description** |
+=============================+=================+
| ``kVideoFrameRate_24Drop``  | 24000 / 1001    |
+-----------------------------+-----------------+
| ``kVideoFrameRate_24``      | 24              |
+-----------------------------+-----------------+
| ``kVideoFrameRate_PAL``     | 25              |
+-----------------------------+-----------------+
| ``kVideoFrameRate_NTSC``    | 30000 / 1001    |
+-----------------------------+-----------------+
| ``kVideoFrameRate_30``      | 30              |
+-----------------------------+-----------------+
| ``kVideoFrameRate_PAL_HD``  | 50              |
+-----------------------------+-----------------+
| ``kVideoFrameRate_NTSC_HD`` | 60000 / 1001    |
+-----------------------------+-----------------+
| ``kVideoFrameRate_60``      | 60              |
+-----------------------------+-----------------+
| ``kVideoFrameRate_Max``     | 0xFFFFFFFF      |
+-----------------------------+-----------------+

GetTicksPerSecond
********************************************************************************

Get the current ticks per second. This is guaranteed to be constant for the duration of the runtime.

::

  prSuiteError (*GetTicksPerSecond)(
    PrTime*  outTicksPerSec);

GetTicksPerVideoFrame
********************************************************************************

Get the current ticks in a video frame rate. inVideoFrameRate may be any of the ``PrVideoFrameRates`` enum.

::

  prSuiteError (*GetTicksPerVideoFrame)(
    PrVideoFrameRates  inVideoFrameRate,
    PrTime*            outTicksPerFrame);

GetTicksPerAudioSample
********************************************************************************

Get the current ticks in an audio sample rate.

+===================================+===================================================================================================================================+
| **Returns**                       | **If**                                                                                                                            |
+===================================+===================================================================================================================================+
| ``kPrTimeSuite_RoundedAudioRate`` | the requested audio sample rate is not an even divisor of the base tick count and therefore times in this rate will not be exact. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ``kPrTimeSuite_Success``          | otherwise                                                                                                                         |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

::

  prSuiteError (*GetTicksPerAudioSample)(
    float    inSampleRate,
    PrTime*  outTicksPerSample);

----

Video Segment Render Suite
================================================================================

This suite uses the built-in software path for rendering, and supports subtree rendering. This means the plug-in can ask the host to render a part of the segment, and then still handle the rest of the rendering. This is useful if, for example, one of the layers has an effect that the plug-in cannot render itself. The plug-in can have the host render that layer, but then handle the other layers along with the compositing.

In version 2, new in CS5.5, the new call ``SupportsInitiateClipPrefetch()`` can be used to query whether or not a clip supports prefetching.

In version 3, new in CS6, the function signatures have been modernized, using ``inSequence­TicksPerFrame`` rather than ``inFrameRateScale`` and ``inFrameRateSampleSize``.

----

Video Segment Suite
================================================================================

This suite provides calls to parse a sequence and get details on video segments. All the queryable node properties are in PrSDKVideoSegmentProperties.h. These properties will be returned as PrSDKStrings, and should be managed using the String Suite. The segments provide a hash value that the caller can use to quickly determine whether or not a segment has changed. This hash value can be maintained even if a segment is shifted in time

In version 4, new in CS5.5, the new call ``AcquireNodeForTime()`` passes back a segment node for a requested time. There are also a few new properties for media nodes: StreamIsContinuousTime, ColorProfileName, ColorProfileData, and ScanlineOffsetToImproveVerticalCentering.

In version 5, new in CC, a new video segment property is available: Effect_ClipName. In version 6, new in CC 2014, ``AcquireFirstNodeInTimeRange()`` and

``AcquireOperatorOwnerNodeID()`` were added, along with the new node type kVid­ eoSegment_NodeType_AdjustmentEffect.

The basic structure of the video segments is that of a tree structure. There is a Compositor node with n inputs. Each of those inputs is a Clip node, which has one input which is a Media node, and it also has n Operators, which are effects.

So, a simple example, three clips in a stack, the top one with three effects looks like this:

::

  Segment
    Compositor Node
      Clip Node
        Media Node (bottom clip) Clip Node
      Clip Node
        Media Node (middle clip) Clip Node
      Clip Node
        Media Node (top clip)
        Clip Operators (Blur, Color Corrector, Motion)

To get a good idea of the segment structure, try the SDK player, create a sequence using the SDK Editing Mode, and watch the text overlay in the Sequence Monitor as you perform edits.

See PrSDKVideoSegmentSuite.h and PrSDKVideoSegmentProperties.h.

----

Window Suite
================================================================================

New in CS4. This is the new preferred way to get the handle of the mainframe window, especially for exporters, who don't have access to the legacy piSuites.
