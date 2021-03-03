from django.db import models
from users import models as user_models
from django.urls import reverse
import datetime


# Create your models here.
class Todo(models.Model):
    content = models.TextField()
    isDone = models.BooleanField(default = False)
    Deadline = models.DateField(null = True, blank = True)
    PostedDay = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null = True, blank = True)

    def get_absolute_url(self):
        return reverse("home:TodoDetail", kwargs={"pk": self.pk})