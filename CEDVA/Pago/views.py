from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import admin
from django.urls import reverse_lazy
from Cedva1.models import *
from AlumnosAdmin.forms import FormularioAlumno 
from Pago.forms import *
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404

@staff_member_required(login_url="/loginuser/")  
def pagos(request):
    return render(request, "pagos.html")  

class registroPagos(CreateView):
    model = Pago
    template_name = 'RegistroPago.html'
    second_model = Alumno
    form_class = FormularioPago
    success_url = reverse_lazy('registroPagos')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk',0)
        alumno = self.second_model.objects.get(id=pk)
        context=super(registroPagos, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            context['alumno']=self.Alumno.objects.get(pk=alumno.id)
            return context 
    
    def post(self, request, pk, *args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST) 
        if form.is_valid():
            registropago = form.save(commit=False)
            registropago.PagoRegistrado = "Mensual"
            registropago.alumno_id = self.kwargs.get('pk')
            registropago.save()
            return render(request,'Registropago.html', {'registropago' : registropago})
        else:
            return self.render_to_response(self.get_context_data(form=form)) 


class diferentepago(CreateView):
    model = Pago
    template_name = 'RegistroPago1.html'
    second_model = Alumno
    form_class = FormularioDELPAGO
    success_url = reverse_lazy('diferentepago')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk',0)
        alumno = self.second_model.objects.get(id=pk)
        context=super(diferentepago, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            context['alumno']=self.Alumno.objects.get(pk=alumno.id)
            return context 
    
    def post(self, request, pk, *args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST) 
        if form.is_valid():
            registropago1 = form.save(commit=False)
            registropago1.PagoRegistrado = "modelo_educativo"
            registropago1.alumno_id = self.kwargs.get('pk')
            registropago1.save()
            return render(request,'Registropago1.html', {'registropago1' : registropago1})
        else:
            return self.render_to_response(self.get_context_data(form=form)) 

class diferentepago1(CreateView):
    model = Pago
    template_name = 'RegistroPago1.html'
    second_model = Alumno
    form_class = FormularioDELPAGO
    success_url = reverse_lazy('diferentepago1')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk',0)
        alumno = self.second_model.objects.get(id=pk)
        context=super(diferentepago1, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            context['alumno']=self.Alumno.objects.get(pk=alumno.id)
            return context 
    
    def post(self, request, pk, *args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST) 
        if form.is_valid():
            registropago1 = form.save(commit=False)
            registropago1.PagoRegistrado = "reincripcion"
            registropago1.alumno_id = self.kwargs.get('pk')
            registropago1.save()
            return render(request,'Registropago1.html', {'registropago1' : registropago1})
        else:
            return self.render_to_response(self.get_context_data(form=form)) 

class diferentepago2(CreateView):
    model = Pago
    template_name = 'RegistroPago1.html'
    second_model = Alumno
    form_class = FormularioDELPAGO
    #second_form_class = FormularioAlumno
    success_url = reverse_lazy('diferentepago2')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk',0)
        context=super(diferentepago2, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            context['alumno']=self.Alumno.objects.get(pk=alumno.id)
            return context 
    
    def post(self, request, *args, **kwargs):
        self.object=self.get_object
        id_alumno = kwargs['pk']
        form=self.form_class(request.POST)
        if form.is_valid():
            registropago1 = form.save(commit=False)
            Alumno.objects.filter(id=id_alumno).update(certificado=True)
            registropago1.PagoRegistrado = "certificado"
            registropago1.Findepagos = True
            registropago1.alumno_id = self.kwargs.get('pk')
            registropago1.save()
            return render(request,'Registropago1.html', {'registropago1' : registropago1})
        else:
            return self.render_to_response(self.get_context_data(form=form)) 

class anual(CreateView):
    model = Pago
    template_name = 'RegistroPago1.html'
    second_model = Alumno
    form_class = FormularioDELPAGO
    success_url = reverse_lazy('anual')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk',0)
        alumno = self.second_model.objects.get(id=pk)
        context=super(anual, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            context['alumno']=self.Alumno.objects.get(pk=alumno.id)
            return context 
    
    def post(self, request, pk, *args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST) 
        if form.is_valid():
            registropago1 = form.save(commit=False)
            registropago1.PagoRegistrado = "anual"
            registropago1.alumno_id = self.kwargs.get('pk')
            registropago1.save()
            return render(request,'Registropago1.html', {'registropago1' : registropago1})
        else:
            return self.render_to_response(self.get_context_data(form=form)) 

class Manual(CreateView):
    model = Pago
    template_name = 'RegistroPago1.html'
    second_model = Alumno
    form_class = FormularioDELPAGO
    success_url = reverse_lazy('Manual')

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk',0)
        alumno = self.second_model.objects.get(id=pk)
        context=super(Manual, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            context['alumno']=self.Alumno.objects.get(pk=alumno.id)
            return context 
    
    def post(self, request, pk, *args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST) 
        if form.is_valid():
            registropago1 = form.save(commit=False)
            registropago1.PagoRegistrado = "Manual"
            registropago1.alumno_id = self.kwargs.get('pk')
            registropago1.save()
            return render(request,'Registropago1.html', {'registropago1' : registropago1})
        else:
            return self.render_to_response(self.get_context_data(form=form))             

def alumnoConPagosPendientes(request):
    year=datetime.now().year 
    month=datetime.now().month 
    day=datetime.now().day
    inicioAlumno=Alumno.objects.all()
    totalc=Pago.objects.filter(fechaPago__year=year, fechaPago__month=month).exclude(Estado_pago=True)
    return render(request,'pagosPendientes.html',{'alumno':totalc})     

def alumnoConPagosnoRealizo(request):
    noPagado=Alumno.objects.raw('''SELECT C.id, C.matricula, C.nombreA, C.apellidoPA, C.apellidoMA
                                 FROM 'Cedva1_alumno' AS C LEFT JOIN 'Cedva1_pago' AS P ON(C.id = P.alumno_id)
                                 WHERE C.id AND P.id IS NULL;''')
    return render(request,'pagonoRealizado.html',{'noPagado':noPagado})  

@staff_member_required(login_url="/loginuser/") 
def pagoalumno(request):
    return render(request, "pagosAlumno.html") 

@staff_member_required(login_url="/loginuser/") 
def alumnoConPagosRetrazados(request):
    year=datetime.now().year 
    month=datetime.now().month 
    day=datetime.now().day
    inicioAlumno=Alumno.objects.all()
    totalc=Pago.objects.filter(fechaPago__year=year, fechaPago__month=month,PagoRegistrado="Mensual")
    return render(request,'pagosCONretrazo.html',{'alumno':totalc,'inicioAlumno':inicioAlumno})     


@staff_member_required(login_url="/loginuser/")    
def AlumnoPagoListView(request,pk): 
    pago=Pago.objects.filter(alumno_id=pk,PagoRegistrado="Mensual")
    Modelo=Pago.objects.filter(alumno_id=pk,PagoRegistrado="modelo_educativo")
    reincripcion=Pago.objects.filter(alumno_id=pk,PagoRegistrado="reincripcion")
    certificado=Pago.objects.filter(alumno_id=pk,PagoRegistrado="certificado")
    anual=Pago.objects.filter(alumno_id=pk,PagoRegistrado="anual")
    Manual=Pago.objects.filter(alumno_id=pk,PagoRegistrado="Manual")
    total = Pago.objects.filter(alumno_id=pk).count()
    alumno = Alumno.objects.filter(id=pk).only('nombreA', 'apellidoPA', 'apellidoMA','especialidad')
    return render(request,'pagosAlumno.html',{'pago':pago,'anual':anual,'Manual':Manual ,'total':total, 'alumno':alumno, 'Modelo':Modelo, 'reincripcion':reincripcion,'certificado':certificado})      

class Actualizarpago(UpdateView):
    model=Pago
    template_name='actualizaPago.html'
    form_class = FormularioPago

    def get_success_url(self):
        return reverse_lazy('pagoalumno',kwargs={'pk':self.object.alumno_id})

class ActualizarpagoOTRO(UpdateView):
    model=Pago
    template_name='actualizaPago.html'
    form_class = FormularioACTUALIZAROTROS

    def get_success_url(self):
        return reverse_lazy('pagoalumno',kwargs={'pk':self.object.alumno_id})

def AlumnoPListView(request):
    model =Alumno.objects.filter(activo_por_pagos=True,certificado=False)
    return render(request,'pagos.html',{'listas':model})      
          


class eliminarPago(DeleteView):
    model = Pago
    template_name = 'PagoElimina.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Pago'] = 'Pago'
        context['list_url'] = reverse_lazy('pagoalumno', kwargs={'pk':self.object.alumno_id})
        return context
    
    def get_success_url(self):
        return reverse_lazy('pagoalumno',kwargs={'pk':self.object.alumno_id})