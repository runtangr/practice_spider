# coding=utf-8
import requests
from lxml import html
import time

EMAIL_URL = 'https://www.zhihu.com/login/email'
EXPLORE_URL = 'https://www.zhihu.com/explore'
CAPTCHA_URL = 'https://www.zhihu.com/captcha.gif?r=1463377588&type=login'

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
          "Host": "www.zhihu.com",
          "Origin": "https://www.zhihu.com",
          "Pragma": "no-cache",
          "Referer": "https://www.zhihu.com/explore"}


def get_captcha(data):
    with open('captcha.gif','wb') as fb:
        fb.write(data)
    return input('captcha:')


def login():
    s = requests.session()
    r = s.get(EXPLORE_URL, headers=header)
    tree = html.fromstring(r.text)
    el = tree.xpath('//input[@name="_xsrf"]')[0]
    xsrf_token = el.attrib['value']

    captcha = s.get('https://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time()*1000),
                    headers=header).content

    data = {
        'email': input('email:'),
        'password': input('password:'),
        'remember_me': 'true',
        'captcha': get_captcha(captcha)

    }

    header['X-Xsrftoken'] = xsrf_token

    r = s.post(EMAIL_URL, headers=header, data=data)
    print(r.json())

if __name__ == "__main__":
    login()


