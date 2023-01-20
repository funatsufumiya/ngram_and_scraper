from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

import argparse

parser = argparse.ArgumentParser(
    description='Scrape text from a webpage.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument(
    'url',
    help='URL to scrape text from.'
)

args = parser.parse_args()
url = args.url

def filter_element(e):
    if e and hasattr(e, "attrs") and e.attrs:
        if e.get('id'):
            id = e.get('id')
            if "head" in id:
                return False
            if "nav" in id:
                return False
            if "menu" in id:
                return False
            if "foot" in id:
                return False
            if "error" in id:
                return False
            if "bookmark" in id:
                return False
            if "announce" in id:
                return False
        if e.get('class'):
            clazz = e.get('class')
            if "head" in clazz:
                return False
            if "nav" in clazz:
                return False
            if "menu" in clazz:
                return False
            if "foot" in clazz:
                return False
            if "error" in clazz:
                return False
            if "bookmark" in clazz:
                return False
            if "announce" in clazz:
                return False
    return True

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False

    es = [e for e in element.parents]
    results = [filter_element(e) for e in es]
    if False in results:
        return False

    # if element.parent.name == 'a':
        # return False

    if isinstance(element, Comment):
        return False

    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

html = urllib.request.urlopen(url).read()
print(text_from_html(html))