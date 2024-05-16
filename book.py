from math import ceil 

from layout import *
from utils import *
from grid import *

class Book:
	def __init__(self):
		self.layouts = []
	
	def add_layout(self, layout):
		self.layouts.append(layout)
	
	def _render_layouts_by_index(self, printer, layout_params):
		i = 0 
		for y in range(0, PAGE_ROWS):
			for x in range(0, PAGE_COLS):
				if i < len(layout_params):
					layout_index, layout_side = layout_params[i]
					if layout_index < len(self.layouts):
						self.layouts[layout_index].render(printer, layout_side, x, PAGE_ROWS - y - 1, layout_index + 1)
				i = i + 1
	
	def render_display(self, printer, debug=False):
		layouts_per_page = PAGE_ROWS * PAGE_COLS
		num_pages = ceil(len(self.layouts) / layouts_per_page)

		for i in range(0, num_pages):
			if debug:
				printer.draw_center_rectangle()

			to_render = []
			for j in range(0, layouts_per_page):
				to_render.append((i * layouts_per_page + j, Side.LEFT if j % 2 == 0 else Side.RIGHT))
			self._render_layouts_by_index(printer, to_render)
			eprint(to_render)
			printer.next_page()

	
	def render(self, printer, max_pages=None, debug=False):
		layouts_per_page = PAGE_ROWS * PAGE_COLS

		layouts = self.layouts
		sheets = ceil(len(layouts) / (layouts_per_page * 2))

		print_range = sheets
		if max_pages != None:
			print_range = min(pages, ceil(max_pages / 2))

		folds = []
		num_folds = ceil(len(self.layouts) / 4)
		for f in range(0, num_folds):
			fold = [
				f * 2,
				f * 2 + 1,
				num_folds * 4 - (f * 2 + 1) - 1,
				num_folds * 4 - (f * 2) - 1,
			]
			folds.append(fold)

		for s in range(0, print_range):
			i = s * (layouts_per_page // 2)

			if debug:
				printer.draw_center_rectangle()

			to_render = []
			for l in range(0, ceil(layouts_per_page / 2)):
				if i + l < len(folds):
					fold = folds[i + l]
					to_render.append((fold[3], Side.LEFT))
					to_render.append((fold[0], Side.RIGHT))
			self._render_layouts_by_index(printer, to_render)

								
			printer.next_page()

			if debug:
				printer.draw_center_rectangle()

			to_render = []
			for l in range(0, ceil(layouts_per_page / 2)):
				if i + l < len(folds):
					fold = folds[i + l]
					to_render.append((fold[1], Side.LEFT))
					to_render.append((fold[2], Side.RIGHT))
			self._render_layouts_by_index(printer, to_render)

			printer.next_page()


