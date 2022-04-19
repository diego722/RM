from django.contrib import admin
from entradaDatos.models import Clientes
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","apellidos","tfno")
    list_filter=("nombre","apellidos")


admin.site.register(Clientes,ClientesAdmin)
