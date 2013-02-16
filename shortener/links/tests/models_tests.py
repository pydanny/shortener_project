from django.test import TestCase

from links.models import Link
from linkmetrics.models import LinkLog


class MockRequest(object):
    META = {}


class LinkTests(TestCase):

    def test_create_normal(self):

        self.assertEqual(Link.objects.count(), 0)
        link = Link.objects.create(
            original_url="https://djangoproject.com",
            identifier="django-project"
        )
        link.save()
        self.assertEqual(Link.objects.count(), 1)

    def test_empty_identifier(self):
        self.assertEqual(Link.objects.count(), 0)
        link = Link.objects.create(
            original_url="https://djangoproject.com",
        )
        link.save()
        self.assertEqual(Link.objects.count(), 1)

    def test_method_log(self):
        self.assertEqual(Link.objects.count(), 0)
        self.assertEqual(LinkLog.objects.count(), 0)
        request = MockRequest()
        link = Link.objects.create(
            original_url="https://djangoproject.com",
        )
        link.log(request)
        self.assertEqual(Link.objects.count(), 1)
        self.assertEqual(LinkLog.objects.count(), 1)
