import sys
import math

from constants import *

def mm_to_point(x):
	return x * 2.83465

def point_to_mm(x):
	return x * 0.352778

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def get_weekday_index(day):
	for i in range(0, 7):
		if WEEKDAYS[i] == day:
			return i
	return None

def is_leap_year(year):
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	return False

