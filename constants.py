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

BLACK = Color(0, 0, 0, 1)
LIGHT_PURPLE = Color(0.40, 0.40, 0, 0)
WHITE = Color(0, 0, 0, 0)

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
	Weekday.MONDAY.value: "Monday",
	Weekday.TUESDAY.value: "Tuesday",
	Weekday.WEDNESDAY.value: "Wednesday",
	Weekday.THURSDAY.value: "Thursday",
	Weekday.FRIDAY.value: "Friday",
	Weekday.SATURDAY.value: "Saturday",
	Weekday.SUNDAY.value: "Sunday",
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

MONTHS = [e for e in Month]

MONTH_NAMES = {
	Month.JANUARY.value: "January",
	Month.FEBRUARY.value: "February",
	Month.MARCH.value: "March",
	Month.APRIL.value: "April",
	Month.MAY.value: "May",
	Month.JUNE.value: "June",
	Month.JULY.value: "July",
	Month.AUGUST.value: "August",
	Month.SEPTEMBER.value: "September",
	Month.OCTOBER.value: "October",
	Month.NOVEMBER.value: "November",
	Month.DECEMBER.value: "December",
}

MONTH_NAMES_SHORT = {
	Month.JANUARY.value: "Jan",
	Month.FEBRUARY.value: "Feb",
	Month.MARCH.value: "Mar",
	Month.APRIL.value: "Apr",
	Month.MAY.value: "May",
	Month.JUNE.value: "Jun",
	Month.JULY.value: "Jul",
	Month.AUGUST.value: "Aug",
	Month.SEPTEMBER.value: "Sep",
	Month.OCTOBER.value: "Oct",
	Month.NOVEMBER.value: "Nov",
	Month.DECEMBER.value: "Dec",
}

MONTH_DAYS = {
	Month.JANUARY.value: 31,
	Month.FEBRUARY.value: 28,
	Month.MARCH.value: 31,
	Month.APRIL.value: 30,
	Month.MAY.value: 31,
	Month.JUNE.value: 30,
	Month.JULY.value: 31,
	Month.AUGUST.value: 31,
	Month.SEPTEMBER.value: 30,
	Month.OCTOBER.value: 31,
	Month.NOVEMBER.value: 30,
	Month.DECEMBER.value: 31,
}

FONTS = {
	"Iosevka": {
		"Tinier": {
			"size": 6,
			"width_ratio": 1 / 2,
			"height_ratio": 5 / 7,
		},
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
		"Medium": {
			"size": 11,
			"width_ratio": 1 / 2,
			"height_ratio": 5 / 7,
		},
		"Big": {
			"size": 14,
			"width_ratio": 1 / 2,
			"height_ratio": 5 / 7,
		},
		"Huge": {
			"size": 16,
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
