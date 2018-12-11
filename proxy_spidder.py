'''
使用代理访问百度
时间 2018-12-08
'''

from urllib import request,error


def main():

	url = 'http://www.baidu.com'

	#使用代理的步骤
	#1、设置代理地址
	proxy = {'http':'112.13.96.39:8927'}
	#2、创建ProxyHandler
	proxy_handler = request.ProxyHandler(proxy)
	#3、创建Opener
	opener = request.build_opener(proxy_handler)
	#4、安装Opener
	request.install_opener(opener)

	try:
		rsp = request.urlopen(url)
		html = rsp.read().decode()
		print(html)
	except error.URLError as e:
		print(e)
	except Exception as e:
		print(e)

if __name__ == '__main__':
	main()