.. _hardware/classid-filetype-subtype:

ClassID, Filetype and Subtype
################################################################################

All plug-in types that support media must identify unique classID, filetype, and subtype.

These are all four character codes, or 'fourCCs'.

+----------------+----------------------------------------------------------------------------------------------------------------------------------------+
| **Identifier** |                                                              **Purpose**                                                               |
+================+========================================================================================================================================+
| ``filetype``   | Identifies the plug-in's associated file type(s).                                                                                      |
|                |                                                                                                                                        |
|                | Plug-ins create lists of filetypes they support.                                                                                       |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``subtype``    | Differentiates between files of the same filetype.                                                                                     |
|                |                                                                                                                                        |
|                | Identifies the codec or compression to be used.                                                                                        |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``classID``    | With the new editing mode system starting in CS4, the classID is far less important.                                                   |
|                |                                                                                                                                        |
|                | It is used as part of the identification for exporters in the Editing Mode XML.                                                        |
|                |                                                                                                                                        |
|                | And plug-ins may share information with most other plug-ins running in the same process using the :ref:`hardware/classdata-functions`. |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------+
