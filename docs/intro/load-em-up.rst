.. _intro/load-em-up:

Load Em Up
################################################################################

Plug-in Caching
================================================================================

On its first launch, Premiere Pro loads all the plug-ins, reads the :ref:`resources/pipl-resource`, and sends any startup selectors to determine the plug-ins' capabilities. To speed up future application launches, it saves some of these capabilities in what we call the plug-in cache (the registry on Windows, a Property List file on macOS).

The next time the application is launched, the cached data is used wherever possible, rather than loading all the plug-ins on startup. Using this changed data will make the application launch faster, but for a small set of plug-ins that need to be initialized every time, it may be undesirable. These include plug-ins that need to get run-time information that might change in between app launches (i.e. installed codec lists), and plug-ins that check for hardware and need to be able to fail. So we give your plug-in control final say over whether or not it is reloaded each time.

By default, importers, recorders, and exporters are not cached. Exporters can be cached by setting exExporterInfoRec.isCacheable to non-zero during *exSelStartup*. Importers and recorders can be cached by returning ``*IsCacheable`` instead of ``*NoError`` (e.g. for importers, imIsCacheable instead of imNoError) on the startup selector.

By default, legacy video filters and device controllers are cached by default. To specify that legacy video filters must be reloaded each time, rather than cached, Premiere filters should respond to *fsCacheOnLoad*.

----

Resolving Plug-in Loading Problems
================================================================================

There are various tools to help in the development process.

On Windows only, you can force Premiere to reload all the plug-ins by holding down shift on startup. The plug-in cache on macOS may be deleted manually from the user folder, at ``~/Library/Preferences/com.Adobe.Premiere Pro [version].plist.``

For plug-in loading issues, you may first check one of the plug-in loading logs.

On Windows: ``[user folder]\AppData\Roaming\Adobe\Premiere Pro\[version number]\Plugin Loading.log``

On macOS, this is: ``~/Library/Application Support/Adobe/Premiere Pro/[version number]/Plugin Loading.log``

Your plug-in will be listed by path and filename, and the log will contain details on what happened during the plug-in loading process. Starting in CC 2017, it now logs any error codes returned from an effect on *PF_Cmd_GLOBAL_SETUP*.

If the log says a plug-in has been marked as Ignore, the most common culprit is a library dependency that could not be loaded. If your plug-in uses some image processing or proprietary code library, is it installed on the system, and in the right place? On Windows, a tool such as Dependency Walker (depends.exe) is helpful to check a plug-in's dependencies.

----

Library Linkage
================================================================================

On Windows, we strongly recommend dynamically linking to libraries, rather than static linking. In Visual Studio, the runtime library linkage setting is in C/C++ > Code Generation > Runtime Library.

We ask developers to compile with the /MD flag (or /MDd for debug builds), and not with the /MT flag.

Failure to do so can contribute to the problem where the Premiere Pro process can run out of fiber-local storage slots, and subsequent plug-ins fail to load.

----

No Shortcuts
================================================================================

The Premiere Pro plug-in loader does not follow Windows shortcuts. Although it does follow macOS symbolic links, we recommend against using symbolic links in the plug-ins folder, since the plug-in loader checks the timestamp of the symbolic link rather than the timestamp of the plug-in pointed to.

Explanation: If you use a symbolic link and the plug-in fails to load once (for example, if the plug-in pointed to isn't there) it will be marked to ignore when Premiere launches. Even if the plug-in is restored to the proper location, the plug-in loader will check the modification time of

the symbolic link, rather than the plug-in pointed to, and continue to ignore the plug-in until the modification date of the symbolic link is updated. So plug-ins should be placed directly in a plug-ins folder or subfolder.
