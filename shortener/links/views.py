from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.baseconv import base64
from django.utils import timezone
from django.views.generic import RedirectView, ListView, DetailView

from .models import Link
from linkmetrics.models import LinkLog


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


class LinkListView(ListView):

    model = Link


class LinkDetailView(DetailView):

    model = Link

    def get_object(self):
        identifier = self.kwargs['identifier']
        if '-' in identifier or '_' in identifier:
            return get_object_or_404(Link, identifier=identifier)

        # decode based on the identifier
        pk = base64.decode(identifier)
        try:
            link = Link.objects.get(Q(pk=pk) | Q(identifier=identifier))
        except Link.DoesNotExist:
            raise Http404

        return link

    def get_context_data(self, *args, **kwargs):
        context = super(LinkDetailView, self).get_context_data(**kwargs)
        # Ghetto style just to get it working
        counts = []
        for date in self.object.linklog_set.dates('created', 'day'):

            count = LinkLog.objects.filter(
                    created__day=date.day,
                    created__month=date.month,
                    created__year=date.year,
                    link=self.object
                ).count()
            counts.append(
                {"date": date + timezone.timedelta(1),  # timezone to fix weird off-by-one
                "count": count}
            )

        context['counts'] = counts
        return context
