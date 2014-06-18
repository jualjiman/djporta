 # -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ThumbnailField

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

	def __unicode__(self): # __str__(self):
		return self.campo

class ExperienciaProfesional(models.Model):
	class Meta:
		verbose_name_plural = "Experiencia Profesional"

	puesto = models.CharField(max_length=50)
	lugar = models.CharField(max_length=50)
	fecha = models.CharField(max_length=50) 
	info = models.TextField(blank=True)

	def __unicode__(self): # __str__(self):
		return self.puesto

class Estudio(models.Model):

	titulo = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(blank=True)
	fecha = models.CharField(max_length=50)
	lugar = models.CharField(max_length=50, blank=True)
	completado = models.BooleanField(default=False)

	def __unicode__(self): # __str__(self):
		return self.titulo

class Proyecto(models.Model):
	titulo = models.CharField(max_length=50)
	descripcion = models.TextField(blank=True)
	tecnologias = models.CharField(max_length=80)
	fecha = models.CharField(max_length=50)
	link = models.URLField()
	imagen = ThumbnailField(upload_to='proyectos', size=(694, 418))
	#imagen = models.FileField(upload_to="proyectos")

	def __str__(self):
		return self.titulo
