import logging
from django.shortcuts import render
from entradaDatos.models import Clientes
from django.contrib import messages
from entradaDatos.forms import clientesForms

def showClientes(request):
    showall=Clientes.objects.all()
    return render(request,'inicio.html',{'data':showall})

def insertarClientes(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('apellidos') and request.POST.get('direccion') and request.POST.get('email') and request.POST.get('tfno'):
            saverecord=Clientes()
            saverecord.nombre=request.POST.get('nombre')
            saverecord.apellidos=request.POST.get('apellidos')
            saverecord.direccion=request.POST.get('direccion')
            saverecord.email=request.POST.get('email')
            saverecord.tfno=request.POST.get('tfno')
            saverecord.save()
            messages.success(request,'Sus datos han sido guardados con éxito') 
            return render (request,'insertar.html')
    else:
            return render (request,'insertar.html')


def DatosExternos(request):
    showall=Clientes.objects.all()
    return render(request,'bdexterna.html',{'data':showall})


def Edicion(request,id):
    edicionObjt=Clientes.objects.get(id=id)
    return render (request,'edicion.html',{"Clientes":edicionObjt})

def actualizarCliente(request,id):

        ActualizarCliente=Clientes.objects.get(id=id)
        form=clientesForms(request.POST,instance=ActualizarCliente)
        if form.is_valid():
            form.save()
            messages.success(request,'Datos modificados con éxito')
        return render (request,'edicion.html',{"Clientes":ActualizarCliente})

def anadirDatos(request,id):
    AñadirDato=Clientes.objects.get(id=id)
    return render (request,'anadirDatos.html',{"Clientes":AñadirDato})
     
def agregarDato(request,id):
    AgreDato=Clientes.objects.get(id=id) 
    form=clientesForms(request.POST,instance=AgreDato)   
    if form.is_valid():
            form.save()
            messages.success(request,'Sus datos han sido guardados con éxito') 
            return render (request,'anadirDatos.html',{"Clientes":AgreDato})