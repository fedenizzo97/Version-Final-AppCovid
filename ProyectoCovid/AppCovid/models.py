from django.db import models

# Create your models here.


class Barbijos(models.Model):
    marca= models.CharField(max_length=40)
    tamanio= models.CharField(max_length=20)
    precio= models.IntegerField()

    def __str__(self):

        return f"Barbijos: Marca: {self.marca} Tamaño: {self.tamanio} Precio: {self.precio} "


