# Load Em Up

## Plugin Caching

On its first launch, Premiere Pro loads all the plugins, reads the [plugin Property Lists (PiPL) Resource](../resources/pipl-resource.md), and sends any startup selectors to determine the plugins' capabilities. To speed up future application launches, it saves some of these capabilities in what we call the plugin cache (the registry on Windows, a Property List file on macOS).

The next time the application is launched, the cached data is used wherever possible, rather than loading all the plugins on startup. Using this changed data will make the application launch faster, but for a small set of plugins that need to be initialized every time, it may be undesirable. These include plugins that need to get run-time information that might change in between app launches (i.e. installed codec lists), and plugins that check for hardware and need to be able to fail. So we give your plugin control final say over whether or not it is reloaded each time.

By default, importers, recorders, and exporters are not cached. Exporters can be cached by setting exExporterInfoRec.isCacheable to non-zero during *exSelStartup*. Importers and recorders can be cached by returning `*IsCacheable` instead of `*NoError` (e.g. for importers, imIsCacheable instead of imNoError) on the startup selector.

By default, legacy video filters and device controllers are cached by default. To specify that legacy video filters must be reloaded each time, rather than cached, Premiere filters should respond to *fsCacheOnLoad*.

---

## Resolving Plugin Loading Problems

There are various tools to help in the development process.

On Windows only, you can force Premiere to reload all the plugins by holding down shift on startup. The plugin cache on macOS may be deleted manually from the user folder, at `~/Library/Preferences/com.Adobe.Premiere Pro [version].plist.`

For plugin loading issues, you may first check one of the plugin loading logs.

On Windows: `[user folder]\AppData\Roaming\Adobe\Premiere Pro\[version number]\Plugin Loading.log`

On macOS, this is: `~/Library/Application Support/Adobe/Premiere Pro/[version number]/Plugin Loading.log`

Your plugin will be listed by path and filename, and the log will contain details on what happened during the plugin loading process. Starting in CC 2017, it now logs any error codes returned from an effect on *PF_Cmd_GLOBAL_SETUP*.

If the log says a plugin has been marked as Ignore, the most common culprit is a library dependency that could not be loaded. If your plugin uses some image processing or proprietary code library, is it installed on the system, and in the right place? On Windows, a tool such as Dependency Walker (depends.exe) is helpful to check a plugin's dependencies.

---

## Loading unsigned plugins

MacOS versions 15+ prevent the loading of unsigned plugins. You can avoid this difficulty by adding ad-hoc signing as a custom build step.

`codesign --force --deep --sign - /path/to/plugin.dylib`

Note: Yes, that trailing '-' after '--sign' is important. 

---

## Library Linkage

On Windows, we strongly recommend dynamically linking to libraries, rather than static linking. In Visual Studio, the runtime library linkage setting is in C/C++ > Code Generation > Runtime Library.

We ask developers to compile with the /MD flag (or /MDd for debug builds), and not with the /MT flag.

Failure to do so can contribute to the problem where the Premiere Pro process can run out of fiber-local storage slots, and subsequent plugins fail to load.

---

## No Shortcuts

The Premiere Pro plugin loader does not follow Windows shortcuts. Although it does follow macOS symbolic links, we recommend against using symbolic links in the plugins folder, since the plugin loader checks the timestamp of the symbolic link rather than the timestamp of the plugin pointed to.

Explanation: If you use a symbolic link and the plugin fails to load once (for example, if the plugin pointed to isn't there) it will be marked to ignore when Premiere launches. Even if the plugin is restored to the proper location, the plugin loader will check the modification time of

the symbolic link, rather than the plugin pointed to, and continue to ignore the plugin until the modification date of the symbolic link is updated. So plugins should be placed directly in a plugins folder or subfolder.
