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

    def create(self, validated_data):
        propietario_data = validated_data.pop('propietarios')
        predio = Predio.objects.create(**validated_data)
        
        for propietario in propietario_data:
            predio.propietarios.create(**propietario)
        return predio