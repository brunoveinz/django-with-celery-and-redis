from django.db import models
from padres.models import Padres

# Create your models here.

class Estudiantes(models.Model):
    nombre      = models.CharField(max_length=200)
    edad        = models.IntegerField()
    padre       = models.ForeignKey(Padres, on_delete=models.CASCADE)