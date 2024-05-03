from constants import *

def print_set_color(color):
	print(f"{color.c} {color.m} {color.y} {color.k} setcmykcolor")

def print_stroke(stroke):
	if stroke == Stroke.LIGHT:
		print("LIGHT")
	if stroke == Stroke.DARK:
		print("DARK")
	if stroke == Stroke.DARKER:
		print("DARKER")
	if stroke == Stroke.SOLID:
		print("SOLID")

def print_line(x1, y1, x2, y2):
	print(f"{x1} {y1} {x2} {y2} LINE")

def print_text_vertical(text, size, x, y, color):
	print_set_color(color)
	print(f"{-x} {-y} ({text}) {x} {y} /PlannerFont findfont {size} scalefont setfont T_HORIZ")

def print_text_horizontal(text, size, x, y, color):
	print_set_color(color)
	print(f"({text}) {x} {y} /PlannerFont findfont {size} scalefont setfont T_VERT")

def print_showpage():
	print("showpage")

def print_newpath():
	print("newpath")
	print("0 0 0 1 setcmykcolor")
	print("0.12 setlinewidth")

def print_preamble(paper):
	name = paper["name"]
	height = paper["height"]
	width = paper["width"]

	light_stroke = STROKES[UNIT][Stroke.LIGHT.value]
	dark_stroke = STROKES[UNIT][Stroke.DARK.value]
	darker_stroke = STROKES[UNIT][Stroke.DARKER.value]

	print("""
%!PS-Adobe-3.0
""")
	print(f"""
%%BoundingBox: 0 0 {width - 0} {height - 0}
""")
	print("""
%%Orientation: Portrait
%%Pages: (atend)
""")
	print(f"""
%%DocumentMedia: {name} {width} {height} 0 () ()
""")
	print("""
%%DocumentNeededResources: (atend)
%%EndComments
%%BeginPageSetup
""")
	print(f"""
<< /PageSize [{width} {height}] /Duplex true /Tumble {'true' if PAPER_ORIENTATION == Orientation.HORIZONTAL else 'false'} >> setpagedevice
""")
	print("""
%%EndPageSetup
/LINE { newpath moveto lineto } def
/SOLID { [] 0 setdash stroke } def
/T_VERT { moveto show } def
/T_HORIZ {
translate
270 rotate
0 0 moveto
show
90 rotate
translate
} def
""")
	print(f"""
/LIGHT {{ {light_stroke} setdash stroke }} def
/DARK {{ {dark_stroke} setdash stroke }} def
/DARKER {{ {darker_stroke} setdash stroke }} def
""")
	print_font()

def print_font():
	with open(f"{FONT_FILE}") as f:
		print(f.read())

def print_end():
	print("""
	%%Trailer
	%%Pages: 1
	%%DocumentNeededResources: font Courier-Bold Courier 
	%%EOF
""")
