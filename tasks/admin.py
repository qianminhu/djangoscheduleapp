from django.contrib import admin

# Register your models here.

from tasks.models import CurrentTask, TaskType

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'email', 'frequency', 'date_due')
    list_filter = ['task']
    search_fields = ['task']
#include 'person_in_charge',  in list display

admin.site.register(CurrentTask, TaskAdmin)
admin.site.register(TaskType)

