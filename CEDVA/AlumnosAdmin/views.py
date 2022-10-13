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

class Actualizar(UpdateView):
    model=Alumno
    template_name='actualiza.html'
    context_object_name='cancion'
    fields=('nombreA', 'apellidoPA', 'apellidoMA')

    def get_success_url(self):
        return reverse('alumnos')


class Eliminar(DeleteView):
    model=Alumno
    template_name='AlumnoElimina.html'
    success_url=reverse_lazy('alumnos')

    def get_success_url(self):
        return reverse('alumnos')
    

def registrarAlumno(request):
    form = FormularioTutor(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        nt = form_data.get("nombreT")
        apt = form_data.get("apellidoPT")
        amt = form_data.get("apellidoMT") 
        tel = form_data.get("telefono") 
        pt = form_data.get("padreT") 
                
        obj = Tutor.objects.create(nombreT=nt, apellidoPT=apt, apellidoMT=amt, telefono=tel, padreT=pt)

    Dirform = FormularioDireccion(request.POST or None)
    if Dirform.is_valid():
        form_data = Dirform.cleaned_data
        cal = form_data.get("calle")
        lot = form_data.get("lote")
        manz = form_data.get("manzana")
        col = form_data.get("colonia")
        dm = form_data.get("delegacionMunicipio")
        cp1 = form_data.get("codigopostal")
        cie = form_data.get("ciudadOestado")

        obj2 = Direccion.objects.create(calle=cal, lote=lot, manzana=manz, colonia=col, delegacionMunicipio=dm, codigopostal=cp1, ciudadOestado=cie)

    EspeForm = FormularioEspecialidad(request.POST or None)
    if EspeForm.is_valid():
        form_data = EspeForm.cleaned_data
        nomE = form_data.get("nombreE")

        obj3 = Especialidad.objects.create(nombreE=nomE)

    UserForm = FormularioUsuario(request.POST or None)
    if UserForm.is_valid():
        form_data = UserForm.cleaned_data
        nomU = form_data.get("username")
        pas = form_data.get("password") 

        obj4 = User.objects.create_user(username=nomU, password=pas)

    AlumForm = FormularioAlumno(request.POST or None)
    if AlumForm.is_valid():
        form_data = AlumForm.cleaned_data
        mat = form_data.get("matricula")
        nomA = form_data.get("nombreA")
        snomA = form_data.get("snombreA")
        appA = form_data.get("apellidoPA")
        apmA = form_data.get("apellidoMA")
        eda = form_data.get("edad")
        con = form_data.get("convenio")
        iniC = form_data.get("inicioCurso")
        finC = form_data.get("finalCurso")
        obser = form_data.get("observaciones")

        obj5 = Alumno.objects.create(matricula=mat, nombreA=nomA, snombreA=snomA, apellidoPA=appA, apellidoMA=apmA, edad=eda, convenio=con, inicioCurso=iniC, finalCurso=finC, observaciones=obser)

    context = {
        'form': form,
        'Dirform': Dirform,
        'EspeForm': EspeForm,
        'UserForm': UserForm,
        'AlumForm': AlumForm
    }
        
    return render(request, "registroAlumno.html", context)