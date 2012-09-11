from django.db import models
from django.utils import timezone

class Author(models.Model):
  name = models.CharField(max_length=254)

class Publisher(models.Model):
  name = models.CharField(max_length=254)

class Book(models.Model):
  DB_GOOD = '+'
  DB_POOR = '-'
  CONDITIONS = (
      (DB_GOOD, 'Good'),
      (DB_POOR, 'Poor'))

  # Links
  authors = models.ManyToManyField('Author', related_name='books')
  publisher = models.ForeignKey('Publisher', related_name='books')

  title = models.CharField(max_length=254)
  isbn = models.CharField(max_length=16)
  publish_date = models.DateField(default=timezone.now())
  condition = models.CharField(max_length=1, choices=CONDITIONS, default=DB_GOOD)
  is_required_text = models.BooleanField()
