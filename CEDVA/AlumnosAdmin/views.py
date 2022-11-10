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
from django.views.generic import DetailView
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from AlumnosAdmin.forms import *
from django.shortcuts import get_object_or_404

    
@staff_member_required  
def alumnos(request):
    return render(request, "alumnos.html")

class ver(TemplateView):
    model=Alumno
    template_name='ver.html'

    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs.get('pk', 0)
        alumno=self.model.objects.get(id=pk)
        context = super().get_context_data(**kwargs)
        context['Tutor'] = Tutor.objects.get(id=alumno.tutor_id)
        context['User'] = User.objects.get(id=alumno.user_id)
        context['Especialidad'] = Especialidad.objects.get(id=alumno.especialidad_id)
        context['Direccion'] = Direccion.objects.get(id=alumno.direccion_id)
        context['Alumno'] = Alumno.objects.get(pk=alumno.id)
        return context 


#@login_required(login_url="/loginuser/")    
def AlumnoListView(request):
    model2=Alumno.objects.filter(activo_por_pagos=True,certificado=False)
    model =Alumno.objects.filter(activo_por_pagos=True,certificado=True)
    return render(request,'alumnos.html',{'listas':model,'model2':model2}) 

    
class Eliminar(DeleteView):
    model=Alumno
    template_name='AlumnoElimina.html'
    success_url=reverse_lazy('alumnos')

    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['Tutor'] = Tutor.objects.get(pk=pk)
        context['Direccion'] = Direccion.objects.get(pk=pk)
        context['Especialidad'] = Especialidad.objects.get(pk=pk)
        context['Alumno'] = Alumno.objects.get(pk=pk)
        return context 

    def get_success_url(self):
        return reverse('alumnos')
    

class registrarAlumno(CreateView):
    model = Alumno
    template_name = 'registroAlumno.html'
    form_class = FormularioAlumno
    second_form_class = FormularioTutor
    three_form_class = FormularioDireccion
    four_form_class = FormularioEspecialidad
    five_form_class = FormularioUsuario
 
    success_url = reverse_lazy('registroAlumno')

    def get_context_data(self, **kwargs):
        context = super(registrarAlumno, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.three_form_class(self.request.GET)
        if 'form4' not in context:
            context['form4'] = self.four_form_class(self.request.GET)
        if 'form5' not in context:
            context['form5'] = self.five_form_class(self.request.GET)

            return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.three_form_class(request.POST)
        form4 = self.four_form_class(request.POST)
        form5 = self.five_form_class(request.POST)

        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            registro = form.save(commit=False)
            registro.tutor = form2.save()
            registro.direccion = form3.save()
            registro.especialidad = form4.save()
            registro.user = form5.save()
            registro.save()
            messages.success(request, 'Alumno registrado con éxito.')
            return HttpResponseRedirect(self.get_success_url())

        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4, form5=form5))

class actualizarAlumnos(UpdateView):
    model = Alumno
    second_model = Tutor
    three_model = Direccion
    four_model = Especialidad
    five_model = User
    template_name = 'actualiza.html'
    form_class = FormularioAlumnoUpdate
    second_form_class = FormularioTutor
    three_form_class = FormularioDireccion
    four_form_class = FormularioEspecialidad
    five_form_class = FormularioUsuarioUpdate
    success_url = reverse_lazy('alumnos')

    def get_context_data(self, **kwargs):
        context = super(actualizarAlumnos, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        alumno = self.model.objects.get(id=pk)
        tutor = self.second_model.objects.get(id=alumno.tutor_id)
        direccion = self.three_model.objects.get(id=alumno.direccion_id)
        especialidad = self.four_model.objects.get(id=alumno.especialidad_id)
        user = self.five_model.objects.get(id=alumno.user_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=tutor)
        if 'form3' not in context:
            context['form3'] = self.three_form_class(instance=direccion)
        if 'form4' not in context:
            context['form4'] = self.four_form_class(instance=especialidad)
        if 'form5' not in context:
            context['form5'] = self.five_form_class(instance=user)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_alumno = kwargs['pk']
        alumno = self.model.objects.get(id=id_alumno)
        tutor = self.second_model.objects.get(id=alumno.tutor_id)
        direccion = self.three_model.objects.get(id=alumno.direccion_id)
        especialidad = self.four_model.objects.get(id=alumno.especialidad_id)
        user = self.five_model.objects.get(id=alumno.user_id)
        form = self.form_class(request.POST, instance=alumno)
        form2 = self.second_form_class(request.POST, instance=tutor)
        form3 = self.three_form_class(request.POST, instance=direccion)
        form4 = self.four_form_class(request.POST, instance=especialidad)
        form5 = self.five_form_class(request.POST, instance=user)
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            form.save()
            form2.save()
            form3.save()
            form4.save()
            form5.save()

            messages.success(request, 'Alumno modificado con éxito.')

            return HttpResponseRedirect(self.get_success_url())
        else:
             return HttpResponseRedirect(self.get_success_url())
