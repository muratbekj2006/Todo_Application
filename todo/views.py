from django.shortcuts import render
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
