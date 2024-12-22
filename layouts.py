from calendar import *
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

def make_typeset_test():
	layout = Layout()

	layout.add_shape(TextBox(
		Box(5, 5, 14, 26, Stroke.DARKER, True),
		Text("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\nIt has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.\nIt was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", "Small", BLACK),
		padding_left=10,
		padding_right=10,
	))

	return layout

def make_color_test(grid=True):
	if grid:
		layout = make_base_grid()
	else:
		layout = Layout()

	layout.force_no_num = True

	colors = [
		{
			"name": "Teal",
			"value": TEAL,
		},
		{
			"name": "Purple",
			"value": PURPLE,
		},
		{
			"name": "Green",
			"value": GREEN,
		},
		{
			"name": "Orange",
			"value": ORANGE,
		},
	]

	for i in range(len(colors)):
		color = colors[i]
		layout.add_shape(TextBox(
			ColorBox(0, GRID_HEIGHT - 3 * (i + 1), 6, 2, color["value"], Stroke.SOLID, color["value"]),
			Text(color["name"], "Small", WHITE),
			padding_left = 7,
		))

		layout.add_shape(TextBox(
			ColorBox(7, GRID_HEIGHT - 3 * (i + 1), 5, 1, color["value"], Stroke.SOLID, color["value"]),
			Text(color["name"], "Tiny", WHITE),
			padding_left = 7,
		))

		layout.add_shape(TextBox(
			Box(13, GRID_HEIGHT - 3 * (i + 1), 6, 2, Stroke.SOLID, True, color["value"]),
			Text(color["name"], "Small", color["value"]),
			padding_left = 7,
		))

		layout.add_shape(TextBox(
			Box(20, GRID_HEIGHT - 3 * (i + 1), 4, 1, Stroke.SOLID, True, color["value"]),
			Text(color["name"], "Tiny", color["value"]),
			padding_left = 7,
		))

	return layout

def make_grid(r, c, stroke=Stroke.LIGHT, color=None):
	if color is None:
		color = BLACK

	layout = Layout()
	shapes = []

	# horizontal lines
	shapes.append(Box(0, 0, c, 0, stroke, color=color))
	for i in range(1, r):
		shapes.append(Box(0, i, c, 0, stroke, color=color))
	shapes.append(Box(0, r, c, 0, stroke, color=color))

	# vertical lines
	shapes.append(Box(0, 0, 0, r, stroke, color=color))
	for i in range(1, c):
		shapes.append(Box(i, 0, 0, r, stroke, color=color))
	shapes.append(Box(c, 0, 0, r, stroke, color=color))

	layout.add_shapes(shapes)
	
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
	for i in range(0, GRID_HEIGHT + 1):
		shapes.append(Box(0, i, GRID_WIDTH, 0, Stroke.LIGHT))

	# vertical lines
	for i in range(0, GRID_WIDTH + 1):
		shapes.append(Box(i, 0, 0, GRID_HEIGHT, Stroke.LIGHT))

	layout.add_shapes(shapes)
	
	return layout

def make_base_grid_outline():
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

def make_blank_title():
	layout = make_base_grid()
	layout.add_shape(Box(0, 0, GRID_WIDTH, GRID_HEIGHT, Stroke.DARKER))
	layout.add_shape(Box(0, GRID_HEIGHT - 2, GRID_WIDTH, 2, None, True))
	return layout

def make_title(color, title):
	layout = make_base_grid()
	layout.add_shape(TextBox(
		ColorBox(0, GRID_HEIGHT - 2, GRID_WIDTH, 2, color, Stroke.SOLID, color),
		Text(title, "Medium", WHITE),
		align_h = Align.START,
		padding_left = UNIT / 2,
	))

	return layout

def make_blank_title_double_horizontal():
	layout = make_base_grid()
	shapes = []

	shapes.append(Box(0, 0, GRID_WIDTH, 1, Stroke.BLANK, True))
	shapes.append(Box(0, GRID_HEIGHT // 2, GRID_WIDTH, 1, Stroke.BLANK, True))

	shapes.append(Box(0, 1, GRID_WIDTH, GRID_HEIGHT // 2 - 1, Stroke.DARKER))
	shapes.append(Box(0, GRID_HEIGHT // 2 + 1, GRID_WIDTH, GRID_HEIGHT // 2 - 1, Stroke.DARKER))
	
	shapes.append(Box(0, GRID_HEIGHT // 2 - 2, GRID_WIDTH, 2, None, True))
	shapes.append(Box(0, GRID_HEIGHT - 2, GRID_WIDTH, 2, None, True))

	layout.add_shapes(shapes)
	return layout

def add_month_header(color, calendar, month, left, right):
	width = CALENDAR_DAY_WIDTH
	height = CALENDAR_HEADER_HEIGHT

	left.add_shape(TextBox(
		ColorBox(0, GRID_HEIGHT - height, width, height, color, Stroke.SOLID, color),
		Text(calendar.months[month]["short"].upper(), "Big", WHITE),
		align_h = Align.START,
		padding_left = 5,
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

#		color = BLUE
#		if day == Weekday.SATURDAY or day == Weekday.SUNDAY:
#			color = RED
			
		side.add_shape(TextBox(
			Box(start_x + i * width, GRID_HEIGHT - height, width, height, Stroke.DARK, True),
			Text(WEEKDAY_NAMES[day.value]["short"], CALENDAR_HEADER_TEXT, color),
		))
	

def make_month(color, calendar, month, num_days, start_day, start_week=None):
	left = make_base_grid()
	right = make_base_grid()

	left.set_num_color(color)
	right.set_num_color(color)

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

	add_month_header(color, calendar, month, left, right)

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

#		color = LIGHT_BLUE
#		if WEEKDAYS[weekday] == Weekday.SATURDAY or WEEKDAYS[weekday] == Weekday.SUNDAY:
#			color = LIGHT_RED

		side.add_shape(Box(x, y, CALENDAR_DAY_WIDTH, height, Stroke.DARKER))
		side.add_shape(TextBox(
			Box(x, y + height - 1, CALENDAR_DAY_WIDTH, 1, None, True),
			Text(str(day + 1), "Tiny", color),
			align_h = Align.START,
			padding_left = 4,
		))

		if weekday == 0 and height == CALENDAR_DAY_HEIGHT and start_week is not None:
			left.add_shape(TextBox(
				Box(left_start_x - 1, y, 1, 1, None),
				Text(f"W\n{week + start_week}", "Tinier", color),
			))

		day = day + 1

		weekday = weekday + 1
		if weekday == 7:
			weekday = 0
			week = week + 1
	
	return left, right

def make_month_plan(color, calendar, month, num_days, start_day):
	left = make_base_grid()
	right = make_base_grid()

	left.set_num_color(color)
	right.set_num_color(color)

	half_width = GRID_WIDTH // 2
	half_height = GRID_HEIGHT // 2

	weekday_index = get_weekday_index(start_day) 
	for day in range(1, num_days + 1):
		right.add_shape(TextBox(
			Box(0, GRID_HEIGHT - day, 1, 1, None),
			Text(str(day), "Tiny", color),
		))
		right.add_shape(TextBox(
			Box(1, GRID_HEIGHT - day, 1, 1),
			Text(WEEKDAY_NAMES[WEEKDAYS[weekday_index].value]["long"][0], "Tiny", color),
		))
		weekday_index = weekday_index + 1
		if weekday_index == 7:
			weekday_index = 0
	
	left.add_shape(TextBox(
		ColorBox(0, GRID_HEIGHT - 2, GRID_WIDTH, 2, color, Stroke.SOLID, color),
		Text(calendar.months[month]["name"], "Big", WHITE),
		align_h = Align.START,
		padding_left = UNIT / 2,
	))

	left.add_shape(TextBox(
		Box(0, GRID_HEIGHT - 3, 4, 1, None, True),
		Text("This month", "Small", color),
	))

	
#	right.add_shape(Box(1, GRID_HEIGHT - num_days, 0, GRID_HEIGHT, Stroke.DARK))
#	right.add_shape(Box(2, GRID_HEIGHT - num_days, 0, GRID_HEIGHT, Stroke.DARK))
#	right.add_shape(Box(half_width, 0, 0, GRID_HEIGHT, Stroke.DARK))
#	right.add_shape(Box(0, GRID_HEIGHT - num_days, GRID_WIDTH // 2, 0, Stroke.DARK))

	return left, right
	
def make_weekly_layout(color, calendar, month, num_days, week, start_day):
	left = make_base_grid()
	right = make_base_grid()

	left.set_num_color(color)
	right.set_num_color(color)

	header_height = 2
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

#	left.add_shape(Box(0, GRID_HEIGHT - box_height, box_width, box_height, Stroke.DARKER, False, color))
	left.add_shape(ColorBox(0, GRID_HEIGHT - header_height, box_width, header_height, color, Stroke.SOLID, color))
	left.add_shape(TextBox(
		Box(0, GRID_HEIGHT - header_height, month_width, header_height),
		Text(month_str, "Big", WHITE),
		padding_left = UNIT / 2,
		align_h = Align.START,
	))
#	left.add_shape(Box(0, GRID_HEIGHT - header_height - 1, box_width, 1, None, True))
	
	left.add_shape(TextBox(
		Box(box_width - 2, GRID_HEIGHT - header_height, 2, 1, None, True),
		Text(f"W{week}", "Small", WHITE),
		align_h = Align.END,
		align_v = Align.END,
		padding_right = UNIT / 2,
		padding_bottom = 5,
	))
	left.add_shape(TextBox(
		Box(0, GRID_HEIGHT - header_height - 1, 4, 1, None, True),
		Text("Priorities", "Small", color),
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

		side.add_shape(Box(x, y_bottom, box_width, box_height, Stroke.DARKER, False))
		side.add_shape(Box(x, y_top - header_height, box_width, header_height, Stroke.DARKER, True))
		side.add_shape(Box(x, y_top - header_height, box_width, 0, Stroke.LIGHT, True))
		side.add_shape(TextBox(
			Box(x, y_top - header_height, num_width, header_height),
			Text(str(day), "Small", color),
		))

		side.add_shape(TextBox(
			Box(x + num_width, y_top - header_height, name_width, header_height),
			Text(WEEKDAY_NAMES[WEEKDAYS[i].value]["long"], "Small", color),
			padding_left = UNIT / 2,
			align_h = Align.START,
		))
	
	notes_box_height = GRID_HEIGHT - box_height - 1
	notes_height = 1
	notes_width = 3
	
	right.add_shape(Box(0, notes_box_height, GRID_WIDTH, 1, None, True))
	right.add_shape(Box(0, notes_box_height, 0, 1, Stroke.BLANK))
	right.add_shape(Box(GRID_WIDTH, notes_box_height, 0, 1, Stroke.BLANK))
	right.add_shape(Box(0, 0, GRID_WIDTH, notes_box_height, Stroke.LIGHT, False))
	right.add_shape(TextBox(
		ColorBox(0, notes_box_height - notes_height, notes_width, notes_height, color, Stroke.SOLID, color),
		Text("Notes", "Small", WHITE),
	))

	return left, right

def make_gregorian_year_page(color, year):
	greg = GregorianCalendar()
	layout = Layout(force_no_num=True)

	layout.set_num_color(color)

	gap_x = 1
	gap_y = 1

	for i in range(12):
		row = i // 3
		col = i - row * 3

		x = col * (7 + gap_x)
		y = GRID_HEIGHT - row * (8 + gap_y)
		
		layout.add_shape(TextBox(
			Box(x, y - 1, 7, 1, None, True),
			Text(greg.months[greg.month_order[i]]["name"].upper(), "Small", color),
		))

		for w in range(7):
			layout.add_shape(TextBox(
				Box(x + w, y - 2, 1, 1),
				Text(WEEKDAY_NAMES[WEEKDAYS[w].value]["long"][0], "Tiny", color),
			))
			
		layout.add_shape(Box(x, y - 2, 7, 0, Stroke.DARKER))

		start_day = greg.get_weekday_from_date(year, greg.month_order[i], 1)
		day_index = get_weekday_index(start_day)
		week = 0

		for day in range(greg.months[greg.month_order[i]]["days"]):
			layout.add_shape(TextBox(
				Box(x + day_index, y - week - 3, 1, 1),
				Text(str(day + 1), "Tiny", color),
			))
			day_index += 1
			if (day_index == 7):
				day_index = 0
				week += 1
	
	return layout

def make_monthly_planner(calendar, year, extra_pages):
	layouts = []
	for month in calendar.months:
		num_days = calendar.get_num_days_in_month(year, month)
		start_day = calendar.get_weekday_from_date(year, month, 1)
		left, right = make_month(LIGHT_BLUE, calendar, month, num_days, start_day, None)
		layouts.append(left)
		layouts.append(right)
	
	for i in range(extra_pages):
		base = make_base_grid_with_secret(GRID_HEIGHT, GRID_WIDTH, 7)
		layouts.append(base)

	return layouts

def make_planner(calendar, year, start_month, num_months):
	layouts = []
	month_index = calendar.get_month_index(start_month)

	layouts.append(make_gregorian_year_page(BLUE_GRAY, year))
	layouts.append(make_title(BLUE_GRAY, str(year)))

	quarter_colors = [TEAL, PURPLE, GREEN, ORANGE]

	for i in range(0, num_months):
		month = calendar.month_order[month_index + i]
		num_days = calendar.get_num_days_in_month(year, month) 

		start_day = calendar.get_weekday_from_date(year, month, 1)
		start_week = calendar.get_week_from_date(year, month, 1)

		left, right = make_month(quarter_colors[i // 3], calendar, month, num_days, start_day, start_week)
		layouts.append(left)
		layouts.append(right)
		left, right = make_month_plan(quarter_colors[i // 3], calendar, month, num_days, start_day)
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

				left, right = make_weekly_layout(quarter_colors[i // 3], calendar, prev_month, prev_month_num_days, week, start_day)
				layouts.append(left)
				layouts.append(right)
			start_day = 7 - start_weekday_index + 1
		else:
			start_day = 1

		while start_day < num_days:
			week = calendar.get_week_from_date(year, month, start_day)
			left, right = make_weekly_layout(quarter_colors[i // 3], calendar, month, num_days, week, start_day)
			layouts.append(left)
			layouts.append(right)
			start_day += 7
	
	return layouts
