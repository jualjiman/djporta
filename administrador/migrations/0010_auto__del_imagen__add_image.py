# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Imagen'
        db.delete_table(u'administrador_imagen')

        # Adding model 'Image'
        db.create_table(u'administrador_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('activo', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'administrador', ['Image'])


    def backwards(self, orm):
        # Adding model 'Imagen'
        db.create_table(u'administrador_imagen', (
            ('activo', self.gf('django.db.models.fields.BooleanField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'administrador', ['Imagen'])

        # Deleting model 'Image'
        db.delete_table(u'administrador_image')


    models = {
        u'administrador.email': {
            'Meta': {'object_name': 'Email'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 2, 25, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nattachments': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'administrador.estudio': {
            'LugarLink': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'Meta': {'object_name': 'Estudio'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'completado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'administrador.experienciaprofesional': {
            'Meta': {'object_name': 'ExperienciaProfesional'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'actual': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'desde': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'hasta': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'puesto': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'administrador.image': {
            'Meta': {'object_name': 'Image'},
            'activo': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'})
        },
        u'administrador.informaciongeneral': {
            'Meta': {'object_name': 'InformacionGeneral'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'campo': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'prioridad': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'administrador.mensaje': {
            'Meta': {'object_name': 'Mensaje'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 2, 25, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensaje': ('django.db.models.fields.TextField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'administrador.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'tecnologias': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['administrador']