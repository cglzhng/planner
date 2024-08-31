from constants import *
from utils import *

class GregorianCalendar(object):
	def __init__(self):
		self.months = {
			Month.JANUARY: {
				"name": "January",
				"short": "Jan",
				"days": 31,
			},
			Month.FEBRUARY: {
				"name": "February",
				"short": "Feb",
				"days": 28,
			},
			Month.MARCH: {
				"name": "March",
				"short": "Mar",
				"days": 31,
			},
			Month.APRIL: {
				"name": "April",
				"short": "Apr",
				"days": 30,
			},
			Month.MAY: {
				"name": "May",
				"short": "May",
				"days": 31,
			},
			Month.JUNE: {
				"name": "June",
				"short": "Jun",
				"days": 30,
			},
			Month.JULY: {
				"name": "July",
				"short": "Jul",
				"days": 31,
			},
			Month.AUGUST: {
				"name": "August",
				"short": "Aug",
				"days": 31,
			},
			Month.SEPTEMBER: {
				"name": "September",
				"short": "Sep",
				"days": 30,
			},
			Month.OCTOBER: {
				"name": "October",
				"short": "Oct",
				"days": 31,
			},
			Month.NOVEMBER: {
				"name": "November",
				"short": "Nov",
				"days": 30,
			},
			Month.DECEMBER: {
				"name": "December",
				"short": "Dec",
				"days": 31,
			},
		}
		self.month_order = [e for e in Month]

	def get_month_index(self, month):
		for i in range(0, 12):
			if self.month_order[i] is month:
				return i
		return None
	
	def get_num_days_in_month(self, year, month):
		if is_leap_year(year) and month is Month.FEBRUARY: 
			return 29
		return self.months[month]["days"]

	# Formula taken from https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
	def get_weekday_from_date(self, year, month, day):
		k = day
		m = (month.value - 3) % 12 + 1
		C = year // 100
		Y = year % 100 
		if month is Month.JANUARY or month is Month.FEBRUARY:
			Y = Y - 1
		W = (k + math.floor(2.6 * m - 0.2) - 2 * C + Y + math.floor(Y / 4) + math.floor(C / 4)) % 7
		return Weekday((W - 1) % 7 + 1)
	
	def get_doy_from_date(self, year, month, day):
		doy = 0
		month_index = 0
		while self.month_order[month_index] is not month:
			doy += self.get_num_days_in_month(year, self.month_order[month_index])
			month_index += 1
		doy += day
		return doy
	
	def get_week_from_date(self, year, month, day):
		week = self.get_doy_from_date(year, month, day) // 7 + 1
		# The first week of the year always contains Jan 4
		jan_four = get_weekday_from_date(year, Month.JANUARY, 4)
		if (jan_four.value > 4):
			week -= 1
		return week

class StaticCalendar(object):
	def __init__(self, spec):
		self.months = spec["months"]
		self.start_year = spec["start_year"]
		self.start_month = spec["start_month"]
		self.start_day = spec["start_day"]
		self.start_weekday = spec["start_weekday"]
		self.month_order = [e for e in self.months]	
	
		self._days_per_year = 0
		for month in self.months:
			self._days_per_year += self.months[month]["days"]

	def get_month_index(self, month):
		for i in range(0, len(self.months)):
			eprint(self.month_order[i])
			if self.month_order[i] == month:
				return i
		return None
	
	def get_num_days_in_month(self, year, month):
		return self.months[month]["days"]

	def get_doy_from_date(self, year, month, day):
		doy = 0
		month_index = 0
		while self.month_order[month_index] is not month:
			doy += self.get_num_days_in_month(year, self.month_order[month_index])
			month_index += 1
		doy += day
		return doy

	def get_weekday_from_date(self, year, month, day):
		eprint(f"{year} {month} {day}")
		days = 0
		if year == self.start_year:
			if month == self.start_month:
				days = day - self.start_day
			else:
				days += self.get_num_days_in_month(year, month) - self.start_day
				month_index = self.get_month_index(self.start_month)
				while (self.month_order[month_index] != month):
					days += self.get_num_days_in_month(None, month)
					month_index += 1
				days += day
		else:
			days = self.get_num_days_in_month(None, self.start_month) - self.start_day
			eprint(self.start_month)
			month_index = self.get_month_index(self.start_month)
			eprint(month_index)
			while (self.month_order[month_index] != self.month_order[-1]):
				days += self.get_num_days_in_month(None, month)
				month_index += 1
			days += self._days_per_year * (year - self.start_year - 1)
			month_index = 0
			while (self.month_order[month_index] != month):
				days += self.get_num_days_in_month(None, month)
				month_index += 1
			days += day

		return WEEKDAYS[(get_weekday_index(self.start_weekday) + days) % len(WEEKDAYS)]

	def get_week_from_date(self, year, month, day):
		week = self.get_doy_from_date(year, month, day) // 7 + 1
		return week
