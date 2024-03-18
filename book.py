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
				Text(str(num), 9, 0, 4).render(x, y)
			if side == Side.RIGHT:
				Text(str(num), 9, (GRID_WIDTH - 1) * UNIT, 4).render(x, y)

		for t in self.text:
			t.render(x, y)

