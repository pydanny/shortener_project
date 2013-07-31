from django.core.urlresolvers import reverse
from django.db import models
from django.utils.baseconv import base64
from django.utils.translation import ugettext_lazy as _

from amazonify import amazonify
from model_utils.models import TimeStampedModel

from .validators import validate_five_characters


class Link(TimeStampedModel):

    original_url = models.CharField(_("URL to be shortened"), max_length=255, unique=True)
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
        return reverse("links:redirect", kwargs={'identifier': self.identifier})

    @property
    def tiny(self):
        return base64.encode(self.pk)

    def get_tiny_url(self):
        return reverse("links:redirect", kwargs={'identifier': self.tiny})

    def amazonify(self):
        url = self.original_url
        if url.startswith(
            ("https://amazon.",
                "http://amazon.",
                "http://amzn.",
                "https://amzn.",
                "https://www.amazon.",
                "http://www.amazon.")
            ):
            url = amazonify(url, "mlinar-20")
        return url
