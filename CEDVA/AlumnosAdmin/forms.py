from django.forms import ModelForm
from Cedva1.models import *
from django.contrib.auth.models import User

class FormularioTutor(ModelForm):
    class Meta:
        model = Tutor
        fields = ('nombreT', 'apellidoPT', 'apellidoMT', 'telefono', 'padreT')

class FormularioDireccion(ModelForm):
    class Meta:
        model = Direccion
        fields = ('calle', 'lote', 'manzana', 'colonia', 'delegacionMunicipio', 'codigopostal', 'ciudadOestado')

class FormularioEspecialidad(ModelForm):
    class Meta:
        model = Especialidad
        fields = ('nombreE',)

class FormularioUsuario(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)


class FormularioAlumno(ModelForm):
    class Meta:
        model = Alumno
        fields = ('matricula', 'nombreA', 'snombreA', 'apellidoPA', 'apellidoMA', 'edad', 'convenio', 'inicioCurso', 'finalCurso', 'observaciones')
        