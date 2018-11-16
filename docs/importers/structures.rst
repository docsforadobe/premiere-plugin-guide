.. _importers/structures:

Structures
################################################################################

+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
|                                **Structure**                                |                                                    **Sent with selector**                                                    |
+=============================================================================+==============================================================================================================================+
| :ref:`importers/structure-descriptions.imAcceleratorRec`                    | :ref:`importers/selector-descriptions.imRetargetAccelerator`                                                                 |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imAnalysisRec`                       | :ref:`importers/selector-descriptions.imAnalysis`                                                                            |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imAsyncImporterCreationRec`          | :ref:`importers/selector-descriptions.imCreateAsyncImporter`                                                                 |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imAudioInfoRec7`                     | :ref:`importers/selector-descriptions.imGetInfo8` (member of :ref:`importers/structure-descriptions.imFileInfoRec8`)         |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imCalcSizeRec`                       | :ref:`importers/selector-descriptions.imCalcSize8`                                                                           |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imCheckTrimRec`                      | :ref:`importers/selector-descriptions.imCheckTrim8`                                                                          |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imClipFrameDescriptorRec`            | :ref:`importers/selector-descriptions.imSelectClipFrameDescriptor`                                                           |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imCompleteAsyncClosedCaptionScanRec` | :ref:`importers/selector-descriptions.imCompleteAsyncClosedCaptionScan`                                                      |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imIndColorProfileRec`                | :ref:`importers/selector-descriptions.imGetIndColorProfile`                                                                  |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imCopyFileRec`                       | :ref:`importers/selector-descriptions.imCopyFile`                                                                            |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imDataRateAnalysisRec`               | :ref:`importers/selector-descriptions.imDataRateAnalysis`                                                                    |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imDeferredProcessingRec`             | :ref:`importers/selector-descriptions.imDeferredProcessing`                                                                  |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imDeleteFileRec`                     | :ref:`importers/selector-descriptions.imDeleteFile`                                                                          |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imFileAccessRec8`                    | :ref:`importers/selector-descriptions.imGetInfo8` and :ref:`importers/selector-descriptions.imGetPrefs8`                     |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imFileAttributesRec`                 | :ref:`importers/selector-descriptions.imGetFileAttributes`                                                                   |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imFileInfoRec8`                      | :ref:`importers/selector-descriptions.imGetInfo8`                                                                            |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imFileOpenRec8`                      | :ref:`importers/selector-descriptions.imOpenFile8`                                                                           |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imFileRef`                           | - :ref:`importers/selector-descriptions.imAnalysis`,                                                                         |
|                                                                             | - :ref:`importers/selector-descriptions.imDataRateAnalysis`,                                                                 |
|                                                                             | - :ref:`importers/selector-descriptions.imOpenFile8`,                                                                        |
|                                                                             | - :ref:`importers/selector-descriptions.imQuietFile`,                                                                        |
|                                                                             | - :ref:`importers/selector-descriptions.imCloseFile`,                                                                        |
|                                                                             | - :ref:`importers/selector-descriptions.imGetTimeInfo8`,                                                                     |
|                                                                             | - :ref:`importers/selector-descriptions.imSetTimeInfo8`,                                                                     |
|                                                                             | - :ref:`importers/selector-descriptions.imImportImage` ,                                                                     |
|                                                                             | - :ref:`importers/selector-descriptions.imImportAudio7`                                                                      |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``imFileSpec``                                                              | - :ref:`importers/selector-descriptions.imGetInfo8`,                                                                         |
|                                                                             | - :ref:`importers/selector-descriptions.imGetPrefs8`,                                                                        |
|                                                                             | - :ref:`importers/selector-descriptions.imSaveFile8`,                                                                        |
|                                                                             | - :ref:`importers/selector-descriptions.imDeleteFile`,                                                                       |
|                                                                             | - :ref:`importers/selector-descriptions.imTrimFile8`                                                                         |
|                                                                             |                                                                                                                              |
|                                                                             | Member of:                                                                                                                   |
|                                                                             |                                                                                                                              |
|                                                                             | - :ref:`importers/structure-descriptions.imFileAccessRec8`,                                                                  |
|                                                                             | - :ref:`importers/structure-descriptions.imSaveFileRec8`,                                                                    |
|                                                                             | - :ref:`importers/structure-descriptions.imDeleteFileRec`,                                                                   |
|                                                                             | - :ref:`importers/structure-descriptions.imTrimFileRec8`                                                                     |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imFrameFormat`                       | :ref:`importers/selector-descriptions.imGetSourceVideo` (member of :ref:`importers/structure-descriptions.imSourceVideoRec`) |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imGetNextClosedCaptionRec`           | :ref:`importers/selector-descriptions.imGetNextClosedCaption`                                                                |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imGetPrefsRec`                       | :ref:`importers/selector-descriptions.imGetPrefs8`                                                                           |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imImageInfoRec`                      | :ref:`importers/selector-descriptions.imGetInfo8` (member of :ref:`importers/structure-descriptions.imFileInfoRec8`)         |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imImportAudioRec7`                   | :ref:`importers/selector-descriptions.imImportAudio7`                                                                        |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imImportImageRec`                    | :ref:`importers/selector-descriptions.imImportImage`                                                                         |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imImportInfoRec`                     | :ref:`importers/selector-descriptions.imInit`                                                                                |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imIndFormatRec`                      | :ref:`importers/selector-descriptions.imGetIndFormat`                                                                        |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imIndPixelFormatRec`                 | :ref:`importers/selector-descriptions.imGetIndPixelFormat`                                                                   |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imInitiateAsyncClosedCaptionScanRec` | :ref:`importers/selector-descriptions.imInitiateAsyncClosedCaptionScan`                                                      |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imMetaDataRec`                       | :ref:`importers/selector-descriptions.imGetMetaData` and :ref:`importers/selector-descriptions.imSetMetaData`                |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imPeakAudioRec`                      | :ref:`importers/selector-descriptions.imGetPeakAudio`                                                                        |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imPreferredFrameSizeRec`             | :ref:`importers/selector-descriptions.imGetPreferredFrameSize`                                                               |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imQueryContentStateRec`              | :ref:`importers/selector-descriptions.imQueryContentState`                                                                   |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imQueryDestinationPathRec`           | :ref:`importers/selector-descriptions.imQueryDestinationPath`                                                                |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imQueryInputFileListRec`             | :ref:`importers/selector-descriptions.imQueryInputFileList`                                                                  |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imQueryStreamLabelRec`               | :ref:`importers/selector-descriptions.imQueryStreamLabel`                                                                    |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``imRollCrawlInfoRec``                                                      | ``imGetRollCrawlInfo``                                                                                                       |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``imRollCrawlRenderRec``                                                    | ``imRollCrawlRenderPage``                                                                                                    |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imSaveFileRec8`                      | :ref:`importers/selector-descriptions.imSaveFile8`                                                                           |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imSourceVideoRec`                    | :ref:`importers/selector-descriptions.imGetSourceVideo`                                                                      |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imSubTypeDescriptionRec`             | :ref:`importers/selector-descriptions.imGetSubTypeNames`                                                                     |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imTimeInfoRec8`                      | :ref:`importers/selector-descriptions.imGetTimeInfo8` and :ref:`importers/selector-descriptions.imSetTimeInfo8`              |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`importers/structure-descriptions.imTrimFileRec8`                      | :ref:`importers/selector-descriptions.imTrimFile8`                                                                           |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
