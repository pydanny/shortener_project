from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.baseconv import base64
from django.views.generic import RedirectView
from django.http.request import QueryDict
from django.utils.datastructures import MultiValueDict

from .models import Link


class LinkRedirectView(RedirectView):

    permanent = True
    query_string = True

    def get_redirect_url(self, **kwargs):
        identifier = self.kwargs['identifier']

        # If identifier includes a link it means we don't need to do a base64
        # decode. Just a fetch based on the identifier
        if '-' in identifier or '_' in identifier:
            link = get_object_or_404(Link, identifier=identifier)
            link.log(self.request)
            return link.original_url

        # decode based on the identifier
        pk = base64.decode(identifier)
        try:
            link = Link.objects.get(Q(pk=pk) | Q(identifier=identifier))
        except Link.DoesNotExist:
            raise Http404

        link.log(self.request)
        return link.original_url
