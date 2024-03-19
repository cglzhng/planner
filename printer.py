from constants import *

def print_stroke(stroke):
	if stroke == Stroke.LIGHT:
		print("LIGHT")
	if stroke == Stroke.DARK:
		print("DARK")

def print_line(x1, y1, x2, y2):
	print(f"{x1} {y1} {x2} {y2} LINE")

def print_text_horizontal(text, size, x, y):
	print(f"{-x} {-y} ({text}) {x} {y} /Iosevka findfont {size} scalefont setfont T_HORIZ")

def print_showpage():
	print("showpage")

def print_newpath():
	print("newpath")
	print("0 0 0 1 setcmykcolor")
	print("0.12 setlinewidth")

def print_preamble():
	print("""
%!PS-Adobe-3.0
%%BoundingBox: 24 24 571 818
%%Orientation: Portrait
%%Pages: (atend)
%%DocumentMedia: A4 595 842 0 () ()
%%DocumentNeededResources: (atend)
%%EndComments
%%BeginPageSetup
<< /PageSize [595 842] /Duplex true /Tumble true >> setpagedevice
%%EndPageSetup
/LINE { newpath moveto lineto } def
/LIGHT { [0.20 0.80] 0.10 setdash stroke } def
/DARK { [0.20 0.40] 0.10 setdash stroke } def
/T_HORIZ {
translate
270 rotate
0 0 moveto
show
90 rotate
translate
} def
""")
