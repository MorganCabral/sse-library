from django.template import Context, RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from library.models import *

def index(request):
  template = loader.get_template('books/index.html')
  return HttpResponse(template.render(Context(request)))

def register(request):
  template = loader.get_template('books/register.html')
  return HttpResponse(template.render(RequestContext(request)))

def new_book(request):
  return HttpResponseRedirect('/books/register')
