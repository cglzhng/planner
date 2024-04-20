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

TUMBLE_TOP_MARGIN_BOTTOM_SIDE = 4.7
TUMBLE_BOTTOM_MARGIN_BOTTOM_SIDE = 4

TUMBLE_TOP_MARGIN_TOP_SIDE = 4.5 
TUMBLE_BOTTOM_MARGIN_TOP_SIDE = 3.8

TUMBLE_LEFT_MARGIN_BOTTOM_SIDE = 4
TUMBLE_RIGHT_MARGIN_BOTTOM_SIDE = 4.8

TUMBLE_LEFT_MARGIN_TOP_SIDE = 7
TUMBLE_RIGHT_MARGIN_TOP_SIDE = 1.1

NOTUMBLE_LEFT_MARGIN_BOTTOM_SIDE = 5.5
NOTUMBLE_RIGHT_MARGIN_BOTTOM_SIDE = 3.5

NOTUMBLE_LEFT_MARGIN_TOP_SIDE = 6.5
NOTUMBLE_RIGHT_MARGIN_TOP_SIDE = 1.5

NOTUMBLE_TOP_MARGIN_BOTTOM_SIDE = 4.1
NOTUMBLE_BOTTOM_MARGIN_BOTTOM_SIDE = 4.1

NOTUMBLE_TOP_MARGIN_TOP_SIDE = 4.8
NOTUMBLE_BOTTOM_MARGIN_TOP_SIDE = 3.3

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


p.debug_center_rectangle_duplex()

"""

layout = make_blank_grid_with_secret(GRID_HEIGHT, GRID_WIDTH, 7)

book = Book()

for i in range(0, 11):
 	book.add_layout(layout)

book.render(p)

page1, page2 = make_month(31, Weekday.SATURDAY)
book.add_page(page)
book.add_page(page1)
book.add_page(page2)

"""

p.end()
