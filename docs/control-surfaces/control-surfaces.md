# Control Surfaces

Starting in Premiere Pro CC 2014, a control surface plugin can interface with a hardware control surface. This is the API that provides built-in support for EUCON and Mackie devices to control audio mixing and basic transport controls. The API supports two-way communication with Premiere Pro, so that hardware faders, VU meters, etc are in sync with the application.

Compile the sample plugin into a subfolder of the main application folder: `Plugins\\ ControlSurface\\`

You should see the plugin in the PPro UI in Preferences > Control Surface, when you hit the Add button, as one of the options in the Device Class drop-down next to Mackie and EUCON (currently shows as "SDK Control Surface Sample").

You'll want to implement handlers for any relevant functions defined in the plugin suites here: `adobesdk\controlsurface\plugin`

And to do that, you can use any APIs to call into the host defined in the host suites here: `adobesdk\controlsurface\host`

---

## Calling Sequence

When the application is launched, the control surface plugins are loaded, and the entry point is called. The host ID and API version is passed in, and the plugin passes back ADOBESDK_ControlSurfacePluginFuncs, an array of function pointers.

Next, the Startup() function is called, where the plugin registers a suite of functions as defined in ControlSurfacePluginSuite.h. For each base class it will inherit from (defined in adobesdkcontrolsurfacepluginwrapper), it calls RegisterSuite(). These suites are the way for the host application to call the control surface plugin later on. There are separate base classes for the transport controls, audio mixer, Lumetri Color controls, and more.

Then, CreatePluginInstance() is called. When a project is opened, Connect() is called. Here the plugin instantiates a ControlSurface object, which inherits from any of the previously mentioned base classes. It acquire any host suites it needs, and then it passes back a reference to the ControlSurface object.

---

## Getting Started

Please write us if you would like further guidance.
