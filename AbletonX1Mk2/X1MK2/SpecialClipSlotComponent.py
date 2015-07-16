'''
Created on Jul 13, 2015

@author: aj

'''

from _Framework.ClipSlotComponent import ClipSlotComponent as BaseClipSlotComponent
from _Framework.SubjectSlot import subject_slot
from _Framework.Util import in_range
from .Colors import HsbColor


class SpecialClipSlotComponent(BaseClipSlotComponent):
    """
    Special version of ClipSlotComponent that allows delete buttons to be assigned to each 
    clip in the session, rather than using a single delete button as a modifier that is pressed
    at the same time as the clip launch buttons.
    """
    
    def set_delete_button(self, button):
        '''
        Make a dedicated button for deleting the clip that doesn't need to 
        clicked with the launch button.
        '''
        self._delete_button_value.subject = button
        self._delete_button = button
        self.update()
        
    @subject_slot('value')
    def _delete_button_value(self, value):
        '''
        This method is called when the delete_button is pressed
        '''
        if self.is_enabled():
            if value and self._delete_button:
                self._do_delete_clip()
                
                
    def _deletable_value(self,value):
        if isinstance(value, HsbColor):
            return value.make_red()
        else:
            return value
        
    def update(self):
        super(BaseClipSlotComponent, self).update()
        self._has_fired_slot = False
        button = self._launch_button_value.subject
        delete_button = self._delete_button_value.subject
        if self._allow_updates:
            value_to_send = self._feedback_value()
            if self.is_enabled() and button != None:
                delete_value_to_send = self._deletable_value(value_to_send)
                if value_to_send in (None, -1):
                    button.turn_off()
                elif in_range(value_to_send, 0, 128):
                    button.send_value(value_to_send)
                else:
                    button.set_light(value_to_send)
            if self.is_enabled() and delete_button != None:
                delete_value_to_send = self._deletable_value(value_to_send)
                if value_to_send in (None, -1):
                    delete_button.turn_off()
                elif in_range(value_to_send, 0, 128):
                    delete_button.send_value(delete_value_to_send)
                else:
                    delete_button.set_light(delete_value_to_send)
        else:
            self._update_requests += 1


        
        
         
