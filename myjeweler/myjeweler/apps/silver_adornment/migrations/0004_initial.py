# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sex'
        db.create_table(u'silver_adornment_sex', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'silver_adornment', ['Sex'])

        # Adding model 'SilverRings'
        db.create_table(u'silver_adornment_silverrings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sex', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['silver_adornment.Sex'])),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('art', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('weigth', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'silver_adornment', ['SilverRings'])

        # Adding model 'TypeEarrings'
        db.create_table(u'silver_adornment_typeearrings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'silver_adornment', ['TypeEarrings'])

        # Adding model 'SilverEarrings'
        db.create_table(u'silver_adornment_silverearrings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_earrings', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['silver_adornment.TypeEarrings'])),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('art', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('weigth', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'silver_adornment', ['SilverEarrings'])

        # Adding model 'TypePendants'
        db.create_table(u'silver_adornment_typependants', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'silver_adornment', ['TypePendants'])

        # Adding model 'Pendants'
        db.create_table(u'silver_adornment_pendants', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_pendants', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['silver_adornment.TypePendants'], unique=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('art', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('weigth', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'silver_adornment', ['Pendants'])


    def backwards(self, orm):
        # Deleting model 'Sex'
        db.delete_table(u'silver_adornment_sex')

        # Deleting model 'SilverRings'
        db.delete_table(u'silver_adornment_silverrings')

        # Deleting model 'TypeEarrings'
        db.delete_table(u'silver_adornment_typeearrings')

        # Deleting model 'SilverEarrings'
        db.delete_table(u'silver_adornment_silverearrings')

        # Deleting model 'TypePendants'
        db.delete_table(u'silver_adornment_typependants')

        # Deleting model 'Pendants'
        db.delete_table(u'silver_adornment_pendants')


    models = {
        u'silver_adornment.pendants': {
            'Meta': {'object_name': 'Pendants'},
            'art': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type_pendants': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['silver_adornment.TypePendants']", 'unique': 'True'}),
            'weigth': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'silver_adornment.sex': {
            'Meta': {'object_name': 'Sex'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'silver_adornment.silverearrings': {
            'Meta': {'object_name': 'SilverEarrings'},
            'art': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type_earrings': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['silver_adornment.TypeEarrings']"}),
            'weigth': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'silver_adornment.silverrings': {
            'Meta': {'object_name': 'SilverRings'},
            'art': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sex': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['silver_adornment.Sex']"}),
            'weigth': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'silver_adornment.typeearrings': {
            'Meta': {'object_name': 'TypeEarrings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'silver_adornment.typependants': {
            'Meta': {'object_name': 'TypePendants'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['silver_adornment']