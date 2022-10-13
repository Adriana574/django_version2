from django.urls import path
from alumnosC import views

urlpatterns = [
    path('loginuser2/',views.LoginUser2, name="loginuser2"),
    path('logout2/', views.LogoutUser2, name="logout2"), 
    path('1inicio',views.HomeAlumno,name="1inicio"),
    path('registroPago', views.registroP, name="registroPago"),
    path('avance', views.Avance, name="avance"),
    path('alumnos2', views.AlumnoDatosListView.as_view(), name="alumnos2"),    
]