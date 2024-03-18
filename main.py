from constants import *
from utils import *

from grid import *
from printer import *
from layout import *
from book import *

print_preamble()

print("""
newpath
0 0 0 1 setcmykcolor
0.12 setlinewidth
""")

book = Book()
page = make_blank_grid_with_secret(GRID_HEIGHT, GRID_WIDTH, 7)

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
