# Plug In Installation

Plug-ins must have an installer. This simplifies installation by the user, provides more compact distribution, and ensures all the pieces are installed correctly.

Create a container folder for your plug-in(s) to minimize user confusion.

Don't unintentionally overwrite existing plugins, or replace newer versions.

The installer should find the default installation directories as described below.

It is also appreciated when an installer allows the user to specify an alternate directory.

Plugins should be installed in the common plugin location.

Supported Premiere and After Effects plugins installed here will be loaded by Premiere Pro, After Effects, Audition, and Media Encoder.

Other plugin types, such as QuickTime and VfW codecs should be installed at the operating system level.

---

## Windows

As of Premiere Pro version 22.0, the `\Plug-ins` directories have been renamed `\Plugins`, to better coincide with Apple's Human Interface Guidelines. Premiere Pro will continue to attempt to load plugins from `\Plug-Ins` directories as well, for the foreseeable future. We will continue to specify

Starting in CC, each version of Premiere Pro will create a unique registry key that provide locations of folders of interest for third-party installations for that version.

For example, here are the registry values **for CC 2015.3:**

Key: `HKEY_LOCAL_MACHINE/Software/Adobe/Premiere Pro/10.0/`

Value name: `CommonPluginInstallPath`

Value data: `C:\Program Files\Adobe\Common\Plugins\7.0\MediaCore\\` (or whatever the proper MediaCore plugins folder is; note that this is the same as what the After Effects installer provides for a corresponding registry key)

Starting in CC 2015.3, **control surface plugins** should be installed here:

`/Library/Application Support/Adobe/Common/Plug-ins/ControlSurface/`

**For sequence presets:**

Value name: `SequencePresetsPath`

Value data: `[Adobe Premiere Pro installation path]\Settings\SequencePresets\`

**For sequence preview presets:**

Value name: `SequencePreviewPresetsPath`

Value data: `[Adobe Premiere Pro installation path]\Settings\EncoderPresets\SequencePreview\`

**For exporter presets:**

Value name: `CommonExporterPresetsPath`

Value data: **[User folder]AppDataRoamingAdobeCommonAME7.0Presets\\**

**Effects presets:**

Value name: `PluginInstallPath`

Value data: `[Adobe Premiere Pro installation path]\Adobe Premiere Pro\Plugins\Common`

Third-party installers can start from this path, and then modify the string to build the path to the language-specific effect presets.

**Prior to CC**, the only path given in the registry was the common plug-in path for the most recently installed version of Premiere Pro:

HKEY_LOCAL_MACHINE/Software/Adobe/Premiere Pro/CurrentVersion

Value name: `Plug-InsDir`

Value data: `REG_SZ` containing the full path of the plugin folder.

As an example: `C:\Program Files\Adobe\Common\Plugins\7.0\MediaCore\`

The best way to locate other preset folders was to start from the root path for Premiere Pro in the registry at

`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\\ Adobe Premiere Pro.exe`.

Then, just add the proper subdirectories as described in the macOS section.

---

## macOS

Starting in Premiere Pro version 22.0, The **common plugin location** is:

`/Library/Application Support/Adobe/Common/Plugins/[version]/MediaCore/`

Starting in CC 2015.3, **control surface plugins** should be installed here:

`/Library/Application Support/Adobe/Common/Plugins/ControlSurface/`

Previously, starting in CC 2015, Premiere Pro provided installer hints for Mac. You'll find `com.Adobe.Premiere Pro.paths.plist` at `/Library/Preferences`, which contains hints for your Mac installer to know where to install plugins, and is similar to the registry entries we have been providing on Win.

The **common plugin location** was at:

`/Library/Application Support/Adobe/Common/Plug-ins/[version]/MediaCore/`

Starting in CC 2015.3, **control surface plugins** should be installed here:

`/Library/Application Support/Adobe/Common/Plug-ins/ControlSurface/`

Following OS X Code Signing guidelines, plugins should be installed in this separate shared location rather than in the application bundle.

**For sequence presets:**

`/Settings/SequencePresets/[Your specific folder]/`

**Sequence preview presets:**

`/Settings/EncoderPresets/SequencePreview/[Your editing mode GUID]/`

**Encoder presets:**

`/MediaIO/systempresets/[Your exporter folder]/`

**Effects presets:**

`/Plugins/[language subdirectory]/Effect Presets/` (see [Localization](localization.md#intro-localization) for the list of language codes)

**Editing modes:**

`/Settings/Editing Modes/`

---

## Plugin Naming Conventions

On Windows, Premiere Pro plugins must have the file extension ".prm". On macOS, they have the file extension ".bundle". Other supported plug-in standards use their conventional file extensions: ".aex" for After Effects plugins, ".dll" for VST plugins.

While it is not required for your plugin to load, naming your plugins using the plugin type as a prefix (e.g. ImporterSDK, FilterSDK, etc.) will help reduce user confusion.

---

## Plugin Blocklisting (formerly Blacklisting)

Specific plugins can be blocked from being loaded by MediaCore in specific applications, using blocklists.

!!! note
    This does not work for After Effects plugins loaded by AE, although it does work for AE plugins loaded in Premiere Pro.

In the plugins folder, look for the appropriate blacklist file, and append the the filename of the plugin to the file (e.g. BadPlugin, not BadPlugin.prm). If the file doesn't exist, create it first. "Blocklist.txt" contains names of plugins blacklisted from all apps. Plugins can be blocked from loading in specific apps by including them in "Blocklist Adobe Premiere Pro.txt", or "Blocklist After Effects.txt", etc.

---

## Creating Sequence Presets

Not to be confused with encoder presets or sequence preview encoder presets, sequence presets are the successor to project presets. They contain the video, audio, timecode, and track layout information used when creating a new sequence.

If you wish to add Sequence Presets for the New Sequence dialog, save the settings with a descriptive name and comment. Emulate our settings files. Install the presets as described in this section.

---

## Application-level Preferences

For Windows 7 restricted user accounts, the only place that code has guaranteed write access to a folder is inside the user documents folder and its subfolders.

..Users[user name]AppDataRoamingAdobePremiere Pro[version]\\

This means that you cannot save data or documents in the application folder. There is currently no plugin API for storing preferences in the application prefs folder. Plugins can create their own preferences file in the user's Premiere prefs directory like so:

```cpp
HRESULT herr = SHGetKnownFolderPath(FOLDERID_RoamingAppData, 0, NULL, preferencesPath);
strcat(preferencesPath, "\\Adobe\\Premiere Pro\\[version]\\MyPlugin.preferences");
```

On MacOS: `NSSearchPathForDirectoriesInDomains(NSApplicationSupportDirector y,NSLocalDomainMask,…)`

This should get you started getting the Application Support folder which you can add onto to create something like:

`/Library/Application Support/Adobe/Premiere Pro/[version]/ MyPlugin.preferences`

---

## Dog Ears

Premiere Pro's built-in player has a mode to display statistics, historically known as "dog ears", which can be useful in debugging and tuning performance of importers, effects, transitions, and transmitters. The statistics include frames per second, frames dropped during playback, pixel format rendered, render size, and field type being rendered.

You can bring up the debug console in Premiere Pro. You can do this via Ctrl/Cmd-F12. To enable the dog ears, type this:

```cpp
debug.set EnableDogEars=true
```

to disable, use this:

```cpp
debug.set EnableDogEars=false
```

If the enter keystroke seems to go to the wrong panel, this is an intermittent panel focus problem. Click the Tools or Info panel before typing in the Console panel, and the enter key will be processed properly.

Once enabled, the player displays the statistics as black text on a partially transparent background. This allows you to still see the underlying video (to some extent) and yet also read the text. When you turn off dog ears, the setting may not take effect until you switch or reopen your current sequence.

!!! note
    If you are developing a transmitter, displaying dog ears will result in duplicate calls to PushVideo for the same frame. This happens because the player routinely updates the dog ears on a timer even when the frame hasn't changed for updated stats. As of CS6, this triggers a PushVideo to active transmitters as a side effect.
