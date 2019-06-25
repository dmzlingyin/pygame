#******************************************************************
# Autho:lingyin
# Date:2019-06-24 22:41
# The main function of this program is that download the pictures on a website
#******************************************************************

#此网站运用了ajax技术，暂时不能解决

import requests
from bs4 import BeautifulSoup

# main site url
Url = 'http://taim9.com/?p=101&paage=1'

Url_list = []


def get_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    html = requests.get(url, headers=headers)
    print(html.text)
    soup = BeautifulSoup(html.text, "html5lib")
    return soup


soup = get_url(Url)
images = soup.find_all('img', title="田英章欧体毛笔楷书字汇田字格版高清字帖")

for img in images:
    print(img)
