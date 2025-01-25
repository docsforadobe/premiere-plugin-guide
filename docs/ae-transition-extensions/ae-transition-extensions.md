.. _ae-transition-extensions/ae-transition-extensions:

AE Transition Extensions
################################################################################

This chapter describes how to build native transitions in Premiere Pro based on the After Effects API. From a user-perspective, plugins built this way can show their parameters directly in the Effect Controls panel, even providing custom parameter UI in that panel or in the Sequence Monitor. Such plugins can run not only in Premiere Pro, but also in After Effects, although they will appear as effects rather than transitions.

The transition extensions work on top of effects built using the After Effects SDK. Since AE effects only have a single input, the second input is a layer parameter defined by the plugin.
