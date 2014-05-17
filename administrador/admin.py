from django.contrib import admin
from .models import *

# Register your models here.
class InfoGralAdmin(admin.ModelAdmin):
	list_display = ('campo','info','categoria')

class ExpProAdmin(admin.ModelAdmin):
	list_display = ('puesto','lugar','fecha')

class EstAdmin(admin.ModelAdmin):
	list_display = ('titulo','nombre','lugar','completado')

class ProyeAdmin(admin.ModelAdmin):
	list_display = ('titulo','descripcion','fecha')

admin.site.register(InformacionGeneral,InfoGralAdmin)
admin.site.register(ExperienciaProfesional,ExpProAdmin)
admin.site.register(Estudio,EstAdmin)
admin.site.register(Proyecto,ProyeAdmin)