from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from Cedva1.models import * 
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required(login_url="/loginuser/")  
def pagos(request):
    return render(request, "pagos.html")  

@staff_member_required(login_url="/loginuser/") 
def pagoalumno(request):
    return render(request, "pagosAlumno.html") 

class AlumnoPagoListView(ListView):
    model =Pago
    template_name='pagosAlumno.html'
    context_object_name='listas'

class Actualizarpago(UpdateView):
    model=Pago
    template_name='actualizaPago.html'
    context_object_name='pago' 
    fields=('folio', 'tipoPago', 'monto','fechaPago','mesPagado','horapago')   

    def get_success_url(self):
        return reverse('pagoalumno')

class AlumnoPListView(ListView):
    model =Alumno
    template_name='pagos.html'
    context_object_name='listas'       

class EliminarPago(DeleteView):
    model=Pago
    template_name='PagoElimina.html'
    context_object_name='pagoelimina'

    def get_success_url(self):
        return reverse('pagoalumno')