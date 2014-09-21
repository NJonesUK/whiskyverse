# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DistilleryProfile.Body'
        db.delete_column(u'recommender_distilleryprofile', 'Body')

        # Deleting field 'DistilleryProfile.Spicy'
        db.delete_column(u'recommender_distilleryprofile', 'Spicy')

        # Deleting field 'DistilleryProfile.Tobacco'
        db.delete_column(u'recommender_distilleryprofile', 'Tobacco')

        # Deleting field 'DistilleryProfile.Nutty'
        db.delete_column(u'recommender_distilleryprofile', 'Nutty')

        # Deleting field 'DistilleryProfile.Smoky'
        db.delete_column(u'recommender_distilleryprofile', 'Smoky')

        # Deleting field 'DistilleryProfile.Distillery'
        db.delete_column(u'recommender_distilleryprofile', 'Distillery_id')

        # Deleting field 'DistilleryProfile.Winey'
        db.delete_column(u'recommender_distilleryprofile', 'Winey')

        # Deleting field 'DistilleryProfile.Longitude'
        db.delete_column(u'recommender_distilleryprofile', 'Longitude')

        # Deleting field 'DistilleryProfile.Honey'
        db.delete_column(u'recommender_distilleryprofile', 'Honey')

        # Deleting field 'DistilleryProfile.Latitude'
        db.delete_column(u'recommender_distilleryprofile', 'Latitude')

        # Deleting field 'DistilleryProfile.Postcode'
        db.delete_column(u'recommender_distilleryprofile', 'Postcode')

        # Deleting field 'DistilleryProfile.Malty'
        db.delete_column(u'recommender_distilleryprofile', 'Malty')

        # Deleting field 'DistilleryProfile.Floral'
        db.delete_column(u'recommender_distilleryprofile', 'Floral')

        # Deleting field 'DistilleryProfile.Medicinal'
        db.delete_column(u'recommender_distilleryprofile', 'Medicinal')

        # Deleting field 'DistilleryProfile.Sweetness'
        db.delete_column(u'recommender_distilleryprofile', 'Sweetness')

        # Deleting field 'DistilleryProfile.Fruity'
        db.delete_column(u'recommender_distilleryprofile', 'Fruity')

        # Adding field 'DistilleryProfile.distillery'
        db.add_column(u'recommender_distilleryprofile', 'distillery',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['whisky.Distillery']),
                      keep_default=False)

        # Adding field 'DistilleryProfile.body'
        db.add_column(u'recommender_distilleryprofile', 'body',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.sweetness'
        db.add_column(u'recommender_distilleryprofile', 'sweetness',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.smokey'
        db.add_column(u'recommender_distilleryprofile', 'smokey',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.medicinal'
        db.add_column(u'recommender_distilleryprofile', 'medicinal',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.tobacco'
        db.add_column(u'recommender_distilleryprofile', 'tobacco',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.honey'
        db.add_column(u'recommender_distilleryprofile', 'honey',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.spicy'
        db.add_column(u'recommender_distilleryprofile', 'spicy',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.winey'
        db.add_column(u'recommender_distilleryprofile', 'winey',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.nutty'
        db.add_column(u'recommender_distilleryprofile', 'nutty',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.malty'
        db.add_column(u'recommender_distilleryprofile', 'malty',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.fruity'
        db.add_column(u'recommender_distilleryprofile', 'fruity',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.floral'
        db.add_column(u'recommender_distilleryprofile', 'floral',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.postcode'
        db.add_column(u'recommender_distilleryprofile', 'postcode',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=15),
                      keep_default=False)

        # Adding field 'DistilleryProfile.latitude'
        db.add_column(u'recommender_distilleryprofile', 'latitude',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.longitude'
        db.add_column(u'recommender_distilleryprofile', 'longitude',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DistilleryProfile.Body'
        db.add_column(u'recommender_distilleryprofile', 'Body',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Spicy'
        db.add_column(u'recommender_distilleryprofile', 'Spicy',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Tobacco'
        db.add_column(u'recommender_distilleryprofile', 'Tobacco',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Nutty'
        db.add_column(u'recommender_distilleryprofile', 'Nutty',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Smoky'
        db.add_column(u'recommender_distilleryprofile', 'Smoky',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Distillery'
        db.add_column(u'recommender_distilleryprofile', 'Distillery',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['whisky.Distillery']),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Winey'
        db.add_column(u'recommender_distilleryprofile', 'Winey',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Longitude'
        db.add_column(u'recommender_distilleryprofile', 'Longitude',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Honey'
        db.add_column(u'recommender_distilleryprofile', 'Honey',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Latitude'
        db.add_column(u'recommender_distilleryprofile', 'Latitude',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Postcode'
        db.add_column(u'recommender_distilleryprofile', 'Postcode',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=15),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Malty'
        db.add_column(u'recommender_distilleryprofile', 'Malty',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Floral'
        db.add_column(u'recommender_distilleryprofile', 'Floral',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Medicinal'
        db.add_column(u'recommender_distilleryprofile', 'Medicinal',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Sweetness'
        db.add_column(u'recommender_distilleryprofile', 'Sweetness',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DistilleryProfile.Fruity'
        db.add_column(u'recommender_distilleryprofile', 'Fruity',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'DistilleryProfile.distillery'
        db.delete_column(u'recommender_distilleryprofile', 'distillery_id')

        # Deleting field 'DistilleryProfile.body'
        db.delete_column(u'recommender_distilleryprofile', 'body')

        # Deleting field 'DistilleryProfile.sweetness'
        db.delete_column(u'recommender_distilleryprofile', 'sweetness')

        # Deleting field 'DistilleryProfile.smokey'
        db.delete_column(u'recommender_distilleryprofile', 'smokey')

        # Deleting field 'DistilleryProfile.medicinal'
        db.delete_column(u'recommender_distilleryprofile', 'medicinal')

        # Deleting field 'DistilleryProfile.tobacco'
        db.delete_column(u'recommender_distilleryprofile', 'tobacco')

        # Deleting field 'DistilleryProfile.honey'
        db.delete_column(u'recommender_distilleryprofile', 'honey')

        # Deleting field 'DistilleryProfile.spicy'
        db.delete_column(u'recommender_distilleryprofile', 'spicy')

        # Deleting field 'DistilleryProfile.winey'
        db.delete_column(u'recommender_distilleryprofile', 'winey')

        # Deleting field 'DistilleryProfile.nutty'
        db.delete_column(u'recommender_distilleryprofile', 'nutty')

        # Deleting field 'DistilleryProfile.malty'
        db.delete_column(u'recommender_distilleryprofile', 'malty')

        # Deleting field 'DistilleryProfile.fruity'
        db.delete_column(u'recommender_distilleryprofile', 'fruity')

        # Deleting field 'DistilleryProfile.floral'
        db.delete_column(u'recommender_distilleryprofile', 'floral')

        # Deleting field 'DistilleryProfile.postcode'
        db.delete_column(u'recommender_distilleryprofile', 'postcode')

        # Deleting field 'DistilleryProfile.latitude'
        db.delete_column(u'recommender_distilleryprofile', 'latitude')

        # Deleting field 'DistilleryProfile.longitude'
        db.delete_column(u'recommender_distilleryprofile', 'longitude')


    models = {
        u'recommender.distilleryprofile': {
            'Meta': {'object_name': 'DistilleryProfile'},
            'body': ('django.db.models.fields.IntegerField', [], {}),
            'distillery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whisky.Distillery']"}),
            'floral': ('django.db.models.fields.IntegerField', [], {}),
            'fruity': ('django.db.models.fields.IntegerField', [], {}),
            'honey': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.IntegerField', [], {}),
            'longitude': ('django.db.models.fields.IntegerField', [], {}),
            'malty': ('django.db.models.fields.IntegerField', [], {}),
            'medicinal': ('django.db.models.fields.IntegerField', [], {}),
            'nutty': ('django.db.models.fields.IntegerField', [], {}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'smokey': ('django.db.models.fields.IntegerField', [], {}),
            'spicy': ('django.db.models.fields.IntegerField', [], {}),
            'sweetness': ('django.db.models.fields.IntegerField', [], {}),
            'tobacco': ('django.db.models.fields.IntegerField', [], {}),
            'winey': ('django.db.models.fields.IntegerField', [], {})
        },
        u'whisky.country': {
            'Meta': {'object_name': 'Country'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'whisky.distillery': {
            'Meta': {'object_name': 'Distillery'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whisky.Country']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whisky.Region']", 'null': 'True', 'blank': 'True'})
        },
        u'whisky.region': {
            'Meta': {'object_name': 'Region'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['recommender']