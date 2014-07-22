# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
	infos = InformacionGeneral.objects.filter(categoria = "IG").order_by("prioridad")
	tecnos = InformacionGeneral.objects.filter(categoria = "TG").order_by("prioridad")
	lengs = InformacionGeneral.objects.filter(categoria = "LG").order_by("prioridad")
	exps = ExperienciaProfesional.objects.all().order_by("-desde")
	estus = Estudio.objects.all().order_by("-fecha")
	proyes = Proyecto.objects.all().order_by("-fecha")
	
	return render(request,"index.html",{"infos": infos, "tecnos":tecnos,"lengs":lengs,"exps":exps,"estus":estus,"proyes":proyes})
