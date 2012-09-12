# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('library_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
        ))
        db.send_create_signal('library', ['Author'])

        # Adding model 'Publisher'
        db.create_table('library_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
        ))
        db.send_create_signal('library', ['Publisher'])

        # Adding model 'Book'
        db.create_table('library_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(related_name='books', to=orm['library.Publisher'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('publish_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 9, 11, 0, 0))),
            ('condition', self.gf('django.db.models.fields.CharField')(default='+', max_length=1)),
            ('is_required_text', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('library', ['Book'])

        # Adding M2M table for field authors on 'Book'
        db.create_table('library_book_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['library.book'], null=False)),
            ('author', models.ForeignKey(orm['library.author'], null=False))
        ))
        db.create_unique('library_book_authors', ['book_id', 'author_id'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('library_author')

        # Deleting model 'Publisher'
        db.delete_table('library_publisher')

        # Deleting model 'Book'
        db.delete_table('library_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table('library_book_authors')


    models = {
        'library.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        'library.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'books'", 'symmetrical': 'False', 'to': "orm['library.Author']"}),
            'condition': ('django.db.models.fields.CharField', [], {'default': "'+'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_required_text': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 9, 11, 0, 0)'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'books'", 'to': "orm['library.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        'library.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['library']