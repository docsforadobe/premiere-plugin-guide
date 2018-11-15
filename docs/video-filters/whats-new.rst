.. _video-filters/whats-new:

Whats New
################################################################################

What's New in Premiere Pro CS5?
================================================================================

In the Effects panel, video filters now appear with badges to advertise if they support YUV, 32- bit, and accelerated rendering.

The user can filter the list of effects to show only the effects that support those rendering modes. Video filters will automatically receive YUV and 32-bit badges if they advertise support using the existing ``fsGetPixelFormatsSupported``.

Custom badges can also be created. See Effect Badging for more information.

----

What's New in Premiere Pro CS3?
================================================================================

Checkbox controls are now supported directly in the Effect Controls panel.

Filters can specify whether or not they want a setup button in the Effect Controls panel during ``fsHasSetupDialog``, by returning ``fsHasNoSetupDialog`` or ``fsNoErr``.

Previously, this was set in the PiPL resource.
