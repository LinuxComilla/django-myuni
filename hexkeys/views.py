from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.conf import settings

from models import Hexkey

def redirect(self, hexkey):
	p = get_object_or_404(Hexkey, key=hexkey)
	obj = p.object
	if not hasattr(obj, 'get_absolute_url'):
		raise Http404
	return HttpResponseRedirect(obj.get_absolute_url())
