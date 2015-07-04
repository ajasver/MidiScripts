# http://remotescripts.blogspot.com
# hanz.petrov@gmail.com
# Note and CC Mappings for the FCB1020 script (APC emulation) are defined in this file
# Values may be edited with any text editor (but avoid using tabs for indentation)

# Combination Mode offsets
# ------------------------

TRACK_OFFSET = -1 #offset from the left of linked session origin; set to -1 for auto-joining of multiple instances
SCENE_OFFSET = 0 #offset from the top of linked session origin (no auto-join)

# Buttons / Pads
# -------------
# Valid Note/CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments are permitted

BUTTONCHANNEL = 0 #Channel assignment for all mapped buttons/pads; valid range is 0 to 15
MESSAGETYPE = 0 #Message type for buttons/pads; set to 0 for MIDI Notes, 1 for CCs.
        #When using CCs for buttons/pads, set BUTTONCHANNEL and SLIDERCHANNEL to different values.

# General
PLAY = 7 #Global play
STOP = 8 #Global stop
REC = 9 #Global record
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
DEVICELOCK = 99 #Device Lock (lock "blue hand")
DEVICEONOFF = 94 #Device on/off
DEVICENAVLEFT = 92 #Device nav left
DEVICENAVRIGHT = 93 #Device nav right
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
SESSIONLEFT = 95 #Session left
SESSIONRIGHT = 96 #Session right
SESSIONUP = -1 #Session up
SESSIONDOWN = -1 #Session down
ZOOMUP = 97 #Session Zoom up
ZOOMDOWN = 98 #Session Zoom down
ZOOMLEFT = -1 #Session Zoom left
ZOOMRIGHT = -1 #Session Zoom right

# Track Navigation
TRACKLEFT = 90 #Track left
TRACKRIGHT = 91 #Track right

# Scene Navigation
SCENEUP = -1 #Scene down
SCENEDN = -1 #Scene up

# Scene Launch
SELSCENELAUNCH = -1 #Selected scene launch
SCENELAUNCH = (0, #Scene 1 Launch
               1, #Scene 2
               2, #Scene 3
               3, #Scene 4
               4, #Scene 5
               )

# Clip Launch / Stop
SELCLIPLAUNCH = 94 #Selected clip launch
STOPALLCLIPS = 5 #Stop all clips

# 8x5 Matrix note assignments
# Track no.:     1   2   3   4   5   6   7   8
CLIPNOTEMAP = ((10, 20, 30, 40, 50, 60, 70, 80), #Row 1
               (11, 21, 31, 41, 51, 61, 71, 81), #Row 2
               (12, 22, 32, 42, 52, 62, 72, 82), #Row 3
               (13, 23, 33, 43, 53, 63, 73, 83), #Row 4
               (14, 24, 34, 44, 54, 64, 74, 84), #Row 5
               )

# Track Control
MASTERSEL = 6 #Master track select
TRACKSTOP = (15, #Track 1 Clip Stop
             25, #Track 2
             35, #Track 3
             45, #Track 4
             55, #Track 5
             65, #Track 6
             75, #Track 7
             85, #Track 8
             )
TRACKSEL = (16, #Track 1 Select
            26, #Track 2
            36, #Track 3
            46, #Track 4
            56, #Track 5
            66, #Track 6
            76, #Track 7
            86, #Track 8
            )
TRACKMUTE = (17, #Track 1 On/Off
             27, #Track 2
             37, #Track 3
             47, #Track 4
             57, #Track 5
             67, #Track 6
             77, #Track 7
             87, #Track 8
             )
TRACKSOLO = (18, #Track 1 Solo
             28, #Track 2
             38, #Track 3
             48, #Track 4
             58, #Track 5
             68, #Track 6
             78, #Track 7
             88, #Track 8
             )
TRACKREC = (19, #Track 1 Record
            29, #Track 2
            39, #Track 3
            49, #Track 4
            59, #Track 5
            69, #Track 6
            79, #Track 7
            89, #Track 8
            )


# Pad Translations for Drum Rack

PADCHANNEL = 0 # MIDI channel for Drum Rack notes
DRUM_PADS = (-1, 11, 12, 13, # MIDI note numbers for 4 x 4 Drum Rack
             14, 15, 16, 17, # Mapping will be disabled if any notes are set to -1
             18, 19, 20, 21, # Notes will be "swallowed" if already mapped elsewhere
             22, 23, 24, 25,
             )

# Sliders / Knobs
# ---------------
# Valid CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments will be ignored

SLIDERCHANNEL = 0 #Channel assignment for all mapped CCs; valid range is 0 to 15
TEMPO_TOP = 180.0 # Upper limit of tempo control in BPM (max is 999)
TEMPO_BOTTOM = 100.0 # Lower limit of tempo control in BPM (min is 0)

TEMPOCONTROL = 0 #Tempo control CC assignment; control range is set above
MASTERVOLUME = 1 #Master track volume
CUELEVEL = -1 #Cue level control
CROSSFADER = -1 #Crossfader control

TRACKVOL = (3, #Track 1 Volume
            5, #Track 2
            7, #Track 3
            9, #Track 4
            11, #Track 5
            13, #Track 6
            15, #Track 7
            17, #Track 8
            )
TRACKPAN = (-1, #Track 1 Pan
            -1, #Track 2
            -1, #Track 3
            -1, #Track 4
            -1, #Track 5
            -1, #Track 6
            -1, #Track 7
            -1, #Track 8
            )
TRACKSENDA = (2, #Track 1 Send A
              4, #Track 2
              6, #Track 3
              8, #Track 4
              10, #Track 5
              12, #Track 6
              14, #Track 7
              16, #Track 8
              )
TRACKSENDB = (-1, #Track 1 Send B
              -1, #Track 2
              -1, #Track 3
              -1, #Track 4
              -1, #Track 5
              -1, #Track 6
              -1, #Track 7
              -1, #Track 8
              )
TRACKSENDC = (-1, #Track 1 Send C
              -1, #Track 2
              -1, #Track 3
              -1, #Track 4
              -1, #Track 5
              -1, #Track 6
              -1, #Track 7
              -1, #Track 8
              )
PARAMCONTROL = (18, #Param 1 #All 8 params must be assigned to positive values in order for param control to work
                19, #Param 2
                20, #Param 3
                21, #Param 4
                22, #Param 5
                23, #Param 6
                24, #Param 7
                25, #Param 8
                )