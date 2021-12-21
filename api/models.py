from django.db import models
from .choices import predio

# Create your models here.

class Propietario(models.Model):
  name = models.CharField(max_length=50, blank=False, null=False)
  identificacion = models.IntegerField(blank=False, null=False)
  predios = models.ForeignKey('Predio', on_delete=models.CASCADE, blank=True, null=True)

class Predio(models.Model):
  name = models.CharField(max_length=50, blank=False, null=False)
  type_predio = models.CharField(max_length=50, choices=predio, default='urbano', blank=False, null=False)
  matricula_inmobiliaria = models.IntegerField(blank=False, null=False)
  cedula_catastral = models.IntegerField(blank=False, null=False)
  propietarios = models.ForeignKey(Propietario, on_delete=models.CASCADE)