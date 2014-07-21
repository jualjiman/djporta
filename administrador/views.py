# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
	infos = InformacionGeneral.objects.filter(categoria = "IG")
	tecnos = InformacionGeneral.objects.filter(categoria = "TG")
	lengs = InformacionGeneral.objects.filter(categoria = "LG")
	exps = ExperienciaProfesional.objects.all()
	estus = Estudio.objects.all()
	proyes = Proyecto.objects.all()
	
	return render(request,"index.html",{"infos": infos, "tecnos":tecnos,"lengs":lengs,"exps":exps,"estus":estus,"proyes":proyes})
