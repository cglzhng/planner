from enum import Enum

# Size in pt (horizontal)
A4_WIDTH = 842
A4_HEIGHT = 595
A5_WIDTH = 595
A5_HEIGHT = 420

class PaperSize(Enum):
	A5 = 1
	A6 = 2

BOOK_SIZE = PaperSize.A6

match BOOK_SIZE:
	case PaperSize.A5:
		PAPER_WIDTH = A4_WIDTH
		PAPER_HEIGHT = A4_HEIGHT
		UNIT = 12
		GRID_WIDTH = 32
		GRID_HEIGHT = 46
		MARGIN_X_TOP_SHEET = 22
		MARGIN_Y_TOP_SHEET = 15
		MARGIN_X_BOTTOM_SHEET = 22
		MARGIN_Y_BOTTOM_SHEET = 25
		MARGIN_GAP = 28
		CALENDAR_DAY_WIDTH = 8
		CALENDAR_DAY_HEIGHT = 7
	case PaperSize.A6:
		PAPER_WIDTH = A5_WIDTH
		PAPER_HEIGHT = A5_HEIGHT
		UNIT = 12
		GRID_WIDTH = 22
		GRID_HEIGHT = 32
		MARGIN_X_TOP_SHEET = 18
		MARGIN_Y_TOP_SHEET = 15
		MARGIN_X_BOTTOM_SHEET = 18
		MARGIN_Y_BOTTOM_SHEET = 25
		MARGIN_GAP = 20
		CALENDAR_DAY_WIDTH = 5
		CALENDAR_DAY_HEIGHT = 5

class Stroke(Enum):
	BLANK = 1
	LIGHT = 2
	DARK = 3

class Orientation(Enum):
	HORIZONTAL = 1
	VERTICAL = 2

class Side(Enum):
	LEFT = 1
	RIGHT = 2
	TOP = 3
	BOTTOM = 4

class Color(object):
	def __init__(self, c, m, y, k):
		self.c = c
		self.m = m
		self.y = y
		self.k = k

BLACK = Color(0, 0, 0, 1)
LIGHT_PURPLE = Color(0.40, 0.40, 0, 0)

SMALL_TEXT_SIZE = 7

class Weekday(Enum):
	MONDAY = 1
	TUESDAY = 2
	WEDNESDAY = 3
	THURSDAY = 4
	FRIDAY = 5
	SATURDAY = 6 
	SUNDAY = 7

Fonts = {
	"Iosevka": {
		"Tiny": {
			"size": 7,
			"width_ratio": 1 / 2,
			"height_ratio": 6 / 7,
		},
		"Small": {
			"size": 9,
			"width_ratio": 1 / 2,
			"height_ratio": 5 / 7,
		},
	},
}

FONT_FILE = "iosevka-regular.t42"
FONT = Fonts["Iosevka"]
