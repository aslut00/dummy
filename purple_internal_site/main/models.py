from django.db import models

# Create your models here.

class User(models.Model):
    pid = models.CharField(max_length=15)
    ppw = models.CharField(max_length=15)
