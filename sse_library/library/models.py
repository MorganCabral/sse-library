from django.db import models
from django.utils import timezone
import datetime, sha

DEFAULT_CHECKOUT_DURATION = datetime.timedelta(weeks=3)

class CheckoutException(Exception):
  pass

class CheckinException(Exception):
  pass

class ConsistencyError(Exception):
  pass

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

      Relations:
      * has many authors
      * has one publisher
      * has many transactions
  """

  # Foreign Keys
  authors = models.ManyToManyField('Author', related_name='books')
  publisher = models.ForeignKey('Publisher',
      related_name='books',
      null=True,
      blank=True,
      default=None)

  # Fields
  title = models.CharField(max_length=254)
  isbn = models.CharField(max_length=17, unique=True)
  publish_date = models.DateField(default=timezone.now())
  condition = models.CharField(max_length=254, default='Good')
  is_missing = models.BooleanField(default=False)
  is_required_text = models.BooleanField(default=False)

class Patron(models.Model):
  """ Library user who borrows books.

      Relations:
        * has many transactions
  """

  # Fields
  name = models.CharField(max_length=254)
  email = models.EmailField(max_length=7)
  uid = models.CharField(max_length=9)

  def checked_out_books(self):
    """ Returns the patron's currently checked out books.

    Returns a generator.

    Returns:
      collection of books checked out
    """

    return (t.book for t in self.transactions.filter(
        is_transaction_completed=False))

  def checkout(self, book):
    """ Attempt to check out a book.

    Exceptions:
      Book is already checked out by someone
      Book is missing
    """

    if book.is_missing:
      raise CheckoutException("{0} is missing.".format(book.title))

    if book.is_required_text:
      raise CheckoutException("{0} is a required textbook.".format(book.title))

    active_book_transactions = Transaction.objects.filter(
        book=book, is_transaction_completed=False)

    if active_book_transactions.exists():
      existing_transaction = active_book_transactions.all()[0]
      raise CheckoutException("{0} is currently checked out by {1}".format(
          book.title, existing_transaction.borrower.name))

    # Create and save transaction
    checkout_transaction = Transaction.objects.create(
        book=book, borrower=self)

  def checkin(self, book):
    """ Attempt to check in (return) a book.

    Exceptions:
      There is no existing transaction for this user and book.
    """

    book_transaction = Transaction.objects.filter(
        is_transaction_completed=False, book=book, borrower=self)

    if not book_transaction.exists():
      raise CheckinException(
          "{0} is not checked out by {1} or is already returned".format(
              book.title, self.name))

    # This should never happen
    if book_transaction.count() != 1:
      raise ConsistencyError("{0} has multiple transactions with {1}".format(
          self.name, book.title))

    book_transaction = book_transaction[0]

    book_transaction.is_transaction_completed = True
    book_transaction.return_date = timezone.now()

    book_transaction.save()

class Transaction(models.Model):
  """ Check out a book.

      Relations:
      * belongs to a book
      * belongs to a borrower
  """

  # Foreign Keys
  book = models.ForeignKey('Book', related_name='transactions')
  borrower = models.ForeignKey('Patron', related_name='transactions')

  # Fields
  checkout_date = models.DateField(default=timezone.now())
  due_date = models.DateField(default=timezone.now() +
      DEFAULT_CHECKOUT_DURATION)
  return_date = models.DateField(default=None, blank=True, null=True)
  is_transaction_completed = models.BooleanField(default=False)
