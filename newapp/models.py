from django.db import models

# Create your models here.

class user_login(models.Model):
    names = models.CharField(max_length=200)
    passwords = models.CharField(max_length=100)

class unversity(models.Model):
    name = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    department = models.IntegerField()
    teachers = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Userprofile(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=100)