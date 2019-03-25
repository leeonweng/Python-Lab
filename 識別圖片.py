# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:42:50 2018

@author: Home love
"""

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR/tesseract.exe'
image = Image.open("D:\Desktop\XXD.jpg")
text = pytesseract.image_to_string(image)
print(text)