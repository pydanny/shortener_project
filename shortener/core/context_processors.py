from django.contrib.sites.models import Site

def site(request):
    context = {}
    context['site'] = Site.objects.get_current()
    context['STATIC_URL'] = 'https://s3.amazonaws.com/shortener/'
    return context
