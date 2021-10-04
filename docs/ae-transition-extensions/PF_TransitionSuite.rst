.. _ae-transition-extensions/PF_TransitionSuite:

PF_TransitionSuite
################################################################################

In PrSDKAESupport.h, we've added ``PF_TransitionSuite::RegisterTransitionInputParam()``.

This call must be made before the ``PF_ADD_PARAM()`` call during ``PF_Cmd_PARAM_SETUP``.

Pass in the param to be used as the input layer for the other side of the transition.

This enables your effect to be applied between two clips in the timeline just like our native transitions, but it will show up in the Effect Controls panel with full keyframable parameters similar to existing AE effects.
