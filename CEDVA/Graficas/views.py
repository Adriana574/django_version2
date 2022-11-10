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
from datetime import datetime
from django.views.generic.base import TemplateView
from django.db.models import Sum, Count
from django.db.models.functions import Coalesce




class grafico(TemplateView): 
    template_name= "grafico.html"
    
    def get_report_year_month(self,*args, **kwargs):
        data = [] 
        anio = self.kwargs.get('date')
        year= anio
       # print(request.GET)  

        total1=Pago.objects.filter(fechaPago__year=year,fechaPago__month='01',PagoRegistrado="Mensual").count()
        
        total2=Pago.objects.filter(fechaPago__year=year,fechaPago__month='02',PagoRegistrado="Mensual").count()

        total3=Pago.objects.filter(fechaPago__year=year,fechaPago__month='03',PagoRegistrado="Mensual").count()

        total4=Pago.objects.filter(fechaPago__year=year,fechaPago__month='04',PagoRegistrado="Mensual").count()

        total5=Pago.objects.filter(fechaPago__year=year,fechaPago__month='05',PagoRegistrado="Mensual").count()        
        
        total6=Pago.objects.filter(fechaPago__year=year,fechaPago__month='06',PagoRegistrado="Mensual").count()

        total7=Pago.objects.filter(fechaPago__year=year,fechaPago__month='07',PagoRegistrado="Mensual").count()

        total8=Pago.objects.filter(fechaPago__year=year,fechaPago__month='08',PagoRegistrado="Mensual").count()

        total9=Pago.objects.filter(fechaPago__year=year,fechaPago__month='09',PagoRegistrado="Mensual").count()

        total10=Pago.objects.filter(fechaPago__year=year,fechaPago__month='10',PagoRegistrado="Mensual").count()

        total11=Pago.objects.filter(fechaPago__year=year,fechaPago__month='11',PagoRegistrado="Mensual").count()

        total12=Pago.objects.filter(fechaPago__year=year,fechaPago__month='12',PagoRegistrado="Mensual").count() 

        data = [total1,total2,total3,total4,total5,total6,total7,total8,total9,total10,total11,total12]

        return data

    def get_report_Con_Convenio(self):
        
        year=datetime.now().year 
        totalc=Alumno.objects.filter(convenio='SI',inicioCurso__year=year).count()
       
       
        return totalc

    def get_report_Sin_Convenio(self):
        year=datetime.now().year 
        totala=Alumno.objects.filter(convenio='NO',inicioCurso__year=year).count()
        return totala

    def get_año(self):
        year=datetime.now().year 
        return year 

    def get_alumnos_activos(self):
        alumnos=Alumno.objects.filter(activo_por_pagos=True)
        print(alumnos)
        return alumnos

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['buscaraño'] = self.get_año()
        context['reportConConvenio'] = self.get_report_Con_Convenio()
        context['reportSinConvenio'] = self.get_report_Sin_Convenio()
        context['report_year_month'] = self.get_report_year_month()
        context['report_alumnos_activos'] = self.get_alumnos_activos()
        return context
