from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Max
# Create your views here.
from .forms import TaskForm
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
        

# CRUD Tasks
# Create
class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    form_class = TaskForm

    def form_valid(self, form):
        task = form.save(commit=False)
        max_order = Task.objects.filter(list=task.list).aggregate(Max('order'))['order__max'] or 0
        task.order = max_order + 1
        task.save()
        return super().form_valid(form) 

    def get_success_url(self):
        return reverse_lazy('todolist', kwargs={'list_id': self.object.list.id})

# Read
class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

    def get_object(self):
        list_id = self.kwargs['list_id']
        task_id = self.kwargs['task_id']
        return get_object_or_404(Task, id=task_id, list_id=list_id)

# Update
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'

    def get_success_url(self):
        return reverse_lazy('todolist', kwargs={'list_id': self.object.list.id})

# Delete
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete_form.html'

    def get_success_url(self):
        return reverse_lazy('todolist', kwargs={'list_id': self.object.list.id})


class ListCreateView(CreateView):
    model = List
    fields = ['title']
    template_name = 'list_form.html'

    def get_success_url(self):
        return reverse_lazy('home')

