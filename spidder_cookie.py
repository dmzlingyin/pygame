'''
利用cookie登录网页
Date:2018-12-09
目标网站：mail.163.com
'''

from urllib import request,parse
from http import cookiejar


#创建一个CookieJar实例
cookie = cookiejar.CookieJar()

#生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

#创建http请求管理器
http_handler = request.HTTPHandler()

#生成HTTPS管理器
https_handler = request.HTTPSHandler()

#创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)


def login():
	'''
	此处填写你的用户名和密码，用来登录，获取cookie
	'''
	url = 'https://mail.163.com/'

	data = {'email':'dmzlingyin@163.com','password':'lingyin-123'}

	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'}
	#对data进行编码
	data = parse.urlencode(data)

	req = request.Request(url,headers = headers,data = data.encode())

	#使用opener发送请求,会自动的提取cookie
	rsp = opener.open(req)



def getHomePage():
	url = 'https://mail.163.com/js6/main.jsp?sid=qAzVoVOOREqSciuakROOqtfPpxCqyUXc&df=mail163_letter#module=welcome.WelcomeModule%7C%7B%7D'

	#用已经获取到的cookie进行登录
	rsp = opener.open(url)
	html = rsp.read().decode()

	with open('cookie.html','w') as f:
		f.write(html)


def main():

	
	login()
	getHomePage()


if __name__ == '__main__':
	main()




