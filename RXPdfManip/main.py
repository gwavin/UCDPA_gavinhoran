# importing required modules
import PyPDF2
# creating a pdf file object
pdfFileObj = open('rename\oldPdf\DBPrint Job (9).pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page obje
pageObj = pdfReader.getPage(0)

#print(pdfReader.getFields())
# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
