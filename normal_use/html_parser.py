from html.parser import HTMLParser
from html.entities import name2codepoint

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request


class MyhtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


test_html = '''
<html>
<head></head>
<body>
<!-- test html parser -->
    <br />
    &nbsp; &nbsp;
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>
'''

parser = MyhtmlParser()
# parser.feed(test_html)

with request.urlopen('https://www.python.org/events/python-events/') as f:
   html_data = f.read().decode('utf-8')
   parser.feed(html_data)
