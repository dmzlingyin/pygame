import PyPDF2
	
pdfFile = open('example.pdf','rb')
	
pdfReader = PyPDF2.PdfFileReader(pdfFile)

print(pdfReader.numPages)

page = pdfReader.getPage(1)

print(page.extractText())

pdfFile.close()