from django.db import models
from django.utils import timezone

class Author(models.Model):
  """ Author of a book.
  
      Relations:
      * has many books
  """
  name = models.CharField(max_length=254)

class Publisher(models.Model):
  """ Publisher of books.

      Relations:
      * has many books
  """
  name = models.CharField(max_length=254)

class Book(models.Model):
  """ Book model.

      Constants:
      * DB_GOOD database shortand for a book in good condition
      * DB_POOR database shortand for a book in poor condition
      * CONDITIONS mapping from database shorthands to human-readable name

      Relations:
      * has many authors
      * has one publisher
  """

  DB_GOOD = '+'
  DB_POOR = '-'
  CONDITIONS = (
      (DB_GOOD, 'Good'),
      (DB_POOR, 'Poor'))

  # Foreign Keys
  authors = models.ManyToManyField('Author', related_name='books')
  publisher = models.ForeignKey('Publisher', related_name='books')

  # Fields
  title = models.CharField(max_length=254)
  isbn = models.CharField(max_length=16)
  publish_date = models.DateField(default=timezone.now())
  condition = models.CharField(max_length=1, choices=CONDITIONS, default=DB_GOOD)
  is_required_text = models.BooleanField()
