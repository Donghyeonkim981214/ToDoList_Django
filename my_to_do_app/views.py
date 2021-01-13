# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.views import View
from django.views.generic.list import ListView

from .models import *

"""
def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)
"""
class IndexView(ListView):
    template_name = 'my_to_do_app/index.html'
    model = Todo

"""
def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("create Todo를 할 거야! =>" + user_input_str)
"""
class CreateTodoView(View):
    def post(self, request):
        user_input_str = request.POST['todoContent']
        new_todo = Todo(content=user_input_str)
        new_todo.save()
        return HttpResponseRedirect(reverse('index'))

"""
def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한 todo의 id", done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))
"""

class DoneTodoView(View):
    def get(self, request):
        done_todo_id = request.GET['todoNum']
        todo = Todo.objects.get(id = done_todo_id)
        todo.isDone = True
        todo.save()
        return HttpResponseRedirect(reverse('index'))
