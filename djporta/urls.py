from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from administrador.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djporta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'administrador.views.home', name='home'),
    url(r'^estudios/$', 'administrador.views.estudios', name='estudios'),
    url(r'^proyectos/$', 'administrador.views.proyectos', name='proyectos'),
    url(r'^contactame/$', 'administrador.views.contactame', name='contactame'),
    #url(r'^messages/$', 'administrador.views.messages', name='messages'), #recibia mensajes de mailgun y los guardaba en la bd