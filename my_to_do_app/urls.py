from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name = 'index'),

    path('createTodo/', views.createTodo, name="createTodo"),
    #path('createTodo/', views.CreateTodoView.as_view(), name="createTodo"),

    path('doneTodo/', views.doneTodo, name='doneTodo')
    #path('doneTodo/', views.DoneTodoView.as_view(), name='doneTodo')
]
