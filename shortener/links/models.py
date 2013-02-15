from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class Link(TimeStampedModel):

    original_url = models.CharField(_("URL to be shortened"), max_length=255)
    identifier = models.CharField(_("Identifier"), max_length=100, db_index=True)
    count = models.IntegerField(_("count"), null=True, blank=True, default=0)

    def __unicode__(self):
        return self.original_url

    @property
    def count(self):
        return self.linklog_set.count()

    def log(self, ip_address):
        self.linklog_set.create(
            link=self,
            ip_address=ip_address
        )
