from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializer import MunicipioSerializer,EstadoSerializer
from .models import Municipio,Estado
# Create your views here.

class MunicipioView(viewsets.ModelViewSet):
    serializer_class = MunicipioSerializer
    queryset = Municipio.objects.all()


class EstadoView(viewsets.ModelViewSet):
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()


class MunicipiosPorEstadoList(generics.ListAPIView):
    serializer_class = MunicipioSerializer
    def get_queryset(self):
        estado_id = self.kwargs['estado_id']  # Obten el ID del estado desde los parámetros de la URL
        return Municipio.objects.filter(estado=estado_id)