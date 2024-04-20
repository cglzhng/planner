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

TOP_MARGIN_BOTTOM_SIDE = 4.7
BOTTOM_MARGIN_BOTTOM_SIDE = 4

TOP_MARGIN_TOP_SIDE = 4.5 
BOTTOM_MARGIN_TOP_SIDE = 3.8

LEFT_MARGIN_BOTTOM_SIDE = 4
RIGHT_MARGIN_BOTTOM_SIDE = 4.8

LEFT_MARGIN_TOP_SIDE = 7
RIGHT_MARGIN_TOP_SIDE = 1.1

measurements = Measurements(
	top_line_count = TOP_LINE_COUNT,
	bottom_line_count = BOTTOM_LINE_COUNT,
	left_line_count = LEFT_LINE_COUNT,
	right_line_count = RIGHT_LINE_COUNT,
	top_margin_top_side = TOP_MARGIN_TOP_SIDE,
	bottom_margin_top_side = BOTTOM_MARGIN_TOP_SIDE,
	left_margin_top_side = LEFT_MARGIN_TOP_SIDE,
	right_margin_top_side = RIGHT_MARGIN_TOP_SIDE,
	top_margin_bottom_side = TOP_MARGIN_BOTTOM_SIDE,
	bottom_margin_bottom_side = BOTTOM_MARGIN_BOTTOM_SIDE,
	left_margin_bottom_side = LEFT_MARGIN_BOTTOM_SIDE,
	right_margin_bottom_side = RIGHT_MARGIN_BOTTOM_SIDE,
)

p = Printer(PAPER, PAPER_ORIENTATION, measurements)
p.start()

layout = make_blank_grid_with_secret(GRID_HEIGHT, GRID_WIDTH, 7)

book = Book()

for i in range(0, 11):
 	book.add_layout(layout)

book.render(p)

"""
page1, page2 = make_month(31, Weekday.SATURDAY)
book.add_page(page)
book.add_page(page1)
book.add_page(page2)

"""

p.end()
