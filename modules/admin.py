from django.contrib import admin
from models import Module, ModuleInstance, ModuleInstanceForm

class ModuleInstanceAdmin(admin.ModelAdmin):
	form = ModuleInstanceForm

admin.site.register(Module)
admin.site.register(ModuleInstance, ModuleInstanceAdmin)
