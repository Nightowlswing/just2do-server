from django.db import models
from django.utils import timezone
# from datetime import date
# Create your models here.
class Todo(models.Model):
    description = models.CharField(max_length=200)
    day = models.DateField(default = timezone.now())
    user = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)
    def __str__(self):
        return self.description