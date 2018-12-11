import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/subject/20438964/reviews'
html = requests.get(url).text
#print(html)
soup = BeautifulSoup(html,'lxml-xml')
p = soup.findAll('div',class_="main-bd")
for i in p:
	print(i.p)
