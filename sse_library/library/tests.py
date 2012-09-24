from django import test
from django.utils import timezone

from library.models import *

class BookRelationsTest(test.TestCase):
  
  def setUp(self):
    self.author_a = Author.objects.create(name='Author A')
    self.author_b = Author.objects.create(name='Author B')
    self.publisher = Publisher.objects.create(name='Publisher')

    self.book = Book(title='Book', isbn='978-0-306-40615-7',
        publish_date=timezone.now(), is_required_text=True,
        publisher=self.publisher)

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

class TransactionRelationsTest(test.TestCase):
  def setUp(self):
    self.patron = Patron.objects.create(
        name='Kyle Kim',
        email='kok6969@rit.edu',
        uid='001234567')

    self.publisher = Publisher.objects.create(
        name='Publisher')

    self.some_book = Book.objects.create(
        title='Some Book',
        isbn='978-0-306-40615-7',
        is_required_text=False,
        publisher=self.publisher)

    self.required_book = Book.objects.create(
        title='Required Book',
        isbn='978-3-16-148410-0',
        is_required_text=True,
        publisher=self.publisher)

    self.missing_book = Book.objects.create(
        title='Missing Book',
        isbn='978-0-945962-14-4',
        is_required_text=False,
        is_missing=True,
        publisher=self.publisher)

  def test_checkout_saves_transaction(self):
    self.patron.checkout(self.some_book)
    self.assertTrue(Transaction.objects.exists())

    self.assertEqual(  # Maybe fragile?
        self.some_book,
        self.patron.transactions.all()[0].book)

  def test_checkout_missing_book_fails(self):
    self.assertRaises(CheckoutException,
        self.patron.checkout, self.missing_book)

  def test_checkout_required_book_fails(self):
    self.assertRaises(CheckoutException,
        self.patron.checkout, self.required_book)

class PatronTest(test.TestCase):
  def setUp(self):
    self.patron = Patron.objects.create(
        name='Kyle Kim',
        email='kok6969@rit.edu',
        uid='001234567')

    self.publisher = Publisher.objects.create(
        name='Publisher')

    self.book_a = Book.objects.create(
        title='Book A',
        isbn='978-0-306-40615-7',
        publisher=self.publisher)

    self.book_b = Book.objects.create(
        title='Book B',
        isbn='978-3-16-148410-0',
        publisher=self.publisher)

  def test_checked_out_books(self):
    self.patron.checkout(self.book_a)

    self.assertTrue(self.book_a in self.patron.checked_out_books())
    self.assertFalse(self.book_b in self.patron.checked_out_books())

    self.patron.checkout(self.book_b)

    self.assertTrue(self.book_b in self.patron.checked_out_books())
