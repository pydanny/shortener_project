from django.core.urlresolvers import reverse
from django.db import models
from django.utils.baseconv import base64
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from .validators import validate_five_characters


class Link(TimeStampedModel):

    original_url = models.CharField(_("URL to be shortened"), max_length=255)
    identifier = models.CharField(_("Identifier"),
                                    max_length=100,
                                    blank=True,
                                    validators=[validate_five_characters],
                                    db_index=True)

    def __unicode__(self):
        return self.original_url

    @property
    def count(self):
        return self.linklog_set.count()

    def log(self, request):
        self.linklog_set.create_from_request(
            link=self,
            request=request
        )

    def get_identifier_url(self):
        return reverse("links_redirect", kwargs={'identifier': self.identifier})

    @property
    def tiny(self):
        return base64.encode(self.pk)

    def get_tiny_url(self):
        return reverse("links_redirect", kwargs={'identifier': self.tiny})
