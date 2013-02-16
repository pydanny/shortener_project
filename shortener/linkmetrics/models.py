from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from .managers import LingLogManager
from links.models import Link


class LinkLog(TimeStampedModel):
    """
        TODO - consider moving this to Redis or MongoDB
    """

    link = models.ForeignKey(Link)

    http_accept_language = models.CharField(_("HTTP_ACCEPT_LANGUAGE"), max_length=255, blank=True)
    http_host = models.CharField(_("HTTP_HOST"), max_length=255, blank=True)
    http_referer = models.CharField(_("HTTP_REFERER"), max_length=255, blank=True)
    http_user_agent = models.CharField(_("HTTP_USER_AGENT"), max_length=255, blank=True)
    query_string = models.TextField(_("QUERY_STRING"), blank=True)
    remote_addr = models.CharField(_("REMOTE_ADDR"), max_length=255, blank=True)
    remote_host = models.CharField(_("REMOTE_HOST"), max_length=255, blank=True)
    request_method = models.CharField(_("REQUEST_METHOD"), max_length=30, blank=True)

    objects = LingLogManager()

    def __unicode__(self):
        return "{0}: {1}".format(
            self.created,
            self.link.original_url
        )
