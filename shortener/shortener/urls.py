from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(settings.ADMIN_DOCS_URL_BASE, include('django.contrib.admindocs.urls')),
    url(settings.ADMIN_URL_BASE, include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^', include("links.urls")),
)
