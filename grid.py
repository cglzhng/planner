from constants import *
from printer import *

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

		print_set_color(BLACK)

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

