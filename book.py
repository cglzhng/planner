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
	
	def render(self, side, num=None):
		if side == Side.LEFT:
			x = MARGIN_X
			y = MARGIN_Y
		if side == Side.RIGHT:
			x = A4_WIDTH - MARGIN_X - GRID_WIDTH * UNIT
			y = MARGIN_Y

		self.grid.render(x, y)

		if num is not None:
			if side == Side.LEFT:
				Text(str(num), 9, 5, 4).render(x, y)
			if side == Side.RIGHT:
				Text(str(num), 9, (GRID_WIDTH - 1) * UNIT + 5, 4).render(x, y)

		for t in self.text:
			t.render(x, y)

class Book:
	def __init__(self):
		self.pages = []
	
	def add_page(self, page):
		self.pages.append(page)
	
	def render(self):
		pages = self.pages
		for i in range(0, len(pages) // 4):
			if i + 3 < len(pages):
				pages[i + 3].render(Side.LEFT, i + 4)
			pages[i].render(Side.RIGHT, i + 1)
			print_showpage()
			if i + 1 < len(pages):
				pages[i + 1].render(Side.LEFT, i + 2)
			if i + 2 < len(pages):
				pages[i + 2].render(Side.RIGHT, i + 3)
			print_showpage()


