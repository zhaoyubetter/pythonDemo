from bs4 import BeautifulSoup as BS
import re

text = '''
<a  href="https://m.weibo.cn/p/searchall?containerid=231522type%3D1%26q%3D%23Pomellato+for+Women%23%26t%3D10&luicode=10000011&lfid=1076032175173250" data-hide="">
    <span class="surl-text">#Pomellato for Women#</span></a>
        “当你可以表达自我时；当你了解自己内心的敏感并为之坦诚时，真正独属于你的美油然而生。”Pomellato宝曼兰朵2017艺术广告掌镜人、国际著名时尚摄影大师彼得·林德伯格(Peter Lindbergh)如是阐述此次拍摄主题。六位来自不同专业领域、年龄各异的魅力女人在镜头前一如本色，袒露真 ​​​...
        <a href="/status/4113817984553285">全文</a>
'''

soup = BS(text, 'html.parser')
# movies = soup.findAll('a', attrs={'target': '_blank', 'href': re.compile('http://movie.mtime.com/(\d+)/')})
# print(soup.a.replace_with(''))

for match in soup.findAll('a'):     # unwrap a
    print(match.text)
    print(match.get('href'))        # 子链接
    # print(match.unwrap())
for match in soup.findAll('span'):  # unwrap span
    match.unwrap()
print(re.sub(r'\s', '', soup.text))  # remove space
