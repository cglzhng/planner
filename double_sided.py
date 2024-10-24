from math import ceil

from constants import *
from utils import *

class DoubleSidedRenderer:
	def __init__(self):
		self.leafs = []
	
	def add_leaf(self, top, bottom):
		self.leafs.append({
			"top": top,
			"bottom": bottom,
		})

	def render(self, printer, debug=False):
		layouts_per_page = PAGE_ROWS * PAGE_COLS

		leafs = self.leafs
		sheets = ceil(len(leafs) / layouts_per_page)

		for sheet in range(sheets):
			if debug:
				printer.draw_center_rectangle()
			# top of each leaf
			for row in range(PAGE_ROWS):
				for col in range(PAGE_COLS):
					leaf_index = row * PAGE_ROWS + col + sheet * layouts_per_page
					if leaf_index < len(leafs):
						leaf = leafs[leaf_index]
						if leaf["top"] is not None:
							layout = leaf["top"]["layout"]
							side = leaf["top"]["side"]
							num = leaf["top"]["num"]
							layout.render(printer, side, col, PAGE_ROWS - row - 1, num)

			printer.next_page()

			if debug:
				printer.draw_center_rectangle()
			# bottom of each leaf
			for row in range(PAGE_ROWS):
				for col in range(PAGE_COLS):
					leaf_index = row * PAGE_ROWS + (PAGE_COLS - col - 1) + sheet * layouts_per_page
					if leaf_index < len(leafs):
						leaf = leafs[leaf_index]
						if leaf["bottom"] is not None:
							layout = leaf["bottom"]["layout"]
							side = leaf["bottom"]["side"]
							num = leaf["bottom"]["num"]
							layout.render(printer, side, col, PAGE_ROWS - row - 1, num)
		
			printer.next_page()
