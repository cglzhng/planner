from enum import Enum
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# A4 size in pt (horizontal)
A4_WIDTH = 842
A4_HEIGHT = 595

# constants
UNIT = 14
GRID_WIDTH = 28
GRID_HEIGHT = 40
MARGIN_X = 20
MARGIN_Y = 17

def insert_segment(line, segment):
	i = 0

	while i < len(line):
		if line[i].start > segment.start:
			break
		i = i + 1

	j = i

	while i > 0:
		# This segment overlaps with the segment at i - 1
		if line[i - 1].end >= segment.start: 
			if segment.start == line[i - 1].start:
				# This segment completely consumes the segment at i, so "combine"
				# And keep trying to combine segments
				i = i - 1
			elif line[i - 1].stroke != segment.stroke:
				# They are different stroke types, so break the segment at i - 1
				# And stop here since we can't combine anymore 
				line[i - 1].end = segment.start
				break
			else:
				# They are the same stroke type, so combine
				# And keep trying to combine segments
				segment.start = line[i - 1].start
				segment.end = max(line[i - 1].end, segment.end)
				i = i - 1
		else:
			break

	while j < len(line):
		# This segment overlaps with the segment at j
		if segment.end >= line[j].start:
			if segment.end >= line[j].end:
				# This segment completely consumes the segment at j, so "combine"
				# And keep trying to combine segments
				j = j + 1
			elif line[j].stroke != segment.stroke:
				# They are different stroke types, so break the segment at j
				# And stop here since we can't combine anymore
				line[j].start = segment.end
				break
			else:	
				# They are the same stroke type, so combine
				# And keep trying to combine segments
				segment.end = max(line[j].end, segment.end)
				j = j + 1
		else:
			break

	# we want the line to contain [0, i) and [j, len(line))
	# and insert the new segment at i

	diff = j - i
	for x in range(j, len(line)):
		line[x - diff] = line[x]
	
	line.insert(i, segment)
	del line[len(line) - diff:]

def test_insert_segment():
	t = [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 5),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.LIGHT, 4, 8))
	eprint(t)

	t = [
		Segment(Stroke.LIGHT, 3, 5),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.LIGHT, 1, 17))
	eprint(t)

	t = [
		Segment(Stroke.LIGHT, 1, 3),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.LIGHT, 3, 6))
	eprint(t)

	t = [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 5),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.LIGHT, 10, 13))
	eprint(t)

	t = [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 5),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.DARK, 4, 9))
	eprint(t)

	t = [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 4),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.DARK, 1, 5))
	eprint(t)

	t = [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 4),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.DARK, 9, 17))
	eprint(t)

	t = [
		Segment(Stroke.DARK, 1, 2),
		Segment(Stroke.LIGHT, 3, 4),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.DARK, 12, 16),
	]
	insert_segment(t, Segment(Stroke.DARK, 2, 13))
	eprint(t)

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

def print_stroke(stroke):
	if stroke == Stroke.LIGHT:
		print("LIGHT")
	if stroke == Stroke.DARK:
		print("DARK")

def print_line(x1, y1, x2, y2):
	print(f"{x1} {y1} {x2} {y2} LINE")

def print_text_horizontal(text, size, x, y):
	print(f"{-x} {-y} ({text}) {x} {y} /Iosevka findfont {size} scalefont setfont T_HORIZ")

def print_preamble():
	print( """
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
/LINE { moveto lineto } def
/LIGHT { [0.30 1.10] 0.15 setdash stroke } def
/DARK { [0.30 0.70] 0.15 setdash stroke } def
/T_HORIZ {
translate
270 rotate
0 0 moveto
show
90 rotate
translate
} def
""")

"""
		print(f"/Iosevka findfont")
		print(f"{self.size} scalefont")
		print(f"setfont")
		print(f"{x_real} {y_real} translate")
		print(f"270 rotate")
		print(f"0 0 moveto")
		print(f"({self.text}) show")
		print(f"90 rotate")
		print(f"{-x_real} {-y_real} translate")
"""

class Segment(object):
	def __init__(self, stroke, start, end):
		self.stroke = stroke
		self.start = start
		self.end = end
	
	def __repr__(self):
		return f"{self.stroke} [{self.start}, {self.end}]"

class Grid(object):
	def __init__(self):
		self.horizontal = [[] for i in range(0, GRID_HEIGHT + 1)]
		self.vertical = [[] for i in range(0, GRID_WIDTH + 1)]

	def add_horizontal_segment(self, row, start, end, stroke):
		insert_segment(self.horizontal[row], Segment(stroke, start, end))

	def add_vertical_segment(self, column, start, end, stroke):
		insert_segment(self.vertical[column], Segment(stroke, start, end))

	def render(self, x, y):
		x_real = y
		y_real = A4_WIDTH - x - GRID_WIDTH * UNIT 
		# vertical lines get printed as horizontal
		# they are also printed top-to-bottom
		for i, line in enumerate(self.vertical):
			for segment in line:
				if segment.stroke == Stroke.BLANK:
					continue
				print_line(
					segment.start * UNIT + x_real,
					(len(self.vertical) - i - 1) * UNIT + y_real,
					segment.end * UNIT + x_real,
					(len(self.vertical) - i - 1) * UNIT + y_real,
				)
				print_stroke(segment.stroke)

		# horizontal lines get printed as vertical	
		for i, line in enumerate(self.horizontal):
			for segment in line:
				if segment.stroke == Stroke.BLANK:
					continue
				print_line(
					i * UNIT + x_real,
					segment.start * UNIT + y_real,
					i * UNIT + x_real, 
					segment.end * UNIT + y_real,
				)
				print_stroke(segment.stroke)

class Text(object):
	def __init__(self, text, size, x, y, orientation=Orientation.HORIZONTAL):
		self.text = text
		self.size = size
		self.x = x
		self.y = y
		self.orientation = orientation
	
	def render(self, rx, ry):
		x_real = ry + self.y
		y_real = A4_WIDTH - rx - self.x

		print_text_horizontal(self.text, self.size, x_real, y_real)
			

class Page(object):
	def __init__(self):
		self.grid = Grid()
		self.text = []
	
	def render(self, side, num=None):
		if side == Side.LEFT:
			x = MARGIN_X
			y = MARGIN_Y
		if side == Side.RIGHT:
			x = A4_WIDTH - MARGIN_X - GRID_WIDTH * UNIT
			y = MARGIN_Y

		self.grid.render(x, y)

		if num is not None:
			if side == Side.LEFT:
				Text(str(num), 9, 0, 4).render(x, y)
			if side == Side.RIGHT:
				Text(str(num), 9, (GRID_WIDTH - 1) * UNIT, 4).render(x, y)

		for t in self.text:
			t.render(x, y)

# grid with r rows and c columns
# hobonichi secret line at column s
def make_blank_grid_with_secret(r, c, s):
	page = Page()

	# horizontal lines	
	page.grid.add_horizontal_segment(0, 0, c, Stroke.DARK)
	for i in range(1, r):
		page.grid.add_horizontal_segment(i, 0, c, Stroke.LIGHT)
	page.grid.add_horizontal_segment(r, 0, c, Stroke.DARK)

	# vertical lines
	page.grid.add_vertical_segment(0, 0, r, Stroke.DARK)
	for i in range(1, c):
		page.grid.add_vertical_segment(i, 0, r, Stroke.LIGHT)
	page.grid.add_vertical_segment(s, 0, r, Stroke.DARK)
	page.grid.add_vertical_segment(c, 0, r, Stroke.DARK)
	
	return page

def render_two_grids_on_a4(g1, g2):
	g1.render(Side.LEFT, 119)
	g2.render(Side.RIGHT)

print_preamble()

print("""
newpath
0 0 0 1 setcmykcolor
0.12 setlinewidth
""")

grid = make_blank_grid_with_secret(GRID_HEIGHT, GRID_WIDTH, 7)
render_two_grids_on_a4(grid, grid)

print(
"""
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
