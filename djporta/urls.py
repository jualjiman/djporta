from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djporta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'administrador.views.home', name='home'),
    url(r'^estudios/$', 'administrador.views.estudios', name='estudios'),
    url(r'^proyectos/$', 'administrador.views.proyectos', name='proyectos'),
    url(r'^contactame/$', 'administrador.views.contactame', name='contactame'),
)

# urlpatterns += patterns('',
# 	url(r'^var/www/djporta/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),)

# if settings.DEBUG:
#     urlpatterns += patterns('',
#              (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),)

#     urlpatterns += patterns('',
#             (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),)
