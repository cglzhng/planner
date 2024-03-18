from enum import Enum

# A4 size in pt (horizontal)
A4_WIDTH = 842
A4_HEIGHT = 595

UNIT = 14
GRID_WIDTH = 28
GRID_HEIGHT = 40
MARGIN_X = 13
MARGIN_Y = 15

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
