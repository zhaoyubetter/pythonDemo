# spider to get email address
import re
import requests

from html.parser import HTMLParser
from html.entities import name2codepoint

# email 正则
s_email_regex = r'[a-zA-Z0-9_\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-\.]+'  # 111@ddd-cc.com.com

# 以下为内容
def collect_content(s_content, s_regex):
    result = []
    regex = re.compile(s_regex)  # compile
    emails = regex.findall(s_content)
    result.extend(emails)
    return result


# htmlParser 从特定网址上爬
class MyHTMLParser(HTMLParser):

    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.email_data_origin = ''

    def handle_data(self, data):
        if self.lasttag == 'a':
            self.email_data_origin = self.email_data_origin + ", " + data

    def generate_origin(self):
        return self.email_data_origin


req = requests.get('http://www.modemonline.com/fashion/press-days/spring-summer-2014/press-days-search')
parser = MyHTMLParser()
parser.feed(req.text)
origin_str = parser.generate_origin()
with open('../email-result.txt', 'w') as f:
    result = collect_content(origin_str, s_email_regex)
    f.write('\n'.join(result))
# 写入文件

# collect_content(req.text, s_email_regex)

# with open('website.txt', mode='r') as f:
#     collect_content(f.read(), s_email_regex)
