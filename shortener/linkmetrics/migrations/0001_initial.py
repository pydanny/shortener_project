# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LinkLog'
        db.create_table(u'linkmetrics_linklog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['links.Link'])),
            ('http_accept_language', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('http_host', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('http_referer', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('http_user_agent', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('query_string', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('remote_addr', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('remote_host', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('request_method', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'linkmetrics', ['LinkLog'])


    def backwards(self, orm):
        # Deleting model 'LinkLog'
        db.delete_table(u'linkmetrics_linklog')


    models = {
        u'linkmetrics.linklog': {
            'Meta': {'object_name': 'LinkLog'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'http_accept_language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'http_host': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'http_referer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'http_user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['links.Link']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'query_string': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'remote_addr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'remote_host': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        u'links.link': {
            'Meta': {'object_name': 'Link'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'original_url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['linkmetrics']