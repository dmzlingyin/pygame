import requests
from bs4 import BeautifulSoup
import re
import sys


# #Spider类
# class Spider(object):
# 	def __init__(self,url,page_start,page_end):
# 		self.url = url
# 		self.page_start = page_start
# 		self.page_end = page_end + 1

# 	def start(self):
# 		for page in (self.page_start,self.page_end):
# 			url = self.url + ''

url = 'https://tech.sina.com.cn/'

def Get_Url(url):
	html = requests.get(url)
	html.encoding='utf-8'
	soup = BeautifulSoup(html.text,'lxml-xml')
	return soup

#列出所有it新闻的标题

link_list = []

def Title():

	soup = Get_Url(url)
	a_tag = soup.find_all('a')
	title_list = []
	
	for link in a_tag:
		if re.match(r'^https://tech.sina.com.cn/it',link['href']):
			title_list.append(link.text.strip())
			link_list.append(link['href'])
	return title_list



# def Get_Content():
# 	for link in link_list:

# 		soup = Get_Url(link)
# 		p = soup.find_all('div',{'class':'article'})
# 		for x in p:
# 			print(x.text)
			
Title()
# Get_Content()
link = link_list[6]
soup = Get_Url(link)
print(link)


print(soup.select(''))