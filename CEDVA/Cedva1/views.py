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
from . models import * 
from django.contrib.admin.views.decorators import staff_member_required
 
def LoginUser(request):
    if request.user.username=="":
        return render(request,"index.html")
    else:
        return HttpResponseRedirect("/homepage")

@staff_member_required(login_url="/loginuser/") 
def HomePage(request):
    return render(request, "director/inicio.html") 

def clicklogin(request):
    if request.method!="POST":
        return HttpResponse("<h1> Methoid not allowed<h1>")
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        
        user=authenticate(username=username,password=password)
        if user!=None:
            login(request,user)
            if request.user.is_staff:
                return HttpResponseRedirect('/homepage')
            else:      
                return HttpResponseRedirect('/1inicio')  
        else:
            messages.error(request, "Usuario invalido verifique los datos")
            return HttpResponseRedirect('/')
        

def LogoutUser(request):
    logout(request)
    request.user=None
    return HttpResponseRedirect("/loginuser")       