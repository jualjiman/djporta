# -*- coding: utf-8 -*-

import cStringIO as StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
"""import requests"""

fbAppId = 848121238581514
fb = {
	"url" : "",
	"title" : "CV Juan Alberto Jiménez Ángel",
	"description" : "Autodidacta, inquieto y apasionado con las nuevas tecnologías de desarrollo de software que actualmente están permitiendo ser al mundo un lugar más rápido y cómodo.",
}

# Create your views here.
def home(request):
	infos = InformacionGeneral.objects.filter(categoria = "IG", activo = True).order_by("-prioridad")
	tecnos = InformacionGeneral.objects.filter(categoria = "TG", activo = True).order_by("-prioridad")
	lengs = InformacionGeneral.objects.filter(categoria = "LG", activo = True).order_by("-prioridad")
	exps = ExperienciaProfesional.objects.filter(activo = True).order_by("-desde")

	return render(
		request,
		"index.html",
		{
			"infos": infos, 
			"tecnos":tecnos,
			"lengs":lengs,
			"exps":exps,
		})

def estudios(request):
	estus = Estudio.objects.filter(activo = True).order_by("-fecha")
	
	return render(
		request,
		"estudios.html",
		{
			"estus":estus,
		})

def proyectos(request):
	proyes = Proyecto.objects.filter(activo = True).order_by("-fecha")
	
	return render(
		request,
		"proyectos.html",
		{
			"proyes":proyes,
		})

"""
siempre estar pendiente de colocar el form como las variables que le pasas al template 
tambien de colocar la linea de encoding para utf8 en cada lugar donde vayas a usar acentos o caracteres epeciales
importar el form 
"""

"""
requests.post(
"https://api.mailgun.net/v2/jualjiman.com/messages",
auth=("api", "key-1fe898bc8e3b6d509eb0af3801efa6f7"),

data={"from": nombre + " <" + email + ">",
      "to": ["contacto@jualjiman.com",],
      "subject": "Mensaje desde jualjiman.com",
      "text": mensaje})
"""
def contactame(request):
	if request.is_ajax():
	    nombre = request.POST['name']
	    email = request.POST['email']
	    mensaje = request.POST['message']

	    dfrom = nombre + " <" +  email + ">"
	    mensaje = dfrom + "\n\n" + mensaje

	    send_mail(
			'Mensaje desde Jualjiman.com', 
			mensaje, 
			"Jualjiman's mailer <mailer@jualjiman.com>", 
			['contacto@jualjiman.com',], 
			fail_silently=False
		)

	    msj = Mensaje(nombre=dfrom, email=email,mensaje=mensaje)
	    msj.save()

	    return HttpResponse('Ok')
	else:
		form = ContactForm()
		return render(
			request,
			"contactame.html",
			{
				"form": form,
			})


# Handler for HTTP POST to http://myhost.com/messages for the route defined above
@csrf_exempt
def messages(request):
	if request.method == 'POST':
		sender    = request.POST.get('sender')
		recipient = request.POST.get('recipient')
		subject   = request.POST.get('subject', '')

		body_plain = request.POST.get('body-plain', '')
		body_without_quotes = request.POST.get('stripped-text', '')
		# note: other MIME headers are also posted here...

		nattachments = 0
		# attachments:
		for key in request.FILES:
			file = request.FILES[key]
			nattachments += 1
        	# do something with the file
		
		msg = Email(sender=sender,recipient=recipient,subject=subject,body=body_without_quotes,nattachments=nattachments)
		msg.save()
    # Returned text is ignored but HTTP status code matters:
    # Mailgun wants to see 2xx, otherwise it will make another attempt in 5 minutes
	return HttpResponse('OK')