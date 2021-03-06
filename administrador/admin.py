from django.contrib import admin
from .models import *
from sorl.thumbnail.shortcuts import get_thumbnail

# Register your models here.
class InfoGralAdmin(admin.ModelAdmin):
	list_display = ('campo','info','categoria','prioridad','activo',)
	search_fields = ('campo',)
	list_filter = ('categoria',)

class ExpProAdmin(admin.ModelAdmin):
	list_display = ('puesto','lugar','desde','hasta','actual','activo',)
	search_fields = ('puesto','lugar',)

class EstAdmin(admin.ModelAdmin):
	list_display = ('titulo','nombre','lugar','completado','fecha','activo',)
	search_fields = ('titulo','nombre','lugar',)

class ProyeAdmin(admin.ModelAdmin):
	list_display = ('titulo','descripcion','fecha', 'imagen_proyecto','activo',)
	search_fields = ('titulo',)

	def imagen_proyecto(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'100x60', crop='center').url #format='PNG', quality=99

	imagen_proyecto.allow_tags = True

class ImageAdmin(admin.ModelAdmin):
	list_display = ("show_avatar", "activo")

	def show_avatar(self,obj):
		return '<img src="%s" />' % get_thumbnail(obj.imagen,'80x80', crop='center').url #format='PNG', quality=99

	show_avatar.allow_tags = True

class MensAdmin(admin.ModelAdmin):
	list_display = ('nombre','email','mensaje','fecha')

class Messages(admin.ModelAdmin):
	list_display = ('sender','recipient','subject','nattachments','fecha')

admin.site.register(InformacionGeneral,InfoGralAdmin)
admin.site.register(ExperienciaProfesional,ExpProAdmin)
admin.site.register(Estudio,EstAdmin)
admin.site.register(Proyecto,ProyeAdmin)
admin.site.register(Mensaje,MensAdmin)
admin.site.register(Email,Messages)
admin.site.register(Imagen,ImageAdmin)
