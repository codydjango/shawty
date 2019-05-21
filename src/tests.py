# Very simple unit tests for functions.
import unittest

from helpers import is_valid_url


class Test(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main(verbosity=2)
