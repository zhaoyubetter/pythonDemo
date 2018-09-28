# crawl data
import requests
import re
import json
import time
from bs4 import BeautifulSoup as BS

headers = {
    'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'
}

# 全文extend_url
extend_url = 'https://m.weibo.cn/statuses/extend?id=%s'
# 宝曼兰朵
brand_url = 'https://m.weibo.cn/api/container/getIndex?uid=2175173250&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%AE%9D%E6%9B%BC%E5%85%B0%E6%9C%B5&type=uid&value=2175173250&containerid=1076032175173250'


# 获取微博正文的url地址
def get_weibo_url():
    urls = []
    for i in range(1, 164):  # 164 这里需要变动的。。。
        if i != 1:
            urls.append(brand_url + ('&page=%s' % i))
        else:
            urls.append(brand_url)
    return urls


def crawl(url):
    resp = requests.get(url, headers)
    content = ''
    if resp.status_code == 200:
        json_data = json.loads(resp.text)  # 包含unicode编码
        page = json_data.get('data').get('cardlistInfo').get('page')  # 当前页
        if page is None:
            content = content + '>>>>>>>>>>>>>>>>> 当前第%s页' % 1 + '\n'
            # print('>>>>>>>>>>>>>>>>> 当前第%s页' % 1)
        else:
            content = content + '>>>>>>>>>>>>>>>>> 当前第%s页' % page + '\n'
            # print('>>>>>>>>>>>>>>>>> 当前第%s页' % page)

        cards = json_data.get('data').get('cards')  # 每屏 11个
        for text in cards:
            created_time = (text.get('mblog').get('created_at'))
            more_data = analyze_text((text.get('mblog').get('text')))
            created_text = more_data[0]
            content = content + '发布于：%s' % created_time + '\n'
            content = content + created_text + '\n'
            content = content + '****' * 20 + '\n'
            # print('发布于：%s' % created_time)
            # print(created_text)
            # print('****' * 20)
        return created_time, content


def analyze_text(text):
    '''
    分析文本，返回去掉text中 html的标签的内容，如果text中包含全文，获取其对应的 a 中 的 href 内，返回元祖
    :param text:
    :return: content and href
    '''
    soup = BS(text, 'html.parser')
    sub_href = ''

    for match in soup.findAll('a'):  # unwrap a
        if '全文' == match.text:
            sub_href = match.get('href')  # 子链接
            return extend_text(sub_href), sub_href
    for match in soup.findAll('span'):  # unwrap span
        match.unwrap()

    content = re.sub(r'\s', '', soup.text)  # remove space

    return content, sub_href


def extend_text(sub_href):
    '''
    发请求获取微博全文
    :param sub_href: 子链接
    :return:
    '''
    t = sub_href.split('/')
    if t is not None and len(t) > 0:
        resp = requests.get(extend_url % t[-1], headers)
        if resp.status_code == 200:
            json_data = json.loads(resp.text)  # 包含unicode编码
            content = json_data.get('data').get('longTextContent')  # 全文都在这里

            # 去掉html标签
            soup = BS(content, 'html.parser')
            for match in soup.findAll('a'):  # unwrap a
                match.unwrap()
            for match in soup.findAll('span'):  # unwrap span
                match.unwrap()

            return re.sub(r'\s', '', soup.text)  # remove space


# 每年形成一个文件
def write_to_file(content):
    created_date = content[0]
    created_content = content[1]
    a = re.match(r'(\d{4})-\d{2}-\d{2}', created_date)
    if a is not None:
        filename = a.group(1)
    else:
        filename = time.strftime('%Y', time.localtime())

    print(filename)
    with open('../y_generate/%s.txt' % filename, 'a+', encoding='utf-8') as file:
        file.write(created_content)


def main():
    urls = get_weibo_url()
    for u in urls:
        write_to_file(crawl(u))


# 问题所在，请求如下单个电影链接时时不时会爬取不到数据
# Crawl(Create_Ajax_URL('http://movie.mtime.com/98604/'))
#
# if __name__ == '__main__':
# #main()