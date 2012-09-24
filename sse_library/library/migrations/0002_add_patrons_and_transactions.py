# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Transaction'
        db.create_table('library_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transactions', to=orm['library.Book'])),
            ('borrower', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transactions', to=orm['library.Patron'])),
            ('checkout_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 9, 24, 0, 0))),
            ('due_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 10, 15, 0, 0))),
            ('return_date', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('is_transaction_completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('library', ['Transaction'])

        # Adding model 'Patron'
        db.create_table('library_patron', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=7)),
            ('uid', self.gf('django.db.models.fields.CharField')(max_length=9)),
        ))
        db.send_create_signal('library', ['Patron'])

        # Adding field 'Book.is_missing'
        db.add_column('library_book', 'is_missing',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Book.publisher'
        db.alter_column('library_book', 'publisher_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['library.Publisher']))

        # Changing field 'Book.isbn'
        db.alter_column('library_book', 'isbn', self.gf('django.db.models.fields.CharField')(unique=True, max_length=17))
        # Adding unique constraint on 'Book', fields ['isbn']
        db.create_unique('library_book', ['isbn'])


        # Changing field 'Book.condition'
        db.alter_column('library_book', 'condition', self.gf('django.db.models.fields.CharField')(max_length=254))

    def backwards(self, orm):
        # Removing unique constraint on 'Book', fields ['isbn']
        db.delete_unique('library_book', ['isbn'])

        # Deleting model 'Transaction'
        db.delete_table('library_transaction')

        # Deleting model 'Patron'
        db.delete_table('library_patron')

        # Deleting field 'Book.is_missing'
        db.delete_column('library_book', 'is_missing')


        # User chose to not deal with backwards NULL issues for 'Book.publisher'
        raise RuntimeError("Cannot reverse this migration. 'Book.publisher' and its values cannot be restored.")

        # Changing field 'Book.isbn'
        db.alter_column('library_book', 'isbn', self.gf('django.db.models.fields.CharField')(max_length=16))

        # Changing field 'Book.condition'
        db.alter_column('library_book', 'condition', self.gf('django.db.models.fields.CharField')(max_length=1))

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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_missing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_required_text': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isbn': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '17'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 9, 24, 0, 0)'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'books'", 'null': 'True', 'blank': 'True', 'to': "orm['library.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '254'})
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
            'checkout_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 9, 24, 0, 0)'}),
            'due_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 10, 15, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_transaction_completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'return_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['library']