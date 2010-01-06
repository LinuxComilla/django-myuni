from django import forms
from django.db.models import get_model

person_model = get_model('people', 'Person')

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = person_model
		fields = ['username', 'first_name', 'last_name', 'email']
