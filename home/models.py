from operator import mod
from statistics import mode
from django.db import models

# Create your models here.
class todo(models.Model):
    Description = models.TextField()
    Completed = models.BooleanField(default=False) 
    Created_by = models.DateField(auto_now_add=True) 


