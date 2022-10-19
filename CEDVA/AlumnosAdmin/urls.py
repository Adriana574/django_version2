from django.urls import path
from AlumnosAdmin import views

urlpatterns = [
    path('alumnos', views.AlumnoListView.as_view(), name="alumnos"),
    path('registroAlumno', views.registrarAlumno.as_view(), name="registroAlumno"), 
    path('<int:pk>/ver', views.ver.as_view(), name="ver"),
    path('<int:pk>/delete',views.Eliminar.as_view(),name='elimina'), 

    ]