.. _resources/impt-resource:

IMPT Resource
################################################################################

Premiere Pro looks for an IMPT resource to identify a plug-in as an importer.

Before Premiere Pro 1.0, the IMPT resource was also used to declare the file extension supported by an importer.

Since file extensions are now declared during imGetIndFormat, the drawtype four character code in the IMPT resource is no longer used by Premiere Pro.

However, a unique drawtype fourcc is needed for the importer to function properly in After Effects on macOS.

Do not use 0x4D4F6F76. This is already reserved by After Effects.

::

  1000 IMPT DISCARDABLE BEGIN
  0x12345678 // Put your own unique hexadecimal code here
  END
