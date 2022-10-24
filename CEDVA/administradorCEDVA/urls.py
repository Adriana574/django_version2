from django.urls import path

from . import views



urlpatterns = [
   
  
    path('adminadd',views.AdministradorCreateView, name="adminadd"),
   # path('adminadd',views.userADDCreateView.as_view(), name="adminadd"),
    
]