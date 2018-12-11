import PyPDF2
	
def PDFmerge(pdfs,output):
		
	#创建一个pdf文件合并对象
	pdfMerger = PyPDF2.PdfFileMerger()
	
	#逐个添加pdf
	for pdf in pdfs:
		with open(pdf,'rb') as f:
			pdfMerger.append(f)

	#将内存中合并的pdf文件写入
	with open(output,'wb') as f:
		pdfMerger.write(f)
	
def main():
	#需要合并的pdf名称
	pdfs = ['example.pdf','testexample.pdf']
		
	#合并完成的pdf名称
	output = 'combined_example.pdf'
	#调用PDFmerge函数，进行合并
	PDFmerge(pdfs,output)
if __name__ == '__main__':
	main()