from django.contrib import admin
from .models import *
from sorl.thumbnail.shortcuts import get_thumbnail

# Register your models here.
class InfoGralAdmin(admin.ModelAdmin):
	list_display = ('campo','info','categoria','prioridad')

class ExpProAdmin(admin.ModelAdmin):
	list_display = ('puesto','lugar','desde','hasta')

class EstAdmin(admin.ModelAdmin):
	list_display = ('titulo','nombre','lugar','completado','fecha')

class ProyeAdmin(admin.ModelAdmin):
	list_display = ('titulo','descripcion','fecha', 'imagen_proyecto')

	def imagen_proyecto(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'100x60', crop='center').url #format='PNG', quality=99

	imagen_proyecto.allow_tags = True

class MensAdmin(admin.ModelAdmin):
	list_display = ('nombre','email','mensaje','fecha')

admin.site.register(InformacionGeneral,InfoGralAdmin)
admin.site.register(ExperienciaProfesional,ExpProAdmin)
admin.site.register(Estudio,EstAdmin)
admin.site.register(Proyecto,ProyeAdmin)
admin.site.register(Mensaje,MensAdmin)
