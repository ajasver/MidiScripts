# http://remotescripts.blogspot.com
# hanz.petrov@gmail.com
# Note and CC Mappings for the AJX X1 MK2 are defined in this file.
# Values may be edited with any text editor (but avoid using tabs for indentation)

# Session Highligher Size
# -----------------------

SESSION_WIDTH = 2
SESSION_HEIGHT = 4

# Combination Mode offsets
# ------------------------

TRACK_OFFSET = 0#offset from the left of linked session origin; set to -1 for auto-joining of multiple instances
SCENE_OFFSET = 0 #offset from the top of linked session origin (no auto-join)

# Buttons / Pads
# -------------
# Valid Note/CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments are permitted

BUTTONCHANNEL = 0 #Channel assignment for all mapped buttons/pads; valid range is 0 to 15
MESSAGETYPE = 0 #Message type for buttons/pads; set to 0 for MIDI Notes, 1 for CCs.
        #When using CCs for buttons/pads, set BUTTONCHANNEL and SLIDERCHANNEL to different values.

# General
PLAY = -1 #Global play
STOP = -1 #Global stop
REC = -1 #Global record
TAPTEMPO = -1 #Tap tempo
NUDGEUP = -1 #Tempo Nudge Up
NUDGEDOWN = -1 #Tempo Nudge Down
UNDO = -1 #Undo
REDO = -1 #Redo
LOOP = -1 #Loop on/off
PUNCHIN = -1 #Punch in
PUNCHOUT = -1 #Punch out
OVERDUB = -1 #Overdub on/off
METRONOME = -1 #Metronome on/off
RECQUANT = -1 #Record quantization on/off
DETAILVIEW = -1 #Detail view switch
CLIPTRACKVIEW = -1 #Clip/Track view switch

# Device Control
DEVICELOCK = -1 #Device Lock (lock "blue hand")
DEVICEONOFF = -1 #Device on/off
DEVICENAVLEFT = -1 #Device nav left
DEVICENAVRIGHT = -1 #Device nav right
DEVICEBANKNAVLEFT = -1 #Device bank nav left
DEVICEBANKNAVRIGHT = -1 #Device bank nav right
DEVICEBANK = (-1, #Bank 1 #All 8 banks must be assigned to positive values in order for bank selection to work
              -1, #Bank 2
              -1, #Bank 3
              -1, #Bank 4
              -1, #Bank 5
              -1, #Bank 6
              -1, #Bank 7
              -1, #Bank 8
              )

# Arrangement View Controls
SEEKFWD = -1 #Seek forward
SEEKRWD = -1 #Seek rewind

# Session Navigation (aka "red box")
SESSIONLEFT = 18 #Session left
SESSIONRIGHT = 19 #Session right
SESSIONUP = 0 #Session up
SESSIONDOWN = 127 #Session down
ZOOMUP = -1 #Session Zoom up
ZOOMDOWN = -1 #Session Zoom down
ZOOMLEFT = -1 #Session Zoom left
ZOOMRIGHT = -1 #Session Zoom right

# Track Navigation
TRACKLEFT = -1 #Track left
TRACKRIGHT = -1 #Track right

# Scene Navigation
SCENEUP = -1 #Scene down
SCENEDN = -1 #Scene up

# Scene Lau-1nch
SELSCENELAUNCH = -1 #Selected scene launch
SCENELAUNCH = (-1, #Scene 1 Launch
               -1, #Scene 2
               -1, #Scene 3
               -1, #Scene 4
               -1, #Scene 5
               )

# Clip Launch / Stop
SELCLIPLAUNCH = -1 #Selected clip launch
STOPALLCLIPS = -1 #Stop all clips

# 8x5 Matrix note assignments
# Track no.:     1   2   3   4   5   6   7   8
CLIPNOTEMAP = ((30, 31), #Row 1
               (32, 33), #Row 2
               (34, 35), #Row 3
               (36, 37))

DELETECLIPNOTEMAP = (38, 39)

# Track Control
MASTERSEL = -1 #Master track select
TRACKSTOP = (-1, #Track 1 Clip Stop
             -1)
TRACKSEL = (70, #Track 1 Select
           71, #Track 8
           )
TRACKMUTE = (88, #Track 1 On/Off
             89, #Track 2
             )
TRACKSOLO = (40,
            41,
            )
TRACKREC = (42, #Track 1 Solo
             43, #Track 2
             )

EQCUTS = ((58,56,54),
          (59,57,55),
         )

FILTER_ON = (8,9)

FX1_ON = (20,21)
FX2_ON = (22,23)


# Pad Translations for Drum Rack

PADCHANNEL = 0 # MIDI channel for Drum Rack notes
DRUM_PADS = (-1, -1, -1, -1, # MIDI note numbers for 4 x 4 Drum Rack
             -1, -1, -1, -1, # Mapping will be disabled if any notes are set to -1
             -1, -1, -1, -1, # Notes will be "swallowed" if already mapped elsewhere
             -1, -1, -1, -1,
             )

# Sliders / Knobs
# ---------------
# Valid CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments will be ignored

SLIDERCHANNEL = 0 #Channel assignment for all mapped CCs; valid range is 0 to 15
TEMPO_TOP = 180.0 # Upper limit of tempo control in BPM (max is 999)
TEMPO_BOTTOM = 100.0 # Lower limit of tempo control in BPM (min is 0)

TEMPOCONTROL = -1 #Tempo control CC assignment; control range is set above
MASTERVOLUME = -1 #Maser track volume
CUELEVEL = -1 #Cue level control
CROSSFADER = -1 #Crossfader control

TRACKVOL = (68, #Track 1 Volume
            69, #Track 2
            )
TRACKPAN = (-1, #Track 1 Pan
            -1, #Track 2 
            )
TRACKSENDA = (2, #Track 1 Send A
              3, #Track 2
              )
TRACKSENDB = (4, #Track 1 Send B
              5, #Track 2 
              )
TRACKSENDC = (6, #Track 1 Send C
              7, #Track 2
              
              )
PARAMCONTROL = (-1, #Param 1 #All 8 params must be assigned to positive values in order for param control to work
                -1, #Param 2
                -1, #Param 3
                -1, #Param 4
                -1, #Param 5
                -1, #Param 6
                -1, #Param 7
                -1, #Param 8
                )
EQGAINS = ((50,48,46),
           (51,49,47),
           )

FILTERS = ((0,-1),
           (1,-1),
           )

#Colors
BASE_COLOR_TABLE = ((115, 127, 127, 16726484),
 (124, 73, 127, 15810688),
 (3, 127, 118, 15549221),
 (0, 125, 127, 16712965),
 (81, 110, 114, 5538020),
 (85, 126, 127, 197631),
 (90, 115, 124, 8940772),
 (105, 115, 114, 14183652),
 (33, 100, 127, 8912743),
 (44, 124, 119, 1769263),
 (55, 119, 127, 2490280),
 (67, 110, 127, 6094824),
 (9, 125, 123, 16149507),
 (12, 107, 127, 16753961),
 (17, 120, 127, 16773172),
 (24, 118, 110, 14939139))


