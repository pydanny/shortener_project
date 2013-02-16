from django.db import models
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
