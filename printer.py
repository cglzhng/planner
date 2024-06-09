from dataclasses import dataclass

from constants import *
from utils import *
from ps import *

@dataclass
class Margins:
	top: float
	bottom: float
	left: float
	right: float

@dataclass
class Measurements:
	top_line_count: int
	bottom_line_count: int
	left_line_count: int
	right_line_count: int

	tumble_top_margins: Margins
	tumble_bottom_margins: Margins

	notumble_top_margins: Margins
	notumble_bottom_margins: Margins

class Printer(object):
	def __init__(self, paper, orientation, measurements):
		self.paper = paper
		self.orientation = orientation
		self.measurements = measurements

		self.set_values()

		self.side = Side.TOP

	def start(self):
		print_preamble(self.paper)
	
	def end(self):
		print_end()
	
	def set_values(self):

		if self.orientation == Orientation.HORIZONTAL:
			top_margins = self.measurements.tumble_top_margins
			bottom_margins = self.measurements.tumble_bottom_margins
		if self.orientation == Orientation.VERTICAL:
			top_margins = self.measurements.notumble_top_margins
			bottom_margins = self.measurements.notumble_bottom_margins

		paper = self.paper

		y_min = 20 - self.measurements.bottom_line_count + 1
		y_max = paper["height"] - (20 - self.measurements.top_line_count + 1)
		x_min = 20 - self.measurements.left_line_count + 1
		x_max = paper["width"] - (20 - self.measurements.right_line_count + 1)

		self.margin_y = mm_to_point(max(
			bottom_margins.top,
			bottom_margins.bottom,
			top_margins.top,
			top_margins.bottom,
		))

		# Since the margins are different on both sides, we must have a different y_min and y_max for both sides of the paper.

		d = self.margin_y - mm_to_point(bottom_margins.bottom)
		self.y_min_bottom = y_min + d

		d = self.margin_y - mm_to_point(bottom_margins.top)
		self.y_max_bottom = y_max - d

		d = self.margin_y - mm_to_point(top_margins.bottom)
		self.y_min_top = y_min + d

		d = self.margin_y - mm_to_point(top_margins.top)
		self.y_max_top = y_max - d
		
		self.margin_x = mm_to_point(max(
			top_margins.left,
			top_margins.right,
			bottom_margins.left,
			bottom_margins.right,
		))

		# Since the margins are different on both sides, we must have a different x_min and x_max for both sides of the paper.
		
		d = self.margin_x - mm_to_point(bottom_margins.left)
		self.x_min_bottom = x_min + d

		d = self.margin_x - mm_to_point(bottom_margins.right)
		self.x_max_bottom = x_max - d

		d = self.margin_x - mm_to_point(top_margins.left)
		self.x_min_top = x_min + d
		eprint(f"x min top d {d}")
		eprint(f"x min top {self.x_min_top}")

		d = self.margin_x - mm_to_point(top_margins.right)
		self.x_max_top = x_max - d

	def _get_min_max(self):
		if self.side == Side.TOP:
			return (
				self.x_min_top,
				self.y_min_top,
				self.x_max_top,
				self.y_max_top,
			)
		if self.side == Side.BOTTOM:
			return (
				self.x_min_bottom,
				self.y_min_bottom,
				self.x_max_bottom,
				self.y_max_bottom,
			)
	
	def get_margin_x(self):
		if self.orientation == Orientation.HORIZONTAL:
			return self.margin_y
		if self.orientation == Orientation.VERTICAL:
			return self.margin_x
	
	def get_margin_y(self):
		if self.orientation == Orientation.HORIZONTAL:
			return self.margin_x
		if self.orientation == Orientation.VERTICAL:
			return self.margin_y
		
	def get_width(self):
		x_min, y_min, x_max, y_max = self._get_min_max()

		if self.orientation == Orientation.HORIZONTAL:
			return y_max - y_min
		if self.orientation == Orientation.VERTICAL:
			return x_max - x_min
	
	def get_height(self):
		x_min, y_min, x_max, y_max = self._get_min_max()

		if self.orientation == Orientation.HORIZONTAL:
			return x_max - x_min
		if self.orientation == Orientation.VERTICAL:
			return y_max - y_min
	
	def draw_text(self, text, x, y, size=12, color=BLACK, orientation=Orientation.HORIZONTAL, reverse=False):
		x_min, y_min, x_max, y_max = self._get_min_max()

		if (self.orientation == Orientation.HORIZONTAL):
			if orientation == Orientation.HORIZONTAL:
				print_text_vertical(text, size, x_min + y, y_max - x, color)
			if orientation == Orientation.VERTICAL:
				print_text_horizontal(text, size, x_min + y, y_max - x, color)

		if (self.orientation == Orientation.VERTICAL):
			if orientation == Orientation.HORIZONTAL:
				print_text_horizontal(text, size, x_min + x, y_min + y, color)
			if orientation == Orientation.VERTICAL:
				if (reverse):
					print_text_vertical_reverse(text, size, x_min + x, y_min + y, color)
				else:
					print_text_vertical(text, size, x_min + x, y_min + y, color)
				
	
	def draw_line(self, x1, y1, x2, y2, stroke):
		x_min, y_min, x_max, y_max = self._get_min_max()

		print_newpath()

		if (self.orientation == Orientation.HORIZONTAL):
			print_line(x_min + y1, y_max - x1, x_min + y2, y_max - x2)

		if (self.orientation == Orientation.VERTICAL):
			print_line(x_min + x1, y_min + y1, x_min + x2, y_min + y2)

		print_stroke(stroke)
	
	def draw_rectangle(self, x, y, width, height, color):
		x_min, y_min, x_max, y_max = self._get_min_max()
		
		if self.orientation == Orientation.HORIZONTAL:
			print_rectangle(x_min + y, y_max - x, height, width)

		if self.orientation == Orientation.VERTICAL:
			print_rectangle(x_min + x, y_min + y, width, height)

		print_set_color(color)
		print_fill()

	def draw_center_rectangle(self):
		x_min, y_min, x_max, y_max = self._get_min_max()

		eprint(f"{x_min} {y_min} {x_max} {y_max}")

		print_newpath()

		print_line(x_min, y_min, x_min, y_max)
		print_stroke(Stroke.SOLID)
		print_line(x_min, y_max, x_max, y_max)
		print_stroke(Stroke.SOLID)
		print_line(x_max, y_max, x_max, y_min)
		print_stroke(Stroke.SOLID)
		print_line(x_max, y_min, x_min, y_min)
		print_stroke(Stroke.SOLID)

	def next_page(self):
		print_showpage()
		if self.side == Side.TOP:
			self.side = Side.BOTTOM
		else:
			self.side = Side.TOP
	
	def debug_center_rectangle_duplex(self):
		self.draw_center_rectangle()
		self.draw_text("TOP", 10, 10)
		self.next_page()

		self.draw_center_rectangle()
		self.draw_text("BOTTOM", 10, 10)
		self.next_page()








# Count the number of lines printed at the bottom (n1). Then 20 - n1 + 1 is the minimum y (y_min) that we can print.
# Count the number of lines printed at the top (n2). Then A4_WIDTH - (20 - n2 + 1) is the maximum y (y_max) that we can print. 
# And, y_max - y_min is the height of the maximum area that we can print.
#
# Next, measure (with a ruler) the actual margins at the top and bottom, in mm.
#
# The larger margin must be used in order to create a symmetric image. 
# 
# FINDINGS:
# n1 = 7
# n2 = 7
#
# Top margin on bottom side: 4.7mm
# Bottom margin on bottom side: 4mm
#
# Top margin on top side: 4.5mm
# Bottom margin on top side: 3.8mm
def height_calibration_print():
	for i in range(0, 20):
		print_newpath()
		print_line(0, i, 100, i) 
		print_stroke(Stroke.SOLID)
	
	for i in range(0, 20):
		print_newpath()
		print_line(0, A4_WIDTH - i, 100, A4_WIDTH - i)
		print_stroke(Stroke.SOLID)
	
	print_text_vertical("TOP", 12, 100, 100, BLACK)

	print_showpage()

	for i in range(0, 20):
		print_newpath()
		print_line(0, i, 100, i) 
		print_stroke(Stroke.SOLID)
	
	for i in range(0, 20):
		print_newpath()
		print_line(0, A4_WIDTH - i, 100, A4_WIDTH - i)
		print_stroke(Stroke.SOLID)

	print_text_vertical("BOTTOM", 12, 100, 100, BLACK)


# Count the number of lines printed at the left (n1). Then 20 - n1 + 1 is the minimum x (x_min) that we can print.
# Count the number of lines printed at the right (n2). Then A4_HEIGHT - (20 - n2 + 1) is the maximum x (x_max) that we can print. 
# And, x_max - x_min is the width of the maximum area that we can print.
#
# Next, measure (with a ruler) the actual margins at the left and right, in mm.
# 
# The larger margin must be used in order to create a symmetric image.
# 
# FINDINGS:
# n1 = 7
# n2 = 8
#
# Left margin on bottom side: 4mm
# Right margin on bottom side: 4.8mm
#
# Left margin on top side: 7mm
# Right margin on top side: 1.1mm
#
# Since there is a difference between the two sides of the paper, we must also take that into account.
def width_calibration_print():
	for i in range(0, 20):
		print_newpath()
		print_line(i, 0, i, 100) 
		print_stroke(Stroke.SOLID)
	
	for i in range(0, 20):
		print_newpath()
		print_line(A4_HEIGHT - i, 0, A4_HEIGHT - i, 100)
		print_stroke(Stroke.SOLID)

	print_text_vertical("TOP", 12, 100, 100, BLACK)

	print_showpage()

	for i in range(0, 20):
		print_newpath()
		print_line(i, 0, i, 100) 
		print_stroke(Stroke.SOLID)
	
	for i in range(0, 20):
		print_newpath()
		print_line(A4_HEIGHT - i, 0, A4_HEIGHT - i, 100)
		print_stroke(Stroke.SOLID)

	print_text_vertical("BOTTOM", 12, 100, 100, BLACK)

