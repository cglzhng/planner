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

def get_month_index(month):
	for i in range(0, 12):
		if MONTHS[i] == month:
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

def get_num_days_in_month(year, month):
	if is_leap_year(year) and month == Month.FEBRUARY:
		return 29
	return MONTH_DAYS[month.value]

# Formula taken from https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
def get_weekday_from_date(year, month, day):
	k = day
	m = (month.value - 3) % 12 + 1
	C = year // 100
	Y = year % 100 
	if month == Month.JANUARY or month == Month.FEBRUARY:
		Y = Y - 1
	W = (k + math.floor(2.6 * m - 0.2) - 2 * C + Y + math.floor(Y / 4) + math.floor(C / 4)) % 7
	return Weekday((W - 1) % 7 + 1)

def get_doy_from_date(year, month, day):
	doy = 0
	month_index = 1
	while Month(month_index) != month:
		doy += get_num_days_in_month(year, Month(month_index))
		month_index += 1
	doy += day
	return doy

def get_week_from_date(year, month, day):
	week = get_doy_from_date(year, month, day) // 7 + 1
	# The first week of the year always contains Jan 4
	jan_four = get_weekday_from_date(year, Month.JANUARY, 4)
	if (jan_four.value > 4):
		week -= 1
	return week
