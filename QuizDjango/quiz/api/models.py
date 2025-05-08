from django.db import models

class Pacientes (models.Model):
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30)
    edad = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre
    
class Especialidades (models.Model):
    nombre = models.CharField(max_length=30, null=False)
    descripcion = models.CharField(max_length=80)
    
    def __str__(self):
        return self.descripcion
    
class Doctores (models.Model): 
    nombre = models.CharField(max_length=20, null=False)
    apellido = models.CharField(max_length=20)
    anhosExperiencia = models.CharField(max_length=50)
    Especialidades = models.ManyToManyField(Especialidades, through='DoctoresEspecialidades', related_name='doctores')

    def __str__(self):
        return self.apellido

class Citas (models.Model):
    Pacientes = models.ForeignKey(Pacientes, on_delete=models.CASCADE, related_name="Citas")
    Doctores = models.ForeignKey(Doctores, on_delete=models.CASCADE, related_name="Citas")
    fecha = models.DateField(null=False)
    hora = models.TimeField(auto_now=True)
    motivo = models.CharField(max_length=100)

    def __str__(self):
        return self.fecha
    
class DoctoresEspecialidades (models.Model):
    Doctores = models.ForeignKey(Doctores, on_delete=models.CASCADE, related_name="DoctoresEspecialidades")
    Especialidades = models.ForeignKey(Especialidades, on_delete=models.CASCADE, related_name="DoctoresEspecialidades")
    
    def __str__(self):
        return self.Doctores
    