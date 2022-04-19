"""POC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from entradaDatos import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showClientes,name='showClientes'),
    path('Insertar',views.insertarClientes,name='insertarClientes'),
    path('Bdexterna',views.DatosExternos,name='DatosExternos'),
    path('Edicion/<int:id>',views.Edicion,name='Edicion'), 
    path('Actualizar/<int:id>',views.actualizarCliente,name='actualizarCliente'),
    path('Anadir/<int:id>',views.anadirDatos,name='anadirDatos'),
    path('Agregar/<int:id>',views.agregarDato,name='agregarDato'),
]
