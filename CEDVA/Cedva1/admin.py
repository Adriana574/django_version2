from django.contrib import admin
from .models import Tutor
from .models import Direccion
from .models import Escuela
from .models import Especialidad 
from .models import Administrador
from .models import Alumno
from .models import Pago

class TutorAdmin(admin.ModelAdmin):
	readonly_fields=('created','update')
	
		
admin.site.register(Tutor,TutorAdmin)
admin.site.register(Direccion)
admin.site.register(Escuela)
admin.site.register(Especialidad) 
admin.site.register(Administrador)
admin.site.register(Alumno)
admin.site.register(Pago)



