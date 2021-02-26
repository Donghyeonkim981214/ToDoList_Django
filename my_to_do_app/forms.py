from django import forms
from . import models
import datetime

current_year = datetime.date.today().year
YEARS= [x for x in range(current_year,current_year+5)]

class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = (
            "content",
            "Deadline",
        )
        widgets = {
            "Deadline": forms.SelectDateWidget(years=YEARS),
        }

    def save(self):
        todo = super().save(commit=False)
        return todo
    
    def clean_Deadline(self):
        cleaned_data = super().clean()
        Deadline = self.cleaned_data['Deadline']
        today = datetime.date.today()
        if Deadline is not None and Deadline < today:
             self.add_error("Deadline", forms.ValidationError("Deadline must be more than today"))
        super(CreateTodoForm, self).clean()
