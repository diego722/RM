from django import forms
from entradaDatos.models import Clientes

class clientesForms(forms.ModelForm):
    class Meta:
        model=Clientes
        fields="__all__"