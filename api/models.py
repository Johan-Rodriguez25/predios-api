from django.db import models
from .choices import predio

class Propietario(models.Model):
  name = models.CharField(max_length=50, blank=False, null=False)
  identificacion = models.BigIntegerField(blank=False, null=False)
  created = models.DateTimeField(auto_now_add=True)

class Predio(models.Model):
  name = models.CharField(max_length=50, blank=True, null=True)
  direccion = models.CharField(max_length=50, blank=True, null=True)
  type_predio = models.CharField(max_length=50, choices=predio, default='urbano', blank=False, null=False)
  matricula_inmobiliaria = models.CharField(max_length=250, blank=False, null=False)
  cedula_catastral = models.BigIntegerField(blank=False, null=False)
  created = models.DateTimeField(auto_now_add=True)
  propietarios = models.ManyToManyField(Propietario, blank=True, null=True)