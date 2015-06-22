

# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import CurrentTask
from django.views.generic import WeekArchiveView


urlpatterns = patterns('', (r'^(?P<year>d{4})/(?P<week>d{2})/$', date_based.archive_week, tasks_list)



def index(request):
    latest_task_list = CurrentTask.objects.order_by('-date_due')[:20]
    output = ', '.join([(p.task + ": " + p.person_in_charge) for p in latest_task_list])
    return HttpResponse("EatWith Office Tasks \n" + output)
    # change format of what to return (save as another variable?)



"""def detail(request, tasks):
    return HttpResponse("You're looking at task %s." % tasks)

def results(request, tasks):
    response = "You're looking at the results of task %s."
    return HttpResponse(response % tasks)


class IndexView(generic.ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'latest_task_list'

    def get_queryset(self):
        return CurrentTask.objects.order_by('-date_due')[:20]"""

