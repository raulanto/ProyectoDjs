from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Municipio
@receiver(pre_save)
def generar_codigo(sender, instance, **kwargs):
    if sender == Municipio:
        estado = instance.estado.nombre.replace(" ", "").upper()
        municipio = instance.nombre.replace(" ", "").upper()
        codigo = estado[:4] + municipio[3:]
        instance.codigo = codigo
