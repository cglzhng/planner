from enum import Enum
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# A4 size in pt
WIDTH = 595
HEIGHT = 842

# constants
UNIT = 14
GRID_WIDTH = 28
GRID_HEIGHT = 40

class Stroke(Enum):
	BLANK = 1
	LIGHT = 2
	DARK = 3

class Segment(object):
	def __init__(self, stroke, start, end):
		self.stroke = stroke
		self.start = start
		self.end = end

class Grid(object):
	def __init__(self):
		self.horizontal = [[] for i in range(0, GRID_HEIGHT + 1)]
		self.vertical = [[] for i in range(0, GRID_WIDTH + 1)]

	def add_horizontal_segment(self, row, start, end, stroke):
		self.horizontal[row].append(Segment(stroke, start, end))

	def add_vertical_segment(self, column, start, end, stroke):
		self.vertical[column].append(Segment(stroke, start, end))

	def print(self, x, y):
		x_real = y
		y_real = HEIGHT - x - (len(self.vertical) - 1) * UNIT 
		# vertical lines get printed as horizontal
		for i, line in enumerate(self.vertical):
			for segment in line:
				if segment.stroke == Stroke.BLANK:
					continue
				print(f"{segment.start * UNIT + x_real} {i * UNIT + y_real} moveto")
				print(f"{segment.end * UNIT + x_real} {i * UNIT + y_real} lineto")
				if segment.stroke == Stroke.LIGHT:
					print(f"[0.30 1.10] 0.15 setdash")
				if segment.stroke == Stroke.DARK:
					print(f"[0.30 0.70] 0.15 setdash")
				print("stroke")

		# horizontal lines get printed as vertical	
		for i, line in enumerate(self.horizontal):
			for segment in line:
				if segment.stroke == Stroke.BLANK:
					continue
				print(f"{i * UNIT + x_real} {segment.start * UNIT + y_real} moveto")
				print(f"{i * UNIT + x_real} {segment.end * UNIT + y_real} lineto")
				if segment.stroke == Stroke.LIGHT:
					print(f"[0.30 1.10] 0.15 setdash")
				if segment.stroke == Stroke.DARK:
					print(f"[0.30 0.70] 0.15 setdash")
				print("stroke")

# grid with r rows and c columns
# hobonichi secret line at column s
def make_blank_grid(r, c, s):
	grid = Grid()

	# horizontal lines	
	for i in range(0, r + 1):
		grid.add_horizontal_segment(i, 0, c, Stroke.LIGHT)

	# vertical lines
	for i in range(0, c + 1):
		if (i == s):
			grid.add_vertical_segment(i, 0, r, Stroke.DARK)
		else:
			grid.add_vertical_segment(i, 0, r, Stroke.LIGHT)
	
	return grid



print(
"""
%!PS-Adobe-3.0
%%BoundingBox: 24 24 571 818
%%Orientation: Portrait
%%Pages: (atend)
%%DocumentMedia: A4 595 842 0 () ()
%%DocumentNeededResources: (atend)
%%EndComments
%%BeginPageSetup
<< /PageSize [595 842] >> setpagedevice
%%EndPageSetup
"""
)

print("""
newpath
0 0 0 1 setcmykcolor
0.12 setlinewidth
""")

grid = make_blank_grid(40, 28, 21)
grid.print(20, 17)
grid.print(430, 17)

print(
"""
stroke
showpage
"""
)

print(
"""
%%Trailer
%%Pages: 1
%%DocumentNeededResources: font Courier-Bold Courier 
%%EOF
"""
)
