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
	left.grid.add_horizontal_segment(GRID_HEIGHT - 2, 0, GRID_WIDTH, Stroke.DARK)
	left.grid.add_horizontal_segment(GRID_HEIGHT - 1, 0, GRID_WIDTH, Stroke.BLANK)
	right.grid.add_horizontal_segment(GRID_HEIGHT - 1, 0, GRID_WIDTH, Stroke.BLANK)

	for i in range(0, 4):
		left.grid.add_vertical_segment(i * CALENDAR_DAY_WIDTH, GRID_HEIGHT - 2, GRID_HEIGHT, Stroke.DARK)
		right.grid.add_vertical_segment(i * CALENDAR_DAY_WIDTH, GRID_HEIGHT - 2, GRID_HEIGHT, Stroke.DARK)
		for j in range(0, CALENDAR_DAY_WIDTH - 1):
			left.grid.add_vertical_segment(i * CALENDAR_DAY_WIDTH + j + 1, GRID_HEIGHT - 2, GRID_HEIGHT, Stroke.BLANK)	
			right.grid.add_vertical_segment(i * CALENDAR_DAY_WIDTH + j + 1, GRID_HEIGHT - 2, GRID_HEIGHT, Stroke.BLANK)	

def make_month(num_days, start_day):
	left = make_blank_grid()
	right = make_blank_grid()

	make_month_header(left, right)

	start_y = GRID_HEIGHT - 2 - CALENDAR_DAY_HEIGHT

	week = 0
	weekday = start_day.value - 1
	days = 0

	while days < num_days:
		y = start_y - week * CALENDAR_DAY_HEIGHT
		
		if weekday < 3:
			x = CALENDAR_DAY_WIDTH * (weekday + 1)
			left.grid.add_rectangle(x, y, CALENDAR_DAY_WIDTH, CALENDAR_DAY_HEIGHT, Stroke.DARK)
		else:
			x = CALENDAR_DAY_WIDTH * (weekday - 3)
			right.grid.add_rectangle(x, y, CALENDAR_DAY_WIDTH, CALENDAR_DAY_HEIGHT, Stroke.DARK)

		days = days + 1

		weekday = weekday + 1
		if weekday == 7:
			weekday = 0
			week = week + 1
	

	return left, right
	


