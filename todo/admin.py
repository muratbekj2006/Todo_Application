from django.contrib import admin
from .models import*
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'deadline', 'order', 'is_starred', 'is_completed')
    list_filter = ['list', 'is_starred', 'is_completed']

admin.site.register(List)
admin.site.register(Task, TaskAdmin)