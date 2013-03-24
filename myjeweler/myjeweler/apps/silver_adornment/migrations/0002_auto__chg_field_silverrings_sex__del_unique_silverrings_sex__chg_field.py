# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'SilverEarrings', fields ['type_earrings']
        db.delete_unique(u'silver_adornment_silverearrings', ['type_earrings_id'])

        # Removing unique constraint on 'SilverRings', fields ['sex']
        db.delete_unique(u'silver_adornment_silverrings', ['sex_id'])


        # Changing field 'SilverRings.sex'
        db.alter_column(u'silver_adornment_silverrings', 'sex_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['silver_adornment.Sex']))

        # Changing field 'SilverEarrings.type_earrings'
        db.alter_column(u'silver_adornment_silverearrings', 'type_earrings_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['silver_adornment.TypeEarrings']))

    def backwards(self, orm):

        # Changing field 'SilverRings.sex'
        db.alter_column(u'silver_adornment_silverrings', 'sex_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['silver_adornment.Sex'], unique=True))
        # Adding unique constraint on 'SilverRings', fields ['sex']
        db.create_unique(u'silver_adornment_silverrings', ['sex_id'])


        # Changing field 'SilverEarrings.type_earrings'
        db.alter_column(u'silver_adornment_silverearrings', 'type_earrings_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['silver_adornment.TypeEarrings'], unique=True))
        # Adding unique constraint on 'SilverEarrings', fields ['type_earrings']
        db.create_unique(u'silver_adornment_silverearrings', ['type_earrings_id'])


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