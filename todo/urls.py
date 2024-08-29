from django.urls import path
from .views import*
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('todo-list/<int:list_id>/', TodoListView.as_view(), name='todolist'),
]