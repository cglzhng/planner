from math import ceil 

from utils import *
from grid import *

class Text(object):
	def __init__(self, text, size, x, y, orientation=Orientation.HORIZONTAL):
		self.text = text
		self.size = size
		self.x = x
		self.y = y
		self.orientation = orientation
	
	def render(self, rx, ry):
		x_real = ry + self.y
		y_real = A4_WIDTH - rx - self.x

		print_text_horizontal(self.text, self.size, x_real, y_real)
			

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
			x = A4_WIDTH - margin_x - GRID_WIDTH * UNIT
			y = margin_y

		self.grid.render(x, y)

		if num is not None:
			if side == Side.LEFT:
				Text(str(num), 7, 4, 3).render(x, y)
			if side == Side.RIGHT:
				Text(str(num), 7, (GRID_WIDTH - 1) * UNIT + 4, 3).render(x, y)

		for t in self.text:
			t.render(x, y)

class Book:
	def __init__(self):
		self.pages = []
	
	def add_page(self, page):
		self.pages.append(page)
	
	def render(self):
		pages = self.pages

		for i in range(0, ceil(len(pages) / 4)):

			print_newpath()
			if i * 4 + 3 < len(pages):
				pages[i * 4 + 3].render(Side.TOP, Side.LEFT, i * 4 + 4)

			pages[i].render(Side.TOP, Side.RIGHT, i * 4 + 1)
			print_showpage()

			print_newpath()
			if i * 4 + 1 < len(pages):
				pages[i * 4 + 1].render(Side.BOTTOM, Side.LEFT, i * 4 + 2)
			if i * 4 + 2 < len(pages):
				pages[i * 4 + 2].render(Side.BOTTOM, Side.RIGHT, i * 4 + 3)
			print_showpage()


