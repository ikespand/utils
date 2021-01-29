# -*- coding: utf-8 -*-
"""
Scirpt to merge pdf files from given pdf or images.

This is a temporary script file.
"""

from PyPDF2 import PdfFileMerger
import glob

# Provide a list of pdf files which needed to be merged
pdfs = ['1-PhD_Degree.pdf', 
        '2-Master_degree_with_grades.pdf', 
        '3-Bachelor_degree_with_grades.pdf']

# Merge degree
merger = PdfFileMerger()

#for pdf in pdfs:
#    merger.append(pdf)

merger.append(pdfs[0])
merger.append(pdfs[1], pages=(0, 1)) # Select specific pages
merger.append(pdfs[2], pages=(0, 1)) # Select specific pages

merger.write("DegreeCertificates.pdf")
merger.close()

# %% Reduce image dpi so that it can be merged with other similiar size pdf
from PIL import Image

images = glob.glob('btech_marksheets/*.jpg')

for image in images:
    img = Image.open(image)
    img.save(image,quality=15, dpi=(300,300))


# %% Merge above images and save as pdf
import img2pdf
images = glob.glob('btech_marksheets/*.jpg')
images.sort()

#  Save as images as pdf
with open("btech_marksheets.pdf","wb") as f:
    f.write(img2pdf.convert(images))

# Merge above pdf with 1 other pdf (Transcripts)
pdfs = ['2-Master_degree_with_grades.pdf', 
        'btech_marksheets.pdf']

merger = PdfFileMerger()
merger.append(pdfs[0], pages=(1, 3))
merger.append(pdfs[1])

merger.write("Transcripts.pdf")
merger.close()
