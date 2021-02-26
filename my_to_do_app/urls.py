from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('createTodo/', views.TodoCreateView.as_view(), name ="TodoCreate"),
    path('doneTodo/', views.TodoDone, name ='TodoDone'),
    path('delete/<int:pk>', views.TodoDeleteView.as_view(), name ='TodoDelete'),
    path('todos/<slug:slug>', views.TodoListView.as_view(), name ='TodoList'),
    path('todo/<int:pk>', views.TodoDetailView.as_view(), name ='TodoDetail'),
    path('todo_update/<int:pk>', views.TodoUpdateView.as_view(), name ='TodoUpdate'),
]