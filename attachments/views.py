from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from django.contrib.auth.models import User

from forms import AttachmentForm

def new_attachment(request, attach_to=None, template_name='uploads/new_upload.html', extra_context={}, success_url=None):
	if attach_to is None: attach_to = request.user
	if request.method == 'POST':
		form = AttachmentForm(request.POST, request.FILES)
		if form.is_valid():
			success = form.save(request, attach_to)
			if success_url is not None:
				return HttpResponseRedirect(success_url)
			return HttpResponseRedirect(attach_to.get_absolute_url())
	else:
		form = AttachmentForm()
	
	data = {'form': form}
	data.update(extra_context)
	return render_to_response(template_name, data, context_instance=RequestContext(request))
