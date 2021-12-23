from django.db.models import fields
from .models import Propietario, Predio
from rest_framework import serializers

class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propietario
        fields = ('id', 'name', 'identificacion', 'created')

class PredioSerializer(serializers.ModelSerializer):
    propietarios = PropietarioSerializer(many=True)

    class Meta:
        model = Predio
        fields = ('id', 'name', 'direccion', 'type_predio', 'matricula_inmobiliaria', 'cedula_catastral', 'created', 'propietarios')