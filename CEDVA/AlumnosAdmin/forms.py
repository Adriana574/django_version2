from django.forms import ModelForm
from Cedva1.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

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

class FormularioUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username',
                'email', 
                ]
        labels = {
                'username': 'Nombre de usuario',
                'email': 'Correo del alumno',
        } 
        widgets = {
                'username': forms.TextInput(attrs={
                'placeholder': 'Nombre de usuario',
                'autofocus': 'autofocus',
                'class': 'form-control ', }),
                'email': forms.TextInput(attrs={
                'placeholder': 'Correo del alumno',
                'autofocus': 'autofocus',
                'class': 'form-control ', }),
        }


class FormularioAlumno(ModelForm):
    class Meta:
        model = Alumno
        fields = ('matricula', 'nombreA', 'snombreA', 'apellidoPA', 'apellidoMA', 'edad', 'convenio', 'inicioCurso', 'finalCurso', 'observaciones')
        

class FormularioUsuarioUpdate(ModelForm):
    class Meta:
        model = User
        fields = [
                'username',
                'email', 
                ]
        labels = {
                'username': 'Nombre de usuario',
                'email': 'Correo del alumno',
        } 


class FormularioAlumnoUpdate(ModelForm):
    inicioCurso = forms.DateField(label='Fecha inicio de Curso', widget=forms.TextInput(attrs={'type': 'date','class': 'form-control  datetimepicker'}), required=True)
    finalCurso = forms.DateField(label='Fecha final de Curso', widget=forms.TextInput(attrs={'type': 'date','class': 'form-control  datetimepicker'}), required=True)
    
    class Meta:
        model = Alumno
        fields = ('matricula', 'nombreA', 'snombreA', 'apellidoPA', 'apellidoMA', 'edad', 'convenio', 'inicioCurso', 'finalCurso', 'observaciones')