from django.db import models

# Create your models here.

class Padres(models.Model):
    nombre           = models.CharField(max_length=200)
    email            = models.EmailField(max_length=200, unique=True)
