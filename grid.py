from utils import *
from constants import *
from printer import *

def insert_segment(line, segment, debug=False):

	if (debug):
		eprint(line)

	i = 0

	while i < len(line):
		if line[i].start >= segment.start:
			break
		i = i + 1

	j = i

	while i > 0:
		# This segment overlaps with the segment at i - 1
		if line[i - 1].end >= segment.start: 
			if segment.start == line[i - 1].start:
				# This segment completely consumes the segment at i - 1, so "combine"
				# And keep trying to combine segments
				i = i - 1
			elif line[i - 1].stroke != segment.stroke:
				# Special case check: If segment is completely contained in line[i - 1], we need to break line[i - 1] on the right side as well
				if line[i - 1].end > segment.end:
					line.insert(i, Segment(line[i - 1].stroke, segment.end, line[i - 1].end))

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

	if (debug):
		eprint(line)


def equal_segment(s1, s2):
	return s1.stroke == s2.stroke and s1.start == s2.start and s1.end == s2.end

def equal_lines(l1, l2):
	if len(l1) != len(l2):
		return False
	
	for i in range(0, len(l1)):
		if not equal_segment(l1[i], l2[i]):
			return False
	
	return True

def test_lines(l1, l2):
	if equal_lines(l1, l2):
		eprint("Test passed!")
	else:
		eprint("TEST FAILED!")
		eprint("Expected:")
		eprint(l2)
		eprint("Got:")
		eprint(l1)


def test_insert_segment():
	t = [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 5),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.LIGHT, 4, 8))
	test_lines(t, [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 10),
		Segment(Stroke.LIGHT, 12, 16),
	])

	t = [
		Segment(Stroke.LIGHT, 3, 5),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.LIGHT, 1, 17))
	test_lines(t, [
		Segment(Stroke.LIGHT, 1, 17),
	])

	t = [
		Segment(Stroke.LIGHT, 1, 3),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.LIGHT, 3, 6))
	test_lines(t, [
		Segment(Stroke.LIGHT, 1, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	])

	t = [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 5),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.LIGHT, 10, 13))
	test_lines(t, [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 5),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 16),
	])

	t = [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 5),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.DARK, 4, 9))
	test_lines(t, [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 4),
		Segment(Stroke.DARK, 4, 9),
		Segment(Stroke.LIGHT, 9, 10),
		Segment(Stroke.LIGHT, 12, 16),
	])

	t = [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 4),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.DARK, 1, 5))
	test_lines(t, [
		Segment(Stroke.DARK, 1, 5),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),

	])

	t = [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 4),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.LIGHT, 12, 16),
	]
	insert_segment(t, Segment(Stroke.DARK, 9, 17))
	test_lines(t, [
		Segment(Stroke.LIGHT, 1, 2),
		Segment(Stroke.LIGHT, 3, 4),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 9),
		Segment(Stroke.DARK, 9, 17),
	])

	t = [
		Segment(Stroke.DARK, 1, 2),
		Segment(Stroke.LIGHT, 3, 4),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.DARK, 12, 16),
	]
	insert_segment(t, Segment(Stroke.DARK, 2, 13))
	test_lines(t, [
		Segment(Stroke.DARK, 1, 16),
	])

	t = [
		Segment(Stroke.DARK, 1, 16),
	]
	insert_segment(t, Segment(Stroke.LIGHT, 3, 6))
	test_lines(t, [
		Segment(Stroke.DARK, 1, 3),
		Segment(Stroke.LIGHT, 3, 6),
		Segment(Stroke.DARK, 6, 16),
	])

	t = [
		Segment(Stroke.DARK, 1, 2),
		Segment(Stroke.LIGHT, 3, 4),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.DARK, 12, 16),
	]
	insert_segment(t, Segment(Stroke.LIGHT, 6, 7))
	test_lines(t, [
		Segment(Stroke.DARK, 1, 2),
		Segment(Stroke.LIGHT, 3, 4),
		Segment(Stroke.LIGHT, 6, 7),
		Segment(Stroke.LIGHT, 8, 10),
		Segment(Stroke.DARK, 12, 16),
	])

	t = [
		Segment(Stroke.LIGHT, 0, 8),
		Segment(Stroke.DARK, 8, 12),
		Segment(Stroke.LIGHT, 12, 20),
	]
	insert_segment(t, Segment(Stroke.DARK, 12, 16))
	test_lines(t, [
		Segment(Stroke.LIGHT, 0, 8),
		Segment(Stroke.DARK, 8, 16),
		Segment(Stroke.LIGHT, 16, 20),
	])

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

	def add_rectangle(self, x, y, width, height, stroke):
		self.add_horizontal_segment(y, x, x + width, stroke)
		self.add_horizontal_segment(y + height, x, x + width, stroke)
		self.add_vertical_segment(x, y, y + height, stroke)
		self.add_vertical_segment(x + width, y, y + height, stroke)

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
					(len(self.vertical) - segment.start - 1) * UNIT + y_real,
					i * UNIT + x_real, 
					(len(self.vertical) - segment.end - 1) * UNIT + y_real,
				)
				print_stroke(segment.stroke)

