from django.urls import path
from .views import*
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('todo-list/<int:list_id>/', TodoListView.as_view(), name='todolist'),
    path('todo-list/<int:list_id>/<int:task_id>/', TaskDetailView.as_view(), name='task_detail'),
    path('todo-list/<int:list_id>/task/create/', TaskCreateView.as_view(), name='task_create'),
    path('todo-list/list-new/', ListCreateView.as_view(), name='list_create'),
    path('todo-list/<int:list_id>/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('todo-list/<int:list_id>/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('todo-list/<int:pk>/delete/', ListDeleteView.as_view(), name='list_delete'),
    path('task/<int:list_id>/<int:task_id>/toggle_complete/', TaskToggleView.as_view(), name='task_toggle'),
]