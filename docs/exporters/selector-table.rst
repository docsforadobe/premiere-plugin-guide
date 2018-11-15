.. _exporters/selector-table:

Selector Table
################################################################################

This table summarizes the various selector commands an exporter can receive.

+-----------------------------------+------------------------------------+------------+
|           **Selector**            |             **param1**             | **param2** |
+===================================+====================================+============+
| ``exSelStartup``                  | ``exExporterInfoRec*``             | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelBeginInstance``            | ``exExporterInstanceRec*``         | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelGenerateDefaultParams``    | ``exGenerateDefaultParamRec*``     | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelPostProcessParams``        | ``exPostProcessParamsRec*``        | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelValidateParamChanged``     | ``exParamChangedRec*``             | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelGetParamSummary``          | ``exParamSummaryRec*``             | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelParamButton``              | ``exParamButtonRec*``              | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelExport``                   | ``exDoExportRec*``                 | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelQueryExportFileExtension`` | ``exQueryExportFileExtensionRec*`` | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelQueryOutputFileList``      | ``exQueryOutputFileList*``         | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelQueryStillSequence``       | ``exQueryStillSequenceRec*``       | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelQueryOutputSettings``      | ``exQueryOutputSettingsRec*``      | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelValidateOutputSettings``   | ``exValidateOutputSettingsRec*``   | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelEndInstance``              | ``exExporterInstanceRec*``         | unused     |
+-----------------------------------+------------------------------------+------------+
| ``exSelShutdown``                 | ``exExporterInfoRec*``             | unused     |
+-----------------------------------+------------------------------------+------------+
