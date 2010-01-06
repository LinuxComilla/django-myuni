from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
def resolve_semester(value):
	if value == 'autumn':
		return "Autumn Semster"
	elif value == 'spring':
		return "Spring Semester"
	else: return None

register.filter('resolve_semester', resolve_semester)
