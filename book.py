from math import ceil 

from utils import *
from grid import *

class Text(object):
	def __init__(self, text, size, x, y, color=BLACK, orientation=Orientation.HORIZONTAL):
		self.text = text
		self.size = size
		self.x = x
		self.y = y
		self.orientation = orientation
		self.color = color
	
	def render(self, rx, ry):
		x_real = ry + self.y
		y_real = A4_WIDTH - rx - self.x

		print_text_horizontal(self.text, self.size, x_real, y_real, self.color)

class Page(object):
	def __init__(self):
		self.grid = Grid()
		self.text = []
	
	def render(self, face, side, num=None):
		if face == Side.TOP:
			margin_x = MARGIN_X_TOP_SHEET
			margin_y = MARGIN_Y_TOP_SHEET
		if face == Side.BOTTOM:
			margin_x = MARGIN_X_BOTTOM_SHEET
			margin_y = MARGIN_Y_BOTTOM_SHEET
		if side == Side.LEFT:
			x = margin_x
			y = margin_y
		if side == Side.RIGHT:
			x = margin_x + GRID_WIDTH * UNIT + MARGIN_GAP
			y = margin_y

		self.grid.render(x, y)

		if num is not None:
			if side == Side.LEFT:
				Text(str(num), 7, 4, 3, PAGE_NUMBER_COLOR).render(x, y)
			if side == Side.RIGHT:
				Text(str(num), 7, (GRID_WIDTH - 1) * UNIT + 4, 3, PAGE_NUMBER_COLOR).render(x, y)

		for t in self.text:
			t.render(x, y)

class Book:
	def __init__(self):
		self.pages = []
	
	def add_page(self, page):
		self.pages.append(page)
	
	def render(self, num_spreads=None):
		pages = self.pages
		sheets = ceil(len(pages) / 4)

		print_range = sheets
		if num_spreads != None:
			print_range = min(sheets, ceil(num_spreads / 2))

		eprint(print_range)

		for s in range(0, print_range):
			i = s * 2 

			print_newpath()

			# the ith last page
			n = sheets * 4 - i - 1
			if n < len(pages):
				pages[n].render(Side.TOP, Side.LEFT, n + 1)

			# the ith page
			pages[i].render(Side.TOP, Side.RIGHT, i + 1)

			print_showpage()

			if num_spreads != None and num_spreads % 2 == 1:
				break

			print_newpath()

			# the (i + 1)th page
			n = i + 1
			if n < len(pages):
				pages[n].render(Side.BOTTOM, Side.LEFT, n + 1)

			# the (i + 1)th last page
			n = sheets * 4 - i - 2
			if n < len(pages):
				pages[n].render(Side.BOTTOM, Side.RIGHT, n + 1)
			print_showpage()


