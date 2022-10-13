from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Cedva1.models import *

def LoginUser2(request):
    if request.user.username=="":
        return render(request,"index.html")
    else:
        return HttpResponseRedirect("1inicio")

@login_required(login_url="/loginuser2/")        
def HomeAlumno(request):
    return render(request, "inicioA.html")

@login_required(login_url="/loginuser2/")
def registroP(request):
    return render(request, "registroP.html")  

@login_required(login_url="/loginuser2/")
def Avance(request):
    return render(request, "avanze.html")      

def LogoutUser2(request):
    logout(request)
    request.user=None
    return HttpResponseRedirect("/loginuser2")  

class AlumnoDatosListView(ListView):
    model = Alumno
    template_name='dato.html'
    context_object_name='listas'         