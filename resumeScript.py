import tkinter
from tkinter import filedialog
import spacy
from spacypdfreader import pdf_reader
from spacy import displacy
import webbrowser
import os
from spacy.matcher import Matcher
from spacy.lang.en import English
import re
from spacy.pipeline import EntityRuler
import resumeScriptFunctions
from spellchecker import SpellChecker
from textblob import TextBlob


nlp = spacy.load("en_core_web_lg")

#Initialize Tkinter Root Window and create Root Object
root = tkinter.Tk()
#Hide the Root Window
root.withdraw()

file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
print(f"Selected file: {file_path}")
doc = pdf_reader(file_path, nlp)

remove_ws = " ".join(doc.text.split())
#print(remove_ws)

doc2 = nlp(remove_ws)

resumeScriptFunctions.get_resume_name(doc2)






#This is to have a HTML visual of the doc with labels, POS, etc
#Uncomment to use it
'''
html = displacy.render(doc2, style="ent")

output_path = "dependency_parse.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

# Check if the file exists and is not empty
if os.path.isfile(output_path):
    print(f"File {output_path} created successfully.")
    if os.path.getsize(output_path) > 0:
        print(f"File {output_path} is not empty, opening in web browser.")
        # Open the HTML file in the default web browser
        webbrowser.open(f"file://{os.path.realpath(output_path)}")
    else:
        print(f"File {output_path} is empty.")
else:
    print(f"Failed to create file {output_path}.")
  

'''