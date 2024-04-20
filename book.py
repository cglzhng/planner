from math import ceil 

from utils import *
from grid import *

class Text(object):
	def __init__(self, text, size, color=BLACK, orientation=Orientation.HORIZONTAL):
		self.text = text
		self.size = size
		self.orientation = orientation
		self.color = color
		self.x = 0
		self.y = 0
	
	def set_to(self, x, y):
		self.x = x
		self.y = y
	
	def center_in(self, x, y, width, height):
		length = len(self.text) * self.size["size"] * self.size["width_ratio"]
		t_x = (width * UNIT - length) / 2
		t_y = (height * UNIT - self.size["size"] * self.size["height_ratio"]) / 2
		self.x = x * UNIT + t_x
		self.y = y * UNIT + t_y
		
	
	def render(self, printer, rx, ry):
		printer.draw_text(self.text, rx + self.x, ry + self.y, self.size["size"], self.color, self.orientation)

class Layout(object):
	def __init__(self):
		self.grid = Grid()
		self.text = []

	def add_text(self, text):
		self.text.append(text)
	
	def render(self, printer, side, col, row, num=None):
		width_full = printer.get_width()
		height_full = printer.get_height()

		width = GRID_WIDTH * UNIT
		height = GRID_HEIGHT * UNIT

		margin_x = (width_full - PAGE_COLS * width - (PAGE_COLS - 1) * GAP_COL) / 2

		x = margin_x + col * (width + GAP_COL)

		margin_y = (height_full - PAGE_ROWS * height - (PAGE_ROWS - 1) * GAP_ROW) / 2

		y = margin_y + row * (height + GAP_ROW)

		self.grid.render(printer, x, y)

		if num is not None:
			t = Text(str(num), FONT["Tiny"], LIGHT_PURPLE)
			if side == Side.LEFT:
				t.center_in(0, 0, 1, 1)
			if side == Side.RIGHT:
				t.center_in(GRID_WIDTH - 1, 0, 1, 1)
			t.render(printer, x, y)

		for t in self.text:
			t.render(printer, x, y)

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
						self.layouts[layout_index].render(printer, layout_side, x, y, layout_index + 1)
				i = i + 1
	
	def render(self, printer, max_pages=None):
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

		eprint(folds)

		for s in range(0, print_range):
			i = s * (layouts_per_page // 2)

			printer.draw_center_rectangle()

			to_render = []
			for l in range(0, ceil(layouts_per_page / 2)):
				if i + l < len(folds):
					fold = folds[i + l]
					eprint(fold)
					to_render.append((fold[3], Side.LEFT))
					to_render.append((fold[0], Side.RIGHT))
			self._render_layouts_by_index(printer, to_render)

								
			printer.next_page()
			printer.draw_center_rectangle()

			to_render = []
			for l in range(0, ceil(layouts_per_page / 2)):
				if i + l < len(folds):
					fold = folds[i + l]
					to_render.append((fold[1], Side.LEFT))
					to_render.append((fold[2], Side.RIGHT))
			self._render_layouts_by_index(printer, to_render)

			printer.next_page()


