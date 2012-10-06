from django import forms

from library.models import Book

class BookRegisterForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ('isbn',)
