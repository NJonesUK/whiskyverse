# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'whisky_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'whisky', ['Country'])

        # Adding model 'Region'
        db.create_table(u'whisky_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'whisky', ['Region'])

        # Adding model 'Whisky'
        db.create_table(u'whisky_whisky', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('strength', self.gf('django.db.models.fields.IntegerField')()),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('cask_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('bottled_in', self.gf('django.db.models.fields.IntegerField')()),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'whisky', ['Whisky'])

        # Adding model 'Distillery'
        db.create_table(u'whisky_distillery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whisky.Region'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whisky.Country'])),
        ))
        db.send_create_signal(u'whisky', ['Distillery'])

        # Adding model 'DistilleryWhisky'
        db.create_table(u'whisky_distillerywhisky', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('distillery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whisky.Distillery'])),
            ('whisky', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whisky.Whisky'])),
        ))
        db.send_create_signal(u'whisky', ['DistilleryWhisky'])

        # Adding model 'Brand'
        db.create_table(u'whisky_brand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whisky.Country'])),
        ))
        db.send_create_signal(u'whisky', ['Brand'])

        # Adding model 'BrandWhisky'
        db.create_table(u'whisky_brandwhisky', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whisky.Brand'])),
            ('whisky', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whisky.Whisky'])),
        ))
        db.send_create_signal(u'whisky', ['BrandWhisky'])

        # Adding model 'Bottler'
        db.create_table(u'whisky_bottler', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'whisky', ['Bottler'])

        # Adding model 'Type'
        db.create_table(u'whisky_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'whisky', ['Type'])

        # Adding model 'District'
        db.create_table(u'whisky_district', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'whisky', ['District'])

        # Adding model 'UserScore'
        db.create_table(u'whisky_userscore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('whisky', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whisky.Whisky'])),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'whisky', ['UserScore'])

        # Adding unique constraint on 'UserScore', fields ['user', 'whisky']
        db.create_unique(u'whisky_userscore', ['user_id', 'whisky_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'UserScore', fields ['user', 'whisky']
        db.delete_unique(u'whisky_userscore', ['user_id', 'whisky_id'])

        # Deleting model 'Country'
        db.delete_table(u'whisky_country')

        # Deleting model 'Region'
        db.delete_table(u'whisky_region')

        # Deleting model 'Whisky'
        db.delete_table(u'whisky_whisky')

        # Deleting model 'Distillery'
        db.delete_table(u'whisky_distillery')

        # Deleting model 'DistilleryWhisky'
        db.delete_table(u'whisky_distillerywhisky')

        # Deleting model 'Brand'
        db.delete_table(u'whisky_brand')

        # Deleting model 'BrandWhisky'
        db.delete_table(u'whisky_brandwhisky')

        # Deleting model 'Bottler'
        db.delete_table(u'whisky_bottler')

        # Deleting model 'Type'
        db.delete_table(u'whisky_type')

        # Deleting model 'District'
        db.delete_table(u'whisky_district')

        # Deleting model 'UserScore'
        db.delete_table(u'whisky_userscore')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'whisky.bottler': {
            'Meta': {'object_name': 'Bottler'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'whisky.brand': {
            'Meta': {'object_name': 'Brand'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whisky.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'whisky.brandwhisky': {
            'Meta': {'object_name': 'BrandWhisky'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whisky.Brand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'whisky': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whisky.Whisky']"})
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
        u'whisky.distillerywhisky': {
            'Meta': {'object_name': 'DistilleryWhisky'},
            'distillery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whisky.Distillery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'whisky': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whisky.Whisky']"})
        },
        u'whisky.district': {
            'Meta': {'object_name': 'District'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'whisky.region': {
            'Meta': {'object_name': 'Region'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'whisky.type': {
            'Meta': {'object_name': 'Type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'whisky.userscore': {
            'Meta': {'unique_together': "(('user', 'whisky'),)", 'object_name': 'UserScore'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'whisky': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whisky.Whisky']"})
        },
        u'whisky.whisky': {
            'Meta': {'object_name': 'Whisky'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'bottled_in': ('django.db.models.fields.IntegerField', [], {}),
            'cask_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'strength': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['whisky']