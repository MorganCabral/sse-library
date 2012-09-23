from django.db import models
from django.utils import timezone
from datetime import timedelta
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

class Transaction(models.Model):
  
  ACTIONS = (
    ('Renew', 'Renew'),
    ('ChkOut', 'Check Out'),
    ('ChkIn', 'Check in'))

  #Foreign Keys
  #TODO:Add in FKs to users
  book = models.ForeignKey(Book)

  #Fields
  date= models.DateTimeField(db_column='Date of Transaction', default = timezone.now())
  due_date = models.DateTimeField(db_column='Due Back',default= timezone.now() + timedelta(days=7))
  #TODO:Make tables for conditions/actions to make the site more configurable and so that things (such as conditions) can be used in multiple objects
  action = models.CharField(max_length=90, choices=ACTIONS, default='ChkOut')
  trans_notes = models.CharField(max_length=500)
