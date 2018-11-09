.. _intro/best-practices:

Best Practices
################################################################################

When a plug-in receives a selector it doesn't recognize, it should always return the code specific to the plug-in type that means the selector is not supported (i.e. imUnsupported, rmUnsupported, etc).

In this way, new selectors can be added to the API and legacy plug-ins will automatically answer whether or not they support it.

----

Structure Alignment
================================================================================

All the sample projects include PrSDKTypes.h.

This header sets the proper (single-byte) structure alignment and specifies the necessary (C-style) external linkage.
