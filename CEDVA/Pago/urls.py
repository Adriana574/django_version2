from django.urls import path
from Pago import views

urlpatterns = [

path('pagos', views.AlumnoPListView, name="pagos"),
path('pendientes', views.alumnoConPagosPendientes, name="pendientes"),
path('norealizo', views.alumnoConPagosnoRealizo, name="norealizo"),
path('<int:pk>/registroPagos', views.registroPagos.as_view(), name="registroPagos"),
path('<int:pk>/diferentepago',views.diferentepago.as_view(), name="diferentepagos"),
path('<int:pk>/reincripcion',views.diferentepago1.as_view(), name="reincripcion"),
path('<int:pk>/certificado',views.diferentepago2.as_view(), name="certificado"),
path('<int:pk>/anual',views.anual.as_view(), name="anual"),
path('<int:pk>/Manual',views.Manual.as_view(), name="Manual"),
path('<int:pk>/pagoalumno', views.AlumnoPagoListView, name="pagoalumno"),
path('<int:pk>/pago',views.Actualizarpago.as_view(),name='actualizaP'),
path('<int:pk>/Actualizarpago',views.ActualizarpagoOTRO.as_view(),name='Actualizarpago'),
path('<int:pk>/deletePago',views.eliminarPago.as_view(),name='eliminar'),
]
