from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Todoitem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    item_title = models.CharField('Item Title', max_length=200)
    item_data = models.DateField('Item Data', auto_now_add=False, auto_now=False)
    item_done = models.CharField('Item Done', max_length=4)