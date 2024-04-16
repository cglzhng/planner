from book import *

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

def make_blank_grid():
	page = Page()

	# horizontal lines	
	page.grid.add_horizontal_segment(0, 0, GRID_WIDTH, Stroke.DARK)
	for i in range(1, GRID_HEIGHT):
		page.grid.add_horizontal_segment(i, 0, GRID_WIDTH, Stroke.LIGHT)
	page.grid.add_horizontal_segment(GRID_HEIGHT, 0, GRID_WIDTH, Stroke.DARK)

	# vertical lines
	page.grid.add_vertical_segment(0, 0, GRID_HEIGHT, Stroke.DARK)
	for i in range(1, GRID_WIDTH):
		page.grid.add_vertical_segment(i, 0, GRID_HEIGHT, Stroke.LIGHT)
	page.grid.add_vertical_segment(GRID_WIDTH, 0, GRID_HEIGHT, Stroke.DARK)
	
	return page

def make_month_header(left, right):
	left.grid.add_horizontal_segment(GRID_HEIGHT - 2, GRID_WIDTH - 3 * CALENDAR_DAY_WIDTH, GRID_WIDTH, Stroke.DARK)
	left.grid.add_horizontal_segment(GRID_HEIGHT - 1, GRID_WIDTH - 3 * CALENDAR_DAY_WIDTH, GRID_WIDTH, Stroke.BLANK)
	right.grid.add_horizontal_segment(GRID_HEIGHT - 2, 0, 4 * CALENDAR_DAY_WIDTH, Stroke.DARK)
	right.grid.add_horizontal_segment(GRID_HEIGHT - 1, 0, 4 * CALENDAR_DAY_WIDTH, Stroke.BLANK)

	days = ["MONDAY", "TUESDAY", "WEDNESDAY"]
	for i in range(0, 3):
		x = GRID_WIDTH - 3 * CALENDAR_DAY_WIDTH
		left.grid.add_vertical_segment(x + i * CALENDAR_DAY_WIDTH, GRID_HEIGHT - 2, GRID_HEIGHT, Stroke.DARK)
		for j in range(0, CALENDAR_DAY_WIDTH - 1):
			left.grid.add_vertical_segment(x + i * CALENDAR_DAY_WIDTH + j + 1, GRID_HEIGHT - 2, GRID_HEIGHT, Stroke.BLANK)
		t = Text(days[i], FONT["Small"], LIGHT_PURPLE)
		t.center_in(x + i * CALENDAR_DAY_WIDTH, GRID_HEIGHT - 2, CALENDAR_DAY_WIDTH, 2)
		left.add_text(t)
	
	days = ["Thursday", "Friday", "Saturday", "Sunday"]
	for i in range(0, 4):
		right.grid.add_vertical_segment(i * CALENDAR_DAY_WIDTH, GRID_HEIGHT - 2, GRID_HEIGHT, Stroke.DARK)
		for j in range(0, CALENDAR_DAY_WIDTH - 1):
			right.grid.add_vertical_segment(i * CALENDAR_DAY_WIDTH + j + 1, GRID_HEIGHT - 2, GRID_HEIGHT, Stroke.BLANK)
		t = Text(days[i], FONT["Small"], LIGHT_PURPLE)
		t.center_in(i * CALENDAR_DAY_WIDTH, GRID_HEIGHT - 2, CALENDAR_DAY_WIDTH, 2)
		right.add_text(t)

	right.grid.add_vertical_segment(4 * CALENDAR_DAY_WIDTH, GRID_HEIGHT - 2, GRID_HEIGHT, Stroke.DARK)

def make_month(num_days, start_day):
	left = make_blank_grid()
	right = make_blank_grid()

	make_month_header(left, right)

	start_y = GRID_HEIGHT - 2 - CALENDAR_DAY_HEIGHT
	left_start_x = GRID_WIDTH - 3 * CALENDAR_DAY_WIDTH

	week = 0
	weekday = start_day.value - 1
	day = 0

	while day < num_days:
		y = start_y - week * CALENDAR_DAY_HEIGHT
		
		if weekday < 3:
			x = left_start_x + CALENDAR_DAY_WIDTH * weekday
			side = left
		else:
			x = CALENDAR_DAY_WIDTH * (weekday - 3)
			side = right

		side.grid.add_rectangle(x, y, CALENDAR_DAY_WIDTH, CALENDAR_DAY_HEIGHT, Stroke.DARK)
		side.grid.add_rectangle(x, y + CALENDAR_DAY_HEIGHT - 1, 2, 1, Stroke.DARK)
		side.grid.add_vertical_segment(x + 1, y + CALENDAR_DAY_HEIGHT - 1, y + CALENDAR_DAY_HEIGHT, Stroke.BLANK)
		num = Text(str(day), FONT["Tiny"], LIGHT_PURPLE)
		num.center_in(x, y + CALENDAR_DAY_HEIGHT - 1, 2, 1)
		side.add_text(num)

		day = day + 1

		weekday = weekday + 1
		if weekday == 7:
			weekday = 0
			week = week + 1
	

	return left, right
	


