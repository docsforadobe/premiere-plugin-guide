.. _video-filters/VideoRecord:

VideoRecord
################################################################################

A video filter is passed a handle to a VideoRecord with almost every selector.

::

  typedef struct {
    PrMemoryHandle          specsHandle;
    ``PPixHand``                source;
    ``PPixHand``                destination;
    csSDK_int32             part;
    csSDK_int32             total;
    char                    previewing;
    void*                   privateData;
    VFilterCallBackProcPtr  callBack;
    BottleRec*              bottleNecks;
    short                   version;
    short                   sizeFlags;
    csSDK_int32             flags;
    TDB_TimeRecord*         tdb;
    PrMemoryHandle          instanceData;
    piSuitesPtr             piSuites;
    PrTimelineID            timelineData;
    char                    altName[MAX_FXALIAS];
    PrPixelFormat           pixelFormatSupported;
    csSDK_int32             pixelFormatIndex;
    csSDK_uint32            instanceID;
    TDB_TimeRecord          tdbTimelineLocation;
    csSDK_int32             sessionPluginID;
  } VideoRecord, **VideoHandle;

+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``specsHandle``          | Instance settings, persistent across Premiere sessions.                                                                                                                                                    |
|                          |                                                                                                                                                                                                            |
|                          | Create this handle during ``fsInitSpec`` or ``fsSetup``.                                                                                                                                                   |
|                          |                                                                                                                                                                                                            |
|                          | Populated by Premiere if the filter's parameters can be manipulated in the Effect Controls Panel.                                                                                                          |
|                          |                                                                                                                                                                                                            |
|                          | Use Premiere's memory allocation callbacks to allocate memory for the ``specsHandle``.                                                                                                                     |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``source``               | ``PPixHand`` for the source video frame.                                                                                                                                                                   |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``destination``          | ``PPixHand`` for the destination video frame, always the same size as source.                                                                                                                              |
|                          |                                                                                                                                                                                                            |
|                          | Store the output frame here during ``fsExecute``.                                                                                                                                                          |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``part``                 | How far into the effect you are.                                                                                                                                                                           |
|                          |                                                                                                                                                                                                            |
|                          | ``part`` varies from 0 to total, inclusive.                                                                                                                                                                |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``total``                | Total length of the video filter.                                                                                                                                                                          |
|                          |                                                                                                                                                                                                            |
|                          | Divide part by total to calculate the percentage of the time-variant filter for a given ``fsExecute``.                                                                                                     |
|                          |                                                                                                                                                                                                            |
|                          | This value doesn't necessarily correspond to frames or fields.                                                                                                                                             |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``previewing``           | Unsupported                                                                                                                                                                                                |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``privateData``          | Data private to Premiere.                                                                                                                                                                                  |
|                          |                                                                                                                                                                                                            |
|                          | Pass to the frame-retrieval callback when requesting a frame.                                                                                                                                              |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``callBack``             | Pointer to ``VFilterCallbackProcPtr``, used for retrieving frames (or fields, for interlaced video) from source clips.                                                                                     |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``bottleNecks``          | Pointer to Premiere's bottleRec functions.                                                                                                                                                                 |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``version``              | Version of this structure (``kVideoFilterVersion``).                                                                                                                                                       |
|                          |                                                                                                                                                                                                            |
|                          | - Premiere Pro CS5 = ``VIDEO_FILTER_VERSION_11``                                                                                                                                                           |
|                          | - Premiere Pro CS3 = ``VIDEO_FILTER_VERSION_10``                                                                                                                                                           |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``sizeFlags``            | Field-rendering information.                                                                                                                                                                               |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``flags``                | If doing a lower-quality render, Premiere will pass in ``kEf­fectFlags_DraftQuality`` during ``fsExecute``.                                                                                                |
|                          |                                                                                                                                                                                                            |
|                          | The filter can then optionally render a faster, lower-quality image for previewing.                                                                                                                        |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``tdb``                  | Pointer to a time database record describing the sequence timebase.                                                                                                                                        |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``instanceData``         | Handle to private instance data that persists across invocations.                                                                                                                                          |
|                          |                                                                                                                                                                                                            |
|                          | Allocate the memory for this during ``fsExecute`` and deallocate during ``fsDisposeData``.                                                                                                                 |
|                          |                                                                                                                                                                                                            |
|                          | Do not use this field during fsSetup.                                                                                                                                                                      |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``piSuites``             | Pointer to callback piSuites.                                                                                                                                                                              |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``timelineData``         | Only available during ``fsInitSpec`` and ``fsSetup``.                                                                                                                                                      |
|                          |                                                                                                                                                                                                            |
|                          | This opaque handle to the timeline database is required by ``timelineFuncs`` callbacks available in piSuites.                                                                                              |
|                          |                                                                                                                                                                                                            |
|                          | This handle is useful in or- der to have a preview in a modal setup dialog during ``fsSetup``.                                                                                                             |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``altName``              | Unused.                                                                                                                                                                                                    |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pixelFormatSupported`` | Only valid during ``fsGetPixelFormatsSupported``.                                                                                                                                                          |
|                          |                                                                                                                                                                                                            |
|                          | Return pixel type supported.                                                                                                                                                                               |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pixelFormatIndex``     | Only valid during ``fsGetPixelFormatsSupported``.                                                                                                                                                          |
|                          |                                                                                                                                                                                                            |
|                          | Index of fourCC of pixel type supported.                                                                                                                                                                   |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``instanceID``           | The runtime instance ID uniquely identifies filters during a session.                                                                                                                                      |
|                          |                                                                                                                                                                                                            |
|                          | This is the same ID that is passed to players in ``prt­FilterRec``.                                                                                                                                        |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``tdbTimelineLocation``  | A time database record describing the location of the filter in sequence.                                                                                                                                  |
|                          |                                                                                                                                                                                                            |
|                          | Only valid during ``fsInitSpec`` and ``fsSetup``.                                                                                                                                                          |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``sessionPluginID``      | This ID should be used in the File Registration Suite for registering external files (such as textures, logos, etc) that are used by a plug-in instance but do not appear as footage in the Project Panel. |
|                          |                                                                                                                                                                                                            |
|                          | Registered files will be taken into account when trimming or copying a project using the Project Manager.                                                                                                  |
+--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

VFilterCallBackProcPtr
================================================================================

Pointer to a callback for retrieving frames (or fields, for interlaced video) from the source clip.

Do not expect real-time performance from this callback.

::

  typedef short (CALLBACK *VFilterCallBackProcPtr)(
    csSDK_int32  frame;
    PPixHand     thePort;
    RECT*        theBox;
    Handle       privateData);

+-----------------+--------------------------------------------------------------------------------------------+
|  **Parameter**  |                                      **Description**                                       |
+=================+============================================================================================+
| ``frame``       | Frame requested. The frame value passed in should be frame * samplesize.                   |
|                 |                                                                                            |
|                 | The callback will always return the current field (upper or lower) during field rendering. |
+-----------------+--------------------------------------------------------------------------------------------+
| ``thePort``     | ``PPixHand`` where Premiere will store the frame                                           |
+-----------------+--------------------------------------------------------------------------------------------+
| ``theBox``      | Bounds of the frame you want Premiere to retrieve.                                         |
+-----------------+--------------------------------------------------------------------------------------------+
| ``privateData`` | Handle provided by Premiere in ``VideoRecord.private­Data``                                |
+-----------------+--------------------------------------------------------------------------------------------+

----

sizeFlags
================================================================================

For sizeFlags, the following bit flags are of interest:

+-------------------+------------------------------------------------------------+
|     **Flag**      |                      **Description**                       |
+===================+============================================================+
| ``gvFieldsEven``  | The video filter should render upper-field dominance       |
+-------------------+------------------------------------------------------------+
| ``gvFieldsOdd``   | The video filter should render lower-field dominance       |
+-------------------+------------------------------------------------------------+
| ``gvFieldsFirst`` | The video filter is currently rendering the dominant field |
+-------------------+------------------------------------------------------------+
