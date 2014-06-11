# DOMAIN: jualjiman.com
<virtualhost *:80>
WSGIScriptAlias / "/var/zpanel/hostdata/zadmin/public_html/jualjiman_com/djporta/djporta/wsgi.py"
DocumentRoot "/var/zpanel/hostdata/zadmin/public_html/jualjiman_com/djporta"

ServerName jualjiman.com
ServerAlias jualjiman.com www.jualjiman.com

Alias /static/ "/var/zpanel/hostdata/zadmin/public_html/jualjiman_com/djporta/administrador/static/"
Alias /media/ "/var/zpanel/hostdata/zadmin/public_html/jualjiman_com/djporta/administrador/static/images/"

<Directory />
Options FollowSymLinks Indexes
AllowOverride All
Order Allow,Deny
Allow from all
</Directory>

<Directory "/var/zpanel/hostdata/zadmin/public_html/jualjiman_com/djporta">
<Files wsgi.py>
Options FollowSymLinks Indexes
AllowOverride All
Order Allow,Deny
Allow from all
</Files>
</Directory>

<Directory "/var/zpanel/hostdata/zadmin/public_html/jualjiman_com/djporta/administrador/static/">
Options +Indexes
Options FollowSymLinks Indexes
AllowOverride All
Order Allow,Deny
Allow from all
</Directory>

<Directory "/var/zpanel/hostdata/zadmin/public_html/jualjiman_com/djporta/administrador/static/images/">
Options FollowSymLinks Indexes
AllowOverride All
Order Allow,Deny
Allow from all
</Directory>

ErrorLog "/var/zpanel/hostdata/zadmin/public_html/jualjiman_com/djporta/Errorlog.log"
CustomLog "/var/zpanel/hostdata/zadmin/public_html/jualjiman_com/djporta/access.log" combined
CustomLog "/var/zpanel/hostdata/zadmin/public_html/jualjiman_com/djporta/bandwidth.log" common
</virtualhost>
# END DOMAIN: jualjiman.com
################################################################

