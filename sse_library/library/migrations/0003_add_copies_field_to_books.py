# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.copies'
        db.add_column('library_book', 'copies',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Book.copies'
        db.delete_column('library_book', 'copies')


    models = {
        'library.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        'library.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'books'", 'symmetrical': 'False', 'to': "orm['library.Author']"}),
            'condition': ('django.db.models.fields.CharField', [], {'default': "'Good'", 'max_length': '254'}),
            'copies': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_missing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_required_text': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isbn': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '17'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 10, 4, 0, 0)'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'books'", 'null': 'True', 'blank': 'True', 'to': "orm['library.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'No Title'", 'max_length': '254'})
        },
        'library.patron': {
            'Meta': {'object_name': 'Patron'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '9'})
        },
        'library.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        'library.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transactions'", 'to': "orm['library.Book']"}),
            'borrower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transactions'", 'to': "orm['library.Patron']"}),
            'checkout_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 10, 4, 0, 0)'}),
            'due_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 10, 25, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_transaction_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'return_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['library']