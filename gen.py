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
		print(f"[0.30 1.10] 0.15 setdash")
	if stroke == Stroke.DARK:
		print(f"[0.30 0.70] 0.15 setdash")
	print("stroke")

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
				print(f"{segment.start * UNIT + x_real} {(len(self.vertical) - i - 1) * UNIT + y_real} moveto")
				print(f"{segment.end * UNIT + x_real} {(len(self.vertical) - i - 1) * UNIT + y_real} lineto")
				print_stroke(segment.stroke)

		# horizontal lines get printed as vertical	
		for i, line in enumerate(self.horizontal):
			for segment in line:
				if segment.stroke == Stroke.BLANK:
					continue
				print(f"{i * UNIT + x_real} {segment.start * UNIT + y_real} moveto")
				print(f"{i * UNIT + x_real} {segment.end * UNIT + y_real} lineto")
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
		print(f"/Times-Roman findfont")
		print(f"{self.size} scalefont")
		print(f"setfont")
		print(f"{x_real} {y_real} translate")
		print(f"270 rotate")
		print(f"0 0 moveto")
		print(f"({self.text}) show")
		print(f"90 rotate")
		print(f"{-x_real} {-y_real} translate")
			

class Page(object):
	def __init__(self):
		self.grid = Grid()
		self.text = []
	
	def render(self, side):
		if side == Side.LEFT:
			x = MARGIN_X
			y = MARGIN_Y
		if side == Side.RIGHT:
			x = A4_WIDTH - MARGIN_X - GRID_WIDTH * UNIT
			y = MARGIN_Y

		self.grid.render(x, y)

		for t in self.text:
			t.render(x, y)
		

# grid with r rows and c columns
# hobonichi secret line at column s
def make_blank_grid_with_secret(r, c, s):
	page = Page()

	# horizontal lines	
	for i in range(0, r + 1):
		page.grid.add_horizontal_segment(i, 0, c, Stroke.LIGHT)

	# vertical lines
	for i in range(0, c + 1):
		if (i == s):
			page.grid.add_vertical_segment(i, 0, r, Stroke.DARK)
		else:
			page.grid.add_vertical_segment(i, 0, r, Stroke.LIGHT)
	
	page.text.append(Text("This is a test", 32, 0, 0))
	
	return page

def render_two_grids_on_a4(g1, g2):
	g1.render(Side.LEFT)
	g2.render(Side.RIGHT)

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
