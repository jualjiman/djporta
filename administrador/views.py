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
	    send_simple_message()

	    return HttpResponse('Ok')
	else:
		form = ContactForm()
		return render(request,"contactame.html",{"form": form})

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v2/sandbox58531cd99f8b406d9932f7ff5259395c.mailgun.org/messages",
		auth=("api", "key-1fe898bc8e3b6d509eb0af3801efa6f7"),
		data={"from": "Mailgun Sandbox <postmaster@sandbox58531cd99f8b406d9932f7ff5259395c.mailgun.org>",
        	"to": "Juan Alberto Jimenez Angel <jualjiman@gmail.com>",
        	"subject": "Hello Juan Alberto Jimenez Angel",
        	"text": "Congratulations Juan Alberto Jimenez Angel, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})

