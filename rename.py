#导入模块
import os

#定义一个函数，用来重命名文件
def main():
	i = 0

	for filename in os.listdir('xyz'):
		dst = "Lingyin" + str(i) + ".jpg"
		src = 'xyz/' + filename
		dst = 'xyz/' + dst
		print('第 %s 张图片已更名成功！' % str(i+1))


		os.rename(src,dst)
		i += 1

if __name__ == "__main__":
	main()