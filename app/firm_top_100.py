# 参考：
# https://blog.csdn.net/SKI_12/article/details/78411824?locationNum=5&fps=1

import requests
import re
import time
import json
from bs4 import BeautifulSoup as BS

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}


def get_movie_url():
    urls = []
    for i in range(1, 11):
        if i != 1:
            url = 'http://www.mtime.com/top/movie/top100/index-%s.html' % i
        else:
            url = 'http://www.mtime.com/top/movie/top100'
        r = requests.get(url, headers=headers)
        soup = BS(r.text, 'lxml')
        movies = soup.findAll('a', attrs={'target': '_blank', 'href': re.compile('http://movie.mtime.com/(\d+)/')})
        for m in movies:
            urls.append(m.get('href'))

    return urls


def create_ajax_req(url):
    movie_id = url.split('/')[-2]  # http://movie.mtime.com/12231/
    t = time.strftime('%Y%m%d%H%M%S0368', time.localtime())
    ajax_url = 'http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services' \
               '&Ajax_CallBackMethod=GetMovieOverviewRating' \
               '&Ajax_CrossDomain=1&Ajax_RequestUrl=%s&t=%s&Ajax_CallBackArgument0=%s' % (url, t, movie_id)
    return ajax_url


def crawl(ajax_url):
    req = requests.get(ajax_url, headers)
    if req.status_code == 200:
        req.encoding = 'utf-8'
        # get result json
        result = re.findall(r'=(.+?);', req.text)[0]

        if result is not None:
            value = json.loads(result)

            movieTitle = value.get('value').get('movieTitle')
            TopListName = value.get('value').get('topList').get('TopListName')
            Ranking = value.get('value').get('topList').get('Ranking')
            movieRating = value.get('value').get('movieRating')
            RatingFinal = movieRating.get('RatingFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            print(movieTitle)
            if value.get('value').get('boxOffice'):
                TotalBoxOffice = value.get('value').get('boxOffice').get('TotalBoxOffice')
                TotalBoxOfficeUnit = value.get('value').get('boxOffice').get('TotalBoxOfficeUnit')
                print('票房：%s%s' % (TotalBoxOffice, TotalBoxOfficeUnit))

            print('%s——No.%s' % (TopListName, Ranking))
            print('综合评分：%s 导演评分：%s 画面评分：%s 故事评分：%s 音乐评分：%s' % (
                RatingFinal, RDirectorFinal, RPictureFinal, RStoryFinal, ROtherFinal))
            print('****' * 20)


def main():
    urls = get_movie_url()
    for u in urls:
        crawl(create_ajax_req(u))


# 问题所在，请求如下单个电影链接时时不时会爬取不到数据
# Crawl(Create_Ajax_URL('http://movie.mtime.com/98604/'))

if __name__ == '__main__':
    main()
