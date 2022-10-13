from django.db import models
from django.forms import ModelForm


class Tutor(models.Model):
	idtutor=models.BigAutoField(primary_key=True,  blank=False)
	nombreT=models.CharField(max_length=100)
	apellidoPT=models.CharField(max_length=100)
	apellidoMT=models.CharField(max_length=100)
	telefono=models.CharField(max_length=100)
	padreT=models.CharField(max_length=100)
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "tutor"
		verbose_name_plural = "tutores"

	def __str__(self):
		return self.nombreT


class Direccion(models.Model):
	iddireccion=models.BigAutoField(primary_key=True,  blank=False)
	calle=models.CharField(max_length=100)
	lote=models.IntegerField()
	manzana=models.IntegerField()
	colonia=models.CharField(max_length=100)
	delegacionMunicipio=models.CharField(max_length=100)
	codigopostal=models.IntegerField()
	ciudadOestado=models.CharField(max_length=100)
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "direccion"
		verbose_name_plural = "direcciones"

	def __str__(self):
		return self.calle



class Usuario(models.Model):
	idusuario=models.BigAutoField(primary_key=True,  blank=False)
	user=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	tipo=models.IntegerField()
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)


	class Meta:
		verbose_name = "usuario"
		verbose_name_plural = "usuarios"

	def __str__(self):
		return self.user
		
						
class Escuela(models.Model):
	idescuela=models.BigAutoField(primary_key=True)
	plantel=models.CharField(max_length=100)
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "plantel"
		verbose_name_plural = "planteles"

	def __str__(self):
		return self.plantel
 
class Especialidad(models.Model):
	idespecialidad=models.BigAutoField(primary_key=True)
	idescuela = models.ForeignKey(Escuela,related_name="subcategories8",blank=True , null= True, on_delete=models.CASCADE)
	nombreE=models.CharField(max_length=100)
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "especialidad"
		verbose_name_plural = "especialidades"

	def __str__(self):
		return self.nombreE		

class Administrador(models.Model):
	idadministrador=models.BigAutoField(primary_key=True,  blank=False)
	idescuela = models.ForeignKey(Escuela,related_name="subcategories5",blank=True , null= True, on_delete=models.CASCADE)
	idusuario= models.ForeignKey(Usuario,related_name="subcategories6",blank=True , null= True, on_delete=models.CASCADE )
	nombre=models.CharField(max_length=100)
	apellidoP=models.CharField(max_length=100)
	apellidoM=models.CharField(max_length=100)
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)
	

	class Meta:
		verbose_name = "administrador"
		verbose_name_plural = "administradores"

	def __str__(self):
		return self.nombre		
	
			
class Alumno(models.Model):
	idalumno = models.BigAutoField(primary_key=True)
	idescuela = models.ForeignKey(Escuela, related_name="subcategories",blank=True , null= True, on_delete=models.CASCADE )
	idespecialidad = models.ForeignKey(Especialidad,related_name="subcategories1",blank=True , null= True, on_delete=models.CASCADE )
	iddireccion= models.ForeignKey(Direccion,related_name="subcategories2",blank=True , null= True, on_delete=models.CASCADE )
	idtutor= models.ForeignKey(Tutor,related_name="subcategories3",blank=True , null= True, on_delete=models.CASCADE )
	idusuario= models.ForeignKey(Usuario,related_name="subcategories4",blank=True , null= True, on_delete=models.CASCADE )
	matricula=models.CharField(max_length=100,blank=True)
	nombreA=models.CharField(max_length=100)
	snombreA=models.CharField(max_length=100)
	apellidoPA=models.CharField(max_length=100)
	apellidoMA=models.CharField(max_length=100)
	edad=models.IntegerField()
	convenio=models.CharField(max_length=800)
	inicioCurso=models.DateField()
	finalCurso=models.DateField()
	observaciones=models.CharField(max_length=1000)
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "alumno"
		verbose_name_plural = "alumnos"

	def __str__(self):
		return self.matricula
								

class Pago(models.Model):
	idpago=models.BigAutoField(primary_key=True)
	idalumno = models.ForeignKey(Alumno, related_name="subcategories7",blank=True , null= True, on_delete=models.CASCADE)
	folio=models.IntegerField()
	tipoPago=models.CharField(max_length=100)
	monto=models.IntegerField()
	fechaPago=models.DateField()
	mesPagado=models.CharField(max_length=12)
	horapago=models.TimeField()
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True) 