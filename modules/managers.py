from django.db import models

from myuni.timeperiods.utils import get_current_year, get_current_semester

import datetime

class ModuleInstanceManager(models.Manager):
	def current(self):
		q = None
		if get_current_year() is not None:
			q = get_current_year().modules.all()
		if get_current_semester() is not None:
			q = q | get_current_semester().modules.all()
		return q
	
	def current_for(self, module):
		if isinstance(module, basestring):
			return self.current().filter(module__code=module)
		else:
			return self.current().filter(module=module)
