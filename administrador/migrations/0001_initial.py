# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InformacionGeneral'
        db.create_table(u'administrador_informaciongeneral', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campo', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'administrador', ['InformacionGeneral'])

        # Adding model 'ExperienciaProfesional'
        db.create_table(u'administrador_experienciaprofesional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('puesto', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fecha', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('info', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'administrador', ['ExperienciaProfesional'])

        # Adding model 'Estudio'
        db.create_table(u'administrador_estudio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fecha', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('completado', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'administrador', ['Estudio'])

        # Adding model 'Proyecto'
        db.create_table(u'administrador_proyecto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('tecnologias', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('fecha', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('imagen', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'administrador', ['Proyecto'])


    def backwards(self, orm):
        # Deleting model 'InformacionGeneral'
        db.delete_table(u'administrador_informaciongeneral')

        # Deleting model 'ExperienciaProfesional'
        db.delete_table(u'administrador_experienciaprofesional')

        # Deleting model 'Estudio'
        db.delete_table(u'administrador_estudio')

        # Deleting model 'Proyecto'
        db.delete_table(u'administrador_proyecto')


    models = {
        u'administrador.estudio': {
            'Meta': {'object_name': 'Estudio'},
            'completado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'administrador.experienciaprofesional': {
            'Meta': {'object_name': 'ExperienciaProfesional'},
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'puesto': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'administrador.informaciongeneral': {
            'Meta': {'object_name': 'InformacionGeneral'},
            'campo': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        },
        u'administrador.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fecha': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'tecnologias': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['administrador']