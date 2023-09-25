from django import forms
from django.contrib.auth.forms import UserChangeForm

class InformeFormulario(forms.Form):
    tipo=forms.CharField(max_length=20)
    titulo=forms.CharField(max_length=100)
    subtitulo=forms.CharField(max_length=100)
    fecha=forms.DateField()
    contenido=forms.CharField(max_length=6000)


