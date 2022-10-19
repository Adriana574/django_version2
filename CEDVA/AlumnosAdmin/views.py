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
    template_name='ver.html'

    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['Tutor'] = Tutor.objects.get(pk=pk)
        context['Direccion'] = Direccion.objects.get(pk=pk)
        context['Alumno'] = Alumno.objects.get(pk=pk)
        return context 


#@login_required(login_url="/loginuser/") 
class AlumnoListView(ListView):
    model = Alumno
    template_name='alumnos.html'
    context_object_name='listas'

    
class Eliminar(DeleteView):
    model=Alumno
    template_name='AlumnoElimina.html'
    success_url=reverse_lazy('alumnos')

    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['Tutor'] = Tutor.objects.get(pk=pk)
        context['Direccion'] = Direccion.objects.get(pk=pk)
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
 
    success_url = reverse_lazy('alumnos')

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
            return HttpResponseRedirect(self.get_success_url())

        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4, form5=form5))

class actualizarAlumnos(UpdateView)
    model = Alumno