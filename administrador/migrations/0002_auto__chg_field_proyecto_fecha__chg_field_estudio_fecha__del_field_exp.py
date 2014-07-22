# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Proyecto.fecha'
        db.alter_column(u'administrador_proyecto', 'fecha', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Estudio.fecha'
        db.alter_column(u'administrador_estudio', 'fecha', self.gf('django.db.models.fields.DateField')())
        # Deleting field 'ExperienciaProfesional.fecha'
        db.delete_column(u'administrador_experienciaprofesional', 'fecha')

        # Adding field 'ExperienciaProfesional.desde'
        db.add_column(u'administrador_experienciaprofesional', 'desde',
                      self.gf('django.db.models.fields.DateField')(default=datetime.date.today),
                      keep_default=False)

        # Adding field 'ExperienciaProfesional.hasta'
        db.add_column(u'administrador_experienciaprofesional', 'hasta',
                      self.gf('django.db.models.fields.DateField')(default=datetime.date.today, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InformacionGeneral.prioridad'
        db.add_column(u'administrador_informaciongeneral', 'prioridad',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Proyecto.fecha'
        db.alter_column(u'administrador_proyecto', 'fecha', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Estudio.fecha'
        db.alter_column(u'administrador_estudio', 'fecha', self.gf('django.db.models.fields.CharField')(max_length=50))
        # Adding field 'ExperienciaProfesional.fecha'
        db.add_column(u'administrador_experienciaprofesional', 'fecha',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 7, 21, 0, 0), max_length=50),
                      keep_default=False)

        # Deleting field 'ExperienciaProfesional.desde'
        db.delete_column(u'administrador_experienciaprofesional', 'desde')

        # Deleting field 'ExperienciaProfesional.hasta'
        db.delete_column(u'administrador_experienciaprofesional', 'hasta')

        # Deleting field 'InformacionGeneral.prioridad'
        db.delete_column(u'administrador_informaciongeneral', 'prioridad')


    models = {
        u'administrador.estudio': {
            'Meta': {'object_name': 'Estudio'},
            'completado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'administrador.experienciaprofesional': {
            'Meta': {'object_name': 'ExperienciaProfesional'},
            'desde': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'hasta': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True', 'blank': 'True'}),
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
            'info': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'prioridad': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'administrador.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
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