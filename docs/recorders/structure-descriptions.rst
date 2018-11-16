.. _recorders/structure-descriptions:

Structure Descriptions
################################################################################

.. _recorders/structure-descriptions.recInfoRec8:

recInfoRec8
================================================================================

Selector: :ref:`recorders/selector-descriptions.recmod_Startup8`

Describes the recorder's capabilities to Premiere.

::

  typedef struct {
    csSDK_int32   recmodID;
    csSDK_int32   fileType;
    csSDK_int32   classID;
    int           canVideoCap;
    int           canAudioCap;
    int           canStepCap;
    int           canStillCap;
    int           canRecordLimit;
    int           acceptsTimebase;
    int           acceptsBounds;
    int           multipleFiles;
    int           canSeparateVidAud;
    int           canPreview;
    int           wantsEvents;
    int           wantsMenuInactivate;
    int           acceptsAudioSettings;
    int           canCountFrames;
    int           canAbortDropped;
    int           requestedAPIVersion;
    int           canGetTimecode;
    int           reserved[16];
    csSDK_int32   prefTimescale;
    csSDK_int32   prefSamplesize;
    csSDK_int32   minWidth;
    csSDK_int32   minHeight;
    csSDK_int32   maxWidth;
    csSDK_int32   maxHeight;
    int           prefAspect;
    csSDK_int32   prefPreviewWidth;
    csSDK_int32   prefPreviewHeight;
    prUTF16Char   recmodName[256];
    csSDK_int32   audioOnlyFileType;
    int           canSearchScenes;
    int           canCaptureScenes;
    prPluginID    outRecorderID;
  } recInfoRec, *recInfoPtr;

+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``recmodID``             | Premiere's internal identifier for the plug-in. Never change this value.                                                                                     |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``fileType``             | Four character code for the captured file (for example 'AVIV' for Video for Windows .AVI files, and 'MOOV' for QuickTime .MOV files).                        |
|                          |                                                                                                                                                              |
|                          | Invent a unique code for proprietary formats as necessary, but make sure an importer is installed that supports the fourcc.                                  |
|                          |                                                                                                                                                              |
|                          | If no such importer is installed, pressing the record button will result in a recorder error before the ``recmod_PrepRecord`` selector is even sent.         |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``classID``              | Class identifier, used to differentiate between plug-ins that support the same fileType.                                                                     |
|                          |                                                                                                                                                              |
|                          | ClassID is the identifying characteristic of plug-ins which form a media abstraction layer.                                                                  |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canVideoCap``          | If set, the recorder can capture video.                                                                                                                      |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canAudioCap``          | If set, the recorder can capture audio                                                                                                                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canStepCap``           | Unused                                                                                                                                                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canStillCap``          | Unused                                                                                                                                                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canRecordLimit``       | If set, the recorder can accepts recording time limits.                                                                                                      |
|                          |                                                                                                                                                              |
|                          | The recorder will receive the user-specified record limit in ``recCapParmsRec.record`` limit.                                                                |
|                          |                                                                                                                                                              |
|                          | The plug-in must enforce the time limit during capture.                                                                                                      |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``acceptsTimebase``      | If set, the recorder can capture to an arbitrary timebase.                                                                                                   |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``acceptsBounds``        | If set, the recorder can capture to an arbitrary frame size.                                                                                                 |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``multipleFiles``        | Unused                                                                                                                                                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canSeparateVidAud``    | Unused                                                                                                                                                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canPreview``           | Unused                                                                                                                                                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``wantsEvents``          | Unused                                                                                                                                                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``wantsMenuInactivate``  | Unused                                                                                                                                                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``acceptsAudioSettings`` | Unused, do not set                                                                                                                                           |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canCountFrames``       | If set, the recorder is expected to count frames and quit when the count is reached.                                                                         |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canAbortDropped``      | If set, the recorder can abort when frames are dropped                                                                                                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``requestedAPIVersion``  | Unused                                                                                                                                                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canGetTimecode``       | Can provide timecode from the capture stream (like DV).                                                                                                      |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``reserved[16]``         | Do not use.                                                                                                                                                  |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``activeDuringSetup``    | If set, that the recorder shouldn't be deactivated before a ``recmod_GetSetupInfo8`` selector is issued                                                      |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``prefTimescale``        | Frames per second, in scale over sampleSize.                                                                                                                 |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``prefSamplesize``       |                                                                                                                                                              |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``minWidth``             | Define the minimum and maximum frame sizes the plug-in can capture. If the plug-in can only capture to a single fixed size, then set them to the same value. |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``minHeight``            |                                                                                                                                                              |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``minWidth``             |                                                                                                                                                              |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``minHeight``            |                                                                                                                                                              |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``prefAspect``           | Preferred frame aspect ratio for the captured frames.                                                                                                        |
|                          |                                                                                                                                                              |
|                          | Shift the width into the high order word and the height into the low order word.                                                                             |
|                          |                                                                                                                                                              |
|                          | For example, store 640x480 (a 4:3 aspect ratio) as: ``prefAspect = (640 << 16) + 480;``                                                                      |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``prefPreviewWidth``     | Unused                                                                                                                                                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``prefPreviewHeight``    | Unused                                                                                                                                                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``recmodName[256]``      | The recorder's name (appears in the Capture Format pulldown menu).                                                                                           |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``audioOnlyFileType``    | File type for audio-only captures. If 0, the video file type will be used.                                                                                   |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canSearchScenes``      | If true, the recorder can detect a scene boundary for searching purposes                                                                                     |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``canCaptureScenes``     | If true, the recorder can identify when it has reached the end of a scene                                                                                    |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``outRecorderID``        | New in Premiere Pro 2.0. A GUID identifier is now required for all recorders. Editing Mode XMLs use these GUIDs to refer to recorders.                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

.. _recorders/structure-descriptions.recCapSetups8:

recCapSetups8
================================================================================

Selector: :ref:`recorders/selector-descriptions.recmod_GetSetupInfo8`

Enumerate custom setup buttons for the Capture Settings dialog, and pull-down menu items in the Capture panel.

::

  typedef struct {
    int            customSetups;
    csSDK_int32    enableflags;
    recSetupItem8  setups[4];
  } recCapSetups8;

+------------------+---------------------------------------------------------------------------------+
| ``customSetups`` | Number of setup buttons (up to 4).                                              |
+------------------+---------------------------------------------------------------------------------+
| ``enableflags``  | Bitstring where bits 0 to 3 correspond with setups 1 to 4.                      |
|                  |                                                                                 |
|                  | Set the appropriate bits to indicate to Premiere which setups should be enabled |
+------------------+---------------------------------------------------------------------------------+
| ``setups[4]``    | Four recSetupItem8s used to label the setup buttons.                            |
|                  |                                                                                 |
|                  | A ``recSetupItem8`` is just a ``prUTF16Char[256]``.                             |
+------------------+---------------------------------------------------------------------------------+

----

.. _recorders/structure-descriptions.recDisplayPos:

recDisplayPos
================================================================================

Selector: :ref:`recorders/selector-descriptions.recmod_SetDisp`, :ref:`recorders/selector-descriptions.recmod_Open` (member of :ref:`recorders/structure-descriptions.recOpenParms`)

Describes the display position for preview frames.

::

  typedef struct {
    prWnd  wind;
    int    originTop;
    int    originLeft;
    int    dispWidth;
    int    dispHeight;
    int    mustresize;
  } recDisplayPos;

+----------------+---------------------------------------------------------------------------------------------------------------------+
| ``wind``       | The window.                                                                                                         |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| ``originTop``  | ``originTop`` and ``originLeft`` identify the offset in pixels from the top left of the window in which to display. |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| ``originLeft`` |                                                                                                                     |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| ``dispWidth``  | Display area dimensions.                                                                                            |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| ``dispHeight`` |                                                                                                                     |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| ``mustresize`` | If set, the video must be resized to fit within these bounds (see ``recmod_SetDisp``).                              |
+----------------+---------------------------------------------------------------------------------------------------------------------+

----

.. _recorders/structure-descriptions.recOpenParms:

recOpenParms
================================================================================

Selector: :ref:`recorders/selector-descriptions.recmod_Open`

Provides capture session information; save this information in private instance data.

::

  typedef struct {
    recDisplayPos      disp;
    void               *callbackID;
    char               *setup;
    FormatChangedFunc  formatFunc;
    AudioPeakDataFunc  audioPeakDataFunc;
  } recOpenParms;

+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``disp``              | Preview display area                                                                                                    |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``callbackID``        | Premiere's instance identifier for this recording session. Save this value for use with callback routines.              |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``setup``             | If not null, points to settings saved from a previous recording session.                                                |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``formatFunc``        | Use to inform Premiere of a new aspect ratio so the Capture panel can be updated                                        |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
| ``audioPeakDataFunc`` | New in CS5. Callback function to send audio metering data to be displayed by Premiere in the Audio Master Meters panel. |
+-----------------------+-------------------------------------------------------------------------------------------------------------------------+

----

.. _recorders/structure-descriptions.recCapturedFileInfo:

recCapturedFileInfo
================================================================================

Selector: :ref:`recorders/selector-descriptions.recmod_StartRecord`

Provide pixel aspect ratio and starting timecode of the captured clip.

::

  typedef struct {
    unsigned        int pixelAspectRatioNum;
    unsigned        int pixelAspectRatioDen;
    char            timeCode[31];
    TDB_TimeRecord  tdb;
    char            date[31];
  } recCapturedFileInfo;

+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pixelAspectRatioNum`` | Fill in the clip's pixel aspect ratio.                                                                                                                    |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pixelAspectRatioDen`` |                                                                                                                                                           |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``timeCode``            | Provide the text representation of the starting timecode, as known by the recorder. If the recorder can provide it, and it is non-zero then fill this in. |
|                         |                                                                                                                                                           |
|                         | Don't fill this in if the timecode is zero. As of CS5.5, that will result in odd starting timecodes, such as "08;06;40;11".                               |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``tdb``                 | Timebase of the captured file.                                                                                                                            |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``date``                | New in Premiere Elements 7. The date of the the captured file, formatted in one of the following ways: "d/m/y" or "d/m/y h:m" or "d/m/y h:m:s"            |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

----

.. _recorders/structure-descriptions.recFileSpec8:

recFileSpec8
================================================================================

Selector: :ref:`recorders/selector-descriptions.recmod_PrepRecord8` (member of :ref:`recorders/structure-descriptions.recCapParmsRec8`)

Used to describe the capture destination file.

::

  typedef struct {
    short        volID;
    csSDK_int32  parID;
    prUTF16Char  name[kPrMaxPath];
  } recFileSpec8;

+-----------+-----------------+
| ``volID`` | Unused          |
+-----------+-----------------+
| ``parID`` | Unused          |
+-----------+-----------------+
| ``name``  | Full file path. |
+-----------+-----------------+

----

.. _recorders/structure-descriptions.recSetupParms:

recSetupParms
================================================================================

Selector: :ref:`recorders/selector-descriptions.recmod_ShowOptions`

Indicates which settings dialog should be displayed, and provides any previously saved settings.

::

  typedef struct {
    uintptr_t  parentwind;
    int        setupnum;
    char       *setup;
  } recSetupParms;

+----------------+---------------------------------------------------------------+
| ``parentwind`` | Parent window owner.                                          |
+----------------+---------------------------------------------------------------+
| ``setupnum``   | Which setup button (1-4) was selected by the user.            |
+----------------+---------------------------------------------------------------+
| ``setup``      | If not null, points to saved settings from previous sessions. |
+----------------+---------------------------------------------------------------+

----

.. _recorders/structure-descriptions.recCapParmsRec8:

recCapParmsRec8
================================================================================

Selector: :ref:`recorders/selector-descriptions.recmod_PrepRecord8`

Specifies capture settings.

::

  typedef struct {
    void                   *callbackID;
    int                    stepcapture;
    int                    capVideo;
    int                    capAudio;
    int                    width;
    int                    height;
    csSDK_int32            timescale;
    csSDK_int32            samplesize;
    csSDK_int32            audSubtype;
    csSDK_uint32           audrate;
    int                    audsamplesize;
    int                    stereo;
    char                   *setup
    int                    abortondrops;
    int                    recordlimit;
    recFileSpec8           thefile;
    StatusDispFunc         statFunc;
    PrerollFunc            prerollFunc;
    csSDK_int32            frameCount;
    char                   reportDrops;
    short                  currate;
    short                  timeFormat;
    csSDK_int32            timeCode;
    csSDK_int32            inHandleAmount;
    ReportSceneFunc        reportSceneFunc;
    int                    captureScenes;
    SceneCapturedFunc8     sceneCapturedFunc;
    bool                   recordImmediate;
    GetDeviceTimecodeFunc  getDeviceTimecodeFunc;
  } recCapParmsRec8;

+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``callbackID``            | Premiere's instance identifier for this recording session. Save this value for use with callback routines.                  |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``stepcapture``           | Unused                                                                                                                      |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``capVideo``              | If set, capture video.                                                                                                      |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``capAudio``              | If set, capture audio.                                                                                                      |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``width``                 | Dimensions of the video frames to capture. These are only sent if ``acceptsBounds`` was set in the ``recInfoRec``.          |
|                           |                                                                                                                             |
|                           | If the plug-in doesn't accept bounds, capture to the preferred dimensions we previously set in ``recInfoRec8``.             |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``height``                |                                                                                                                             |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``timescale``             | Recording timebase. Only sent if accept ``sTimebase`` was set in the ``recInfoRec8``.                                       |
|                           |                                                                                                                             |
|                           | Otherwise, capture using the timebase we previously set in ``recInfoRec8``.                                                 |
|                           |                                                                                                                             |
|                           | This supercedes ``currate`` below.                                                                                          |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``samplesize``            |                                                                                                                             |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``audSubtype``            | Unused                                                                                                                      |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``audrate``               | Unused                                                                                                                      |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``audsamplesize``         | Unused                                                                                                                      |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``stereo``                | Unused                                                                                                                      |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``setup``                 | Pointer to private instance data allocated in response to ``recmod_GetSetupInfo8``.                                         |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``abortondrops``          | If set, stop capture if frames are dropped.                                                                                 |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``recordlimit``           | Recording time limit, in seconds, only valid if ``canRecordLimit`` was set in ``recInfoRec8``.                              |
|                           |                                                                                                                             |
|                           | Value passed in by Premiere. The plug-in must enforce the limit during capture.                                             |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``thefile``               | Structure of type recFileSpec8 describing the capture destination file, only valid during ``recmod_PrepRecord8``.           |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``statFunc``              | Callback function pointer for use during capture to call into Premiere and update status information in the Capture Panel.  |
|                           |                                                                                                                             |
|                           | See ``StatusDispFunc`` for more information.                                                                                |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``preroll``               | Callback function pointer to initiate device control pre-roll.                                                              |
|                           |                                                                                                                             |
|                           | This callback is only initialized if it will be needed, meaning only it if doing an in/out capture or batch capture.        |
|                           |                                                                                                                             |
|                           | Otherwise, this function pointer to be set to NULL. See PrerollFunc for more information.                                   |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``frameCount``            | If canCountFrames was set in ``recInfoRec8``, the number of frames to capture. No device polling will be done.              |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``reportDrops``           | If non-zero, report dropped frames when they occur (by returning ``rmErrVidDataErr``).                                      |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``currate``               | Frames per second to capture at (23, 24, 25, 30, 59). This is superceded by timescale / samplesize above.                   |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``timeFormat``            | 0 = non-drop frame, 1 = drop frame timecode.                                                                                |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``timeCode``              | Timecode for in-point of capture (-1 means ignore).                                                                         |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``inHandleAmount``        | Number of frames of handle (buffered lead-in), previous to the user-specified capture in point, the record module requires. |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``reportSceneFunc``       | Obsolete. Use sceneCapturedFunc8 instead.                                                                                   |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``captureScenes``         | True if user has initiated scene capture                                                                                    |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``sceneCapturedFunc``     | Use this callback during scene capture to report the end of a scene                                                         |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``recordImmediate``       | If non-zero, begin recording immediately after device control returns from seek for pre-roll; don't wait for a timecode.    |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``getDeviceTimecodeFunc`` | New for Premiere Pro CS3. Use this callback to ask the device controller for its current timecode.                          |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------+

----

.. _recorders/structure-descriptions.recGetTimecodeRec:

recGetTimecodeRec
================================================================================

Selector: :ref:`recorders/selector-descriptions.recmod_Idle`

Allows the recorder to supply timecode information.

::

  typedef struct {
    csSDK_int32  status;
    short        currate;
    short        timeFormat;
    csSDK_int32  timeCode;
    short        autoDetectDropness;
  } recGetTimecodeRec;

+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``status``             | 0 indicates valid timecode, 1 indicates it's unknown or stale.                                                                        |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``currate``            | 30 for NTSC timecode, 25 for PAL.                                                                                                     |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``timeFormat``         | 0 for non-drop, 1 for drop-frame timecode.                                                                                            |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``timeCode``           | Timecode as an integer, represented in the absolute number of frames.                                                                 |
|                        |                                                                                                                                       |
|                        | For example, 00;00;04;03 in NTSC drop-frame timecode would be represented as 123.                                                     |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``autoDetectDropness`` | Non-zero if device controller has set DeviceRec.autoDetectDropness to true.                                                           |
|                        |                                                                                                                                       |
|                        | This means that the device controller is relying on the recorder to determining whether the timecode is drop-frame or non-drop-frame. |
|                        |                                                                                                                                       |
|                        | The recorder must call ``FormatChangedFunc`` if there is any change.                                                                  |
+------------------------+---------------------------------------------------------------------------------------------------------------------------------------+

----

.. _recorders/structure-descriptions.recCapInfoRec:

recCapInfoRec
================================================================================

Selector: :ref:`recorders/selector-descriptions.recmod_QueryInfo`

Allows the recorder to supply the resolution and pixel aspect ratio of the clip being logged.

::

  typedef struct {
    csSDK_int32  version;
    int          timeScale;
    int          sampleSize;
    csSDK_int32  vidSubType;
    int          width;
    int          height;
    int          depth;
    int          fieldType;
    int          quality;
    csSDK_int32  pixelAspectRatio;
    csSDK_int32  audSubType;
    int          audRate;
    int          audSampleSize;
    int          audStereo;
    int          reserved[10];
    char         *setup;
  } recCapInfoRec;

+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``version``          | The version of this structure. ``kRecCapInfoRecVersion``                                                                         |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``timeScale``        | Unused. A logged clip gets it's frame rate from the device controller in ``cmdStatus``.                                          |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``sampleSize``       |                                                                                                                                  |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``vidSubType``       | Unused.                                                                                                                          |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``width``            | Video resolution                                                                                                                 |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``height``           |                                                                                                                                  |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``depth``            | Unused.                                                                                                                          |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``fieldType``        |                                                                                                                                  |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``quality``          |                                                                                                                                  |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``pixelAspectRatio`` | Pixel aspect ratio. This uses a representation where the numerator is bit-shifted 16 to the left, and OR'd with the denominator. |
|                      |                                                                                                                                  |
|                      | For example NTSC DV 0.9091 PAR is ``(10 << 16) \ 11``.                                                                           |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``audSubType``       | Unused.                                                                                                                          |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``audRate``          |                                                                                                                                  |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``audSampleSize``    |                                                                                                                                  |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``audStereo``        |                                                                                                                                  |
+----------------------+----------------------------------------------------------------------------------------------------------------------------------+

----

.. _recorders/structure-descriptions.recSceneDetectionParmsRec:

recSceneDetectionParmsRec
================================================================================

Selectors: ``recmod_StartSceneSearch``

Used for scene searching. searchingForward is provided as a hint as the state of the device, and the reportSceneFunc should be used to notify Premiere of a scene boundary.

::

  typedef struct {
    void             *callbackID;
    ReportSceneFunc  reportSceneFunc;
    int              searchingForward;
    int              searchMode;
    short            isDropFrame;
    csSDK_int32      earliestTimecode;
    csSDK_int32      greatestTimecode;
  } recSceneDetectionParmsRec;

+----------------------+---------------------------------------------------------------------------------+
|    ``callbackID``    |                          Required for reportSceneFunc                           |
+======================+=================================================================================+
| ``reportSceneFunc``  | Use this to report the scenes                                                   |
+----------------------+---------------------------------------------------------------------------------+
| ``searchingForward`` | True if the tape is playing forward                                             |
+----------------------+---------------------------------------------------------------------------------+
| ``searchMode``       | Either ``sceneSearch_FastScan`` or scene ``Search_SlowScan``                    |
+----------------------+---------------------------------------------------------------------------------+
| ``isDropFrame``      | True if drop-frame, false otherwise                                             |
+----------------------+---------------------------------------------------------------------------------+
| ``earliestTimecode`` | Only set for ``sceneSearch_SlowScan``: in point for range to report scene edge  |
+----------------------+---------------------------------------------------------------------------------+
| ``greatestTimecode`` | Only set for ``sceneSearch_SlowScan``: out point for range to report scene edge |
+----------------------+---------------------------------------------------------------------------------+
