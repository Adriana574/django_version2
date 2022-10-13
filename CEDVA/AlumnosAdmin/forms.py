from django.forms import ModelForm
from Cedva1.models import *


class FormularioAlumno(ModelForm):
    class Meta:
        model = Tutor
        fields = ('nombreT', 'apellidoPT', 'apellidoMT', 'telefono', 'padreT')

class FormularioDireccion(ModelForm):
    class Meta:
        model = Direccion
        fields = ('calle', 'lote', 'manzana', 'colonia', 'delegacionMunicipio', 'codigopostal', 'ciudadOestado')