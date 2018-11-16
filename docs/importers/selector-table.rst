.. _importers/selector-table:

Selector Table
################################################################################

Before implementing a handler for a certain selector, make sure that it is really necessary for your importer. Many selectors are optional, and only useful for certain special needs.

The Synth column indicates whether or not the selector is applicable to synthetic importers. Custom importers can respond to any of the selectors.

+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
|                            **Selector**                            |                             **param1**                              |                            **param2**                             | **Synth** |
+====================================================================+=====================================================================+===================================================================+===========+
| :ref:`importers/selector-descriptions.imInit`                      | :ref:`importers/structure-descriptions.imImportInfoRec`*            | unused                                                            | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imShutdown`                  | unused                                                              | unused                                                            | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetIndFormat`              | ``(int) index``                                                     | :ref:`importers/structure-descriptions.imIndFormatRec`*           | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetSupports8`              | unused                                                              | unused                                                            | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetSupports7`              | unused                                                              | unused                                                            | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetInfo8`                  | :ref:`importers/structure-descriptions.imFileAccessRec8`*           | :ref:`importers/structure-descriptions.imFileInfoRec8`*           | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imCloseFile`                 | :ref:`importers/structure-descriptions.imFileRef`*                  | ``(void*) PrivateData**``                                         | No        |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetIndPixelFormat`         | ``(int) index``                                                     | :ref:`importers/structure-descriptions.imIndPixelFormatRec`*      | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetPreferredFrameSize`     | :ref:`importers/structure-descriptions.imPreferredFrameSizeRec`*    | unused                                                            | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imSelectClipFrameDescriptor` | :ref:`importers/structure-descriptions.imFileRef`                   | :ref:`importers/structure-descriptions.imClipFrameDescriptorRec`* | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetSourceVideo`            | :ref:`importers/structure-descriptions.imFileRef`                   | :ref:`importers/structure-descriptions.imSourceVideoRec`*         | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imCreateAsyncImporter`       | :ref:`importers/structure-descriptions.imAsyncImporterCreationRec`* | unused                                                            | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imImportImage`               | :ref:`importers/structure-descriptions.imFileRef`                   | :ref:`importers/structure-descriptions.imImportImageRec`*         | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imImportAudio7`              | :ref:`importers/structure-descriptions.imFileRef`                   | :ref:`importers/structure-descriptions.imImportAudioRec7`*        | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imResetSequentialAudio`      | :ref:`importers/structure-descriptions.imFileRef`                   | :ref:`importers/structure-descriptions.imImportAudioRec7`*        | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetSequentialAudio`        | :ref:`importers/structure-descriptions.imFileRef`                   | :ref:`importers/structure-descriptions.imImportAudioRec7`*        | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetPrefs8`                 | :ref:`importers/structure-descriptions.imFileAccessRec8`*           | :ref:`importers/structure-descriptions.imGetPrefsRec`*            | Yes       |
+--------------------------------------------------------------------+---------------------------------------------------------------------+-------------------------------------------------------------------+-----------+

The following selectors are optional, to provide custom file handling:

+-----------------------------------------------------+----------------------------------------------------------+---------------------------------------------------------+-----------+
|                    **Selector**                     |                        **param1**                        |                       **param2**                        | **Synth** |
+=====================================================+==========================================================+=========================================================+===========+
| :ref:`importers/selector-descriptions.imOpenFile8`  | :ref:`importers/structure-descriptions.imFileRef`*       | :ref:`importers/structure-descriptions.imFileOpenRec8`* | No        |
+-----------------------------------------------------+----------------------------------------------------------+---------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imQuietFile`  | :ref:`importers/structure-descriptions.imFileRef`*       | ``(void*) PrivateData**``                               | No        |
+-----------------------------------------------------+----------------------------------------------------------+---------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imSaveFile8`  | :ref:`importers/structure-descriptions.imSaveFileRec8`*  | unused                                                  | No        |
+-----------------------------------------------------+----------------------------------------------------------+---------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imDeleteFile` | :ref:`importers/structure-descriptions.imDeleteFileRec`* | unused                                                  | No        |
+-----------------------------------------------------+----------------------------------------------------------+---------------------------------------------------------+-----------+

The following selectors are optional, for better support copying and trimming files using the Project Manager:

+---------------------------------------------------------------+--------------------------------------------------------------------+-----------------------------------------------------------+-----------+
|                         **Selector**                          |                             **param1**                             |                        **param2**                         | **Synth** |
+===============================================================+====================================================================+===========================================================+===========+
| :ref:`importers/selector-descriptions.imCalcSize8`            | :ref:`importers/structure-descriptions.imCalcSizeRec`*             | :ref:`importers/structure-descriptions.imFileAccessRec8`* | No        |
+---------------------------------------------------------------+--------------------------------------------------------------------+-----------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imCheckTrim8`           | :ref:`importers/structure-descriptions.imCheckTrimRec`*            | :ref:`importers/structure-descriptions.imFileAccessRec8`* | No        |
+---------------------------------------------------------------+--------------------------------------------------------------------+-----------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imTrimFile8`            | :ref:`importers/structure-descriptions.imFileAccessRec8`*          | :ref:`importers/structure-descriptions.imTrimFileRec8`*   | No        |
+---------------------------------------------------------------+--------------------------------------------------------------------+-----------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imCopyFile`             | :ref:`importers/structure-descriptions.imCopyFileRec`*             | unused                                                    | No        |
+---------------------------------------------------------------+--------------------------------------------------------------------+-----------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imRetargetAccelerator`  | :ref:`importers/structure-descriptions.imAcceleratorRec`*          | unused                                                    | No        |
+---------------------------------------------------------------+--------------------------------------------------------------------+-----------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imQueryDestinationPath` | :ref:`importers/structure-descriptions.imQueryDestinationPathRec`* | unused                                                    | No        |
+---------------------------------------------------------------+--------------------------------------------------------------------+-----------------------------------------------------------+-----------+

The following selectors are used for embedded Closed Captioning support:

+-------------------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------+-----------+
|                              **Selector**                               |                    **param1**                     |                                  **param2**                                  | **Synth** |
+=========================================================================+===================================================+==============================================================================+===========+
| :ref:`importers/selector-descriptions.imInitiateAsyncClosedCaptionScan` | :ref:`importers/structure-descriptions.imFileRef` | :ref:`importers/structure-descriptions.imInitiateAsyncClosedCaptionScanRec`* | No        |
+-------------------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetNextClosedCaption`           | :ref:`importers/structure-descriptions.imFileRef` | :ref:`importers/structure-descriptions.imGetNextClosedCaptionRec`*           | No        |
+-------------------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imCompleteAsyncClosedCaptionScan` | :ref:`importers/structure-descriptions.imFileRef` | :ref:`importers/structure-descriptions.imCompleteAsyncClosedCaptionScanRec`* | No        |
+-------------------------------------------------------------------------+---------------------------------------------------+------------------------------------------------------------------------------+-----------+

The following selectors are optional, useful for a subset of importers:

+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
|                          **Selector**                          |                            **param1**                            |                             **param2**                              | **Synth** |
+================================================================+==================================================================+=====================================================================+===========+
| :ref:`importers/selector-descriptions.imAnalysis`              | :ref:`importers/structure-descriptions.imFileRef`                | :ref:`importers/structure-descriptions.imAnalysisRec`*              | Yes       |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imDataRateAnalysis`      | :ref:`importers/structure-descriptions.imFileRef`                | :ref:`importers/structure-descriptions.imDataRateAnalysisRec`*      | No        |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetTimeInfo8`          | :ref:`importers/structure-descriptions.imFileRef`                | :ref:`importers/structure-descriptions.imTimeInfoRec8`*             | No        |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imSetTimeInfo8`          | :ref:`importers/structure-descriptions.imFileRef`                | :ref:`importers/structure-descriptions.imTimeInfoRec8`*             | No        |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetFileAttributes`     | :ref:`importers/structure-descriptions.imFileAttributesRec`*     | unused                                                              |           |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetMetaData`           | :ref:`importers/structure-descriptions.imFileRef`                | :ref:`importers/structure-descriptions.imMetaDataRec`*              | No        |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imSetMetaData`           | :ref:`importers/structure-descriptions.imFileRef`                | :ref:`importers/structure-descriptions.imMetaDataRec`*              | No        |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetRollCrawlInfo`      | :ref:`importers/structure-descriptions.imRollCrawlInfoRec`*      | unused                                                              | Yes       |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imRollCrawlRenderPage`   | :ref:`importers/structure-descriptions.rollCrawlRenderRec`*      | unused                                                              | Yes       |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imDeferredProcessing`    | :ref:`importers/structure-descriptions.imDeferredProcessingRec`* | unused                                                              | No        |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetAudioChannelLayout` | :ref:`importers/structure-descriptions.imFileRef`                | :ref:`importers/structure-descriptions.imGetAudioChannelLayoutRec`* | Yes       |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetPeakAudio`          | :ref:`importers/structure-descriptions.imFileRef`                | :ref:`importers/structure-descriptions.imPeakAudioRec`*             | Yes       |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imQueryContentState`     | :ref:`importers/structure-descriptions.imQueryContentStateRec`*  | unused                                                              | No        |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imQueryStreamLabel`      | :ref:`importers/structure-descriptions.imQueryStreamLabelRec`*   | unused                                                              | Yes       |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetIndColorSpace`      | :ref:`importers/structure-descriptions.ColorProfileRec`          | unused                                                              | Yes       |
+----------------------------------------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------+-----------+

Used only in After Effects:

+-------------------------------------------------------------+------------------------------+-------------------------------+-----------+
|                        **Selector**                         |          **param1**          |          **param2**           | **Synth** |
+=============================================================+==============================+===============================+===========+
| :ref:`importers/selector-descriptions.imGetSubTypeNames`    | ``(csSDK_int32) fileType``   | :ref:`importers/structure-descriptions.imSubTypeDescriptionRec`*` | No        |
+-------------------------------------------------------------+------------------------------+-------------------------------+-----------+
| :ref:`importers/selector-descriptions.imGetIndColorProfile` | ``(int) index``              | :ref:`importers/structure-descriptions.imIndColorProfileRec`*     | No        |
+-------------------------------------------------------------+------------------------------+-------------------------------+-----------+
| :ref:`importers/selector-descriptions.imQueryInputFileList` | :ref:`importers/structure-descriptions.imQueryInputFileListRec`* | unused                        | No        |
+-------------------------------------------------------------+------------------------------+-------------------------------+-----------+
