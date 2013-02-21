from django.conf.urls.defaults import patterns, url

from links import views

urlpatterns = patterns("",

    url(
        regex = "^(?P<identifier>[-_\.\w]+)/$",
        view = views.LinkRedirectView.as_view(),
        name = "links_redirect",
    ),
    url(
        regex = "^~list/$",
        view = views.LinkListView.as_view(),
        name = "links_list",
    ),
    url(
        regex = "^(?P<identifier>[-_\.\w]+)/info/$",
        view = views.LinkDetailView.as_view(),
        name = "links_detail",
    ),

)