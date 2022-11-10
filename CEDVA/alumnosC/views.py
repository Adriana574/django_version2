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
from django.contrib import admin
from django.urls import reverse_lazy
from Cedva1.models import *
from Pago.forms import *
from alumnosC.forms import *
from datetime import datetime
from django.views.generic.base import TemplateView
from django.db.models import Sum, Count
from django.db.models.functions import Coalesce


def LoginUser2(request):
    if request.user.username=="":
        return render(request,"index.html")
    else:
        return HttpResponseRedirect("1inicio")

@login_required(login_url="/loginuser2/")        
def HomeAlumno(request):
    model=Alumno
    return render(request, "inicioA.html",{'model':model}) 

@login_required(login_url="/loginuser2/")
def registroP(request):
    return render(request, "registroP.html")  


class Avance(TemplateView):
    template_name= "graficaAVANCE.html"
    model=Alumno

    def get_report(self, *args, **kwargs):
        data = []
        year=datetime.now().year
        pk = self.kwargs.get('pk', 0)
        alumno=self.model.objects.get(user=pk)

        total1=Pago.objects.filter(alumno=alumno.id,fechaPago__year=year).count()
        
     

        data = [total1]

        return data

    def get_reportaño1(self, *args, **kwargs):
        data = []
        year=datetime.now().year
        pk = self.kwargs.get('pk', 0)
        alumno=self.model.objects.get(user=pk)

        total1=Pago.objects.filter(alumno=alumno.id,fechaPago__year=(year+1)).count()


        data = [total1]

        return data 

    def get_reportaño2(self, *args, **kwargs):
        data = []
        year=datetime.now().year
        pk = self.kwargs.get('pk', 0)
        alumno=self.model.objects.get(user=pk)

        total1=Pago.objects.filter(alumno=alumno.id,fechaPago__year=(year+2)).count()


        data = [total1]

        return data  

    def get_pagos(self, *args, **kwargs):
        pk = self.kwargs.get('pk', 0)
        year=datetime.now().year
        alumno=self.model.objects.get(user=pk)

        total1=Pago.objects.filter(alumno=alumno.id,fechaPago__year=year)

        return total1  

    def get_pagosuno(self, *args, **kwargs):
        pk = self.kwargs.get('pk', 0)
        year=datetime.now().year
        alumno=self.model.objects.get(user=pk)

        total1=Pago.objects.filter(alumno=alumno.id,fechaPago__year=(year+1))

        return total1 

    def get_pagosdos(self, *args, **kwargs):
        pk = self.kwargs.get('pk', 0)
        year=datetime.now().year
        alumno=self.model.objects.get(user=pk)

        total1=Pago.objects.filter(alumno=alumno.id,fechaPago__year=(year+2))

        return total1                    

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['PAGOS'] = self.get_pagos()
        context['PAGOSuno'] = self.get_pagosuno()
        context['PAGOSdos'] = self.get_pagosdos()
        context['report_Alumno'] = self.get_report()
        context['report_Alumno_años'] = self.get_reportaño1()
        context['report_Alumno_añosdos'] = self.get_reportaño2()
        return context
      

def LogoutUser2(request):
    logout(request)
    request.user=None
    return HttpResponseRedirect("/loginuser2")  

class AlumnoDatosListView(TemplateView):
    model=Alumno
    template_name='dato.html'

    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs.get('pk', 0)
        alumno=self.model.objects.get(user=pk)
        context = super().get_context_data(**kwargs)
        context['Tutor'] = Tutor.objects.get(id=alumno.tutor_id)
        context['User'] = User.objects.get(id=alumno.user_id)
        context['Especialidad'] = Especialidad.objects.get(id=alumno.especialidad_id)
        context['Direccion'] = Direccion.objects.get(id=alumno.direccion_id)
        context['Alumno'] = Alumno.objects.get(pk=alumno.id)
        return context 

class registroP(CreateView):
    model = Pago
    template_name = 'registroP.html'
    second_model = Alumno
    form_class =  registroalumnoPag
    success_url = reverse_lazy('registroPago')
 
    def get_context_data(self, **kwargs):
        context=super(registroP, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            return context 

    def post(self, request, pk, *args, **kwargs):
        self.object=self.get_object
        user=self.kwargs.get('pk')
        alumnoid=Alumno.objects.filter(user_id=user).only('id')
        form=self.form_class(request.POST) 
        if form.is_valid():
            registroalumnoPag = form.save(commit=False) 
            registroalumnoPag.alumno_id = alumnoid
            registroalumnoPag.save()
            return render(request,'registroP.html', {'registroalumnoPag' : registroalumnoPag})
        else:
            return self.render_to_response(self.get_context_data(form=form)) 