#首先，导入csv模块
import csv

#被读取的csv文件名
filename = 'example.csv'

#初始化字段和行列表
fields = []
rows = []


#打开并读取
with open(filename,'r') as csvfile:
	#创建一个csv reader对象
	csvreader = csv.reader(csvfile)
	
	#通过第一行，提取csv文件的字段
	#在python3中，需要使用next(csvreader),但是在Python2中，使用csvreader.next()
	fields = next(csvreader)

	#逐行读取数据
	for row in csvreader:
		rows.append(row)

	#获取总行数
	print('Total no. of rows: %d' % (csvreader.line_num))

#打印字段名称	
print('field names are:' + ','.join(field for field in fields))

#打印前五行
print('\nFist 5 rows are:\n')
for row in rows[:5]:
	#解析行的每一列
	for col in row:
		print('%10s' % col)
	print('\n')
