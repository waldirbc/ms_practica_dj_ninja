from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    edad = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
