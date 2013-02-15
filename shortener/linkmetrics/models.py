from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from links.models import Link


class LinkLog(TimeStampedModel):
    """
        TODO - consider moving this to Redis or MongoDB
    """

    link = models.ForeignKey(Link)
    ip_address = models.IPAddressField(_("IP Address"))

    def __unicode__(self):
        return "{0}: {1}".format(
            self.created,
            self.original_url
        )
