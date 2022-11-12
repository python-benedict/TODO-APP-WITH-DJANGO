from django.db import models

# Create your models here.
class MyToDo(models.Model):
    task = models.CharField(max_length=100, unique=True)
    
    def _str__(self):
        return self.task