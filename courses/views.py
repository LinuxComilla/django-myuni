from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import Course, CourseType

def courses_list(request, type_slug='all', template='courses/course.list.html'):
	type = None
	if (type_slug == 'all'):
		courses = Course.objects.all()
	else:
		type = get_object_or_404(CourseType,slug=type_slug)
		courses = Course.objects.filter(type=type)
	course_types = CourseType.objects.all()
	data = { 'courses': courses, 'course_types': course_types, 'course_type': type }
	return render_to_response(template, data, context_instance=RequestContext(request))

def course_detail(request, course_code, template='courses/course.html'):
	course = get_object_or_404(Course, code=course_code)
	data = { 'course' : course }
	return render_to_response(template, data, context_instance=RequestContext(request))
