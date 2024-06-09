import os
from deep_translator import GoogleTranslator
import PyPDF2
import tkinter as tk 

##root = tk.Tk()
##
##label = tk.Label(root, text="Hello, Tkinter!")
##label.pack()
##
##button = tk.Button(root, text="Click Me!", command=click_function)
##button.pack()
##root.mainloop()
filename = input("Enter filename:")
df_file = open(filename,"rb")
pdf_reader = PyPDF2.PdfReader(filename)
num_pages= len(pdf_reader.pages)
for page_num in range(num_pages):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    translated_text = GoogleTranslator(source="en",target="hi").translate(text)
    with open("file1.pdf","a") as file:
        file.write(translated_text)
