# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Agenda'
        db.create_table('speakers_agenda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('talk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['speakers.Talk'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('day', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('start', self.gf('django.db.models.fields.TimeField')()),
            ('finish', self.gf('django.db.models.fields.TimeField')()),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('speakers', ['Agenda'])


    def backwards(self, orm):
        # Deleting model 'Agenda'
        db.delete_table('speakers_agenda')


    models = {
        'speakers.agenda': {
            'Meta': {'ordering': "('day', 'start')", 'object_name': 'Agenda'},
            'day': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'finish': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['speakers.Talk']", 'null': 'True', 'blank': 'True'})
        },
        'speakers.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'speakers.talk': {
            'Meta': {'object_name': 'Talk'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'speaker': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['speakers.Speaker']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['speakers']