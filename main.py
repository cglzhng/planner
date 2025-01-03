from constants import *
from utils import *

from calendar import *
from grid import *
from printer import *
from layouts import *
from book import *

# Values obtained from calibration prints and measuring with a ruler

BOTTOM_LINE_COUNT = 7
TOP_LINE_COUNT = 7
LEFT_LINE_COUNT = 7
RIGHT_LINE_COUNT = 8

TUMBLE_TOP_MARGINS = Margins(
	top=4.5,
	bottom=3.8,
	left=7,
	right=1.1,
)

TUMBLE_BOTTOM_MARGINS = Margins(
	top=4.7,
	bottom=4,
	left=4,
	right=4.8,
)

NOTUMBLE_TOP_MARGINS = Margins(
	top=4.8,
	bottom=3.3,
	left=7,
	right=1,
)

NOTUMBLE_BOTTOM_MARGINS = Margins(
	top=4.1,
	bottom=4.1,
	left=5.1,
	right=3.5,
)

measurements = Measurements(
	top_line_count = TOP_LINE_COUNT,
	bottom_line_count = BOTTOM_LINE_COUNT,
	left_line_count = LEFT_LINE_COUNT,
	right_line_count = RIGHT_LINE_COUNT,

	tumble_top_margins = TUMBLE_TOP_MARGINS,
	tumble_bottom_margins = TUMBLE_BOTTOM_MARGINS,
	
	notumble_top_margins = NOTUMBLE_TOP_MARGINS,
	notumble_bottom_margins = NOTUMBLE_BOTTOM_MARGINS,
)

p = Printer(PAPER, PAPER_ORIENTATION, measurements)
p.start()

plain_book = Book()
planner_book = Book()
display_book = Book()

sv = StaticCalendar(SV_CALENDAR_SPEC)
greg = GregorianCalendar()

layouts = make_planner(greg, 2024, Month.JANUARY, 12)
for layout in layouts:
	planner_book.add_layout(layout)
planner_book.render_signature(p, 4, debug=False)



"""
layout = make_base_grid_with_secret(GRID_HEIGHT, GRID_WIDTH, 5)
blank = make_blank_layout()

plain_book.add_layout(blank)
for i in range(0, 78):
	layout = make_base_grid_with_secret(GRID_HEIGHT, GRID_WIDTH, 5)
	plain_book.add_layout(layout)
plain_book.add_layout(blank)

plain_book.render_signature(p, 4, debug=False)



spring1, spring2 = make_month(sv, "Spring", 28, Weekday.MONDAY)
planner_book.add_layout(blank)
layouts = make_monthly_planner(sv, 2, 6)
for layout in layouts:
	planner_book.add_layout(layout)
planner_book.add_layout(blank)
planner_book.render(p, debug=False)

planner_book.add_layout(blank)
layouts = make_planner(greg, 2024, Month.APRIL, 1)
for layout in layouts:
	planner_book.add_layout(layout)
planner_book.add_layout(blank)

title = make_blank_title()
display_book.add_layout(title)
horizontal_double_page = make_blank_title_double_horizontal()
display_book.add_layout(horizontal_double_page)

typeset = make_typeset_test()
display_book.add_layout(typeset)

plain = make_base_grid_with_secret(GRID_HEIGHT, GRID_WIDTH, 5)

week1, week2 = make_weekly_layout(greg, Month.OCTOBER, 31, 18, 6)
display_book.add_layout(week1)
display_book.add_layout(week2)

year_page = make_gregorian_year_page(2024)
display_book.add_layout(year_page)

title_page = make_title("2024", BLUE_GRAY)
display_book.add_layout(title_page)

plan1, plan2 = make_month_plan(greg, Month.DECEMBER, 31, Weekday.SATURDAY)
display_book.add_layout(plan1)
display_book.add_layout(plan2)

week1, week2 = make_weekly_layout(greg, Month.OCTOBER, 31, 18, 6)
display_book.add_layout(week1)
display_book.add_layout(week2)

color_test = make_color_test(grid=False)
display_book.add_layout(color_test)

display_book.render_single(p, debug=False)
display_book.render_display(p, debug=False)

"""

p.end()
