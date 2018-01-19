# coding=utf-8

import requests
from lxml import html

LOGIN_URL = 'https://github.com/login'
SESSION_URL = 'https://github.com/session'
REPOS_URL = 'https://github.com/dashboard/ajax_your_repos?utf8=%E2%9C%93&your_repos_cursor={}'

s = requests.session()
r = s.get(LOGIN_URL)
tree = html.fromstring(r.text)
el = tree.xpath('//input[@name="authenticity_token"]')[0]
authenticity_token = el.attrib['value']

data = {
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'login': input("username:"),
    'password': input("password:")
}

r_login = s.post(SESSION_URL, data=data)
tree_login = html.fromstring(r_login.text)

# Load all repos
el_repos_cursor = tree_login.xpath('//input[@name="your_repos_cursor"]')[0]
repos_cursor = el_repos_cursor.attrib['value']

repos_data = {
            'utf8': '✓',
            'your_repos_cursor': repos_cursor
            }
r_more_repo = s.get(REPOS_URL.format(repos_cursor), params=repos_data)
tree_more_repo = html.fromstring(r_more_repo.text)
more_repo_list = tree_more_repo.xpath('//a[@itemprop="name codeRepository"]')
for more_data in more_repo_list:
    print(more_data.text)




