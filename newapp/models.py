from django.db import models

# Create your models here.

class user_login(models.Model):
    names = models.CharField(max_length=200)
    passwords = models.CharField(max_length=100)

class unversity(models.Model):
    name = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    department = models.CharField(max_length=50)
    teachers = models.CharField(max_length=50)
    
    # def __str__(self):
    #     return f"{self.teachers}--{self.name}--{self.place}"
    
class Userprofile(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=100)