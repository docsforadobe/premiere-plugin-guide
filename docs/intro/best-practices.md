.. _intro/best-practices:

Best Practices
################################################################################

When a plugin receives a selector it doesn't recognize, it should always return the code specific to the plugin type that means the selector is not supported (i.e. imUnsupported, rmUnsupported, etc).

In this way, new selectors can be added to the API and legacy plugins will automatically answer whether or not they support it.

----

Structure Alignment
================================================================================

All the sample projects include ``PrSDKTypes.h``.

This header sets the proper (single-byte) structure alignment and specifies the necessary (C-style) external linkage.
