from django.forms import ModelForm
from Cedva1.models import *
from django.contrib.auth.models import User
 
class FormularioUsuario(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password','is_staff', 'email',)
    

class FormularioADDM(ModelForm):
    class Meta:
        model = Administrador
        fields = ('nombre', 'apellidoP', 'apellidoM')