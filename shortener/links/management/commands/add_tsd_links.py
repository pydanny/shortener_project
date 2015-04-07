import requests
import sys

from django.core.management.base import BaseCommand
from django.conf import settings

from links.models import Link

class Command(BaseCommand):
    help = 'Adds all the necessary links for a TSD version.'

    def handle(self, *args, **options):
        if len(args) != 2:
            print("Specify a Django version to copy from and another to copy to.")
            sys.exit()

        old, new = args

        for link in Link.objects.filter(
                identifier__startswith=old,
                original_url__startswith="https://docs.djangoproject.com/en/{}".format(old)
            ):
            new_identifier = link.identifier.replace(old, new)
            new_original_url = link.original_url.replace(old, new)
            r = requests.get(new_original_url)
            if not r.ok:
                print "BAD URL:", new_original_url
                continue
            new_link, created = Link.objects.get_or_create(
                identifier=new_identifier,
                original_url=new_original_url
            )
            print created, new_link