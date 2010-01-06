from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from django.db.models import get_model

from models import Module, ModuleInstance

def module_detail(request, module_code, template='modules/module.html'):
	module = get_object_or_404(Module, code=module_code)
	data = { 'module': module }
	return render_to_response(template, data, context_instance=RequestContext(request))

def module_list(request, template='modules/module.list.html'):
	modules = Module.objects.all().order_by('code')
	data = { 'modules': modules }
	return render_to_response(template, data, context_instance=RequestContext(request))

def moduleinstance_detail(request, module_code, year, semester=None, template='modules/moduleinstance.html'):
	year_model = get_model('timeperiods', 'year')
	year = get_object_or_404(year_model, reference=year)
	
	if semester:
		semester_model = get_model('timeperiods', 'semester')
		semester = get_object_or_404(semester_model, year=year, type=semester)
		moduleinstance = get_object_or_404(ModuleInstance, semester=semester, module__code=module_code)
	else:
		moduleinstance = get_object_or_404(ModuleInstance, year=year, module__code=module_code)
	
	data = { 'module': moduleinstance, 'year': year, 'semester': semester }
	
	return render_to_response(template, data, context_instance=RequestContext(request))

def moduleinstance_list(request, year=None, semester=None, template='modules/moduleinstance.list.html'):
	if year:
		year_model = get_model('timeperiods', 'year')
		year = get_object_or_404(year_model, reference=year)
		
		if semester:
			if semester == 'full-year':
				data = { 'modules': year.modules.order_by('module__code'),
			 			 'year': year, 'semester': year }
			else:
			 	semester_model = get_model('timeperiods', 'semester')
				semester = get_object_or_404(semester_model, year=year, type=semester)
				data = { 'modules': semester.modules.order_by('module__code'),
						 'year': year, 'semester': semester }
		else:
			data = { 'modules': year.get_modules().all().order_by('-year', 'semester', 'module__code'),
						 'year': year }
	else:
		data = { 'modules': ModuleInstance.objects.current().order_by('-year', 'semester', 'module__code') }
		
	return render_to_response(template, data, context_instance=RequestContext(request))
