from constants import *
from utils import *
from printer import *


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

	print_text_horizontal("TOP", 12, 100, 100, BLACK)

	print_showpage()

	for i in range(0, 20):
		print_newpath()
		print_line(0, i, 100, i) 
		print_stroke(Stroke.SOLID)
	
	for i in range(0, 20):
		print_newpath()
		print_line(0, A4_WIDTH - i, 100, A4_WIDTH - i)
		print_stroke(Stroke.SOLID)

	print_text_horizontal("BOTTOM", 12, 100, 100, BLACK)


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

	print_text_horizontal("TOP", 12, 100, 100, BLACK)

	print_showpage()

	for i in range(0, 20):
		print_newpath()
		print_line(i, 0, i, 100) 
		print_stroke(Stroke.SOLID)
	
	for i in range(0, 20):
		print_newpath()
		print_line(A4_HEIGHT - i, 0, A4_HEIGHT - i, 100)
		print_stroke(Stroke.SOLID)

	print_text_horizontal("BOTTOM", 12, 100, 100, BLACK)


def draw_centered_rectangle():
	bottom_line_count = 7
	top_line_count = 7
	left_line_count = 7
	right_line_count = 8

	y_min = 20 - bottom_line_count + 1
	y_max = A4_WIDTH - (20 - top_line_count + 1)

	top_margin_bottom_side = 4.7
	bottom_margin_bottom_side = 4

	top_margin_top_side = 4.5
	bottom_margin_top_side = 3.8

	# Since the margins are different on both sides, we must have a different y_min and y_max for both sides of the paper.

	max_margin = top_margin_bottom_side

	d = max_margin - bottom_margin_bottom_side
	y_min_bottom = y_min + d

	d = max_margin - top_margin_bottom_side
	y_max_bottom = y_max - d

	d = max_margin - bottom_margin_top_side
	y_min_top = y_min + d

	d = max_margin - top_margin_top_side
	y_max_top = y_max - d

	x_min = 20 - left_line_count + 1
	x_max = A4_HEIGHT - (20 - right_line_count + 1)

	left_margin_bottom_side = 4
	right_margin_bottom_side = 4.8
	
	left_margin_top_side = 7
	right_margin_top_side = 1.1

	max_margin = left_margin_top_side
	# Since the margins are different on both sides, we must have a different x_min and x_max for both sides of the paper.
	
	d = max_margin - left_margin_bottom_side
	x_min_bottom = x_min + mm_to_point(d)

	d = max_margin - right_margin_bottom_side
	x_max_bottom = x_max - mm_to_point(d)

	d = max_margin - left_margin_top_side
	x_min_top = x_min + mm_to_point(d)

	d = max_margin - right_margin_top_side
	x_max_top = x_max - mm_to_point(d)

	# Now let's shrink everything by 2 in case of minor misalignment in the printer.
	x_min_top += 2
	x_max_top -= 2
	x_min_bottom += 2
	x_max_bottom -= 2
	y_min_top += 2
	y_max_top -= 2
	y_min_bottom += 2
	y_max_bottom -= 2
	

	print_newpath()
	print_line(x_min_top, y_min_top, x_min_top, y_max_top)
	print_stroke(Stroke.SOLID)
	print_line(x_min_top, y_max_top, x_max_top, y_max_top)
	print_stroke(Stroke.SOLID)
	print_line(x_max_top, y_max_top, x_max_top, y_min_top)
	print_stroke(Stroke.SOLID)
	print_line(x_max_top, y_min_top, x_min_top, y_min_top)
	print_stroke(Stroke.SOLID)
	print_text_horizontal("TOP", 12, 100, 100, BLACK)

	print_showpage()

	print_newpath()
	print_line(x_min_bottom, y_min_bottom, x_min_bottom, y_max_bottom)
	print_stroke(Stroke.SOLID)
	print_line(x_min_bottom, y_max_bottom, x_max_bottom, y_max_bottom)
	print_stroke(Stroke.SOLID)
	print_line(x_max_bottom, y_max_bottom, x_max_bottom, y_min_bottom)
	print_stroke(Stroke.SOLID)
	print_line(x_max_bottom, y_min_bottom, x_min_bottom, y_min_bottom)
	print_stroke(Stroke.SOLID)
	print_text_horizontal("BOTTOM", 12, 100, 100, BLACK)

	print_showpage()
