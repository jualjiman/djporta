# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from easy_pdf.views import PDFTemplateView
import requests

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

	    dfrom = nombre + " <" +  email + ">"
	    
	    requests.post(
        "https://api.mailgun.net/v2/jualjiman.com/messages",
        auth=("api", "key-1fe898bc8e3b6d509eb0af3801efa6f7"),

        data={"from": nombre + " <" + email + ">",
              "to": ["contacto@jualjiman.com",],
              "subject": "Mensaje desde jualjiman.com",
              "text": mensaje})

	    msj = Mensaje(nombre=dfrom, email=email,mensaje=mensaje)
	    msj.save()

	    return HttpResponse('Ok')
	else:
		form = ContactForm()
		return render(request,"contactame.html",{"form": form})


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

class HelloPDFView(PDFTemplateView):
	template_name = "pdf.html"
	infos = InformacionGeneral.objects.filter(categoria = "IG", activo = True).order_by("-prioridad")
	tecnos = InformacionGeneral.objects.filter(categoria = "TG", activo = True).order_by("-prioridad")
	lengs = InformacionGeneral.objects.filter(categoria = "LG", activo = True).order_by("-prioridad")
	exps = ExperienciaProfesional.objects.filter(activo = True).order_by("-desde")
	
	def get_context_data(self, **kwargs):

		return super(HelloPDFView, self).get_context_data(
            		pagesize="A4",
            		title="Hi there!",
			infos=self.infos,
			tecnos=self.tecnos,
			lengs=self.lengs,
			exps=self.exps,
            		**kwargs
        	)
