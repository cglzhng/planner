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

def make_color_test():
	layout = make_base_grid()
	layout.force_no_num = True

	layout.add_shape(TextBox(
		ColorBox(0, 0, 8, 4, LIGHT_PURPLE, Stroke.DARK),
		Text("Light Purple", FONT["Big"], WHITE),
		padding_left = 7,
	))

	layout.add_shape(TextBox(
		Box(10, 0, 8, 4, None, Stroke.BLANK),
		Text("Light Purple", FONT["Big"], LIGHT_PURPLE),
		padding_left = 7,
	))

	layout.add_shape(TextBox(
		ColorBox(0, 6, 8, 4, LIGHT_GREEN, Stroke.DARK),
		Text("Light Green", FONT["Big"], WHITE),
		padding_left = 7,
	))

	layout.add_shape(TextBox(
		Box(10, 6, 8, 4, None, Stroke.BLANK),
		Text("Light Green", FONT["Big"], LIGHT_GREEN),
		padding_left = 7,
	))

	layout.add_shape(TextBox(
		ColorBox(0, 12, 8, 4, LIGHT_RED, Stroke.DARK),
		Text("Light Red", FONT["Big"], WHITE),
		padding_left = 7,
	))

	layout.add_shape(TextBox(
		Box(10, 12, 8, 4, None, Stroke.BLANK),
		Text("Light Red", FONT["Big"], LIGHT_RED),
		padding_left = 7,
	))

	layout.add_shape(TextBox(
		ColorBox(0, 18, 8, 4, BRIGHT_RED, Stroke.DARK),
		Text("Bright Red", FONT["Big"], WHITE),
		padding_left = 7,
	))

	layout.add_shape(TextBox(
		Box(10, 18, 8, 4, None, Stroke.BLANK),
		Text("Bright Red", FONT["Big"], BRIGHT_RED),
		padding_left = 7,
	))

	layout.add_shape(TextBox(
		ColorBox(0, 24, 8, 4, BLUE_GRAY, Stroke.DARK),
		Text("Blue Gray", FONT["Big"], WHITE),
		padding_left = 7,
	))

	layout.add_shape(TextBox(
		Box(10, 24, 8, 4, None, Stroke.BLANK),
		Text("Blue Gray", FONT["Big"], BLUE_GRAY),
		padding_left = 7,
	))

	layout.add_shape(TextBox(
		ColorBox(0, 30, 8, 4, BROWN, Stroke.DARK),
		Text("Brown", FONT["Huge"], WHITE),
		padding_left = 7,
	))

	layout.add_shape(TextBox(
		Box(10, 30, 8, 4, None, Stroke.BLANK),
		Text("Brown", FONT["Huge"], BROWN),
		padding_left = 7,
	))

	layout.add_shape(TextBox(
		ColorBox(0, 36, 8, 4, TEAL, Stroke.DARK),
		Text("Teal", FONT["Huge"], WHITE),
		padding_left = 7,
	))

	layout.add_shape(TextBox(
		Box(10, 36, 8, 4, None, Stroke.BLANK),
		Text("Teal", FONT["Huge"], TEAL),
		padding_left = 7,
	))

	return layout


# grid with r rows and c columns
# hobonichi secret line at column s
def make_base_grid_with_secret(r, c, s):
	layout = Layout()

	shapes = []

	# horizontal lines
	shapes.append(Box(0, 0, c, 0, Stroke.DARK))
	for i in range(1, r):
		shapes.append(Box(0, i, c, 0, Stroke.LIGHT))
	shapes.append(Box(0, r, c, 0, Stroke.DARK))

	# vertical lines
	shapes.append(Box(0, 0, 0, r, Stroke.DARK))
	for i in range(1, c):
		shapes.append(Box(i, 0, 0, r, Stroke.LIGHT))
	shapes.append(Box(s, 0, 0, r, Stroke.DARK))
	shapes.append(Box(c, 0, 0, r, Stroke.DARK))

	layout.add_shapes(shapes)
	
	return layout

def make_blank_layout():
	layout = Layout(force_no_num=True)
	return layout

def make_base_grid():
	layout = Layout()

	shapes = []

	# horizontal lines
	shapes.append(Box(0, 0, GRID_WIDTH, 0, Stroke.DARK))
	for i in range(1, GRID_HEIGHT):
		shapes.append(Box(0, i, GRID_WIDTH, 0, Stroke.LIGHT))
	shapes.append(Box(0, GRID_HEIGHT, GRID_WIDTH, 0, Stroke.DARK))

	# vertical lines
	shapes.append(Box(0, 0, 0, GRID_HEIGHT, Stroke.DARK))
	for i in range(1, GRID_WIDTH):
		shapes.append(Box(i, 0, 0, GRID_HEIGHT, Stroke.LIGHT))
	shapes.append(Box(GRID_WIDTH, 0, 0, GRID_HEIGHT, Stroke.DARK))

	layout.add_shapes(shapes)
	
	return layout

def add_month_header(calendar, month, left, right):
	width = CALENDAR_DAY_WIDTH
	height = CALENDAR_HEADER_HEIGHT

	left.add_shape(TextBox(
		Box(0, GRID_HEIGHT - height, width, height, Stroke.DARK, True),
		Text(calendar.months[month]["name"], FONT["Medium"], LIGHT_PURPLE),
	))

	for i in range(0, 7):
		day = WEEKDAYS[i]
		if i < 3:
			side = left
			start_x = GRID_WIDTH - 3 * width
		else:
			side = right
			i = i - 3
			start_x = 0
			
		side.add_shape(TextBox(
			Box(start_x + i * width, GRID_HEIGHT - height, width, height, Stroke.DARKER, True),
			Text(WEEKDAY_NAMES[day.value], CALENDAR_HEADER_TEXT, LIGHT_PURPLE),
		))
	

def make_month(calendar, month, num_days, start_day, start_week=None):
	left = make_base_grid()
	right = make_base_grid()

	start_y = GRID_HEIGHT - CALENDAR_HEADER_HEIGHT - CALENDAR_DAY_HEIGHT
	left_start_x = GRID_WIDTH - 3 * CALENDAR_DAY_WIDTH

	start_day_index = get_weekday_index(start_day)

	if start_day != WEEKDAYS[0]:
		for i in range(0, start_day_index):
			if i < 3:
				x = left_start_x + CALENDAR_DAY_WIDTH * i 
				side = left
			else:
				x = CALENDAR_DAY_WIDTH * (i - 3)
				side = right

			side.add_shape(Box(x, start_y, CALENDAR_DAY_WIDTH, CALENDAR_DAY_HEIGHT, Stroke.DARK))

	add_month_header(calendar, month, left, right)

	week = 0
	weekday = start_day_index
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

		side.add_shape(Box(x, y, CALENDAR_DAY_WIDTH, height, Stroke.DARKER))
		side.add_shape(TextBox(
			Box(x, y + height - 1, 2, 1, Stroke.DARKER, True),
			Text(str(day + 1), FONT["Tiny"], LIGHT_PURPLE),
		))

		if weekday == 0 and height == CALENDAR_DAY_HEIGHT and start_week is not None:
			left.add_shape(TextBox(
				Box(left_start_x - 1, y, 1, 1, None),
				Text(f"W{week + start_week}", FONT["Tinier"], LIGHT_PURPLE),
			))

		day = day + 1

		weekday = weekday + 1
		if weekday == 7:
			weekday = 0
			week = week + 1
	
	return left, right

def make_month_plan(calendar, month, num_days, start_day):
	left = make_base_grid()
	right = make_base_grid()

	half_width = GRID_WIDTH // 2
	half_height = GRID_HEIGHT // 2

	weekday_index = get_weekday_index(start_day) 
	for day in range(1, num_days + 1):
		right.add_shape(TextBox(
			Box(0, GRID_HEIGHT - day, 1, 1, None),
			Text(str(day), FONT["Tiny"], LIGHT_PURPLE),
		))
		right.add_shape(TextBox(
			Box(1, GRID_HEIGHT - day, 1, 1),
			Text(WEEKDAY_NAMES[WEEKDAYS[weekday_index].value][0], FONT["Tiny"], LIGHT_PURPLE),
		))
		weekday_index = weekday_index + 1
		if weekday_index == 7:
			weekday_index = 0
	
	left.add_shape(TextBox(
		Box(0, GRID_HEIGHT - 2, 5, 2, Stroke.DARKER, True),
		Text(calendar.months[month]["name"], FONT["Huge"], LIGHT_PURPLE),
	))

	
	right.add_shape(Box(1, GRID_HEIGHT - num_days, 0, GRID_HEIGHT, Stroke.DARK))
	right.add_shape(Box(2, GRID_HEIGHT - num_days, 0, GRID_HEIGHT, Stroke.DARK))
	right.add_shape(Box(half_width, 0, 0, GRID_HEIGHT, Stroke.DARK))
	right.add_shape(Box(0, GRID_HEIGHT - num_days, GRID_WIDTH // 2, 0, Stroke.DARK))

	right.add_shape(TextBox(
		Box(half_width, GRID_HEIGHT - 1, 5, 1, Stroke.DARK, True),
		Text("This month", FONT["Small"], LIGHT_PURPLE),
	))

	return left, right
	
def make_weekly_layout(calendar, month, num_days, week, start_day):
	left = make_base_grid()
	right = make_base_grid()

	header_height = 1
	num_width = 2
	name_width = 10
	month_width = 10
	week_width = 2

	box_width = GRID_WIDTH // 2
	box_height = GRID_HEIGHT // 3

	month_str = calendar.months[month]["name"]
	if start_day + 6 > num_days:
		next_month = calendar.month_order[(calendar.get_month_index(month) + 1) % len(calendar.month_order)]
		month_str = f"{calendar.months[month]['short']}-{calendar.months[next_month]['short']}"

	left.add_shape(TextBox(
		ColorBox(0, GRID_HEIGHT - header_height - 1, month_width, header_height + 1, LIGHT_PURPLE, Stroke.DARK),
		Text(month_str, FONT["Big"], WHITE),
		padding_left = 7,
		align_h = Align.START,
	))
	left.add_shape(TextBox(
		Box(month_width, GRID_HEIGHT - header_height - 1, week_width, header_height + 1, Stroke.DARK, True),
		Text(f"W{week}", FONT["Small"], LIGHT_PURPLE),
	))
	left.add_shape(TextBox(
		Box(0, GRID_HEIGHT - header_height - 2, 5, 1, Stroke.DARK, True),
		Text("Priorities", FONT["Small"], LIGHT_PURPLE),
	))

	for i in range(0, 7):
		day = start_day + i
		if day > num_days:
			day = day - num_days

		if i < 5:
			side = left
			j = i + 1
		else:
			side = right
			j = i - 5

		x = (j % 2) * box_width
		y_top = GRID_HEIGHT - (j // 2) * box_height
		y_bottom = y_top - box_height

		side.add_shape(Box(x, y_bottom, box_width, box_height, Stroke.DARKER))
		side.add_shape(TextBox(
			Box(x, y_top - header_height, num_width, header_height, Stroke.DARKER, True),
			Text(str(day), FONT["Tiny"], LIGHT_PURPLE),
		))

		side.add_shape(TextBox(
			Box(x + num_width, y_top - header_height, name_width, header_height, Stroke.DARKER, True),
			Text(WEEKDAY_NAMES[WEEKDAYS[i].value], FONT["Tiny"], LIGHT_PURPLE),
			padding_left = 7,
			align_h = Align.START,
		))
	
	notes_box_height = GRID_HEIGHT - box_height - 1
	notes_height = 1
	notes_width = 3
	
	right.add_shape(Box(0, notes_box_height, GRID_WIDTH, 1, None, True))
	right.add_shape(Box(0, notes_box_height, 0, 1, Stroke.BLANK))
	right.add_shape(Box(GRID_WIDTH, notes_box_height, 0, 1, Stroke.BLANK))
	right.add_shape(Box(0, 0, GRID_WIDTH, notes_box_height, Stroke.LIGHT))
	right.add_shape(TextBox(
		ColorBox(0, notes_box_height - notes_height, notes_width, notes_height, LIGHT_PURPLE, Stroke.LIGHT),
		Text("Notes", FONT["Small"], WHITE),
	))

	return left, right

def make_monthly_planner(calendar, year, extra_pages):
	layouts = []
	for month in calendar.months:
		num_days = calendar.get_num_days_in_month(year, month)
		start_day = calendar.get_weekday_from_date(year, month, 1)
		left, right = make_month(calendar, month, num_days, start_day, None)
		layouts.append(left)
		layouts.append(right)
	
	for i in range(extra_pages):
		base = make_base_grid_with_secret(GRID_HEIGHT, GRID_WIDTH, 7)
		layouts.append(base)

	return layouts

def make_planner(calendar, year, start_month, num_months):
	layouts = []
	month_index = calendar.get_month_index(start_month)

	for i in range(0, num_months):
		month = calendar.month_order[month_index + i]
		num_days = calendar.get_num_days_in_month(year, month) 

		start_day = calendar.get_weekday_from_date(year, month, 1)
		start_week = calendar.get_week_from_date(year, month, 1)

		left, right = make_month(calendar, month, num_days, start_day, start_week)
		layouts.append(left)
		layouts.append(right)
		left, right = make_month_plan(calendar, month, num_days, start_day)
		layouts.append(left)
		layouts.append(right)
	
	for i in range(0, num_months):
		month = calendar.month_order[month_index + i]
		num_days = calendar.get_num_days_in_month(year, month)
		start_weekday = calendar.get_weekday_from_date(year, month, 1)
		start_weekday_index = get_weekday_index(start_weekday)
		if start_weekday_index != 0:
			if i == 0:
				prev_month = calendar.month_order[month_index + i - 1]
				prev_month_num_days = calendar.get_num_days_in_month(year, prev_month)
				start_day = prev_month_num_days - start_weekday_index
				week = calendar.get_week_from_date(year, month, 1)

				left, right = make_weekly_layout(calendar, prev_month, prev_month_num_days, week, start_day)
				layouts.append(left)
				layouts.append(right)
			start_day = 7 - start_weekday_index + 1
		else:
			start_day = 1

		while start_day < num_days:
			week = calendar.get_week_from_date(year, month, start_day)
			left, right = make_weekly_layout(calendar, month, num_days, week, start_day)
			layouts.append(left)
			layouts.append(right)
			start_day += 7
	
	return layouts