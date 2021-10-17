
import os, sys
import re
import pdfplumber

with pdfplumber.open('A_Handbook_of_Acronyms_and_Initialisms.pdf') as pdf:
    # skip preface and last pages
    for page in pdf.pages[8:-5]:
        lines = page.extract_text().split('\n')
        for line in lines:
            if re.match(r'^[A-Z]+ [A-Z][a-z].+$', line):
                print(line.split()[0])
                

