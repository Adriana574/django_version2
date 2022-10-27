from django.forms import ModelForm
from Cedva1.models import *
from django.contrib.auth.models import User
 

class registroalumnoPag(ModelForm):
    class Meta:
        model = Pago
        fields = ('alumno','folio', 'tipoPago','monto','fechaPago','mesPagado','horapago')


