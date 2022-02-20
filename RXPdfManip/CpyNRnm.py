# this code will successfully rename the old file to the new file; perhaps I should make this a functions?
# The features of the line will have to echo the thrombocalc line for now, I can do this
import shutil
import datetime

# I made this to take a given filename, which I've imaginatively called filename, and to append the time and date to it, in the format
# HHMMSSDDMMYY and then to place that in front of ".png".... Okay, I'm going to do something crazy.
#
def pdf_namer(filename):
    t = '{0:%H%M%S%d%m%y}'.format(datetime.datetime.now())
    a = '.pdf'
    return (filename + t + a)

def csv_time_namer(filename):
    t = '{0:%H%M%S%d%m%y}'.format(datetime.datetime.now())
    b = '.csv'
    return (filename + t + b)




original = r'C:\Users\gavin\OneDrive\Documents\GitHub\UCDPA_gavinhoran\RXPdfManip\rename\oldPdf\DBPrint Job (9).pdf'
target = r'C:\Users\gavin\OneDrive\Documents\GitHub\UCDPA_gavinhoran\RXPdfManip\rename\NewPdf\newFileName.pdf'
target2 = r'C:\Users\gavin\OneDrive\Documents\GitHub\UCDPA_gavinhoran\RXPdfManip\rename\ManipPdf\DBPrint Job (9) sent.pdf'

shutil.copyfile(original, target)

shutil.copyfile(original, target2)