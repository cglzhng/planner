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

class Page(object):
	def __init__(self):
		self.grid = Grid()
		self.text = []

	def add_text(self, text):
		self.text.append(text)
	
	def render(self, printer, side, num=None):
		width_full = printer.get_width()
		height_full = printer.get_height()

		width = GRID_WIDTH * UNIT
		height = GRID_HEIGHT * UNIT

		margin_x = (width_full - 2 * width - MARGIN_GAP) / 2

		if side == Side.LEFT:
			x = margin_x
		if side == Side.RIGHT:
			x = width_full - margin_x - width

		y = (height_full - height) / 2

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
		self.pages = []
	
	def add_page(self, page):
		self.pages.append(page)
	
	def render(self, printer, num_spreads=None):
		pages = self.pages
		sheets = ceil(len(pages) / 4)

		print_range = sheets
		if num_spreads != None:
			print_range = min(sheets, ceil(num_spreads / 2))

		for s in range(0, print_range):
			i = s * 2 

			printer.draw_center_rectangle()

			# the ith last page
			n = sheets * 4 - i - 1
			if n < len(pages):
				pages[n].render(printer, Side.LEFT, n + 1)

			# the ith page
			pages[i].render(printer, Side.RIGHT, i + 1)

			printer.next_page()
			printer.draw_center_rectangle()

			if num_spreads != None and num_spreads % 2 == 1:
				break

			# the (i + 1)th page
			n = i + 1
			if n < len(pages):
				pages[n].render(printer, Side.LEFT, n + 1)

			# the (i + 1)th last page
			n = sheets * 4 - i - 2
			if n < len(pages):
				pages[n].render(printer, Side.RIGHT, n + 1)

			printer.next_page()


