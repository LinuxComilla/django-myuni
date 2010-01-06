from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from schools.models import School

def school_detail(request, reference, template):
	school = School.objects.get(pk=reference)
	data = { 'school': school }
	return render_to_response(template, data, context_instance=RequestContext(request))
