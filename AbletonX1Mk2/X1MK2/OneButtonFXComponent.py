'''
Created on Jul 12, 2015

@author: aj


'''
import Live
from _Framework.DeviceComponent import DeviceComponent


class OneButtonFXComponent(DeviceComponent):
    '''
    Class to interface with a generic one-button FX in the in-line chain on assigned track.  
    To make this flexible with FX from plugins and chains of Plugins, the class will look 
    for the last device in the track it is assigned to, with the device_name given during initialization.
    '''


    def __init__(self, device_name, *a, **k):
        '''
        Set the device name to look for in the track.
        '''
        super(OneButtonFXComponent,self).__init__(*a,**k)
        assert isinstance(device_name, basestring)
        self._device_name = device_name
        self._track = None
        
        
        
    def set_track(self, track):
        assert (track== None) or isinstance(track, Live.Track.Track)
        if self._track != None:
            self._track.remove_devices_listener(self._on_devices_changed)
        
        self._track = track
        if self._track!= None:
            self._track.add_devices_listener(self._on_devices_changed)
        
        self._on_devices_changed()
        
    def _on_devices_changed(self):
        if self._device != None:
            self.set_device(None)
        
        if self._track != None:
            for index in range(len(self._track.devices)):
                device = self._track.devices[-1 * (index + 1)]
                if device.name == self._device_name:
                    self.set_device(device)
                    break
    
    def __str__(self):
        return '1BFX[%s]: T:%s D:%s' % (self._device_name, self._track, self.device()) + '\n' + str([d.name for d in self._track.devices])
    
    
    
        

            
    
    
            
        
    
        