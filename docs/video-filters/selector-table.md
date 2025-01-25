.. _video-filters/selector-table:

Selector Table
################################################################################

This table summarizes the various selector commands a video filter can receive.

+-----------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------+
|                             **Selector**                              | **Optional?** |                                          **Description**                                          |
+=======================================================================+===============+===================================================================================================+
| :ref:`video-filters/selector-descriptions.fsInitSpec`                 | Yes           | Allocate and initialize your parameters with default values without popping a modal setup dialog. |
+-----------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------+
| :ref:`video-filters/selector-descriptions.fsHasSetupDialog`           | Yes           | New for Premiere Pro CS3. Specify whether or not the filter has a setup dialog.                   |
+-----------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------+
| :ref:`video-filters/selector-descriptions.fsSetup`                    | Yes           | Allocate memory for your parameters if necessary.                                                 |
|                                                                       |               |                                                                                                   |
|                                                                       |               | Display your modal setup dialog with default parameter values or previously stored values.        |
|                                                                       |               |                                                                                                   |
|                                                                       |               | Save the new values to ``specsHandle``.                                                           |
+-----------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------+
| :ref:`video-filters/selector-descriptions.fsExecute`                  | No            | Filter the video using the stored parameters from ``specsHandle``.                                |
|                                                                       |               |                                                                                                   |
|                                                                       |               | Be aware of interlaced video, and don't overlook the alpha channel!                               |
+-----------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------+
| :ref:`video-filters/selector-descriptions.fsDisposeData`              | Yes           | Dispose of any instance data created during ``fsExecute``.                                        |
+-----------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------+
| :ref:`video-filters/selector-descriptions.fsCanHandlePAR`             | Yes           | Tell Premiere how your effect handles pixel aspect ratio.                                         |
+-----------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------+
| :ref:`video-filters/selector-descriptions.fsGetPixelFormatsSupported` | Yes           | Gets pixel formats supported. Called iteratively until all formats have been given.               |
+-----------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------+
| :ref:`video-filters/selector-descriptions.fsCacheOnLoad`              | Yes           | Return fsDoNotCacheOnLoad to disable plugin caching for this filter.                              |
+-----------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------+
