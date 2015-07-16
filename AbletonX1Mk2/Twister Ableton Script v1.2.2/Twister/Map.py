CHANNEL = 1		#main channel (0 - 15)

TW_BUTTONS = [4, 5, 6, 7, 8, 9, 10, 11, 100, 101, 102, 103, 24, 25, 26, 27, 12, 13, 14, 15, 0, 1, 2, 3, 68, 69, 70, 71, 28, 29, 30, 31]  #there are 16x2 of these

TW_GRID = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]	#there are 4x4 of these

TW_FADERS = [12, 13, 14, 15, 28, 29, 30, 31]		#there are 8 of these

TW_KNOBS_LEFT = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]	#there are 12 of these

TW_KNOBS_RIGHT = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]		#there are 12 of these

TW_DIALS = [100, 101, 102, 103, 16, 17, 18, 19, 20, 21, 22, 23]		#there are 12 of these

TW_DIAL_BUTTONS = [100, 101, 102, 103, 16, 17, 18, 19, 20, 21, 22, 23]		#there are 12 of these

BACKLIGHT_TYPE = ['static', 'pulse', 'up', 'down']	#this assigns the backlight mode for left_shift_modes 1-4.	If 'static', the value below will be used

BACKLIGHT_VALUE = [127, 96, 64, 32]		#this assigns the led intensity for the backlight if it is in 'static' mode for left_shift_modes 1-4

PAD_TRANSLATION =	((0, 0, 0, 9), (0, 1, 1, 9), (0, 2, 2, 9), (0, 3, 3, 9),		#this is used by DrumRacks to translate input to one of the visible grid squares for triggering
					(1, 0, 4, 9), (1, 1, 5, 9), (1, 2, 6, 9), (1, 3, 7, 9),			#the format is (x position, y position, note-number, channel)
					(2, 0, 8, 9), (2, 1, 9, 9), (2, 2, 10, 9), (2, 3, 11, 9),
					(3, 0, 12, 9), (3, 1, 13, 9), (3, 2, 14, 9), (3, 3, 15, 9))
					
OHM_MAP_ID = [[0, 1, 2, 3, 4, 5, 6, 7],		#these are the notenumbers for the grid when in Livid_Mode
			[8, 9, 10, 11, 12, 13, 14, 15],
			[16, 17, 18 , 19, 20, 21, 22, 23],
			[24, 25, 26, 27, 28, 29, 30, 31],
			[32, 33, 34, 35, 36, 37, 38, 39],
			[40, 41, 42, 43, 44, 45, 46, 47],
			[48, 49, 50, 51, 52, 53, 54, 55],
			[56, 57, 58, 59, 60, 61, 62, 63]]
			
OHM_MAP_CHANNEL = [[15, 15, 15, 15, 15, 15, 15, 15],		#these are the channels for each grid square in Livid_Mode
				[15, 15, 15, 15, 15, 15, 15, 15],
				[15, 15, 15, 15, 15, 15, 15, 15],
				[15, 15, 15, 15, 15, 15, 15, 15],
				[15, 15, 15, 15, 15, 15, 15, 15],
				[15, 15, 15, 15, 15, 15, 15, 15],
				[15, 15, 15, 15, 15, 15, 15, 15],
				[15, 15, 15, 15, 15, 15, 15, 15]]
				
OHM_MAP_VALUE = [[4, 8, 5, 2, 0, 3, 0, 6],			#these are the values that are lit up in Livid_Mode
				[8, 4, 2, 0, 2, 0, 3, 0],
				[5, 2, 0, 3, 0, 2, 0, 3], 
				[2, 0, 3, 0, 1, 0, 2, 0],
				[0, 2, 0, 1, 0, 3, 0, 2], 
				[3, 0, 2, 0, 3, 0, 2, 5],
				[0, 3, 0, 2, 0, 2, 4, 8], 
				[6, 0, 3, 0, 2, 5, 8, 4]]

FOLLOW = True		#this sets whether or not the last selected device on a track is selected for editing when you select a new track

CHOPPER_ENABLE = False		#when set True, this enables the Python ClipChopperComponent in modSlot 4 when a mod isn't present there

#  These are the values for the track offset used for RIGHT_MIXER_MODEs 1-3:

RIGHT_MODE_OFFSETS = [4, 8, 12]

# TWISTER COLORS
# Orange = 66
# Blue = 3
# Cyan = 24
# Green = 48
# Red = 84
# Yellow = 61
# Magenta = 93
# Pink = 103
# Purple = 112

COLOR_MAP = [66, 61, 24, 93, 84, 48, 3]

#	In addition, there are two further color maps that are used depending on whether the RGB or Monochrome 
#		Ohm64 is detected.	The first number is the color used by the RGB (from the ordering in the COLOR_MAP array),
#		the second the Monochrome.	Obviously the Monochrome doesn't use the colors.  
#	However, the flashing status of a color is derived at by modulus.  Thus 1-7 are the raw colors, 8-14 are a fast
#		flashing color, 15-21 flash a little slower, etc.  You can assign your own color maps here:
###	 the first number is Livid(OhmModes) standard, the second is Monomdular standard, the third is Monochrome

MUTE = [2, 2, 7]
SOLO = [3, 9, 127]
ARM = [13, 5, 8]
SEND_RESET = [1, 7, 7]
STOP_CLIPS = [127, 1, 1]
STOP_CLIPS_OFF = [127, 127, 127]
SELECT = [2, 2, 127]
SCENE_LAUNCH = [8, 3, 17]
USER1_COLOR = [4, 4, 29]
USER2_COLOR = [5, 5, 29]
USER3_COLOR = [6, 6, 29]
CROSSFADE_TOGGLE = [4, 4, 127]
TRACK_STOP = [127, 127, 127]
DEVICE_SELECT = [1, 1, 8]
BANK_BUTTONS = [1, 1, 1]
STOP_ALL = [127, 127, 15]
SESSION_NAV = [2, 2, 32]
SESSION_NAV_OFF = [3, 3, 33]
OVERDUB = [4, 4, 127]
LOOP = [3, 3, 127]
STOP = [127, 127, 127]
STOP_OFF = [127, 127, 127]
RECORD = [0, 5, 15]
RECORD_ON = [16, 11, 15]
PLAY = [6, 6, 127]
PLAY_ON = [16, 18, 127]
DEVICE_BANK = [127, 127, 127]
DEVICE_NAV = [1, 1, 127]
DEVICE_ON = [2, 127, 127]
DEVICE_LOCK = [4, 4, 127]
CLIP_RECORDING = [5, 11, 8] 
CLIP_STARTED = [6, 6, 32]
CLIP_STOP = [1, 127, 127]
CLIP_TRG_REC = [12, 4, 8]
CLIP_TRG_PLAY = [13, 2, 15]
ZOOM_STOPPED = [1, 127, 127]
ZOOM_PLAYING = [6, 6, 15]
ZOOM_SELECTED = [9, 1, 8]
STOP_CLIP = [127, 127, 2]
