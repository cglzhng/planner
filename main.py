from constants import *
from utils import *

from grid import *
from printer import *
from layout import *
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

book = Book()

layout = make_test_grid(0, 5, Stroke.LIGHT)
layout.render(p, Side.TOP, 0, 0)

"""

layout = make_blank_grid_with_secret(GRID_HEIGHT, GRID_WIDTH, 5)


for i in range(0, 48):
 	book.add_layout(layout)



layout1, layout2 = make_month(31, Weekday.SATURDAY)
week1, week2 = make_weekly_layout(9, 18, 6)
book.add_layout(layout1)
book.add_layout(layout2)
book.add_layout(week1)
book.add_layout(week2)

book.render_display(p, debug=True)

"""


p.end()
