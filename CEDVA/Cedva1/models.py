from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from AlumnosAdmin.choices import *

from datetime import datetime


class Tutor(models.Model):
	nombreT=models.CharField(max_length=100)
	apellidoPT=models.CharField(max_length=100)
	apellidoMT=models.CharField(max_length=100)
	telefono=models.CharField(max_length=100)
	padreT=models.CharField(max_length=100, choices=padretutores, default='p')
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "tutor"
		verbose_name_plural = "tutores"

	def __str__(self):
		return self.nombreT


class Direccion(models.Model):
	calle=models.CharField(max_length=100)
	lote=models.IntegerField()
	manzana=models.IntegerField()
	colonia=models.CharField(max_length=100)
	delegacionMunicipio=models.CharField(max_length=100)
	codigopostal=models.IntegerField()
	ciudadOestado=models.CharField(max_length=100, choices=ciudades, default='p')
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "direccion"
		verbose_name_plural = "direcciones"

	def __str__(self):
		return self.calle

class Escuela(models.Model):
	plantel=models.CharField(max_length=100)
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "plantel"
		verbose_name_plural = "planteles"

	def __str__(self):
		return self.plantel
 
class Especialidad(models.Model):
	idEscuela = models.ForeignKey(Escuela,related_name="subcategories8",blank=True , null= True, on_delete=models.CASCADE)
	nombreE=models.CharField(max_length=100, choices=especialidades, default='p')
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "especialidad"
		verbose_name_plural = "especialidades"

	def __str__(self):
		return self.nombreE	

class Administrador(models.Model):
	escuela = models.ForeignKey(Escuela,related_name="subcategories5",blank=True , null= True, on_delete=models.CASCADE)
	usuarioA= models.ForeignKey(User,related_name="subcategories6",blank=True , null= True, on_delete=models.CASCADE )
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
	especialidad = models.ForeignKey(Especialidad, related_name="subcategories1",blank=True , null= True, on_delete=models.CASCADE )
	direccion= models.ForeignKey(Direccion, related_name="subcategories2",blank=True , null= True, on_delete=models.CASCADE )
	tutor = models.ForeignKey(Tutor, related_name="subcategories3",blank=True , null= True, on_delete=models.CASCADE )
	user = models.ForeignKey(User, blank=True , null= True, on_delete=models.CASCADE )
	matricula = models.CharField(max_length=100,blank=True)
	activo_por_pagos = models.BooleanField(('active'), default=True,blank=True , null=True)
	nombreA = models.CharField(max_length=100)
	snombreA = models.CharField(max_length=100, blank=True , null= True)
	apellidoPA = models.CharField(max_length=100)
	apellidoMA = models.CharField(max_length=100)
	edad = models.IntegerField()
	convenio = models.CharField(max_length=800, choices=convenio, default='p')
	inicioCurso = models.DateField()
	finalCurso = models.DateField()
	observaciones = models.CharField(max_length=1000)
	certificado = models.BooleanField(('Certificado'), default=False)
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "alumno"
		verbose_name_plural = "alumnos"

	def __str__(self):
		return self.matricula +': '+self.nombreA+' '+self.apellidoPA +' ' +self.apellidoMA + ' : ' + self.especialidad.nombreE
								

class Pago(models.Model):
	alumno = models.ForeignKey(Alumno, related_name="subcategories7",blank=True , null= True, on_delete=models.CASCADE)
	PagoRegistrado=models.CharField(max_length=120,blank=True , null= True)
	folio=models.IntegerField()
	Estado_pago = models.BooleanField(('revicion'),default=False, blank=True , null= True)
	tipoPago=models.CharField(max_length=100)
	monto=models.IntegerField()
	Findepagos = models.BooleanField(('Concluido'), default=False)
	fechaPago=models.DateField()
	mesPagado=models.CharField(max_length=12,blank=True , null= True)
	horapago=models.TimeField()
	created=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.tipoPago