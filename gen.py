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
		self.horizontal[row].append(Segment(stroke, start, end))

	def add_vertical_segment(self, column, start, end, stroke):
		self.vertical[column].append(Segment(stroke, start, end))

	def print(self, x, y):
		x_real = y
		y_real = A4_WIDTH - x - (len(self.vertical) - 1) * UNIT 
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
def make_blank_grid_with_secret(r, c, s):
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

def print_two_grids_on_a4(margin_x, margin_y, g1, g2):
	g1.print(margin_x, margin_y)
	g2.print(A4_WIDTH - margin_x - GRID_WIDTH * UNIT, margin_y)

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

grid = make_blank_grid_with_secret(40, 28, 21)
print_two_grids_on_a4(20, 17, grid, grid)

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
