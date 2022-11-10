from django.urls import path
from alumnosC import views

urlpatterns = [
    path('loginuser2/',views.LoginUser2, name="loginuser2"),
    path('logout2/', views.LogoutUser2, name="logout2"), 
    path('1inicio',views.HomeAlumno,name="1inicio"), 
    path('<int:pk>/registroPago', views.registroP.as_view() , name="registroPago"),
    path('<int:pk>/avance', views.Avance.as_view(), name="avance"),
    path('<int:pk>/alumnos2', views.AlumnoDatosListView.as_view(), name="alumnos2"),    
]