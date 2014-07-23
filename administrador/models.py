 # -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from datetime import date, datetime

# Create your models here.

categorias = (
	('IG', u'Información general'),
	('TG', 'Tecnologias'),
	('LG', 'Lenguajes'),
)

class InformacionGeneral(models.Model):
	class Meta:
		verbose_name_plural = "Informacion General"

	campo = models.CharField(max_length=60)
	info = models.CharField(max_length=90)
	categoria = models.CharField(max_length=2, choices=categorias)
	
	prioridad = models.IntegerField(default=1)

	def __unicode__(self): # __str__(self):
		return self.campo

class ExperienciaProfesional(models.Model):
	class Meta:
		verbose_name_plural = "Experiencia Profesional"

	puesto = models.CharField(max_length=50)
	lugar = models.CharField(max_length=50)
	#fecha = models.CharField(max_length=50) 
	desde = models.DateField(default = date.today)
	hasta = models.DateField(default = date.today, blank = True, null = True)
	info = models.TextField(blank=True)

	def __unicode__(self): # __str__(self):
		return self.puesto

class Estudio(models.Model):

	titulo = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(blank=True)
	#fecha = models.CharField(max_length=50)
	fecha = models.DateField(default = date.today)
	lugar = models.CharField(max_length=50, blank=True)
	completado = models.BooleanField(default=False)

	def __unicode__(self): # __str__(self):
		return self.titulo

class Proyecto(models.Model):
	titulo = models.CharField(max_length=50)
	descripcion = models.TextField(blank=True)
	tecnologias = models.CharField(max_length=80)
	#fecha = models.CharField(max_length=50)
	fecha = models.DateField(default = date.today)
	link = models.URLField(blank=True)
	imagen = ImageField(upload_to="proyectos")

	def __str__(self):
		return self.titulo

class Mensaje(models.Model):
	nombre = models.CharField(max_length=100)
	email = models.EmailField()
	mensaje = models.TextField()
	fecha = models.DateTimeField(default=datetime.now(),editable=False)

	def __str__(self):
		return self.nombre