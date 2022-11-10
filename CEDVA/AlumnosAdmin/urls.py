from django.urls import path
from AlumnosAdmin import views

urlpatterns = [
    path('alumnos', views.AlumnoListView, name="alumnos"),
    path('registroAlumno', views.registrarAlumno.as_view(), name="registroAlumno"), 
    path('<int:pk>/ver', views.ver.as_view(), name="ver"),
    path('<int:pk>/update', views.actualizarAlumnos.as_view(), name="update"),
    path('<int:pk>/delete',views.Eliminar.as_view(),name='elimina'), 

    ]