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
	def __init__(self, stroke, start, end, color=None):
		self.stroke = stroke
		self.start = start
		self.end = end
		self.color = color
	
	def __repr__(self):
		return f"{self.stroke} [{self.start}, {self.end}]"

class Grid(object):
	def __init__(self):
		self.horizontal = [[] for i in range(0, GRID_HEIGHT + 1)]
		self.vertical = [[] for i in range(0, GRID_WIDTH + 1)]

	def add_horizontal_segment(self, row, start, end, stroke, color=None):
		if row >= len(self.horizontal) or row < 0 or end < start:
			return
		if end >= len(self.vertical):
			end = len(self.vertical) - 1
		if start < 0:
			start = 0
		insert_segment(self.horizontal[row], Segment(stroke, start, end, color))

	def add_vertical_segment(self, column, start, end, stroke, color=None):
		if column >= len(self.vertical) or column < 0 or end < start:
			return
		if end >= len(self.horizontal):
			end = len(self.horizontal) - 1
		if start < 0:
			start = 0
		insert_segment(self.vertical[column], Segment(stroke, start, end, color))

	def render(self, printer, x, y):
		for i, line in enumerate(self.vertical):
			for segment in line:
				if segment.stroke == Stroke.BLANK:
					continue
				printer.draw_line(
					x + i * UNIT, 
					y + segment.start * UNIT,
					x + i * UNIT, 
					y + segment.end * UNIT,
					segment.stroke,
                    segment.color,
				)

		for i, line in enumerate(self.horizontal):
			for segment in line:
				if segment.stroke == Stroke.BLANK:
					continue
				printer.draw_line(
					x + segment.start * UNIT,
					y + i * UNIT, 
					x + segment.end * UNIT,
					y + i * UNIT,
					segment.stroke,
                    segment.color,
				)

