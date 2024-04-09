from django.db import models

# Create your models here.

class unversity(models.Model):
    name = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Userprofile(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=100)