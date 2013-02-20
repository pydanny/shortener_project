from django.contrib.sites.models import Site

def site(request):
    context = {}
    context['site'] = Site.objects.get_current()
    return context