#Embedded file name: /Users/versonator/Jenkins/live/Binary/Core_Release_64_static/midi-remote-scripts/_APC/DeviceBankButtonElement.py
from _Framework.ComboElement import ComboElement

class DeviceBankButtonElement(ComboElement):
    """
    ComboElement that will change the channel, while the control is grabbed
    """

    def on_nested_control_element_received(self, control):
        super(DeviceBankButtonElement, self).on_nested_control_element_received(control)
        if control == self.wrapped_control:
            self.wrapped_control.set_channel(1)

    def on_nested_control_element_lost(self, control):
        super(DeviceBankButtonElement, self).on_nested_control_element_lost(control)
        if control == self.wrapped_control:
            self.wrapped_control.set_channel(0)