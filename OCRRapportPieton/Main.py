from os import write
from PIL.Image import new
from FindwordLocalisation import *
from OCR1 import *
from OCR2 import *
import re
first_x = 626
first_y = 480
x_decallage = 650
y_decallage = 130
word = "Panier"
x,y,w,h =find_effetswords(word, first_x, first_y, 650, 130, 1)
new_x = first_x + x
new_y = first_y + y + 25
ocr_result2 = screenValues2(new_x, new_y , 60, 100 ,1)
ocr_result2=ocr_result2.replace("\n\x0c","")
with open("Liste{}.txt".format(word),"w") as f:
    f.write(ocr_result2)