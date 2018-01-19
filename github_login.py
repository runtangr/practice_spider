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

# login
r_login = s.post(SESSION_URL, data=data)
tree_login = html.fromstring(r_login.text)

# get repos cursor
el_repos_cursor = tree_login.xpath('//input[@name="your_repos_cursor"]')[0]
repos_cursor = el_repos_cursor.attrib['value']

# get repos list
repos_data = {
            'utf8': '✓',
            'your_repos_cursor': repos_cursor
            }
r_repo = s.get(REPOS_URL.format(repos_cursor), params=repos_data)
tree_repo = html.fromstring(r_repo.text)
repo_list = tree_repo.xpath('//a[@itemprop="name codeRepository"]')
for repo_data in repo_list:
    print(repo_data.text)




