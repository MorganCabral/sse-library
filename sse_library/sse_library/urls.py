from django.conf.urls import patterns, include, url
from django.contrib import admin  # Enable Admin
admin.autodiscover()

import library.views

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Book routes
    url(r'^books[/]?$', library.views.index),
    url(r'^books/register[/]?', library.views.register),
    url(r'^books/new_book[/]?', library.views.new_book),
)
