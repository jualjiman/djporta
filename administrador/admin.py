from django.contrib import admin
from .models import *
from sorl.thumbnail import get_thumbnail

# Register your models here.
class InfoGralAdmin(admin.ModelAdmin):
	list_display = ('campo','info','categoria')

class ExpProAdmin(admin.ModelAdmin):
	list_display = ('puesto','lugar','fecha')

class EstAdmin(admin.ModelAdmin):
	list_display = ('titulo','nombre','lugar','completado')

class ProyeAdmin(admin.ModelAdmin):
	list_display = ('titulo','descripcion','fecha', 'imagen_proyecto')

	def imagen_proyecto(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'50x50').url

	imagen_proyecto.allow_tags = True

admin.site.register(InformacionGeneral,InfoGralAdmin)
admin.site.register(ExperienciaProfesional,ExpProAdmin)
admin.site.register(Estudio,EstAdmin)
admin.site.register(Proyecto,ProyeAdmin)