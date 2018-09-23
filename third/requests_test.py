import requests

# base use
r = requests.get('https://www.jd.com/')
print(r.status_code)
print(r.text)

# for get
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
print(r.encoding)
print(r.content)  # 2进制 or text
