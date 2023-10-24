from django.db import models

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre