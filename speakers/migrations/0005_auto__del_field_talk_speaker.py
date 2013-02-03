# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Talk.speaker'
        db.delete_column('speakers_talk', 'speaker_id')

        # Adding M2M table for field speaker on 'Talk'
        db.create_table('speakers_talk_speaker', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('talk', models.ForeignKey(orm['speakers.talk'], null=False)),
            ('speaker', models.ForeignKey(orm['speakers.speaker'], null=False))
        ))
        db.create_unique('speakers_talk_speaker', ['talk_id', 'speaker_id'])


    def backwards(self, orm):
        # Adding field 'Talk.speaker'
        db.add_column('speakers_talk', 'speaker',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['speakers.Speaker']),
                      keep_default=False)

        # Removing M2M table for field speaker on 'Talk'
        db.delete_table('speakers_talk_speaker')


    models = {
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
            'speaker': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['speakers.Speaker']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['speakers']