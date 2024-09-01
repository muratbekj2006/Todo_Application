from django.shortcuts import get_object_or_404, redirect
from django.views import View
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
        self.list_obj = List.objects.get(id=self.kwargs['list_id'])
        return Task.objects.filter(list=self.list_obj).order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_obj'] = self.list_obj 
        return context
        

# CRUD Tasks
# Create
class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_form.html'
    form_class = TaskForm

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'

    def form_valid(self, form):
        list_id = self.kwargs['list_id']
        list_obj = List.objects.get(id=list_id)
        
        # For task list auto
        task = form.save(commit=False)
        task.list = list_obj
        
        # order of the list
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


# Toggle
class TaskToggleView(View):
    def post(self, request, list_id, task_id):
        task = get_object_or_404(Task, id=task_id)
        is_starred = request.POST.get('is_starred') == 'on'
        is_completed = request.POST.get('is_completed') == 'on'

        task.is_starred = is_starred
        task.is_completed = is_completed
        task.save()
        return redirect('task_detail', list_id=task.list.id, task_id=task.id)


class ListCreateView(CreateView):
    model = List
    fields = ['title']
    template_name = 'list_form.html'

    def get_success_url(self):
        return reverse_lazy('home')

class ListDeleteView(DeleteView):
    model = List
    template_name = 'list_delete_form.html'

    def get_success_url(self):
        return reverse_lazy('home')


