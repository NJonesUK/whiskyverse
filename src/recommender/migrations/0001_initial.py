# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DistilleryProfile'
        db.create_table(u'recommender_distilleryprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Distillery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whisky.Distillery'])),
            ('Body', self.gf('django.db.models.fields.IntegerField')()),
            ('Sweetness', self.gf('django.db.models.fields.IntegerField')()),
            ('Smoky', self.gf('django.db.models.fields.IntegerField')()),
            ('Medicinal', self.gf('django.db.models.fields.IntegerField')()),
            ('Tobacco', self.gf('django.db.models.fields.IntegerField')()),
            ('Honey', self.gf('django.db.models.fields.IntegerField')()),
            ('Spicy', self.gf('django.db.models.fields.IntegerField')()),
            ('Winey', self.gf('django.db.models.fields.IntegerField')()),
            ('Nutty', self.gf('django.db.models.fields.IntegerField')()),
            ('Malty', self.gf('django.db.models.fields.IntegerField')()),
            ('Fruity', self.gf('django.db.models.fields.IntegerField')()),
            ('Floral', self.gf('django.db.models.fields.IntegerField')()),
            ('Postcode', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('Latitude', self.gf('django.db.models.fields.IntegerField')()),
            ('Longitude', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'recommender', ['DistilleryProfile'])


    def backwards(self, orm):
        # Deleting model 'DistilleryProfile'
        db.delete_table(u'recommender_distilleryprofile')


    models = {
        u'recommender.distilleryprofile': {
            'Body': ('django.db.models.fields.IntegerField', [], {}),
            'Distillery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whisky.Distillery']"}),
            'Floral': ('django.db.models.fields.IntegerField', [], {}),
            'Fruity': ('django.db.models.fields.IntegerField', [], {}),
            'Honey': ('django.db.models.fields.IntegerField', [], {}),
            'Latitude': ('django.db.models.fields.IntegerField', [], {}),
            'Longitude': ('django.db.models.fields.IntegerField', [], {}),
            'Malty': ('django.db.models.fields.IntegerField', [], {}),
            'Medicinal': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'DistilleryProfile'},
            'Nutty': ('django.db.models.fields.IntegerField', [], {}),
            'Postcode': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'Smoky': ('django.db.models.fields.IntegerField', [], {}),
            'Spicy': ('django.db.models.fields.IntegerField', [], {}),
            'Sweetness': ('django.db.models.fields.IntegerField', [], {}),
            'Tobacco': ('django.db.models.fields.IntegerField', [], {}),
            'Winey': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'whisky.country': {
            'Meta': {'object_name': 'Country'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'whisky.distillery': {
            'Meta': {'object_name': 'Distillery'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whisky.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whisky.Region']"})
        },
        u'whisky.region': {
            'Meta': {'object_name': 'Region'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['recommender']