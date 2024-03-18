from constants import *
from utils import *

from grid import *
from printer import *
from layout import *
from book import *

def render_two_grids_on_a4(g1, g2):
	g1.render(Side.LEFT, 119)
	g2.render(Side.RIGHT)

print_preamble()

print("""
newpath
0 0 0 1 setcmykcolor
0.12 setlinewidth
""")

grid = make_blank_grid_with_secret(GRID_HEIGHT, GRID_WIDTH, 7)
render_two_grids_on_a4(grid, grid)

print(
"""
showpage
"""
)

print(
"""
%%Trailer
%%Pages: 1
%%DocumentNeededResources: font Courier-Bold Courier 
%%EOF
"""
)
