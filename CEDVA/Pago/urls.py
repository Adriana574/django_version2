from django.urls import path
from Pago import views

urlpatterns = [

path('pagos', views.AlumnoPListView.as_view(), name="pagos"),
path('<int:pk>/registroPagos', views.registroPagos.as_view(), name="registroPagos"),
path('<int:pk>/pagoalumno', views.AlumnoPagoListView, name="pagoalumno"),
path('<int:pk>/pago',views.Actualizarpago.as_view(),name='actualizaP'),
path('<int:pk>/deletePago',views.eliminarPago.as_view(),name='eliminar'),
]
