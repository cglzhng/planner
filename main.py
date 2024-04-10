from constants import *
from utils import *

from grid import *
from printer import *
from layout import *
from book import *

test_insert_segment()

print_preamble()

book = Book()

page = make_blank_grid_with_secret(GRID_HEIGHT, GRID_WIDTH, 7)

"""
for i in range(0, 48):
	book.add_page(page)
"""

page1, page2 = make_month(31, Weekday.SATURDAY)
book.add_page(page)
book.add_page(page1)
book.add_page(page2)



book.render()

print(
"""
%%Trailer
%%Pages: 1
%%DocumentNeededResources: font Courier-Bold Courier 
%%EOF
"""
)
