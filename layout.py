from book import *

# grid with r rows and c columns
# hobonichi secret line at column s
def make_blank_grid_with_secret(r, c, s):
	page = Page()

	# horizontal lines	
	page.grid.add_horizontal_segment(0, 0, c, Stroke.DARK)
	for i in range(1, r):
		page.grid.add_horizontal_segment(i, 0, c, Stroke.LIGHT)
	page.grid.add_horizontal_segment(r, 0, c, Stroke.DARK)

	# vertical lines
	page.grid.add_vertical_segment(0, 0, r, Stroke.DARK)
	for i in range(1, c):
		page.grid.add_vertical_segment(i, 0, r, Stroke.LIGHT)
	page.grid.add_vertical_segment(s, 0, r, Stroke.DARK)
	page.grid.add_vertical_segment(c, 0, r, Stroke.DARK)
	
	return page

