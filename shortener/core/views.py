from django.contrib.sites.models import Site
from django.views.generic import TemplateView


class HomeView(TemplateView):
    
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['site'] = Site.objects.get_current()
        return context