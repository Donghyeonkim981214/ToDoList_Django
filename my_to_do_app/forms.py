# coding=utf-8
from django import forms


class ContentForm(forms.Form):
    todoContent = forms.CharField(label = 'TODO', max_length = 255)

class IdForm(forms.Form):
    todoId = forms.IntegerField()