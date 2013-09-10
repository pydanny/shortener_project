from django.conf import settings
from django.contrib import admin
from django.contrib.sites.models import Site
from django.utils.safestring import mark_safe

from .models import Link


class LinkAdmin(admin.ModelAdmin):

    verbose_name_plural = "links"
    list_display = ['original_url',  'identifier',  'count', 'created', 'modified', ]

    readonly_fields = ('test_url', 'created', 'modified', 'count')

    def test_url(self, instance):
        site = Site.objects.get_current()
        response = """<a href="{0}{1}/{2}">{0}{1}/{2}</a>""".format(
                "http://",
                site.domain,
                instance.identifier
            )
        return mark_safe(response)

    test_url.short_description = "Test URL"
    test_url.allow_tags = True


admin.site.register(Link, LinkAdmin)