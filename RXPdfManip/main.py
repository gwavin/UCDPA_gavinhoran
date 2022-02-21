# importing required modules
import PyPDF2
import re
import shutil
import datetime
import os

from pathlib import Path


yourpath = 'rename\oldPdf'
# for root, dirs, files in os.walk(yourpath, topdown=False):
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        pdfName = os.path.join(root, name)
        print("Name of file is " + pdfName)

        print("interesting info from filename " + Path(pdfName).stem)

        emailSentTo = re.search(r'[\w\.-]+@[\w\.-]+\.\w+',pdfName)
        timeDateSent = re.search("([0-9]{14})", pdfName)

        print ("email was sent to " + emailSentTo.group(0) + " at " + timeDateSent.group(0) )

        pdfFileObj = open(pdfName, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        text = pageObj.extractText()
        mrn = re.search("MRN:\n(H[0-9]{7})", text)
        orderID = re.search("Order ID:\n\s\s([0-9]{9})", text)
        actualMRN = mrn.group(1)
        actualOrderID = orderID.group(1)
        print("MRN:" + actualMRN + "\n" + "Order ID:" + actualOrderID)
        def pdf_namer(filename):
            # t = '{0:%H%M%S%d%m%y}'.format(datetime.datetime.now())
            a = '.pdf'
            return ('RxPrinted' + Path(pdfName).stem + 'withMRN' + actualMRN + a)
        newName = pdf_namer('rename\oldPdf\DBPrint Job (9).pdf')
        print("new name is " + newName)
        print("\n")
        pdfFileObj.close()

        # original = r'C:\Users\gavin\OneDrive\Documents\GitHub\UCDPA_gavinhoran\RXPdfManip\rename\oldPdf\DBPrint Job (9).pdf'
        # target = r'\rename\NewPdf\' + newName
        # # target2 = r'C:\Users\gavin\OneDrive\Documents\GitHub\UCDPA_gavinhoran\RXPdfManip\rename\ManipPdf\DBPrint Job (9) sent.pdf'
        # #
        # shutil.copyfile(original, target)
        #
        # shutil.copyfile(original, target2)
        #


# this is the end of the for loop




# creating a pdf file object
pdfFileObj = open('rename\oldPdf\mncms.test@healthmail.ie@20220217170651 DBPrint Job (7).pdf', 'rb')
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
#mrn = re.search("MRN:\n(H[0-9]{7})", text)
print(mrn)
orderID = re.search("Order ID:\n\s\s([0-9]{9})", text)
print(orderID)
actualMRN = mrn.group(1)
actualOrderID = orderID.group(1)
print("MRN:" + actualMRN + " and Order ID:" + actualOrderID)
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

# yourpath = 'rename\oldPdf'
# # for root, dirs, files in os.walk(yourpath, topdown=False):
# for root, dirs, files in os.walk(yourpath, topdown=False):
#     for name in files:
#         pdfName = os.path.join(root, name)
#         print("pdfName is " + pdfName)
#
#     for name in dirs:
#         dirName = os.path.join(root, name)
#         print("dirName is " + dirName)

