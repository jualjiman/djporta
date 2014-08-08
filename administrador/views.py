# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
	infos = InformacionGeneral.objects.filter(categoria = "IG", activo = True).order_by("-prioridad")
	tecnos = InformacionGeneral.objects.filter(categoria = "TG", activo = True).order_by("-prioridad")
	lengs = InformacionGeneral.objects.filter(categoria = "LG", activo = True).order_by("-prioridad")
	exps = ExperienciaProfesional.objects.filter(activo = True).order_by("-desde")
	
	return render(request,"index.html",{"infos": infos, "tecnos":tecnos,"lengs":lengs,"exps":exps,})

def estudios(request):
	estus = Estudio.objects.filter(activo = True).order_by("-fecha")
	
	return render(request,"estudios.html",{"estus":estus,})

def proyectos(request):
	proyes = Proyecto.objects.filter(activo = True).order_by("-fecha")
	
	return render(request,"proyectos.html",{"proyes":proyes,})

"""
siempre estar pendiente de colocar el form como las variables que le pasas al template 
tambien de colocar la linea de encoding para utf8 en cada lugar donde vayas a usar acentos o caracteres epeciales
importar el form 
"""
def contactame(request):
	if request.is_ajax():
	    nombre = request.POST['name']
	    email = request.POST['email']
	    mensaje = request.POST['message']

	    msj = Mensaje(nombre=nombre, email=email,mensaje=mensaje)
	    msj.save()

	    return HttpResponse('Ok')
	else:
		form = ContactForm()
		return render(request,"contactame.html",{"form": form})
