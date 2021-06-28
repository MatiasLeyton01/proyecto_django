from django import forms
from django.forms import ModelForm
from .models import Vehiculo

#Creamos nuetra clase para el fmrulario desde la base de datos
class VehiculoForm(ModelForm):

    class Meta:
        model = Vehiculo
        fields = ['patente', 'marca', 'modelo', 'categoria',]
