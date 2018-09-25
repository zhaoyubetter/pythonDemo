from bs4 import BeautifulSoup as BS
import re

text = '''
Pomellato宝曼兰朵特邀中国 IT Girl，时尚博主<a href='/n/Fil小白'>@Fil小白</a> 来到品牌发源地米兰，共赴 <a  href=\"https://m.weibo.cn/p/searchall?containerid=231522type%3D1%26q%3D%23Pomellato+Balera+Party%23%26t%3D10&extparam=%23Pomellato+Balera+Party%23\" data-hide=\"\"><span class=\"surl-text\">#Pomellato Balera Party#</span></a> 复古风情时尚派对，Fil 小白以一身酷黑西装套装现身，颈间佩戴<a  href=\"https://m.weibo.cn/p/searchall?containerid=231522type%3D1%26q%3D%23Pomellato+Tango%E7%B3%BB%E5%88%97%23%26t%3D10&extparam=%23Pomellato+Tango%E7%B3%BB%E5%88%97%23\" data-hide=\"\"><span class=\"surl-text\">#Pomellato Tango系列#</span></a> 玫瑰金镶钻项链，指间巧妙叠戴<a  href=\"https://m.weibo.cn/p/searchall?containerid=231522type%3D1%26q%3D%23Pomellato+Nudo%E7%B3%BB%E5%88%97%23%26t%3D10&extparam=%23Pomellato+Nudo%E7%B3%BB%E5%88%97%23\" data-hide=\"\"><span class=\"surl-text\">#Pomellato Nudo系列#</span></a> 与<a  href=\"https://m.weibo.cn/p/searchall?containerid=231522type%3D1%26q%3D%23Pomellato+Iconica%E7%B3%BB%E5%88%97%23%26t%3D10&extparam=%23Pomellato+Iconica%E7%B3%BB%E5%88%97%23\" data-hide=\"\"><span class=\"surl-text\">#Pomellato Iconica系列#</span></a> 戒指，明丽魅惑间气场全开。"
'''

soup = BS(text, 'html.parser')
# movies = soup.findAll('a', attrs={'target': '_blank', 'href': re.compile('http://movie.mtime.com/(\d+)/')})
# print(soup.a.replace_with(''))

for match in soup.findAll('a'):     # unwrap a
    # print(match.text)
    # print(match.get('href'))        # 子链接
    print(match.unwrap())
for match in soup.findAll('span'):  # unwrap span
    match.unwrap()
print(re.sub(r'\s', '', soup.text))  # remove space

