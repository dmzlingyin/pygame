from zipfile import ZipFile
import os
def get_all_file_paths(directory):
	#初始化一个空的路径列表
	file_paths = []

	#遍历所有的目录和子目录
	for root,directories,files in os.walk(directory):
		for filename in files:
			#连接这两个字符串以形成完整的文件路径。
			filepath = os.path.join(root,filename)
			file_paths.append(filepath)


	#返回所有的目录路径

def main():
	#需要压缩的文件夹的路径
	directory = './python'

	#调用函数获得所有文件的完整路径
	file_paths = get_all_file_paths(directory)

	#打印出要被压缩的文件列表
	print('Following files will be zipped:')
	for file_name in file_paths:
		print(file_name)

	#压缩文件
	with ZipFile('my_python_files.zip','w') as zip:
		#逐个压缩
		for file in file_paths:
			zip.write(file)

	print('All files zipped successfully!')

if __name__ == '__main__':
	main()
