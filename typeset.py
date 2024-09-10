from PIL import ImageFont

from constants import *
from utils import *

def render_textbox(textbox):
	text = textbox.text
	box = textbox.box

	box_x = box.x * UNIT
	box_y = box.y * UNIT
	box_width = box.width * UNIT
	box_height = box.height * UNIT

	pilfont = FONT["Styles"]["Regular"]["PILFonts"][text.size]

	if text.orientation == Orientation.HORIZONTAL:
		max_len = box_width - textbox.padding_left - textbox.padding_right
	if text.orientation == Orientation.VERTICAL:
		max_len = box_height - textbox.padding_top - textbox.padding_bottom

	strings = [] 

	words = text.string.split(" ")

	space_len = pilfont.getlength(" ")

	cur_string = ""
	cur_string_len = 0
	cur_word = ""
	cur_word_len = 0
	for c in text.string + " ": 
		if c == " " and cur_word != "":
			if cur_string != "":
				cur_string += " "
				cur_string_len += space_len
			if cur_string_len + cur_word_len > max_len and cur_string != "":
				strings.append({
					"string": cur_string,
					"length": cur_string_len
				})
				cur_string = ""
				cur_string_len = 0
			cur_string += cur_word
			cur_string_len += cur_word_len
			cur_word = ""
			cur_word_len = 0
		else:
			c_len = pilfont.getlength(c)	
			cur_word += c
			cur_word_len += c_len
	if cur_string != "":
		strings.append({
			"string": cur_string,
			"length": cur_string_len,
		})

	max_string_len = 0
	for string in strings:
		if string["length"] > max_string_len:
			max_string_len = string["length"] 
	
	eprint(max_len)
	eprint(strings)
	

	bbox = pilfont.getbbox("A")
	cap_height = (bbox[3] - bbox[1]) 
	line_height = FONT["LineHeights"][text.size] * cap_height
	offset = (line_height - cap_height) / 2
	girth = line_height * len(strings)
	eprint(cap_height)
	eprint(offset)

	# Bounding box width
	if text.orientation == Orientation.HORIZONTAL:
		text_width = max_string_len 
		text_height = girth
	if text.orientation == Orientation.VERTICAL:
		text_width = girth
		text_height = max_string_len 

	for i, string in enumerate(strings):
		x = box_x
		y = box_y
		if text.orientation == Orientation.HORIZONTAL:
			if textbox.align_h == Align.CENTER:
				t_x = (box_width - string["length"]) / 2
				x = box_x + t_x
			if textbox.align_h == Align.START:
				x = box_x + textbox.padding_left
			if textbox.align_h == Align.END:
				x = box_x + box_width - text_width - textbox.padding_right

			if textbox.align_v == Align.CENTER:
				t_y = (box_height - text_height) / 2
				y = box_y + t_y + (len(strings) - i - 1) * line_height + offset
	#		if self.align_v == Align.START:
	#			y = box_y + box_height - text_height - self.padding_top
	#		if self.align_v == Align.END:
	#			y = box_y + self.padding_bottom

		string["x"] = x
		string["y"] = y

	return strings

