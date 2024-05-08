from math import ceil 

from utils import *
from grid import *

class Text(object):
	def __init__(self, text, size, color=BLACK, orientation=Orientation.HORIZONTAL, reverse=False):
		self.text = text
		self.size = size
		self.orientation = orientation
		self.reverse = reverse
		self.color = color
		self.x = 0
		self.y = 0
	
	def set_to(self, x, y):
		self.x = x
		self.y = y
	
	def center_in(self, x, y, width, height):
		text_length = len(self.text) * self.size["size"] * self.size["width_ratio"]
		text_height = self.size["size"] * self.size["height_ratio"]

		if self.orientation == Orientation.HORIZONTAL:
			r_width = width * UNIT
			r_height = height * UNIT
			r_x = x * UNIT
			r_y = y * UNIT
		else:
			r_width = height * UNIT
			r_height = width * UNIT
			r_x = (x + width) * UNIT
			r_y = y * UNIT

		t_x = (r_width - text_length) / 2
		t_y = (r_height - text_height) / 2
		
		if self.orientation == Orientation.HORIZONTAL:
			self.x = r_x + t_x
			self.y = r_y + t_y
		if self.orientation == Orientation.VERTICAL:
			self.x = r_x - t_y
			self.y = r_y + t_x
	
	def render(self, printer, rx, ry):
		printer.draw_text(self.text, rx + self.x, ry + self.y, self.size["size"], self.color, self.orientation, self.reverse)

class Layout(object):
	def __init__(self):
		self.grid = Grid()
		self.text = []

	def add_text(self, text):
		self.text.append(text)
	
	def render(self, printer, side, col, row, num=None):
		page_width = printer.get_width()
		page_height = printer.get_height()

		width = GRID_WIDTH * UNIT
		height = GRID_HEIGHT * UNIT

		page_margin_x = printer.get_margin_x()
		page_margin_y = printer.get_margin_y()

		if GAP_COL == 0:
			gap_col = ((page_width + 2 * page_margin_x) - PAGE_COLS * width) / PAGE_COLS
			margin_col = gap_col / 2
		else:
			gap_col = GAP_COL
			margin_col = (page_width + 2 * page_margin_x - PAGE_COLS * width - (PAGE_COLS - 1) * GAP_COL) / 2

		margin_x = margin_col - page_margin_x 

		x = margin_x + col * (width + gap_col)

		if GAP_ROW == 0:
			gap_row = ((page_height + 2 * page_margin_y) - PAGE_ROWS * height) / PAGE_ROWS
			margin_row = gap_row / 2
		else:
			gap_row = GAP_ROW
			margin_row = (page_height + 2 * page_margin_y - PAGE_ROWS * height - (PAGE_ROWS - 1) * GAP_ROW) / 2

		margin_y = margin_row - page_margin_y

		y = margin_y + row * (height + gap_row)

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


