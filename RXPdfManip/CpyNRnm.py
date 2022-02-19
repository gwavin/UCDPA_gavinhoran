# this code will successfully rename the old file to the new file; perhaps I should make this a functions?
# The features of the line will have to echo the thrombocalc line for now, I can do this


import shutil

original = r'C:\Users\gavin\OneDrive\Documents\GitHub\UCDPA_gavinhoran\RXPdfManip\rename\oldPdf\DBPrint Job (9).pdf'
target = r'C:\Users\gavin\OneDrive\Documents\GitHub\UCDPA_gavinhoran\RXPdfManip\rename\NewPdf\newFileName.pdf'
target2 = r'C:\Users\gavin\OneDrive\Documents\GitHub\UCDPA_gavinhoran\RXPdfManip\rename\ManipPdf\DBPrint Job (9) sent.pdf'

shutil.copyfile(original, target)

shutil.copyfile(original, target2)