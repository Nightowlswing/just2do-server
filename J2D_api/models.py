from django.db import models
from django.utils import timezone
# from datetime import date
# Create your models here.
class Todo(models.Model):
    description = models.CharField(max_length=200) #task description
    day = models.DateField(default = timezone.now()) #day user selected for this task
    user = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE) #reference to user
    status = models.BooleanField(default=False) #done or not done
    def __str__(self):
        return self.description

class ItemList(models.Model):
    title = models.CharField(max_length=300)
    user = models.ForeignKey('auth.User', related_name='lists', on_delete=models.CASCADE) #reference to user
    def __str__(self):
        return self.title

class Item(models.Model):
    description = models.CharField(max_length=200) #task description
    user = models.ForeignKey('auth.User', related_name='item_lists', on_delete=models.CASCADE) #reference to user
    status = models.BooleanField(default=False) #done or not done
    list_rel = models.ForeignKey('J2D_api.ItemList', related_name='items', on_delete=models.CASCADE)
    def __str__(self):
        return self.description