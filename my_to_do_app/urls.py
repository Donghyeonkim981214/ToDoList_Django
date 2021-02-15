from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.createTodo, name ="createTodo"),
    path('doneTodo/', views.doneTodo, name ='doneTodo')
]