from book import *

def make_test_lines_horizontal(start, num, stroke):
	layout = Layout()
	for i in range(0, num):
		layout.grid.add_horizontal_segment(start + i, 0, GRID_WIDTH, stroke)
	return layout

def make_test_grid_with_secret(start, num, stroke):
	layout = Layout()

	# horizontal lines	
	layout.grid.add_horizontal_segment(start, 0, GRID_WIDTH, Stroke.DARK)
	for i in range(1, num):
		layout.grid.add_horizontal_segment(start + i, 0, GRID_WIDTH, Stroke.LIGHT)
	layout.grid.add_horizontal_segment(start + num, 0, GRID_WIDTH, Stroke.DARK)

	# vertical lines
	layout.grid.add_vertical_segment(0, start, start + num, Stroke.DARK)
	for i in range(1, GRID_WIDTH):
		layout.grid.add_vertical_segment(i, start, start + num, Stroke.LIGHT)
	layout.grid.add_vertical_segment(5, start, start + num, Stroke.DARK)
	layout.grid.add_vertical_segment(GRID_WIDTH, start, start + num, Stroke.DARK)
	
	return layout


# grid with r rows and c columns
# hobonichi secret line at column s
def make_blank_grid_with_secret(r, c, s):
	layout = Layout()

	# horizontal lines	
	layout.grid.add_horizontal_segment(0, 0, c, Stroke.DARK)
	for i in range(1, r):
		layout.grid.add_horizontal_segment(i, 0, c, Stroke.LIGHT)
	layout.grid.add_horizontal_segment(r, 0, c, Stroke.DARK)

	# vertical lines
	layout.grid.add_vertical_segment(0, 0, r, Stroke.DARK)
	for i in range(1, c):
		layout.grid.add_vertical_segment(i, 0, r, Stroke.LIGHT)
	layout.grid.add_vertical_segment(s, 0, r, Stroke.DARK)
	layout.grid.add_vertical_segment(c, 0, r, Stroke.DARK)
	
	return layout

def make_blank_grid():
	layout = Layout()

	# horizontal lines	
	layout.grid.add_horizontal_segment(0, 0, GRID_WIDTH, Stroke.DARK)
	for i in range(1, GRID_HEIGHT):
		layout.grid.add_horizontal_segment(i, 0, GRID_WIDTH, Stroke.LIGHT)
	layout.grid.add_horizontal_segment(GRID_HEIGHT, 0, GRID_WIDTH, Stroke.DARK)

	# vertical lines
	layout.grid.add_vertical_segment(0, 0, GRID_HEIGHT, Stroke.DARK)
	for i in range(1, GRID_WIDTH):
		layout.grid.add_vertical_segment(i, 0, GRID_HEIGHT, Stroke.LIGHT)
	layout.grid.add_vertical_segment(GRID_WIDTH, 0, GRID_HEIGHT, Stroke.DARK)
	
	return layout

def make_month_header(left, right):
	width = CALENDAR_DAY_WIDTH
	height = CALENDAR_HEADER_HEIGHT

	for i in range(0, 3):
		x = GRID_WIDTH - 3 * width 
		left.grid.add_blank_rectangle(x + i * width, GRID_HEIGHT - height, width, height, Stroke.DARKER)
		t = Text(WEEKDAYS[i], CALENDAR_HEADER_TEXT, LIGHT_PURPLE)
		t.center_in(x + i * width, GRID_HEIGHT - height, width, height)
		left.add_text(t)
	
	days = ["Thursday", "Friday", "Saturday", "Sunday"]
	for i in range(0, 4):
		right.grid.add_blank_rectangle(i * width, GRID_HEIGHT - height, width, height, Stroke.DARKER)
		t = Text(WEEKDAYS[i + 3], CALENDAR_HEADER_TEXT, LIGHT_PURPLE)
		t.center_in(i * width, GRID_HEIGHT - height, width, height)
		right.add_text(t)


def make_month(num_days, start_day):
	left = make_blank_grid()
	right = make_blank_grid()

	make_month_header(left, right)

	start_y = GRID_HEIGHT - CALENDAR_HEADER_HEIGHT - CALENDAR_DAY_HEIGHT
	left_start_x = GRID_WIDTH - 3 * CALENDAR_DAY_WIDTH

	week = 0
	weekday = start_day.value - 1
	day = 0

	while day < num_days:
		height = CALENDAR_DAY_HEIGHT
		y = start_y - week * CALENDAR_DAY_HEIGHT
		if y < 0:
			y = 0
			height = GRID_HEIGHT - CALENDAR_HEADER_HEIGHT - week * CALENDAR_DAY_HEIGHT

		
		if weekday < 3:
			x = left_start_x + CALENDAR_DAY_WIDTH * weekday
			side = left
		else:
			x = CALENDAR_DAY_WIDTH * (weekday - 3)
			side = right

		side.grid.add_rectangle(x, y, CALENDAR_DAY_WIDTH, height, Stroke.DARKER)
		side.grid.add_blank_rectangle(x, y + height - 1, 2, 1, Stroke.DARKER)
		num = Text(str(day + 1), FONT["Tiny"], LIGHT_PURPLE)
		num.center_in(x, y + height - 1, 2, 1)
		side.add_text(num)

		day = day + 1

		weekday = weekday + 1
		if weekday == 7:
			weekday = 0
			week = week + 1
	

	return left, right
	
def make_weekly_layout(month, week, start_day):
	left = make_blank_grid()
	right = make_blank_grid()

	header_height = 2
	num_width = 2
	name_width = 5
	month_width = 5
	week_width = 4

	left.grid.add_blank_rectangle(0, GRID_HEIGHT - header_height, month_width, header_height, Stroke.DARKER)
	left.grid.add_blank_rectangle(month_width, GRID_HEIGHT - header_height, week_width, header_height, Stroke.DARKER)
	month = Text(MONTHS[month], FONT["Small"], LIGHT_PURPLE)
	month.center_in(0, GRID_HEIGHT - header_height, month_width, header_height)
	left.add_text(month)
	week = Text(f"Week {week + 1}", FONT["Small"], LIGHT_PURPLE)
	week.center_in(month_width, GRID_HEIGHT - header_height, week_width, header_height)
	left.add_text(week)

	
	for i in range(0, 7):
		if i < 3:
			side = left
			j = i + 1
		else:
			side = right
			j = i - 3

		y_top = GRID_HEIGHT - j * WEEK_DAY_HEIGHT
		y_bottom = GRID_HEIGHT - (j + 1) * WEEK_DAY_HEIGHT

		side.grid.add_rectangle(0, y_bottom, WEEK_DAY_WIDTH, WEEK_DAY_HEIGHT, Stroke.DARKER)
		side.grid.add_blank_rectangle(0, y_top - header_height, num_width, header_height, Stroke.DARKER)
		num = Text(str(start_day + i), FONT["Small"], LIGHT_PURPLE)
		num.center_in(0, y_top - header_height, num_width, header_height)
		side.add_text(num)

		side.grid.add_blank_rectangle(0, y_bottom, num_width, y_top - y_bottom - header_height, Stroke.DARKER)
		name = Text(WEEKDAYS[i], FONT["Small"], LIGHT_PURPLE, Orientation.VERTICAL)
		name.center_in(0, y_bottom, y_top - y_bottom - header_height, num_width)
		eprint(y_top)
		side.add_text(name)
	
		

	return left, right
