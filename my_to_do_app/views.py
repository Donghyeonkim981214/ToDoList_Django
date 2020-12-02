from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'my_to_do_app/index.html')
