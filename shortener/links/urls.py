from django.conf.urls.defaults import patterns, url

from links import views

urlpatterns = patterns("",

    url(
        regex = "^(?P<identifier>[\-\_\.\w]+)/$",
        view = views.LinkRedirectView.as_view(),
        name = "redirect",
    ),
    url(
        regex = "^~links/$",
        view = views.LinkListView.as_view(),
        name = "list",
    ),
    # url(
    #     regex = "^~shorten/$",
    #     view = views.LinkCreateView.as_view(),
    #     name = "create",
    # ),
    url(
        regex = "^(?P<identifier>[\-\_\.\w]+)/info/$",
        view = views.LinkDetailView.as_view(),
        name = "detail",
    ),

)