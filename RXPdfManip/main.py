# importing required modules
import PyPDF2
import re
import shutil
import datetime

# creating a pdf file object
pdfFileObj = open('rename\oldPdf\DBPrint Job (9).pdf', 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# creating a page object
pageObj = pdfReader.getPage(0)
# extracting text from page and calling it "text"
# print(pageObj.extractText())
text = pageObj.extractText()
# printing to check the content
# print(text) ;

# searching for MRN
mrn = re.search("MRN:\n(H[0-9]{7})", text)
# [0-9]{7}
# imtag = re.match(r'<img.*?>', line).group(0)
# print(mrn)
actualMRN = mrn.group(1)
print(actualMRN)
# print(type(text))
# closing the pdf file object
def pdf_namer(filename):
    t = '{0:%H%M%S%d%m%y}'.format(datetime.datetime.now())
    a = '.pdf'
    return ('RxPrinted' + t + 'withMRN' + actualMRN + a)

newName = pdf_namer('rename\oldPdf\DBPrint Job (9).pdf')
print("new name is " + newName)

# original = r'C:\Users\gavin\OneDrive\Documents\GitHub\UCDPA_gavinhoran\RXPdfManip\rename\oldPdf\DBPrint Job (9).pdf'
# target = r'\rename\NewPdf\' + newName
# # target2 = r'C:\Users\gavin\OneDrive\Documents\GitHub\UCDPA_gavinhoran\RXPdfManip\rename\ManipPdf\DBPrint Job (9) sent.pdf'
# #
# shutil.copyfile(original, target)
#
# shutil.copyfile(original, target2)
#

pdfFileObj.close()
