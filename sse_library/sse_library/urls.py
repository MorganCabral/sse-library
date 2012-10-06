from django.conf.urls import patterns, include, url
from django.contrib import admin  # Enable Admin
admin.autodiscover()

from library.views import *

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Book routes
    url(r'^books[/]?$', BookIndexView.as_view()),
    url(r'^books/register[/]?', BookRegisterView.as_view()),
)
