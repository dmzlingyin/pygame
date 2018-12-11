
#导入zip库
from zipfile import ZipFile

#要提取的zip文件名
file_name = "my_python_files.zip"

#以读的方式打开zip文件
with ZipFile(file_name,'r') as zip:
	#打印zip文件内的目录
	zip.printdir()

	#提取所有文件
	print('Extracting all the files now...')
	zip.extractall()
	print('Done!!')