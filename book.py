from math import ceil 

from double_sided import *
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
	
	def render_signature(self, printer, sheets_per_signature, debug=False):
		layouts_per_printer_page = PAGE_ROWS * PAGE_COLS

		layouts = self.layouts
		sheets = ceil(len(layouts / 4))
		signatures = ceil(sheets / sheets_per_signature)

		for s in range(signatures):
			pass	
	
	def render_single(self, printer, max_pages=None, debug=False):
		db = DoubleSidedRenderer()

		layouts = self.layouts
		sheets = ceil(len(layouts) / 4)


		for sheet in range(sheets):
			top1_index = sheets * 4 - sheet * 2 - 1 
			bottom1_index = sheets * 4 - sheet * 2 - 2
			top2_index = sheet * 2
			bottom2_index = sheet * 2 + 1

			top1 = None
			top2 = None
			bottom1 = None
			bottom2 = None
			if top1_index < len(layouts):
				top1 = {
					"layout": layouts[top1_index],
					"side": Side.LEFT,
					"num": top1_index + 1,
				}
			if bottom1_index < len(layouts):
				bottom1 = {
					"layout": layouts[bottom1_index],
					"side": Side.RIGHT,
					"num": bottom1_index + 1,
				}
			if top2_index < len(layouts): 
				top2 = {
					"layout": layouts[top2_index],
					"side": Side.RIGHT,
					"num": top2_index + 1,
				}
			if bottom2_index < len(layouts):
				bottom2 = {
					"layout": layouts[bottom2_index],
					"side": Side.LEFT,
					"num": bottom2_index + 1,
				}

			db.add_leaf(top1, bottom1)
			db.add_leaf(top2, bottom2)

		db.render(printer, debug)

