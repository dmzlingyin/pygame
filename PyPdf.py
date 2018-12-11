import PyPDF2

def PDFrotate(origFileName,newFileName,rotation):
	pdfFile = open(origFileName,'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFile)
	pdfWriter = PyPDF2.PdfFileWriter()

	for page in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(page)
		pageObj.rotateClockwise(rotation)

		pdfWriter.addPage(pageObj)

	newFile = open(newFileName,'wb')
	pdfWriter.write(newFile)

	pdfFile.close()
	newFile.close()
def main():
	origFileName = 'example.pdf'
		
	newFileName = 'testexample.pdf'
	rotation = 270
	PDFrotate(origFileName,newFileName,rotation)

if __name__ == '__main__':
	main()
