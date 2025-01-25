# Debugging Plug-Ins

Once you’ve got the plugin building directly into the plugins folder as explained above, here’s how to specify Premiere Pro as the application to run during debug sessions:

On Windows:

1. In the Visual Studio solution, in the Solution Explorer panel, choose the project you want to debug
2. Right-click it and choose Set as StartUp Project
3. Right-click it again and choose Properties
4. In Configuration Properties > Debugging > Command, provide the path to the executable file of the host application the plugins will be running in (this may be Premiere Pro or After Effects)
5. From there you can either hit the Play button, or you can launch the application and later at any point choose Debug > Attach to Process…

On macOS:

1. In Xcode, in the Project Navigator, choose the xcodeproj you want to debug
2. Choose Product > Scheme > Edit Scheme…
3. Under Run, in the Info tab, for Executable, choose the host application the plugins will be running in (this may be Premiere Pro or After Effects)
4. From there you can either hit the Play button to build and run the current scheme, or you can launch the application and later at any point choose Debug > Attach to Process.

Another way to do this in Visual Studio is by placing a line of code

```cpp
_asm int 3;
```

or

```cpp
DebugBreak();
```

You will then receive the Microsoft error reporting message, but if you hit the Debug button you will enable Just-In-Time Debugging and can attach to the process.
