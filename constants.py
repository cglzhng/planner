from enum import Enum

# Size in pt (horizontal)
A4_WIDTH = 842
A4_HEIGHT = 595
A5_WIDTH = 595
A5_HEIGHT = 420

class PaperSize(Enum):
	A4 = "A4"
	A5 = "A5"
	A6 = "A6"

PAPERS = {
	"A4": {
		"name": "A4",
		"height": 842,
		"width": 595,
	},
	"A5": {
		"name": "A5",
		"width": 595,
		"height": 420,
	},
}


class Stroke(Enum):
	BLANK = "blank"
	LIGHT = "light"
	DARK = "dark"
	DARKER = "darker"
	SOLID = "solid"

STROKES = {}

STROKES[12] = {
	"light": "[0.20 0.80] 0.10",
	"dark": "[0.20 0.40] 0.10",
}

STROKES[10.5] = {
	"light": "[0.20 0.85] 0.10",
	"dark": "[0.30 0.45] 0.15",
	"darker": "[0.20 0.10] 0.10",
}

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

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

FONTS = {
	"Iosevka": {
		"Tiny": {
			"size": 7,
			"width_ratio": 1 / 2,
			"height_ratio": 5 / 7,
		},
		"Small": {
			"size": 9,
			"width_ratio": 1 / 2,
			"height_ratio": 5 / 7,
		},
	},
}

FONT_FILE = "iosevka-regular.t42"
FONT = FONTS["Iosevka"]

BOOK_SIZE = PaperSize.A6

match BOOK_SIZE:
	case PaperSize.A5:
		PAPER = PAPERS["A4"]
		PAPER_ORIENTATION = Orientation.HORIZONTAL
		UNIT = 12
		GRID_WIDTH = 32
		GRID_HEIGHT = 45
		PAGE_ROWS = 1
		PAGE_COLS = 2
		GAP_ROW = 0
		GAP_COL = 28
		CALENDAR_DAY_WIDTH = 8
		CALENDAR_DAY_HEIGHT = 7
		CALENDAR_HEADER_HEIGHT = 2
		CALENDAR_HEADER_TEXT = FONT["Small"]
	case PaperSize.A6:
		PAPER = PAPERS["A4"]
		PAPER_ORIENTATION = Orientation.VERTICAL
		UNIT = 10.5
		GRID_WIDTH = 24
		GRID_HEIGHT = 36
		PAGE_ROWS = 2
		PAGE_COLS = 2
		GAP_ROW = 0
		GAP_COL = 0
		CALENDAR_DAY_WIDTH = 6
		CALENDAR_DAY_HEIGHT = 6
		CALENDAR_HEADER_HEIGHT = 2
		CALENDAR_HEADER_TEXT = FONT["Small"]
		WEEK_DAY_HEIGHT = 9
		WEEK_DAY_WIDTH = 24
