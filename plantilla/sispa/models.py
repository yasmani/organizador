from django.db import models

# Create your models here.
class Solicitudes(models.Model):
    area=models.CharField(max_length=10)
    area_n=models.CharField(max_length=255)
    solicitud= models.CharField(max_length=10)
    solicitud_n=models.CharField(max_length=255)
    titulo=models.CharField(max_length=255)
    detalle=models.CharField(max_length=255)
    responsable=models.CharField(max_length=10)
    responsable_n=models.CharField(max_length=255)
    asignar=models.CharField(max_length=10)
    asignar_a_n=models.CharField(max_length=255)
    adjunto=models.CharField(max_length=255)
    estado=models.CharField(max_length=255)
    observacion=models.CharField(max_length=255)
    usuario_solicitud=models.CharField(max_length=255)
    usuario_solicitud_n=models.CharField(max_length=255)
    departamento=models.CharField(max_length=255)
    fecha_solicitud=models.DateField()
    adjunto_cierre=models.CharField(max_length=255)


class Meta:
    db_table='Solicitudes'

class SOLICITUD(models.Model):
    id_rel=models.CharField(max_length=10)
    solicitud=models.CharField(max_length=255)
    perfil= models.CharField(max_length=10)
    estado=models.CharField(max_length=10)

class Meta:
    db_table='SOLICITUD'



class AREA(models.Model):
    identificador=models.CharField(max_length=10)
    area=models.CharField(max_length=255)
    perfil= models.CharField(max_length=10)

class Meta:
    db_table='AREA'
