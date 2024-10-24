from dataclasses import dataclass

from constants import *
from grid import *
from typeset import *

@dataclass
class ColorBox(object):
	x: int
	y: int
	width: int
	height: int
	color: Color
	stroke: Stroke = None

	def add_to_layout(self, layout):
		if self.width == 0 or self.height == 0:
			return

		box = Box(self.x, self.y, self.width, self.height, self.stroke, True)
		box.add_to_layout(layout)

		layout.rect.append(LayoutRect(self.x * UNIT, self.y * UNIT, self.width * UNIT, self.height * UNIT, self.color))

@dataclass
class Box(object):
	x: int
	y: int
	width: int
	height: int
	stroke: Stroke = None
	blank: bool = False
	color:  Color = None

	def add_to_layout(self, layout):
		if self.width == 0 and self.height == 0:
			return

		if self.width == 0 and self.stroke is not None:
			layout.grid.add_vertical_segment(self.x, self.y, self.y + self.height, self.stroke, self.color)
			return

		if self.height == 0 and self.stroke is not None:
			layout.grid.add_horizontal_segment(self.y, self.x, self.x + self.width, self.stroke, self.color)
			
		if self.blank:
			for i in range(1, self.width):
				layout.grid.add_vertical_segment(self.x + i, self.y, self.y + self.height, Stroke.BLANK)
			for i in range(1, self.height):
				layout.grid.add_horizontal_segment(self.y + i, self.x, self.x + self.width, Stroke.BLANK)

		if self.stroke is not None:
			layout.grid.add_horizontal_segment(self.y, self.x, self.x + self.width, self.stroke, self.color)
			layout.grid.add_horizontal_segment(self.y + self.height, self.x, self.x + self.width, self.stroke, self.color)
			layout.grid.add_vertical_segment(self.x, self.y, self.y + self.height, self.stroke, self.color)
			layout.grid.add_vertical_segment(self.x + self.width, self.y, self.y + self.height, self.stroke, self.color)

@dataclass
class Text(object):
	string: str
	size: str 
	color: Color = BLACK
	align: Side = Side.LEFT
	orientation: Orientation = Orientation.HORIZONTAL
	reverse: bool = False

@dataclass
class TextBox(object):
	box: Box
	text: Text
	align_h: Align = Align.CENTER
	align_v: Align = Align.CENTER
	padding_left: float = 0.0
	padding_right: float = 0.0
	padding_top: float = 0.0
	padding_bottom: float = 0.0

	def add_to_layout(self, layout):
		text = self.text
		box = self.box

		box.add_to_layout(layout)

		strings = render_textbox(self)
		for string in strings:
			layout.text.append(
				LayoutText(
					Text(
						string["string"],
						self.text.size,
						self.text.color,
						self.text.align,
						self.text.orientation,
						self.text.reverse,
					),
					string["x"],
					string["y"],
				)
			)

@dataclass
class LayoutText(object):
	text: Text
	x: float
	y: float

@dataclass
class LayoutRect(object):
	# Unit: pt
	x: int
	y: int
	width: int
	height: int
	color: Color

class Layout(object):
	def __init__(self, force_no_num=False):
		self.grid = Grid()
		self.text = []
		self.rect = []
		self.force_no_num = force_no_num
	
	def add_shape(self, shape):
		shape.add_to_layout(self)

	def add_shapes(self, shapes):
		for shape in shapes:
			shape.add_to_layout(self)
	
	def _render_rect(self, printer, rect, rx, ry):
		printer.draw_rectangle(rx + rect.x, ry + rect.y, rect.width, rect.height, rect.color)
	
	def _render_text(self, printer, layout_text, rx, ry):
		text = layout_text.text
		printer.draw_text(text.string, rx + layout_text.x, ry + layout_text.y, FONT["Sizes"][text.size], text.color, text.orientation, text.reverse)

	
	def render(self, printer, side, col, row, num=None):
		if not self.force_no_num and num is not None:
			t = Text(str(num), "Tiny", LIGHT_BLUE)
			if side == Side.LEFT:
				box = Box(0, 0, 1, 1)
			if side == Side.RIGHT:
				box = Box(GRID_WIDTH - 1, 0, 1, 1)
			TextBox(box, t).add_to_layout(self)

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

		for r in self.rect:
			self._render_rect(printer, r, x, y)

		self.grid.render(printer, x, y)

		for t in self.text:
			self._render_text(printer, t, x, y)

