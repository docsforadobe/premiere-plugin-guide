.. _universals/basic-types-structures:

Basic Types Structures
################################################################################

These types and structures are defined in PrSDKTypes.h and PrSDKStructs.h, and are used throughout the Premiere API.

Premiere defines cross-platform types for convenience when developing plug-ins for both Windows and Mac OS.

+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
|                **Name**                |                                               **Description**                                                |
+========================================+==============================================================================================================+
| ``prColor``                            | An unsigned 32-bit integer that stores an RGB color.                                                         |
|                                        |                                                                                                              |
|                                        | This type is useful for the 8-bpc colors retrieved by the color picker in a video effect or transition.      |
|                                        |                                                                                                              |
|                                        | Color channels are stored as BGRA, in order of increasing memory address from left to right.                 |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``prWnd``                              | A Windows ``HWND`` or Mac OS ``NSView*``                                                                     |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``prParentWnd``                        | A Windows ``HWND`` or Mac OS ``NSWindow*``                                                                   |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``prOffscreen``                        | A Windows ``HDC``                                                                                            |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``prRect``                             | A Windows ``RECT`` or Mac OS ``Rect``.                                                                       |
|                                        |                                                                                                              |
|                                        | Use the utility function pr­ ``SetRect`` to set the dimensions of a ``prRect`` struct.                       |
|                                        |                                                                                                              |
|                                        | This should be used because Mac OS ``Rect`` members have a different ordering than Windows ``RECT`` members. |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``prFloatRect``                        | ::                                                                                                           |
|                                        |                                                                                                              |
|                                        |   typedef struct {                                                                                           |
|                                        |     float left;                                                                                              |
|                                        |     float top;                                                                                               |
|                                        |     float right;                                                                                             |
|                                        |     float bottom;                                                                                            |
|                                        |   } prFloatRect;                                                                                             |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``prRgn``                              | A Windows ``HRGN``                                                                                           |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``prPoint``, ``LongPoint``             | ::                                                                                                           |
|                                        |                                                                                                              |
|                                        |   typedef struct {                                                                                           |
|                                        |     csSDK_int32 x;                                                                                           |
|                                        |     csSDK_int32 y;                                                                                           |
|                                        |   } prPoint, LongPoint;                                                                                      |
|                                        |                                                                                                              |
|                                        | ``LongPoint`` is deprecated, but still used for a couple of Bottleneck callbacks                             |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| prFPoint                               | ::                                                                                                           |
|                                        |                                                                                                              |
|                                        |   typedef struct {                                                                                           |
|                                        |     double x;                                                                                                |
|                                        |     double y;                                                                                                |
|                                        |   } prFPoint64;                                                                                              |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``prPixel``                            | (Deprecated)                                                                                                 |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``prPixelAspectRatio``                 | (Deprecated)                                                                                                 |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``PPix``, ``*PPixPtr``, ``**PPixHand`` | Holds a video frame or field, and contains related attributes such as pixel aspect ratio and pixel format.   |
|                                        |                                                                                                              |
|                                        | Manipulate PPixs using the PPix Suite, never directly.                                                       |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``TDB_TimeRecord``                     | A time database record representing a time value in the context of a video frame rate.                       |
|                                        |                                                                                                              |
|                                        | ::                                                                                                           |
|                                        |                                                                                                              |
|                                        |   typedef struct {                                                                                           |
|                                        |     TDB_Time       value;                                                                                    |
|                                        |     TDB_TimeScale  scale;                                                                                    |
|                                        |     TDB_SampSize   sampleSize;                                                                               |
|                                        |   } TDB_TimeRecord;                                                                                          |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``prBool``                             | Can be either ``kPrTrue`` or ``kPrFalse``                                                                    |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``PrMemoryPtr``, ``*PrMemoryHandle``   | A ``char*``                                                                                                  |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``PrTimelineID``, ``PrClipID``         | A 32-bit signed integer.                                                                                     |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``prUTF8Char``                         | An 8-bit unsigned integer.                                                                                   |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``PrSDKString``                        | An opaque data type that should be accessed using the new String Suite.                                      |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``PrParam``                            | Used for exporter parameters                                                                                 |
|                                        |                                                                                                              |
|                                        | ::                                                                                                           |
|                                        |                                                                                                              |
|                                        |   struct PrParam                                                                                             |
|                                        |   {                                                                                                          |
|                                        |     PrParamType mType;                                                                                       |
|                                        |     union                                                                                                    |
|                                        |     {                                                                                                        |
|                                        |       csSDK_int8   mInt8;                                                                                    |
|                                        |       csSDK_int16  mInt16;                                                                                   |
|                                        |       csSDK_int32  mInt32;                                                                                   |
|                                        |       csSDK_int64  mInt64;                                                                                   |
|                                        |       float        mFloat32;                                                                                 |
|                                        |       double       mFloat64;                                                                                 |
|                                        |       csSDK_uint8  mBool;                                                                                    |
|                                        |       prFPoint64   mPoint;                                                                                   |
|                                        |       prPluginID   mGuid;                                                                                    |
|                                        |       PrMemoryPtr  mMemoryPtr;                                                                               |
|                                        |     };                                                                                                       |
|                                        |   };                                                                                                         |
|                                        |                                                                                                              |
|                                        |   enum PrParamType                                                                                           |
|                                        |   {                                                                                                          |
|                                        |     kPrParamType_Int8 = 1,                                                                                   |
|                                        |     kPrParamType_Int16,                                                                                      |
|                                        |     kPrParamType_Int32,                                                                                      |
|                                        |     kPrParamType_Int64,                                                                                      |
|                                        |     kPrParamType_Float32,                                                                                    |
|                                        |     kPrParamType_Float64,                                                                                    |
|                                        |     kPrParamType_Bool,                                                                                       |
|                                        |     kPrParamType_Point,                                                                                      |
|                                        |     kPrParamType_Guid,                                                                                       |
|                                        |     kPrParamType_PrMemoryPtr                                                                                 |
|                                        |   };                                                                                                         |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``prDateStamp``                        | Used in by importers in ``imFileAttributesRec.cre­ationDateStamp``.                                          |
|                                        |                                                                                                              |
|                                        | ::                                                                                                           |
|                                        |                                                                                                              |
|                                        |   typedef struct                                                                                             |
|                                        |   {                                                                                                          |
|                                        |     csSDK_int32  day;                                                                                        |
|                                        |     csSDK_int32  month;                                                                                      |
|                                        |     csSDK_int32  year;                                                                                       |
|                                        |     csSDK_int32  hours;                                                                                      |
|                                        |     csSDK_int32  minutes;                                                                                    |
|                                        |     double       seconds;                                                                                    |
|                                        |   } prDateStamp;                                                                                             |
+----------------------------------------+--------------------------------------------------------------------------------------------------------------+
