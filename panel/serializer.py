from rest_framework import serializers
from .models import Municipio,Estado

class MunicipioSerializer(serializers.ModelSerializer):
    estado_nombre = serializers.ReadOnlyField(source='estado.nombre')  # Agregar esta línea
    class Meta:
        model=Municipio
        fields = ['id', 'nombre', 'estado', 'codigo', 'estado_nombre']


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estado
        fields='__all__'