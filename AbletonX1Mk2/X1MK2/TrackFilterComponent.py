#Embedded file name: /Users/versonator/Jenkins/live/Binary/Core_Release_64_static/midi-remote-scripts/VCM600/TrackFilterComponent.py
import Live
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.EncoderElement import EncoderElement
from _Framework.ButtonElement import ButtonElement
from _Generic.Devices import get_parameter_by_name
from VCM600.TrackFilterComponent import TrackFilterComponent as BaseTrackFilterComponent
from VCM600.TrackFilterComponent import FILTER_DEVICES

FILTER_DEVICES.update({'AudioEffectGroupDevice': {'Frequency': 'Macro 1',
                'Resonance': 'Macro 2', 'Name': 'FILTER'}})


class TrackFilterComponent(BaseTrackFilterComponent):
    """ Class representing a track's filter, attaches to the last filter in the track """

    def __init__(self):
        super(TrackFilterComponent,self).__init__()
        self._on_off_button = None

    def disconnect(self):
        if self._on_off_control != None:
            self._on_off_button = None
        super(TrackFilterComponent,self).disconnect()

#     def set_track(self, track):
#         if not (track == None or isinstance(track, Live.Track.Track)):
#             raise AssertionError
#         if self._track != None:
#                 if self._on_off_button !=None:
#                     self._on_off_button.turn_off
#         super(TrackFilterComponent, self).set_track(track)

        
    def set_device_on_off(self,on_off,log_message):
        if not isinstance(on_off, ButtonElement):
            raise AssertionError
        if self._device!=None:
            if (self._on_off_button != None): 
                self._on_off_button.disconnect()
                self._on_off_button.remove_value_listener(self._on_off_value)
            
        self._on_off_button = on_off
        self._on_off_button.add_value_listener(self._on_off_value)
        self._update_on_off_button()
        log_message('Filter On/Off %s' % self._on_off_button)
            

    def update(self):
        if self.is_enabled() and self._device != None:
            if self._on_off_button != None:
                self._update_on_off_button()
                parameter = self._on_off_parameter()
                if not parameter.value_has_listener(self._on_device_on_off):
                        parameter.add_value_listener(self._on_device_on_off)
                    
        super(TrackFilterComponent, self).update()
        
                
    def _on_off_parameter(self):
        result = None
        if self._device != None:
            for parameter in self._device.parameters:
                if str(parameter.name).startswith('Device On'):
                    result = parameter
                    break

        return result


    def _on_device_on_off(self):
        self._update_on_off_button()
    
    def _on_off_value(self, value):
        if not self._on_off_button != None:
            raise AssertionError
        if not value in range(128):
            raise AssertionError
        if (not self._on_off_button.is_momentary() or value is not 0):
            parameter =  self._on_off_parameter()
            if (parameter != None and parameter.is_enabled):
                parameter.value =  float(int(parameter.value == 0.0))
    
    
    def _update_on_off_button(self):
        if self.is_enabled() and self._on_off_button != None:
            turn_on = False
            if self._device != None:
                parameter = self._on_off_parameter()
                if parameter != None:
                    turn_on = (parameter.value > 0.0)
                    self._on_off_button.set_light(turn_on)
                    

    def _on_devices_changed(self):
        self._device = None
        if self._track != None:
            for index in range(len(self._track.devices)):
                device = self._track.devices[-1 * (index + 1)]
                if device.class_name in FILTER_DEVICES.keys():
                    if device.class_name == 'AudioEffectGroupDevice':
                        if device.name == FILTER_DEVICES['AudioEffectGroupDevice']['Name']:
                            self._device = device
                            break
                    else:
                        self._device = device
                        break
        self.update()