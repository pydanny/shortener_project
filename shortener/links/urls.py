from django.conf.urls.defaults import patterns, url

from .views import LinkRedirectView

urlpatterns = patterns("",

    url(
        regex = "^(?P<identifier>[-\w]+)/$",
        view = LinkRedirectView.as_view(),
        name = "link_redirect",
    ),
)