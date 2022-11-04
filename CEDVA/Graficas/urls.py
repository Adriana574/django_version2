from django.urls import path
from Graficas import views

urlpatterns = [
    path('grafico',views.grafico.as_view(),name="grafico"),    
]