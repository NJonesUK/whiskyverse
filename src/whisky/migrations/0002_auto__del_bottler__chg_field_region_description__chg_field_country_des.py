# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Bottler'
        db.delete_table(u'whisky_bottler')


        # Changing field 'Region.description'
        db.alter_column(u'whisky_region', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Country.description'
        db.alter_column(u'whisky_country', 'description', self.gf('django.db.models.fields.TextField')(null=True))
        # Adding field 'Whisky.description'
        db.add_column(u'whisky_whisky', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Whisky.strength'
        db.alter_column(u'whisky_whisky', 'strength', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Whisky.bottled_in'
        db.alter_column(u'whisky_whisky', 'bottled_in', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Whisky.age'
        db.alter_column(u'whisky_whisky', 'age', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Whisky.size'
        db.alter_column(u'whisky_whisky', 'size', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Adding field 'Brand.description'
        db.add_column(u'whisky_brand', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Distillery.description'
        db.add_column(u'whisky_distillery', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Distillery.country'
        db.alter_column(u'whisky_distillery', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whisky.Country'], null=True))

        # Changing field 'Distillery.region'
        db.alter_column(u'whisky_distillery', 'region_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['whisky.Region'], null=True))

    def backwards(self, orm):
        # Adding model 'Bottler'
        db.create_table(u'whisky_bottler', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'whisky', ['Bottler'])


        # Changing field 'Region.description'
        db.alter_column(u'whisky_region', 'description', self.gf('django.db.models.fields.TextField')(default='None'))

        # Changing field 'Country.description'
        db.alter_column(u'whisky_country', 'description', self.gf('django.db.models.fields.TextField')(default='None'))
        # Deleting field 'Whisky.description'
        db.delete_column(u'whisky_whisky', 'description')


        # Changing field 'Whisky.strength'
        db.alter_column(u'whisky_whisky', 'strength', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Whisky.bottled_in'
        db.alter_column(u'whisky_whisky', 'bottled_in', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Whisky.age'
        db.alter_column(u'whisky_whisky', 'age', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Whisky.size'
        db.alter_column(u'whisky_whisky', 'size', self.gf('django.db.models.fields.IntegerField')(default=0))
        # Deleting field 'Brand.description'
        db.delete_column(u'whisky_brand', 'description')

        # Deleting field 'Distillery.description'
        db.delete_column(u'whisky_distillery', 'description')


        # Changing field 'Distillery.country'
        db.alter_column(u'whisky_distillery', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['whisky.Country']))

        # Changing field 'Distillery.region'
        db.alter_column(u'whisky_distillery', 'region_id', self.gf('django.db.models.fields.related.ForeignKey')(default='None', to=orm['whisky.Region']))

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
        u'whisky.brand': {
            'Meta': {'object_name': 'Brand'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['whisky.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bottled_in': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cask_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'strength': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['whisky']