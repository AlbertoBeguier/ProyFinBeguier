from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Informe(models.Model):
    # Criptomonedas - Acciones - Retiro Soñado
    tipo=models.CharField(max_length=20)
    titulo=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=100)
    fecha=models.DateField()
    contenido=models.TextField()
    
    
    def __str__(self):
        return f"{self.tipo} - {self.titulo} - {self.fecha}"
    
class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="avatares", blank=True,null=True)

