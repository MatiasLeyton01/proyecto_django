from django.shortcuts import render, redirect
from django.template import loader
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.

#Funcion de mostrar vehiculos
def home(request):
    #Accediendo al objeto que contiene los datos en la base de datos
    #El metodo traera todos los vehiculos en la tabla
    vehiculos = Vehiculo.objects.all()
    #Ahora creamos una variable que le pase los datos del vehiculo al TEMPLATE
    datos = {
        'vehiculos': vehiculos
    }
    #Ahora lo agregamos para que se envie al template
    return render(request, 'core/home.html', datos)


#Funcion de agregar vehiculos
def form_vehiculo(request):
    # El view sera el responsable de entregar el form al template(form_vehiculo.html)
    datos = {
        'form': VehiculoForm()
    }

    #verificamos que peticion sean POST y rescatamos los datos
    if request.method == 'POST':
        #con REQUEST recuperamos los datos del fomrulario
        formulario = VehiculoForm(request.POST)
        # Y validamos el fomrulario
        if formulario.is_valid():
            #Ahora guardamos en la base de datos
            formulario.save()
            #Y mostramos un mensaje
            datos['mensaje'] = "Guardados correctamente"
            
    return render(request, 'core/form_vehiculo.html', datos)


#Funcion de ... Modificar
def form_mod_vehiculo(request, id):
    # El id es el identificador de la tabla Vehiculos
    # Buscamos los datos en la DB
    # Buscamos la patente que llega como dato en la URL
    vehiculo = Vehiculo.objects.get(patente=id)
        #Ahora le entegamos los datos del vehiculo al formulario
    datos = {
        'form': VehiculoForm(instance=vehiculo)
    }
    #Verificamos que la peticion sean post y rescatamos los datos
    if request.method == 'POST':
        #Con REQUEST recuperamos los datos del formulario y 
        #   le agregamos el id modificar
       formulario = VehiculoForm(data=request.POST, instance=vehiculo)
       # y validamos el formulario
       if formulario.is_valid():
           # Guardamos en la base de datos
           formulario.save()
           #Mostramos un mensaje
           datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_vehiculo.html', datos)


#funcion de eliminar
def form_del_vehiculo(request, id):
    #El id es el identificador de la tabla Vehiculos
    #Buscando los datos en la base de datos

    vehiculo = Vehiculo.objects.get(patente=id)
    #Eliminamos el vehiculo de la patente buscada
    vehiculo.delete()
    # Y ahora redirigimos a la pagina HOME ocn el listado
    return redirect(to="home")












