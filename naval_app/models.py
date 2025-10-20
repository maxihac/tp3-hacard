from django.db import models

# Create your models here.
class Empresa(models.Model):
    razonsocial= models.CharField(max_length=150)
    cuil= models.IntegerField()
    direccion=models.CharField(max_length=150)
    telefono=models.CharField(max_length=150)
    email=models.EmailField()
    fecha_alta=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"Empresa: {self.razonsocial} - cuil: {self.cuil} - direccion:{self.direccion} "


class Buque(models.Model):
    nombre= models.CharField(max_length=150)
    imo= models.IntegerField(unique=True)
    eslora=models.IntegerField(default=0)
    manga=models.IntegerField(default=0)
    puntal=models.IntegerField(default=0)
    tripulantes=models.IntegerField(default=0)
    def __str__(self):
        return f"Buque: {self.nombre} - Imo: {self.imo} - tripulantes:{self.tripulantes} "
class Plano(models.Model):
    tipo= models.CharField(max_length=150)
    version=models.IntegerField()
    autor=models.CharField(max_length=150)
    def __str__(self):
        return f"Plano_tipo: {self.tipo} - Version: {self.version} - Autor:{self.autor} "
