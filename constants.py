from PIL import ImageFont
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
	"darker": "[0.20 0.10] 0.10",
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

class Align(Enum):
	START = 1
	CENTER = 2
	END = 3

class Color(object):
	def __init__(self, c, m, y, k):
		self.c = c
		self.m = m
		self.y = y
		self.k = k

BLACK = Color(0, 0, 0, 255)
BLUE = Color(0.75, 0.4, 0, 0)
LIGHT_BLUE = Color(0.4, 0.25, 0, 0)
PURPLE = Color(0.3, 0.8, 0, 0)
LIGHT_PURPLE = Color(0.25, 0.45, 0, 0)
LIGHT_GREEN = Color(0.45, 0, 0.50, 0)
LIGHT_ORANGE = Color(0, 0.4, 0.6, 0)
LIGHT_RED = Color(0, 0.3, 0.2, 0)
RED = Color(0, 0.75, 0.5, 0)
BRIGHT_RED = Color(0, 0.8, 0.8, 0)
BLUE_GRAY = Color(0.2, 0, 0, 0.4)
BROWN = Color(0, 0.4, 0.7, 0.2)
TEAL = Color(0.8, 0, 0.3, 0)
ORANGE = Color(0, 0.4, 0.8, 0)
GREEN = Color(0.4, 0, 0.8, 0)
WHITE = Color(0, 0, 0, 0)

PAGE_NUM_COLOR = LIGHT_BLUE

class Weekday(Enum):
	MONDAY = 1
	TUESDAY = 2
	WEDNESDAY = 3
	THURSDAY = 4
	FRIDAY = 5
	SATURDAY = 6
	SUNDAY = 7

WEEKDAYS = [e for e in Weekday]

WEEKDAY_NAMES = {
	Weekday.MONDAY.value: {
		"long": "Monday",
		"short": "Mon",
	},
	Weekday.TUESDAY.value: {
		"long": "Tuesday",
		"short": "Tue",
	},
	Weekday.WEDNESDAY.value: {
		"long": "Wednesday",
		"short": "Wed",
	},
	Weekday.THURSDAY.value: {
		"long": "Thursday",
		"short": "Thu",
	},
	Weekday.FRIDAY.value: {
		"long": "Friday",
		"short": "Fri",
	},
	Weekday.SATURDAY.value: {
		"long": "Saturday",
		"short": "Sat",
	},
	Weekday.SUNDAY.value: {
		"long": "Sunday",
		"short": "Sun",
	},
}

class Month(Enum):
	JANUARY = 1
	FEBRUARY = 2
	MARCH = 3
	APRIL = 4
	MAY = 5
	JUNE = 6 
	JULY = 7
	AUGUST = 8
	SEPTEMBER = 9
	OCTOBER = 10
	NOVEMBER = 11
	DECEMBER = 12

SV_CALENDAR_SPEC = {
	"months": {
		"Spring": {
			"name": "Spring",
			"short": "Spring",
			"days": 28,
		},
		"Summer": {
			"name": "Summer",
			"short": "Summer",
			"days": 28,
		},
		"Fall": {
			"name": "Fall",
			"short": "Fall",
			"days": 28,
		},
		"Winter": {
			"name": "Winter",
			"short": "Winter",
			"days": 28,
		},
	},
	"start_year": 1,
	"start_month": "Spring",
	"start_day": 1,
	"start_weekday": Weekday.MONDAY,
}


FONTS = {
	"Cooper Hewitt": {
		"Styles": {
			"Regular": {
				"name": "CooperHewitt-Book",
				"ttf": "fonts/cooperhewitt-book.ttf",
				"t42": "fonts/cooperhewitt-book.t42",
			},
		},
		"Sizes": {
			"Tinier": 5,
			"Tiny": 6,
			"Small": 8,
			"Medium": 10,
			"Big": 14,
			"Huge": 18,
		},
		"LineHeights": {
			"Tinier": 1.2,
			"Tiny": 1.5,
			"Small": 2,
			"Medium": 1.5,
			"Big": 1.5,
			"Huge": 1.5,
		},
	},
	"IBM Plex Sans": {
		"Styles": {
			"Regular": {
				"name": "IBMPlexSans-Regular",
				"ttf": "fonts/ibmplexsans-regular.ttf",
				"t42": "fonts/ibmplexsans-regular.t42",
			},
		},
		"Sizes": {
			"Tinier": 6,
			"Tiny": 7,
			"Small": 9,
			"Medium": 11,
			"Big": 14,
			"Huge": 18,
		},
		"LineHeights": {
			"Tinier": 1.5,
			"Tiny": 1.5,
			"Small": 2,
			"Medium": 1.5,
			"Big": 1.5,
			"Huge": 1.5,
		},
	},
	"Fira Sans": {
		"Styles": {
			"Regular": {
				"name": "FiraSans-Regular",
				"ttf": "fonts/firasans-regular.ttf",
				"t42": "fonts/firasans-regular.t42",
			},
			"Italic": {
				"name": "FiraSans-Italic",
				"ttf": "fonts/firasans-italic.ttf",
				"t42": "fonts/firasans-italic.t42",
			},
		},
		"Sizes": {
			"Tinier": 6,
			"Tiny": 7,
			"Small": 9,
			"Medium": 11,
			"Big": 14,
			"Huge": 18,
		},
		"LineHeights": {
			"Tinier": 1.5,
			"Tiny": 1.5,
			"Small": 2,
			"Medium": 1.5,
			"Big": 1.5,
			"Huge": 1.5,
		},
	},
	"Iosevka": {
		"Styles": {
			"Regular": {
				"name": "PlannerFont",
				"t42": "fonts/iosevka-regular.t42",
				"ttf": "fonts/iosevka-regular.ttf",
			},
		},
		"Sizes": {
			"Tinier": 6,
			"Tiny": 7,
			"Small": 9,
			"Medium": 11,
			"Big": 14,
			"Huge": 18,
		},
		"LineHeights": {
			"Tinier": 1.5,
			"Tiny": 1.5,
			"Small": 1.5,
			"Medium": 1.5,
			"Big": 1.5,
			"Huge": 1.5,
		},
	},
}

FONT_RENDER_SIZE = 100

FONT = FONTS["Cooper Hewitt"]

for style in FONT["Styles"]:
	FONT["Styles"][style]["PILFont"] = ImageFont.truetype(FONT["Styles"][style]["ttf"], FONT_RENDER_SIZE)

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
		CALENDAR_HEADER_TEXT = "Small"
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
		CALENDAR_HEADER_TEXT = "Small"
		WEEK_DAY_HEIGHT = 9
		WEEK_DAY_WIDTH = 24
