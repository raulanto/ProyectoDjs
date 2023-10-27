from django.db import models

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, null=False)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE, null=False)
    codigo = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.nombre