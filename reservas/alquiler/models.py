from django.db import models

class Servicios(models.Model):
    codservicio = models.AutoField(primary_key=True)
    servicio = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=7, decimal_places=2)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)
    foto = models.ImageField(upload_to="servicios",blank=True)

    def __str__(self):
        return self.servicio

class Clientes(models.Model):
    codcliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20,blank=True)
    correo = models.CharField(max_length=100,blank=True)
    numcuenta = models.CharField(max_length=50,blank=True)
    foto = models.ImageField(upload_to="clientes",blank=True)
    
    def __str__(self):
        return self.nombre

class Reservas(models.Model):
    codreserva = models.IntegerField(primary_key=True)
    fechareserva = models.DateField()
    clientes_codcliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    servicios_codservicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)

    

 