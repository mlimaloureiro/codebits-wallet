# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Repositories'
        db.create_table(u'walletapp_repositories', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')
             (max_length=200)),
            ('fullname', self.gf('django.db.models.fields.CharField')
             (max_length=400)),
            ('url', self.gf('django.db.models.fields.CharField')
             (max_length=400)),
            ('description', self.gf('django.db.models.fields.CharField')
             (max_length=2000)),
            ('github_id', self.gf('django.db.models.fields.CharField')
             (max_length=100)),
        ))
        db.send_create_signal(u'walletapp', ['Repositories'])

        # Adding field 'Proposition.repositories'
        db.add_column(u'walletapp_proposition', 'repositories',
                      self.gf('django.db.models.fields.related.ForeignKey')(
                          default=1, to=orm['walletapp.Repositories']),
                      keep_default=False)

        # Changing field 'Proposition.created_at'
        db.alter_column(u'walletapp_proposition', 'created_at',
                        self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Proposition.updated_at'
        db.alter_column(u'walletapp_proposition', 'updated_at',
                        self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

    def backwards(self, orm):
        # Deleting model 'Repositories'
        db.delete_table(u'walletapp_repositories')

        # Deleting field 'Proposition.repositories'
        db.delete_column(u'walletapp_proposition', 'repositories_id')

        # Changing field 'Proposition.created_at'
        db.alter_column(u'walletapp_proposition', 'created_at',
                        self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

        # Changing field 'Proposition.updated_at'
        db.alter_column(u'walletapp_proposition', 'updated_at',
                        self.gf('django.db.models.fields.DateTimeField')())

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
        u'walletapp.proposition': {
            'Meta': {'object_name': 'Proposition'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repositories': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walletapp.Repositories']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'walletapp.repositories': {
            'Meta': {'object_name': 'Repositories'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'github_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['walletapp']