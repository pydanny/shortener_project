from django.test import TestCase

from links.models import Link
from linkmetrics.models import LinkLog


class LinkTests(TestCase):

    def setUp(self):
        self.link, created = Link.objects.get_or_create(
            original_url="https://djangoproject.com",
            identifier="django-project"
        )

    def test_identifier_url(self):
        url = self.link.get_identifier_url()
        response = self.client.get(url)
        self.assertEquals(response.status_code, 301)
        self.assertEquals(LinkLog.objects.count(), 1)

    def test_tiny_url(self):
        url = self.link.get_tiny_url()
        response = self.client.get(url)
        self.assertEquals(response.status_code, 301)
        self.assertEquals(LinkLog.objects.count(), 1)
