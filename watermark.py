import PyPDF2
	
def add_watermark(wmFile,pageObj):
	#打开水印pdf文件
	wmFileObj = open(wmFile,'rb')
	
	#创建pdfReader对象，把打开的水印pdf传入
	pdfReader = PyPDF2.PdfFileReader(wmFileObj)
	
	#将水印pdf的首页与传入的原始pdf的页进行合并
	pageObj.mergePage(pdfReader.getPage(0))	
	wmFileObj.close()
	return pageObj
	
def main():
		
	#水印pdf的名称
	mywatermark = 'water.pdf'

	#原始pdf的名称
	origFileName = 'example.pdf'

	#合并后新的pdf名称
	newFileName = 'watermark_example.pdf'

	#打开原始的pdf文件,获取文件指针
	pdfFileObj = open(origFileName,'rb')

	#创建reader对象
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	#创建一个指向新的pdf文件的指针
	pdfWriter = PyPDF2.PdfFileWriter()

	#通过迭代将水印添加到原始pdf的每一页
	for page in range(pdfReader.numPages):
		wmPageObj = add_watermark(mywatermark,pdfReader.getPage(page))
			
		#将合并后的即添加了水印的page对象添加到pdfWriter
		pdfWriter.addPage(wmPageObj)

	#打开新的pdf文件
	newFile = open(newFileName,'wb')
	#将已经添加完水印的pdfWriter对象写入文件
	pdfWriter.write(newFile)


	#关闭原始和新的pdf
	pdfFileObj.close()
	newFile.close()

if __name__ == '__main__':
		main()