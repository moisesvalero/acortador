from django.test import TestCase

from shortener.models import Link


class LinkModelTests(TestCase):
    def test_create_link(self):
        link = Link.objects.create(
            original_url="https://example.com",
            short_code="test12",
        )
        self.assertEqual(link.original_url, "https://example.com")
        self.assertEqual(link.short_code, "test12")
        self.assertEqual(link.clicks_count, 0)
        self.assertTrue(link.is_active)

    def test_link_str(self):
        link = Link.objects.create(
            original_url="https://example.com",
            short_code="abc123",
        )
        self.assertIn("abc123", str(link))
        self.assertIn("example.com", str(link))

    def test_short_url_property(self):
        link = Link.objects.create(
            original_url="https://example.com",
            short_code="abc123",
        )
        self.assertIn("/abc123", link.short_url)

    def test_ordering_newest_first(self):
        Link.objects.create(original_url="https://a.com", short_code="aaaaaa")
        Link.objects.create(original_url="https://b.com", short_code="bbbbbb")
        links = Link.objects.all()
        self.assertGreater(links[0].id, links[1].id)

    def test_default_is_active(self):
        link = Link.objects.create(
            original_url="https://example.com",
            short_code="active1",
        )
        self.assertTrue(link.is_active)

    def test_clicks_count_defaults_to_zero(self):
        link = Link.objects.create(
            original_url="https://example.com",
            short_code="click0",
        )
        self.assertEqual(link.clicks_count, 0)
