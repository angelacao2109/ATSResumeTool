
import PyPDF2
from pdfreader import PDFDocument
import nltk
import os 
import tkinter 
from tkinter import filedialog


root = tkinter.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print(file_path)
#print(os.path.abspath(file_path))

file_name = open(file_path,"rb")
doc = PDFDocument(file_name) 


# find font type
page = next(doc.pages())
sorted(page.Resources.Font.keys())

print((page.Resources.Font.keys()))

for font in page.Resources.Font.keys():
    print(page.Resources.Font[font].BaseFont)


reader = PyPDF2.PdfReader(file_path)

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page
#print(reader.pages[0].extract_text())

resume_text=reader.pages[0].extract_text()

keyword_headers=["EDUCATION","SKILLS","EXPERIENCE","PROJECTS","CERTIFICATIONS"]

for keyword in keyword_headers:
    result=resume_text.find(keyword)
    if result ==-1:
        print(keyword + " is not found")
    else:
        print(keyword+ " is found at index "+str(result))


    




