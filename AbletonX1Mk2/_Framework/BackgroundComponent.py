#Embedded file name: /Users/versonator/Jenkins/live/Binary/Core_Release_64_static/midi-remote-scripts/_Framework/BackgroundComponent.py
from __future__ import absolute_import
from functools import partial
from .ControlSurfaceComponent import ControlSurfaceComponent
from .SubjectSlot import SubjectSlotError

class BackgroundComponent(ControlSurfaceComponent):
    """
    This component resets and adds a no-op listener to every control
    that it receives via arbitrary set_* methods.  It is specially
    useful to give it a layer with every control and low priority such
    that it prevents leaking LED lights or midi notes slipping into
    the midi track.
    """

    def __init__(self, *a, **k):
        super(BackgroundComponent, self).__init__(*a, **k)
        self._control_slots = {}
        self._control_map = {}

    def __getattr__(self, name):
        if len(name) > 4 and name[:4] == 'set_':
            return partial(self._clear_control, name[4:])
        raise AttributeError, name

    def _clear_control(self, name, control):
        slot = self._control_slots.get(name, None)
        if slot:
            del self._control_slots[name]
            self.disconnect_disconnectable(slot)
        if control:
            self._reset_control(control)
            self._control_map[name] = control
            try:
                self._control_slots[name] = self.register_slot(control, lambda *a, **k: self._on_value_listener(control, *a, **k), 'value')
            except SubjectSlotError:
                pass

        else:
            del self._control_map[name]

    def _reset_control(self, control):
        control.reset()

    def _on_value_listener(self, *a, **k):
        pass

    def update(self):
        super(BackgroundComponent, self).update()
        if self.is_enabled():
            for control in self._control_map.itervalues():
                self._reset_control(control)


class ModifierBackgroundComponent(BackgroundComponent):
    """
    This component lights up modifiers IFF they have other owners as
    well.  Only give configurable buttons with prioritized resources
    to this component.
    """

    def __init__(self, *a, **k):
        super(ModifierBackgroundComponent, self).__init__(*a, **k)

    def _reset_control(self, control):
        if len(control.resource.owners) > 1:
            control.set_light(control.is_pressed())
        else:
            control.reset()

    def _on_value_listener(self, sender, value, *a, **k):
        if len(sender.resource.owners) > 1:
            sender.set_light(sender.is_pressed())