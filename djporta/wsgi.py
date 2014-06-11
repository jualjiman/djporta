"""
WSGI config for djporta project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djporta.settings")

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

import os
import sys
import site

#site.addsitedir('/home/ec2-user/.virtualenvs/mysite-main/lib/python2.7/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djporta.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

path = '/var/zpanel/hostdata/zadmin/public_html/jualjiman_com/djporta/'

if path not in sys.path:
    sys.path.append(path)