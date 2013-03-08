# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Employee.skype'
        db.add_column(u'employees_employee', 'skype',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Employee.email'
        db.add_column(u'employees_employee', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Employee.github'
        db.add_column(u'employees_employee', 'github',
                      self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Employee.cell'
        db.add_column(u'employees_employee', 'cell',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Employee.skype'
        db.delete_column(u'employees_employee', 'skype')

        # Deleting field 'Employee.email'
        db.delete_column(u'employees_employee', 'email')

        # Deleting field 'Employee.github'
        db.delete_column(u'employees_employee', 'github')

        # Deleting field 'Employee.cell'
        db.delete_column(u'employees_employee', 'cell')


    models = {
        u'employees.employee': {
            'Meta': {'object_name': 'Employee'},
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'github': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employees.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'employees.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['employees']