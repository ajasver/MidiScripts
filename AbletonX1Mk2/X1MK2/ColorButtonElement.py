'''
Created on Jul 10, 2015

@author: aj

'''

from _Framework.Skin import Skin, SkinColorMissingError
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import InputControlElement
from .Rgb import Rgb
from Push.Colors import Color
from .Colors import HsbColor

ON_VALUE = Rgb.WHITE.shade(2)
OFF_VALUE = Rgb.BLACK

class ColorButtonElement(ButtonElement):
    
    
    def __init__(self, logger, is_momentary, msg_type, channel, identifier, *a, **k):
        """
        Button element that works with the HSB color skin.  Need to use custom button element because
        the _Framework assumes that color data can be sent on one MIDI channel but sending HSB to the X1
        values requires channels 1, 2 and 3 for Hue, Saturation, and Brightness respectively.
        """
        super(ColorButtonElement, self).__init__(is_momentary, msg_type, channel, identifier, *a, **k)       
        self.log_message = logger
        self._last_received_value = -1  
        self.interfaces = [InputControlElement(msg_type = msg_type, channel=i, identifier = identifier, *a, **k) for i in range(3)]
        for i in self.interfaces:
            i.send_depends_on_forwarding = False
            i._set_suppress_script_forwarding(True)
        self._last_message_sent = None
     
    def send_value(self, hsb_value, force = False, channel = None):
        if hsb_value!=self._last_message_sent:
            if len(hsb_value)==3:
                self.log_message ('%s Sending %s over Interfaces %s' % (self.name, hsb_value, [('%s/%s/%s'%(i.message_channel(),i.script_wants_forwarding(),i.send_depends_on_forwarding)) for i in self.interfaces]))
                for c in range(3):
                    self.interfaces[c].send_value(hsb_value[c])#, force=True)
            else:
                self.log_message('%s is not an HSBColor.  Sending as midi value.' % (hsb_value))
                super(ColorButtonElement,self).send_value(hsb_value)
            self._last_message_sent = hsb_value
           
    def set_light(self,value):
        self._set_skin_light(value)
         
    def set_on_off(self, is_turned_on):
        #Uses custom on / off values rather than the default 0 and 127 midi values which won't
        #work for HSB.
        if is_turned_on:
            self.turn_on()
        else:
            self.turn_off()

    def turn_on(self):
        #self.log_message('%s set to ON' % self.name)
        ON_VALUE.draw(self)

    def turn_off(self):
        #self.log_message('%s set to OFF' % self.name)
        OFF_VALUE.draw(self)
        
    def _set_skin_light(self, value):
        #Override the original method to handle HSB values for clip colors as well as actions
        #This case is supposed to be handled by the ClipSlotComponent but it assumes the value
        #is and int rather than an HSB tuple so we have to handle it here instead.

        try:
  #          self.log_message('%s: Looking for %s in skin')
            color = self._skin[value] #check the skin for the right clor
            color.draw(self)
  #          self.log_message('%s Drew color %s' % (self.name,color))
        except SkinColorMissingError, e:
  #          self.log_message('%s: %s not in skin (%s)' % (self.name,value, e))
            try:
  #              self.log_message('%s: Attempt to draw %s' % (self.name,value))
                value.draw(self)
            except Exception, e:
  #              self.log_message('%s: Fallback to draw on/off (%s)' % (self.name,e))
                self.set_on_off(value)
    
