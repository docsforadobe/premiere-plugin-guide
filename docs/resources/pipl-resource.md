# Plug-In Property Lists (PiPL) Resource

For many plugin types, Premiere loads a PiPL (Plug-in Property List) resource. The PiPL is described in a file with a “.r” extension.

The complete PiPL syntax is described in PiPL.r.

You’ll notice that PiPLs are really old. A vestige of 68k macOS programming, they spread to Windows.

However, if you develop from the sample projects, you shouldn’t have to do anything to get them to build properly for Latin languages.

---

## Which Types of Plugins Need PiPLs?

Exporters, players, and recorders do not need PiPLs.

Standard importers do not need PiPLs. Synthetic and custom importers use a basic PiPL to specify their name, and the match name that Premiere uses to identify them. The name appears in the File > New menu.

Device controllers use a basic PiPL to specify their name and the match name that Premiere uses to identify them.

Video filters use an extended PiPL to specify their name, the match name that Premiere uses to identify them, the bin they go in, how they handle pixel aspect ratio, whether or not they have randomness, and their parameters.

For more information on the `ANIM_FilterInfo` and `ANIM_ParamAtom`, see the resources section in [Video Filters](../video-filters/video-filters.md#video-filters-video-filters).

---

## A Basic PiPL Example

```none
#define plugInName "SDK Custom Import"
#define plugInMatchName "SDK Custom Import"

resource 'PiPL' (16000) {
{

  // The plugin type
  Kind {PrImporter},

  // The name as it will appear in a Premiere menu, this can be localized
  Name {plugInName},

  // The internal name of this plugin - do not localize this. This is used for both Premiere and After Effects plugins.
  AE_Effect_Match_Name {plugInMatchName}

  // Transitions and video filters define more PiPL attributes here
}

};
```

---

## How PiPLs Are Processed By Resource Compilers

On macOS, .r files are processed natively by Xcode, as a Build Phase of type Build Carbon Resources. This step is already set for the sample projects.

On Windows, .r files are processed with CnvtPiPL.exe, which creates an .rcp file based upon custom build steps in the project. The .rcp file is then included in the .rc file along with any other resources the plugin uses. These custom build steps are already in place in the sample projects.

To view them, open up the sample project in .NET. In the Solution Explorer, right-click the .r file and choose Properties. In the dialog, choose the Custom Build Step folder. The Command

Line contains the script for executing the CnvtPiPL.exe. Unless you are using a different compiler than the support compiler, or adding support for Asian languages, you should not need to modify the custom build steps. This script may also be found as a text file in the SDK at \\Examples\\ ResourcesWinCustom Build Steps.txt. This text file also describes the additional switches used for Asian languages.
