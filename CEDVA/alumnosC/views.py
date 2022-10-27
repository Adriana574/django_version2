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
from django.db.models import Sum
from django.db.models.functions import Coalesce

def LoginUser2(request):
    if request.user.username=="":
        return render(request,"index.html")
    else:
        return HttpResponseRedirect("1inicio")

@login_required(login_url="/loginuser2/")        
def HomeAlumno(request):

    return render(request, "inicioA.html")

class grafico(TemplateView): 
    template_name= "grafico.html"

    def get_report_year_month(self):
        labels=[]
        data=[]

        queryset = Alumno.objects.order.by('inicioCurso','finalCurso')[:5]
        try:
            for mes in queryset:
                total = Pago.objects.filter(fechaPago__year=2022,fechaPago__month=10).aggregate(r=Coalesce(Sum('total'), 0)).get('r')
                data.append(float(total))
        except:
            pass
        return data
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        context['report_year_month'] = self.get_report_year_month()
        return context


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


 
def registroP(request):
    PAgoAForm = registroalumnoPag(request.POST or None)
    if PAgoAForm.is_valid():
        form_data = PAgoAForm.cleaned_data 
        folio= form_data.get("folio")
        alumno=form_data.get("alumno") 
        tipoPago=form_data.get("tipoPago")
        monto = form_data.get("monto")
        fechaPago = form_data.get("fechaPago")
        mesPagado = form_data.get("mesPagado")
        horapago = form_data.get("horapago")

        obj4 = Pago.objects.create(alumno=alumno, folio=folio, tipoPago=tipoPago, monto = monto, fechaPago=fechaPago, mesPagado=mesPagado,horapago=horapago)

    
    context = {
        'PAgoAForm': PAgoAForm
    }
        
    return render(request, "registroP.html", context) 
         