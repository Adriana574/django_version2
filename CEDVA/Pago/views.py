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
from Pago.forms import FormularioPago
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required(login_url="/loginuser/")  
def pagos(request):
    return render(request, "pagos.html")  

class registroPagos(CreateView):
    model=Pago
    template_name='RegistroPago.html'
    second_model=Alumno
    form_class=FormularioPago

    def get_context_data(self, **kwargs):
        context=super(registroPagos, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
            return context 

    def post(self, request, *args, **kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST)

        if form.is_valid():
            registropago = form.save(commit=False)
            registropago.alumno_id = self.kwargs.get('pk')
            registropago.save()
            return HttpResponseRedirect(self.get_success_url(reverse_lazy('registroPagos')))

        else:
            return self.render_to_response(self.get_context_data(form=form))

@staff_member_required(login_url="/loginuser/") 
def pagoalumno(request):
    return render(request, "pagosAlumno.html") 


@staff_member_required(login_url="/loginuser/")    
def AlumnoPagoListView(request,pk):

    pago=Pago.objects.filter(alumno_id=pk)
    return render(request,'pagosAlumno.html',{'pago':pago})      

class Actualizarpago(UpdateView):
    model=Pago
    template_name='actualizaPago.html'
    form_class = FormularioPago

    def get_success_url(self):
        return reverse_lazy('pagoalumno',kwargs={'pk':self.object.id})

class AlumnoPListView(ListView):
    model =Alumno
    template_name='pagos.html'
    context_object_name='listas'       

class EliminarPago(DeleteView):
    model=Pago
    template_name='PagoElimina.html'
    context_object_name='pagoelimina'

    def get_success_url(self):
        success_url=reverse_lazy('pagoalumno',kwargs={'pk':self.object.id})