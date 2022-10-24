from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Cedva1.models import *
from django.views.generic import DetailView
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm 
from administradorCEDVA.forms import *

@staff_member_required  
def AdministradorCreateView(request):
    UserForm = FormularioUsuario(request.POST or None)
    if UserForm.is_valid():
        form_data = UserForm.cleaned_data
        nomU = form_data.get("username")
        password= form_data.get("password") 
        isStaff=form_data.get("is_staff")
        correo = form_data.get("email")

        obj4 = User.objects.create_user(username=nomU, password=password,is_staff=True, email=correo)

    ADDForm = FormularioADDM(request.POST or None)
    if ADDForm.is_valid():
        form_data = ADDForm.cleaned_data
       
        nombre = form_data.get("nombre") 
        appAD = form_data.get("apellidoP")
        apmAD = form_data.get("apellidoM") 
        obj5 = Administrador.objects.create(nombre=nombre, apellidoP=appAD, apellidoM=apmAD)

    context = {
        'UserForm': UserForm,
        'ADDForm': ADDForm
    }
        
    return render(request, "registroaddmin.html", context) 