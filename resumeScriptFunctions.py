import tkinter
from tkinter import filedialog
import spacy
from spacypdfreader import pdf_reader
from spacy import displacy
import webbrowser
import os
from spacy.matcher import Matcher
import re
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
import re
from spacy.language import Language
import json


nlp = spacy.load("en_core_web_lg")

with open("languages.json", "r") as f:
    lang_data = json.load(f)
    lang_data_list = ''.join(f)
    
lang_doc=nlp(lang_data_list)


ruler = nlp.add_pipe("entity_ruler")
patterns = [
                {"label": "PROGRAMMING LANGUAGE", "pattern": lang} for lang in lang_doc
            ]


#find resume name from resume 
def get_resume_name(doc):
    for ent in doc.ents:
        if ent.label_ =="PERSON":
            break
    print(ent)
    

def get_resume_email(doc):    
    resume_email=""
    matcher = Matcher(nlp.vocab)
    pattern = [{"LIKE_EMAIL": True}]
    matcher.add("EMAIL_ADDRESS", [pattern])
    for token in doc:
        matches = matcher(doc)
    print (nlp.vocab[matches[0][0]].text) #tuple [(match id, start, stop)] is accessing the 1st array 1st element 
    print(doc[matches[0][1]:matches[0][2]].text) #1st array start and stop 




def convert_lang_label(doc):
    matcher = Matcher(nlp.vocab)

    matcher.add("PROGRAMMING_LANGUAGE_PATTERN", patterns)
    for ent in doc.ents:
        print(ent.text, ent.label_)
 




'''
html = displacy.render(doc_res, style="ent")

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
