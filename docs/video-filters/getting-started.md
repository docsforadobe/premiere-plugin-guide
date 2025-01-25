# Getting Started

Begin with one of the two video filter sample projects, progressively replacing its functionality with your own.

---

## Resources

Filter plugins can use PiPL resources to define their behaviors and supported properties.

To provide any parameters in the Effect Controls panel, they must be defined in the PiPL in ANIM_ParamAtom sections, as demonstrated in the example below.

The 'no UI' UI type is for non-keyframeable parameters. After making changes to the PiPL, rebuild the plugin each time, so that the PiPL will be recompiled.

### A Filter PiPL Example

```cpp
#include "PrSDKPiPLVer.h"
#ifndef PRWIN_ENV
#include "PrSDKPiPL.r"
#endif

// The following two strings should be localized
#define plugInName "Cool Video Filter"
#define plugInCategory "SDK Filters"

// This name should not be localized or updated
#define plugInMatchName "SDK Cool Filter"

resource 'PiPL' (16000) {
  {
    // The plugin type
    Kind {PrEffect},

    // The plugin name as it will appear to the user
    Name {plugInName},

    // The internal name of this plugin
    AE_Effect_Match_Name {plugInMatchName},

    // The folder containing the plugin in the Effects Panel
    Category {plugInCategory},

    // The version of the PiPL resource definition
    AE_PiPL_Version {PiPLVerMajor, PiPLVerMinor},

    // The ANIM properties describe the filter parameters, and also how the data is stored in the project file. There is one ANIM_FilterInfo property followed by n ANIM_ParamAtoms
    ANIM_FilterInfo {
      0,
      #ifdef PiPLVer2p3

      // Non-square pixel aspect ratio supported
      notUnityPixelAspectRatio,
      anyPixelAspectRatio,
      reserved4False,
      reserved3False,
      reserved2False,

      #endif
    },

    reserved1False, // These flags are for use by After Effects
    reserved0False, // Not used by Premiere
    driveMe, // Not used by Premiere
    needsDialog, // Not used by Premiere
    paramsNotPointer, // Not used by Premiere
    paramsNotHandle, // Not used by Premiere
    paramsNotMacHandle, // Not used by Premiere
    dialogNotInRender, // Not used by Premiere
    paramsNotInGlobals, // Not used by Premiere
    bgAnimatable, // Not used by Premiere
    fgAnimatable, // Not used by Premiere
    geometric, // Not used by Premiere
    noRandomness, // Not used by Premiere

    // Put the number of parameters here
    2,

    plugInMatchName

    // There is one ANIM_ParamAtom for each parameter
    ANIM_ParamAtom {
      // This is the first property - Zero based count
      0,

      // The name to appear for the control
      "Level",

      // Parameter number goes here - One based count
      1,

      // Put the data type here
      ANIM_DT_SHORT,

      // UI control type
      ANIM_UI_SLIDER,
      0x0,
      0x0, // valid_min (0.0)
      0x405fc000,
      0x0, // valid_max (127.0)
      0x0,
      0x0, // ui_min (0.0)
      0x40590000,
      0x0, // ui_max (100.0)

      #if PiPLVer2p3
      // New - Scale/dontScale UI Range if user modifies
      dontScaleUIRange,
      #endif
    },

    // Set/don't set this if the param should be animated
    animateParam,
    dontRestrictBounds, // Not used by Premiere
    spaceIsAbsolute, // Not used by Premiere
    resIndependent, // Not used by Premiere

    // Bytes size of the param data
    2

    ANIM_ParamAtom {
      1,
      "Target Color", 2,

      // Put the data type here
      ANIM_DT_COLOR_RGB,

      // UI control type
      ANIM_UI_COLOR_RGB,
      0x0,
      0x0,
      0x0,
      0x0,
      0x0,
      0x0,
      0x0,
      0x0,

      #ifdef PiPLVer2p3
      dontScaleUIRange,
      #endif

      // Set/don't set this if the param should be animated
      animateParam,
      dontRestrictBounds,
      spaceIsAbsolute,
      resIndependent,

      // Bytes size of the param data
      4
    },
  }
};
```

---

## Entry Point

```cpp
short xFilter (
  short        selector,
  VideoHandle  theData)
```

*selector* is the action Premiere wants the video filter to perform.

`EffectHandle` provides source and destination buffers, and other useful information.

Return `fsNoErr` if successful, or an appropriate return code.
