from django import test
from django.utils import timezone

from library.models import *

class ModelRelationsTest(test.TestCase):
  
  def setUp(self):
    self.author_a = Author.objects.create(name='Author A')
    self.author_b = Author.objects.create(name='Author B')
    self.publisher = Publisher.objects.create(name='Publisher')

    self.book = Book(title='Book', isbn='978-0-306-40615-7',
        publish_date=timezone.now(), condition=Book.DB_GOOD,
        is_required_text=True, publisher=self.publisher)

    self.book.save()

    self.book.authors.add(self.author_a)
    self.book.authors.add(self.author_b)

    self.book.save()

  def test_book_may_have_many_authors(self):
    book_authors = self.book.authors.all()

    self.assertTrue(self.author_a in book_authors)
    self.assertTrue(self.author_b in book_authors)

  def test_authors_have_many_books(self):
    self.assertTrue(self.book in self.author_a.books.all())
    self.assertTrue(self.book in self.author_b.books.all())

  def test_book_has_one_publisher(self):
    self.assertEqual(self.publisher, self.book.publisher)

  def test_publisher_has_books(self):
    self.assertTrue(self.book in self.publisher.books.all())
