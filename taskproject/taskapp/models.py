from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    manager = models.ForeignKey(User,on_delete=models.CASCADE,default=None)