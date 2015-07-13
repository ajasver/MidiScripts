'''
Created on Jul 8, 2015

@author: aj
'''

from _Framework.Skin import Skin
from _Framework.ButtonElement import Color
from .Colors import HsbColor, Blink, Pulse
from .Rgb import Rgb


ON =  HsbColor(0,0,127)
OFF = HsbColor(0,0,0)


class Defaults:

    class DefaultButton:
        On = HsbColor(0,0,127)
        Off = HsbColor(0,0,0)

class RgbColors:

    class Session:
        Scene = Rgb.GREEN
        SceneTriggered = Rgb.GREEN #Blink(Rgb.GREEN, Rgb.BLACK, 24)
        NoScene = Rgb.BLACK
        ClipStopped = Rgb.AMBER
        ClipStarted = Pulse(Rgb.GREEN.shade(1), Rgb.GREEN) # Pulse(Rgb.GREEN.shade(1), Rgb.GREEN, 48)
        ClipRecording = Pulse(Rgb.RED, Rgb.BLACK) #Pulse(Rgb.RED, Rgb.BLACK, 48)
        ClipTriggeredPlay = Blink(Rgb.GREEN, Rgb.BLACK) #Blink(Rgb.GREEN, Rgb.BLACK, 24)
        ClipTriggeredRecord = Blink(Rgb.RED, Rgb.BLACK) #Blink(Rgb.RED, Rgb.BLACK, 24)
        ClipEmpty = Rgb.BLACK
        RecordButton = Rgb.RED.shade(1.5)

    class Zooming:
        Selected = Rgb.AMBER
        Stopped = Rgb.RED
        Playing = Rgb.GREEN
        Empty = Rgb.BLACK


class StopButtons:

    class Session:
        StopClip = OFF
        StopClipTriggered = OFF


class CrossfadeButtons:

    class Mixer:

        class Crossfade:
            Off = OFF
            A = Rgb.SKY
            B = Rgb.PINK


def make_default_skin():
    return Skin(Defaults)


# def make_biled_skin():
#     return Skin(BiLedColors)


def make_rgb_skin():
    return Skin(RgbColors)


def make_stop_button_skin():
    return Skin(StopButtons)


def make_crossfade_button_skin():
    return Skin(CrossfadeButtons)