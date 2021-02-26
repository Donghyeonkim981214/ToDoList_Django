from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView,  DetailView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import *
from . import forms
import datetime
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import LoggedOutOnlyView, CreatorOnlyView

class HomeView(ListView):
    model = Todo
    context_object_name = 'todos'

    def get_template_names(self):
        if self.request.user.is_authenticated:
            names = ["my_to_do_app/user_index.html"]
        else:
            names = ["my_to_do_app/index.html"]
        return names
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['ings'] = Todo.objects.filter(created_by = self.request.user).filter(isDone = False).filter(Q(Deadline__gte=datetime.date.today()) | Q(Deadline__isnull=True)).order_by('-PostedDay')[:5]
            context['dones'] = Todo.objects.filter(created_by = self.request.user).filter(isDone = True).order_by('-PostedDay')[:5]
            context['failures'] = Todo.objects.filter(created_by = self.request.user).filter(isDone = False).filter(Deadline__isnull=False).exclude(Deadline__gte=datetime.date.today()).order_by('-Deadline')[:5]
        else:
            context['guest_todo'] = Todo.objects.filter(created_by__isnull=True).order_by('-PostedDay')
        return super().get_context_data(**context)


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "my_to_do_app/dos_all.html"
    paginate_by = 5

    def get_queryset(self):
        if self.kwargs['slug'] == 'ings':
            queryset = Todo.objects.filter(created_by = self.request.user).filter(isDone = False).filter(Q(Deadline__gte=datetime.date.today()) | Q(Deadline__isnull=True)).order_by('-PostedDay')
        elif self.kwargs['slug'] == 'dones':
            queryset = Todo.objects.filter(created_by = self.request.user).filter(isDone = True)
        else:
            queryset = Todo.objects.filter(created_by = self.request.user).filter(isDone = False).filter(Deadline__isnull=False).exclude(Deadline__gte=datetime.date.today())
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        if self.kwargs['slug'] == 'ings':
            context['sub'] = 'Ings'
        elif self.kwargs['slug'] == 'dones':
            context['sub'] = 'Successes'
        else:
            context['sub'] = 'Fails'
        return context


class TodoDetailView(CreatorOnlyView, DetailView):
    model = Todo
    template_name = "my_to_do_app/detail_todo.html"
    context_object_name = "todo"



class TodoUpdateView(CreatorOnlyView, UpdateView):
    model = Todo
    template_name = "my_to_do_app/update_Todo.html"
    form_class = forms.CreateTodoForm
    context_object_name = "todo"

    def get_object(self): 
        todo = get_object_or_404(Todo, pk=self.kwargs['pk']) #4
        return todo
    
    def form_valid(self, form):
        todo = form.save()
        todo.save()
        return super().form_valid(form)

def TodoDone(request):
    done_todo_id = request.GET['todoNum']
    todo = Todo.objects.get(id = done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('home:home'))


class TodoDeleteView(CreatorOnlyView, DeleteView):
    model = Todo
    success_url = reverse_lazy('home:home')


class TodoCreateView(CreateView):
    template_name = "my_to_do_app/todo.html"
    form_class = forms.CreateTodoForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        todo = form.save()
        if self.request.user.is_authenticated:
            todo.created_by = self.request.user
        else:
            messages.success(self.request, "You are not logined. your todo will be removed. please login!")
        todo.save()
        return super().form_valid(form)