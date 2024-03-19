from enum import Enum

# A4 size in pt (horizontal)
A4_WIDTH = 842
A4_HEIGHT = 595

UNIT = 12
GRID_WIDTH = 32
GRID_HEIGHT = 46
MARGIN_X_TOP_SHEET = 22
MARGIN_Y_TOP_SHEET = 22
MARGIN_X_BOTTOM_SHEET = 22
MARGIN_Y_BOTTOM_SHEET = 22

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
