from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import*

class HomePageView(ListView):
    model = List
    template_name = 'index.html'
    context_object_name = 'list_types'

class TodoListView(ListView):
    model = Task
    template_name = 'todo_list.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        list_obj = List.objects.get(id=self.kwargs['list_id'])
        return Task.objects.filter(list=list_obj)

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

    def get_object(self):
        list_id = self.kwargs['list_id']
        task_id = self.kwargs['task_id']
        return get_object_or_404(Task, id=task_id, list_id=list_id)

    
