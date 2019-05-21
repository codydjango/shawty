# Very basic unit tests for helper functions.
import unittest

from helpers import is_valid_url, to_emoji_slug


class UrlValidationTest(unittest.TestCase):
    def test_valid_urls(self):
        valid_urls = [
            'http://codydjango.com',
            'https://codydjango.com',
            'http://codydjango.ca',
            'http://subdomain.codydjango.co',
            'https://codydjango.ca/a',
            'https://codydjango.ca/a/asdf',
            'https://codydjango.ca/a/asdf/',
            'https://codydjango.net/a/asdf/?foo',
            'https://codydjango.co/a/asdf/?foo=bar',
            'https://codydjango.com/a/asdf/?foo=bar&baz=bat',
            'https://codydjango.com/a/asdf#link?foo=bar&baz=bat',
        ]

        self.assertTrue(all([is_valid_url(url) for url in valid_urls]))

    def test_invalid_urls(self):
        invalid_urls = [
            'htp://codydjango.com',
            'codydjango.com',
            'www.codydjango.ca',
            'http://subdomain',
        ]

        self.assertFalse(all([is_valid_url(url) for url in invalid_urls]))


class BaseConverterTest(unittest.TestCase):
    def test_valid_urls(self):
        self.assertEqual(to_emoji_slug(0), "😆")
        self.assertEqual(to_emoji_slug(1), "😂")
        self.assertEqual(to_emoji_slug(29), "😩")
        self.assertEqual(to_emoji_slug(30), "😂😆")
        self.assertEqual(to_emoji_slug(31), "😂😂")
        self.assertEqual(to_emoji_slug(299), "😐😩")
        self.assertEqual(to_emoji_slug(300), "😑😆")
        self.assertEqual(to_emoji_slug(301), "😑😂")
        self.assertEqual(to_emoji_slug(4234353453423245324524323452345), "😏🤭😐😎🤫😳😎🙄🤨🤑🤨😶😑🤫😓😭🤗🤭😬😓🤫")


if __name__ == '__main__':
    unittest.main(verbosity=2)
