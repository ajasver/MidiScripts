'''
Created on Jul 7, 2015

@author: aj
'''
from itertools import izip, repeat
from _Framework.ButtonElement import Color
from .MIDI_Map import BASE_COLOR_TABLE

_color_table = {}


class HsbColor(Color):
    '''
    Overrides the HsbColor class to convert the colors from Rgb to Hsb
    '''
    _rgb_value = (0, 0, 0) 
    _hsb_value = (0, 0, 0)
    _hsb_value_dim = (0,0,0)
    
    def __init__(self, h_value = None, s_value = None, b_value = None, rgb_value = None, *a, **k):
        """
        Set midi/rgb value for drawing later
        """
        super(HsbColor, self).__init__(midi_value = h_value,*a, **k)
        if rgb_value is not None:
            self._rgb_value = rgb_value
        
        if h_value != None:
            self._hsb_value = (h_value,100,127)
            if s_value != None:
                self._hsb_value = (h_value,s_value, 127)
                if b_value != None:
                    self._hsb_value = (h_value, s_value, b_value)
            
            
    def midi_value(self):
        return self.convert_to_midi_value()
    
    def dim(self,hsb_value,shade = 2):
        "Dims the HSB value"
        dim_level = shade * 50
        return (hsb_value[0], hsb_value[1], max(hsb_value[2]-dim_level,30))
    
    def brighten(self,hsb_value):
        "Brightens the HSB value"
        return (hsb_value[0],127,hsb_value[2])
        
    def shade(self, shade_level):
        """
        Generate a new shaded RGB from this color.
        """
        assert(shade_level > 0 and shade_level <= 2)
        shade_factor = 1.0 / 2.0 * (2 - shade_level)
        shaded = self.dim(self._hsb_value,shade_level)
        return HsbColor(shaded[0], shaded[1], shaded[2], [ a * b for a, b in izip(self._rgb_value, repeat(shade_factor)) ])

    def highlight(self):
        """
        Generate a new highlighted RGB from this color.
        """
        highlighted = self.brigthen(self._hsb_value)
        return HsbColor(highlighted[0], highlighted[1], highlighted[2], [ a * b for a, b in izip(self._rgb_value, repeat(1.5)) ])


    def draw(self,interface):
#         assert interface.is_rgb
        interface.send_value(self._hsb_value)
        
#     def send_value(self,interface,hsb_value):
#         assert interface.num_delayed_messages >= 3 #and isinstance(interface, ColorButtonElement)
#         interface.hue_interface.send_value(hsb_value[0]) #send the Hue midi value
#         interface.sat_interface.send_value(hsb_value[1]) #send the Saturation midi value
#         interface.bri_interface.send_value(hsb_value[2]) #send the Brightness midi value
        
    def convert_to_midi_value(self):
        raise NotImplementedError, 'HSB values cannot be serialized'
    
    def __iter__(self):
        return iter(self._rgb_value)
    
    def __getitem__(self,index_or_slice):
        return self._rgb_value[index_or_slice]
    
    def __str__(self):
        return "HsbColor[Hue: %s, Sat: %s, Bri %s]" % self._hsb_value 
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self._hsb_value == other._hsb_value)

    def __ne__(self, other):
        return not self.__eq__(other)
        
    
    
class AnimatedColor(Color):
    """
    Creates an animation between two RGB colors.
    The animation is defined by "blink".
    """

    @property
    def midi_value(self):
        return self.convert_to_midi_value()

    def __init__(self, color1, color2 = None, *a, **k):
        super(AnimatedColor, self).__init__(*a, **k)
        self.color1 = color1
        if color2 != None:
            self.color2 = color2
        else: 
            self.color2 = color1.shade(2)
        self.blink_state = 0
      

    def draw(self, interface, blink):
        if blink == 0:
            self.color1.draw(interface)
        else:
            self.color2.draw(interface)
        self.blink_state = (self.blink_state+1) % 8 
        
 
    
class Blink(AnimatedColor):


    def draw(self, interface):
        blink = (self.blink_state/2) % 2
        super(Blink,self).draw(interface,blink)
    
    


class Pulse(AnimatedColor):
    
    def draw(self, interface):
        blink = self.blink_state / 4
        super(Pulse,self).draw(interface,blink)
    
    

    
def toHSB(rgb_val):
    if _color_table.has_key(rgb_val):
        return _color_table[rgb_val]
    rv = rgb_val / 65536
    rp = rv * 65536
    gv = (rgb_val - rp) / 256
    gp = gv * 256
    bv = rgb_val - rp - gp
    rgb_max = max(max(rv, gv), bv)
    rgb_min = min(min(rv, gv), bv)
    bright = rgb_max
    if bright == 0:
        color = HsbColor(10, 10, 60)
        _color_table[rgb_val] = color
        return color
    sat = 255 * (rgb_max - rgb_min) / bright
    if sat == 0:
        sat = 0
        hue = 0
        color = HsbColor(hue, sat, min(bright / 2, 127))
        _color_table[rgb_val] = color
        return color
    hue = 0
    if rgb_max == rv:
        hue = 0 + 43 * (gv - bv) / (rgb_max - rgb_min)
    elif rgb_max == gv:
        hue = 85 + 43 * (bv - rv) / (rgb_max - rgb_min)
    else:
        hue = 171 + 43 * (rv - gv) / (rgb_max - rgb_min)
    if hue < 0:
        hue = 256 + hue
    color = HsbColor(hue / 2, min(sat / 2 + 20, 127), bright / 2)
    _color_table[rgb_val] = color
    return color
    

class CLIP_COLOR_TABLE(object):
    
    def __init__(self, logger):
        self._color_list = []
        self._color_lookup = {}
        self.log_message = logger
        for c in BASE_COLOR_TABLE:
            color = HsbColor(c[0], c[1], c[2])
            self._color_lookup[c[3]] = color
            self._color_list.append(color)
          
            
    def __iter__(self):
        return iter(self._color_list)
     
#     def __getitem__(self, index_or_slice):
#         return self._color_list[index_or_slice]
    
    def __getitem__(self,rgb_key):
    #    self.log_message('Getting pad color %s' % rgb_key)
        if rgb_key in self._color_lookup.keys():  
            hsb = self._color_lookup[int(rgb_key)]
        else:
            hsb = toHSB(rgb_key)
        
     #   self.log_message('Fetched %s' % hsb)
        return hsb
    
        



        
        
        