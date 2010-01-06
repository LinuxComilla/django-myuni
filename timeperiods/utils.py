import datetime

from models import Year, Semester

def get_current_year():
	try:
		return Year.objects.get(start__lte=datetime.datetime.now(), end__gte=datetime.datetime.now())
	except Year.DoesNotExist:
		return None

def get_current_semester():
	try:
		return Semester.objects.get(start__lte=datetime.datetime.now(), end__gte=datetime.datetime.now())
	except Semester.DoesNotExist:
		return None
