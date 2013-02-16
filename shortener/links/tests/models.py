from django.test import TestCase

from links.models import Link


class LinkTests(TestCase):

    def test_create_normal(self):

        self.assertEqual(Link.objects.count(), 0)
        Link.objects.create(
            original_url="https://djangoproject.com",
            identifier="django-project"
        )
        self.assertEqual(Link.objects.count(), 1)
