from django.db import models

# Create your models here.

class Categories(models.Model):
    nombre = models.CharField(max_length=20)
    medida = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre) + " - " + str(self.medida)

class User(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()    
    password = models.CharField(max_length=10)   
    created_at = models.DateField()
    sign_in_count = models.IntegerField()     
    permissions_level = models.IntegerField(default=1)

class Register(models.Model):
    monto =  models.IntegerField(default=False)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=50)
    medida = models.CharField(max_length=15, default=False)
    costos_adicionales = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete= models.DO_NOTHING, null=True)
    categoria = models.ForeignKey(Categories, on_delete= models.DO_NOTHING, null=True)

class TicketType(models.Model):
    name = models.CharField(max_length=30)

class Ticket(models.Model):
    title =  models.CharField(max_length=50)
    ticket_type = models.ForeignKey(TicketType, on_delete= models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete= models.DO_NOTHING, null=True)
    description = models.CharField(max_length=255)
    screenshot = models.FileField(upload_to='screenshots')
