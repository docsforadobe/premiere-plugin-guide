.. _recorders/getting-started:

Getting Started
################################################################################

Selector Calling Sequence
================================================================================

The best ways to get familiar with the recorder API is to observe the messages sent between Pre- miere and the recorder plugin.

``recmod_Startup8`` is sent once when Premiere launches. When Project Settings > Capture Settings is opened, ``recmod_Open`` is sent to create a new recorder instance and open the capture driver. ``recmod_GetSetupInfo8`` is then sent, so the recorder can specify which settings buttons (if any) should be enabled in the Capture Settings window when the recorder is selected.

If one or more settings buttons are enabled and then clicked by the user, ``recmod_ShowOptions`` is sent so the recorder can display a dialog (and save any user choices). When the Capture Settings window is closed, *recmod_Close* is sent to end the capture instance.

Whenever the Capture panel is open, the recorder will receive ``recmod_SetActive`` calls, with a parameter telling it to become active or inactive (based on user activity). ``recmod_SetDisp`` provides the plugin the dimensions of the preview area in the Capture panel. *recmod_Idle* is repeatedly sent until the Record button is pushed, to give the recorder time to update the preview area and play audio coming from the capture hardware.

When the user clicks Record, or starts an In/Out or Batch capture, ``recmod_PrepRecord8`` is sent. The recorder prepares to capture, and if a start timecode is provided, tells the device controller to get the device into position using preRollFunc. The preRollFunc will block until the device is exactly in the right position, and when it returns, the recorder should immediately return back to Premiere, open which ``recmod_StartRecord`` is then sent to the recorder, which should im- mediately starts capturing.

When the recorder starts capturing and returns from ``recmod_StartRecord``, Premiere will repeatedly call ``recmod_ServiceRecord`` to give the recorder processor time. During recording, report status to Premiere with StatusDispFunc.

The capture may be stopped in several ways:

- The user could click the Stop button,
- the capture may reach the predetermined out point of an In/Out or Batch capture,
- or the recorder might return an error from ``recmod_ServiceRecord``.

In all cases, ``recmod_StopRecord`` will be sent to stop the capture, possibly followed by ``recmod_CloseRecord`` if there no more items in the batch.

Finally, ``recmod_Close`` is sent when the Capture panel is closed to destroy the recorder instance. ``recmod_Shutdown`` is sent when Premiere terminates.

----

Try the Sample Recorder Plug-in
================================================================================

Now that you've read the overview of the selector calling sequence above, build the sample re- corder plugin included with this SDK, and give it a whirl. To properly simulate a capture, you'll also need to create an .sdk media file and place it in the proper location.

1) Build the recorder, importer, and exporter into the plugins directory
2) Launch Premiere Pro and use the exporter to transcode any media file into the .sdk file format.
3) Place the newly created media file at "C:\premiere.sdk" on Windows, or "premiere.sdk" on the Desktop on Mac OS.

Now when you "capture" a file, it will use this file, and automatically import it using the importer.

----

Metadata
================================================================================

Pixel aspect ratio and timecode are provided by the recorder by filling out ``recCapturedFileInfo``. Starting in CS4, after a clip has been captured, if Premiere Pro has an XMP handler that supports the clip's filetype, the XMP handler will open the captured file and inject the information. If no such XMP handler is provided, the recorder is responsible for embedding any pixel aspect ratio information to the file, but Premiere will send *imSetTimeInfo8* to the importer to stamp the file with timecode.

----

Save Captured File Dialog
================================================================================

After a single clip is captured, the Save Captured File dialog allows the user to rename the filename of the clip just captured. The recorder is not involved in this process. Instead, the importer is called to open the newly captured clip, and it is sent *imSaveFile8* with the move flag set to true to move the file. This is handled by the importer, since *imSaveFile8* is usually already implement- ed to support the Project Manager.

----

Switching Preview Area Between Different Frame Sizes
================================================================================

FormatChangedFunc enables recorders to tell Premiere when the pixel aspect ratio has changed so the Capture Panel preview area can be resized. It can be called during preview, and even during capture.

----

Scene Detection
================================================================================

A recorder can optionally implement one or both of two features based on scene detection: Scene Capture and Scene Searching. What determines a scene break is up to the discretion of the re- corder. The built-in DV recorder determines scene breaks by time/date breaks in the DV stream. But a recorder could analyze the video for breaks, or use any method it chooses to implement.

Scene Capture
********************************************************************************

Scene Capture enables a recorder to capture a continuous stream to multiple files divided up by scenes.

To support scene capture, the recorder must set ``recInfoRec8.canCaptureScenes`` = kPrTrue during ``recmod_Startup8``. When the user captures with Scene Detect on, ``recCapParmsRec8.captureScenes`` will be non-zero during ``recmod_PrepRecord8``. The recorder should begin capture, and when it detects the end of a scene, call SceneCapturedFunc8, to notify Premiere that a scene has been captured. Premiere passes back the recFileSpec8 to

give the recorder the filepath to which the next scene should be captured. Premiere also reserves memory for and passes back recCapturedFileInfo for the next capture.

Scene Searching
********************************************************************************

Scene Searching enables a recorder to fast forward or rewind to different scenes. The user can hit the Next Scene or Previous Scene buttons several times to seek several scenes away. Of course, this feature is only possible with the help of a device controller as well.

To support scene capture, the recorder must set ``recInfoRec8.canSearchScenes = kPrTrue`` during ``recmod_Startup8``. When the user chooses Next Scene or Previous Scene, the recorder is sent ``recmod_StartSceneSearch``. The scene searching algorithm happens in two passes.

The first pass is a play fast forward or backward in the initial direction. In this mode, when the recorder passes the scene boundary, it should call ReportSceneFunc to tell Premiere the approximate range where the scene boundary is and return rmEndOfScene. Premiere will call *recmod_StopSceneSearch*, followed by ``recmod_StartSceneSearch``, to start a new slow scan scene search in the opposite direction, passing back the approximate range reported by ReportSceneFunc. When the recorder reaches the scene boundary again, it should once again call ReportSceneFunc and return rmEndOfScene.

----

Entry Point
================================================================================

Below is the entry point function prototype for all recorder plugins. Premiere calls this entry point function to drive the recorder based on user input.

.. code-block:: cpp

  int RecEntry (
    csSDK_int32  selector,
    rmStdParms   *stdParms,
    void         *param1,
    void         *param2)

The *selector* is the action Premiere wants the recorder to perform. It tells the recorder the reason for the call.

``stdParms`` provides the recorder with callback functions to access additional information from Premiere or to have Premiere perform tasks.

Parameters 1 and 2 contain state information and vary with the selector; they may contain a specific value or a pointer to a structure.

Return ``rmNoErr`` if successful, or an appropriate return code.

----

Standard Parameters
================================================================================

This structure is sent from Premiere to the plugin with every selector.

.. code-block:: cpp

  typedef struct {
    int               rmInterfaceVer;
    recCallbackFuncs  *funcs;
    piSuitesPtr       piSuites;
  } rmStdParms;

+--------------------+----------------------------------------------+
|     **Member**     |               **Description**                |
+====================+==============================================+
| ``rmInterfaceVer`` | Recorder API version                         |
|                    |                                              |
|                    |                                              |
|                    | - Premiere Pro CS6 - ``RECMOD_VERSION_12``   |
|                    | - Premiere Pro CS5.5 - ``RECMOD_VERSION_11`` |
|                    | - Premiere Pro CS5 - ``RECMOD_VERSION_10``   |
|                    | - Premiere Pro CS4 - ``RECMOD_VERSION_9``    |
|                    | - Premiere Elements 3 - ``RECMOD_VERSION_8`` |
|                    | - Premiere Pro CS3 - ``RECMOD_VERSION_7``    |
+--------------------+----------------------------------------------+
| ``funcs``          | Pointers to callbacks for recorders          |
+--------------------+----------------------------------------------+
| ``piSuites``       | Pointer to universal callback suites         |
+--------------------+----------------------------------------------+

----

Recorder-Specific Callbacks
================================================================================

Recorders have access to ClassData Functions and Memory Functions through the ``recCallbackFuncs``, which is a member of ``rmStdParms``.

``StatusDispFunc``, ``PrerollFunc``, ``ReportSceneFunc``, and ``SceneCapturedFunc8`` are accessible through ``recCapParmsRec8``, which is sent with ``recmod_PrepRecord8``.

.. code-block:: cpp

  typedef struct {
    ClassDataFuncsPtr   classFuncs;
    PlugMemoryFuncsPtr  memoryFuncs;
  } recCallbackFuncs;

  int (*StatusDispFunc){
    void  *callbackID,
    char  *stattext,
    int   framenum};

  csSDK_int32 (*PrerollFunc)( void *callbackID);

  void (*ReportSceneFunc)(
    void          *callbackID,
    csSDK_uint32  inSceneEdgeTimecode,
    csSDK_uint32  inEarliestSceneEdgeTimecode,
    csSDK_uint32  inGreatestSceneEdgeTimecode);

  void (*SceneCapturedFunc8)(
    void                 *callbackID,
    prUTF16Char          *inFileCaptured,
    recFileSpec8         *outNextSceneFilename,
    recCapturedFileInfo  **outFileInfo);

  void (*SceneCapturedFunc)(
    void                 *callbackID,
    char                 *inFileCaptured,
    recFileSpec          *outNextSceneFilename,
    recCapturedFileInfo  **outFileInfo);

  void (*FormatChangedFunc)(
    void            *callbackID,
    unsigned int    inPixelAspectRatioNum,
    unsigned int    inPixelAspectRatioDen,
    unsigned int    inMaxFrameWidth,
    unsigned int    inMaxFrameHeight,
    TDB_TimeRecord  inFramerate,
    int             isDropFrame);

  void (*GetDeviceTimecodeFunc)(
    void            *callbackID,
    csSDK_uint32    *outTimecode,
    TDB_TimeRecord  *outFrameRate,
    int             *outIsDropFrame);

  void (*AudioPeakDataFunc)(
    void              *callbackID,
    recAudioPeakData  *inAudioPeakData)

+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|       **Function**        |                                                                                                              **Description**                                                                                                               |
+===========================+============================================================================================================================================================================================================================================+
| ``classFuncs``            | See ClassData functions                                                                                                                                                                                                                    |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``memoryFuncs``           | Legacy memory-related callbacks. These are the same ones passed in through :ref:`universals/legacy-callback-suites.piSuites`:.                                                                                                             |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``StatusDispFunc``        | Available in recCapParmsRec8 during ``recmod_PrepRecord8``.                                                                                                                                                                                |
|                           |                                                                                                                                                                                                                                            |
|                           | Callback function pointer for use during capture to call into Premiere and update status information in the Capture Window.                                                                                                                |
|                           |                                                                                                                                                                                                                                            |
|                           | - ``callbackID`` is the recording session instance passed in ``recCapParmsRec``.                                                                                                                                                           |
|                           | - ``stattext`` is text Premiere will display at the top of the Capture Window.                                                                                                                                                             |
|                           | - ``framenum`` is the frame number being captured, represented in the absolute number of frames.                                                                                                                                           |
|                           |                                                                                                                                                                                                                                            |
|                           | For example, 00;00;04;03 in NTSC drop-frame timecode would be represented as 123.                                                                                                                                                          |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``PrerollFunc``           | Available in ``recCapParmsRec8`` during ``recmod_PrepRecord8``, only if the user has initiated a device controlled capture (Capture In/Out or Batch Capture).                                                                              |
|                           |                                                                                                                                                                                                                                            |
|                           | Callback function pointer to initiate device control preroll, by sending a ``dsExecute``/``cmdLocate`` message to the device controller.                                                                                                   |
|                           |                                                                                                                                                                                                                                            |
|                           | Callback returns when the deck is playing at the proper frame.                                                                                                                                                                             |
|                           |                                                                                                                                                                                                                                            |
|                           | ``callbackID`` is the recording session instance passed in ``recCapParmsRec``.                                                                                                                                                             |
|                           |                                                                                                                                                                                                                                            |
|                           | Host returns a ``prDevicemodError`` to inform why the preroll failed.                                                                                                                                                                      |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ReportSceneFunc``       | Although this callback is obsolete for Scene Capture (superceded by ``SceneCapturedFunc8``), it is still used for Scene Search to return the scene detected by the recorder.                                                               |
|                           |                                                                                                                                                                                                                                            |
|                           | Available in ``recSceneDetectionParmsRec`` during ``recmod_StartSceneSearch``.                                                                                                                                                             |
|                           |                                                                                                                                                                                                                                            |
|                           | The ``inSceneEdgeTimecode`` parameter marks the timecode of the scene edge, if it can be determined exactly.                                                                                                                               |
|                           |                                                                                                                                                                                                                                            |
|                           | If it cannot, it marks the approximated timecode of the edge, and the ``inEarliestSceneEdgeTimecode`` and ``inGreatestSceneEdgeTimecode`` parameters mark the earliest and latest possible timecodes that the scene would fall in between. |
|                           |                                                                                                                                                                                                                                            |
|                           | If the scene break can be determined exactly, all three return parameters should be set to the same value.                                                                                                                                 |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``SceneCapturedFunc8``    | New in Premiere Pro 2.0.                                                                                                                                                                                                                   |
|                           |                                                                                                                                                                                                                                            |
|                           | Available in ``recCapParmsRec8`` during ``recmod_PrepRecord8``.                                                                                                                                                                            |
|                           |                                                                                                                                                                                                                                            |
|                           | Callback to notify Premiere that a scene has been captured.                                                                                                                                                                                |
|                           |                                                                                                                                                                                                                                            |
|                           | Premiere returns the recFileSpec8 to designate a filename for the next scene to capture and reserves memory for and returns ``recCapturedFileInfo`` for the next capture.                                                                  |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``SceneCapturedFunc``     | Obsolete. Use ``SceneCapturedFunc8`` above.                                                                                                                                                                                                |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``FormatChangedFunc``     | Available in recOpenParms during ``recmod_Open``. Use this when the pixel aspect ratio has changed so the Capture Panel can be resized.                                                                                                    |
|                           |                                                                                                                                                                                                                                            |
|                           | It can be called during preview, and even during capture.                                                                                                                                                                                  |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``GetDeviceTimecodeFunc`` | New in Premiere Pro CS3. Used to ask the device controller for its current timecode.                                                                                                                                                       |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``AudioPeakDataFunc``     | New in Premiere Pro CS5. Available in recOpenParms during ``recmod_Open``. Use this to display audio meters in the Audio Master Meters panel while previewing and capturing.                                                               |
|                           |                                                                                                                                                                                                                                            |
|                           | The values will be updated as long as the capture panel is active or front.                                                                                                                                                                |
|                           |                                                                                                                                                                                                                                            |
|                           | This call can be made from any thread, at any time. Metering can be provided for up to 16 channels, in any configuration desired: 1, 2, 4, 6/5.1, 8, or 16.                                                                                |
|                           |                                                                                                                                                                                                                                            |
|                           | The recorder provides the peak amplitude in ``longAmplitude``, and the current audio amplitude in ``shortAmplitude``.                                                                                                                      |
|                           |                                                                                                                                                                                                                                            |
|                           | The recorder can decide whether to pick a single value in ``longAmplitude``, or do an average over the sound data.                                                                                                                         |
|                           |                                                                                                                                                                                                                                            |
|                           | In Premiere Pro's built-in recorders, the long term peak data is currently buffered for 3 seconds at a time.                                                                                                                               |
|                           |                                                                                                                                                                                                                                            |
|                           | If no new data is sent, it stays on the last value. So set the amplitude values to zero when finished.                                                                                                                                     |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
