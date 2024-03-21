from constants import *
from utils import *

from grid import *
from printer import *
from layout import *
from book import *

print_preamble()

book = Book()
page = make_blank_grid_with_secret(GRID_HEIGHT, GRID_WIDTH, 7)

book.add_page(page)
book.add_page(page)
book.add_page(page)
book.add_page(page)
book.add_page(page)
book.add_page(page)
book.add_page(page)

book.render()

print(
"""
%%Trailer
%%Pages: 1
%%DocumentNeededResources: font Courier-Bold Courier 
%%EOF
"""
)
