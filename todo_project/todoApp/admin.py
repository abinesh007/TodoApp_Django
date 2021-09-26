from django.contrib import admin
from todoApp.models import Tasks

# Register your models here.
class TasksAdmin(admin.ModelAdmin):
	list = ['task_due','task_title','task_hint','task_description']

admin.site.register(Tasks,TasksAdmin)