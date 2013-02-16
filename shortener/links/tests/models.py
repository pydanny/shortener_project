from django.test import TestCase

from links.models import Link


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
