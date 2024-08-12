import cv2
import pytesseract
from OCR1 import  *
from pytesseract import Output

def find_effetswords(word, A, B, C, D, E):
    screenValues(A, B, C, D, E)
    img = cv2.imread(r'C:\Users\yannf\OneDrive\SWSetup\Bureau\PROJET5\OCRRapportPieton\ALLRESULT\thresholdimage.png')

    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        if(d['text'][i] == "Panier") :
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            return x,y,w,h
            

    # cv2.imshow('img', img)
    # cv2.waitKey(0)