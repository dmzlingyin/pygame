import json
import requests
from bs4 import BeautifulSoup
import re
import sys

def GetUrl(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
	html = requests.get(url,headers = headers)
	soup = BeautifulSoup(html.text,'lxml-xml')
	return soup
# html = GetUrl('https://p3.music.126.net/ZFidqIhd85NA-Da7UF2Q6A==/109951163673064746.jpg?param=1366y768')
# soup = GetUrl('https://mm.taobao.com/json/request_top_list.htm?page=1')
# lists = soup.find_all('div',class_='personal-info')
# print(lists)

html = requests.get('https://g.alicdn.com/mission/mission-assets/0.5.46/index.js')
print(json.loads(html.text))