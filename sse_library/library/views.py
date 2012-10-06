from django.template import Context, RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from library.models import *
from library.forms import *

class BookIndexView(TemplateView):
  template_name = 'books/index.html'

  def get_context_data(self, **kwargs):
    context = super(BookIndexView, self).get_context_data(**kwargs)

    context['books'] = Book.objects.order_by('isbn')

    return context

class BookRegisterView(CreateView):
  template_name = 'books/register.html'
  model = Book
  form_class = BookRegisterForm
  success_url = '/books/register/'

  def form_invalid(self, form):
    # I know there is a better way. I tried to look for it, but only found a fish, so meh.
    if form.errors['isbn']:
      same_book = Book.objects.filter(
          isbn=form.data['isbn'])[0]

      del form.errors['isbn']

      same_book.copies = same_book.copies + 1
      same_book.save()

    return super(BookRegisterView, self).form_invalid(form)

  class Meta:
    fields = ('isbn',)
