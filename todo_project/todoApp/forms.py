from django import forms
from todoApp.models import Tasks

#create a form
class TasksForm(forms.ModelForm):
	class Meta:
		model = Tasks
		fields = '__all__'
		