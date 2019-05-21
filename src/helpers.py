import re

ALPHABET = "😆😂🤑🤗🤭🤫🤔🤐🤨😐😑😶😏💩🙄😬😴🤮😎🤓🧐😕😳😭😱😖😣😞😓😩"
BASE = 30

# This helper function takes an incrementing positive integer id that we
# pull from our Urls database table and converts it into a base30 alphabet
# of emoji characters. This will be the new short url.
#
# The reason I'm doing this is because I don't have to think about hash
# collisions. I get the absolute smallest url, and I can easily
# translate back to base 10 later if I decide on a different unique
# slug generation scheme.
def to_emoji_slug(pk):
    if pk == 0:
        return ALPHABET[0]

    digits = []
    while pk:
        digits.append(ALPHABET[int(pk % BASE)])
        pk = int(pk // BASE)

    digits.reverse()

    return ''.join(digits)

# This helper function checks that the url is at least semantically valid.
# I'm using a regex found on stack overflow.
# https://stackoverflow.com/questions/7160737/python-how-to-validate-a-url-in-python-malformed-or-not
def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.match(regex, url):
        return True
    return False
