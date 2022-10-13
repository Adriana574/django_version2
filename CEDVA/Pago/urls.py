from django.urls import path
from Pago import views

urlpatterns = [
   
    path('pagos', views.AlumnoPListView.as_view(), name="pagos"),
    path('<int:pk>/pagoalumno', views.AlumnoPagoListView.as_view(), name="pagoalumno"),
    path('<int:pk>/pago',views.Actualizarpago.as_view(),name='actualizaP'),
    path('<int:pk>/deletePago',views.EliminarPago.as_view(),name='eliminar'),
    ]