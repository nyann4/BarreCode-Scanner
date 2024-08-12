import pyautogui 
from PIL import Image  
import pytesseract  
import cv2
from pathlib import Path
import re

def screenValues2(A, B, C, D, E):
    #Selectionne le chemin 
    root_path = Path(".").resolve()

    down = B
    i=0

    tmp_dir = root_path / "screen modifier"
    try:
      tmp_dir.mkdir(parents=True)
    except:
      pass
    while i != E:
        pprice = str(tmp_dir / "tmp-price{}.png".format(i))
        img = takeScreen(A, down, C, D)
        ocr_result2 = threshold(img, pprice, 85, i)
        down += 40
        i += 1
        return ocr_result2


def takeScreen(posX, posY, pixelX, pixelY):
   screen = pyautogui.screenshot(region=(posX, posY, pixelX, pixelY))
   return screen

def threshold(processed, path, valueTreshold1, i):
   processed.save(path)
   processed = cv2.imread(path)
   processed = cv2.cvtColor(processed, cv2.COLOR_RGB2GRAY)
   # processed = cv2.threshold(processed, valueTreshold1, 100, cv2.THRESH_OTSU)[1] 
#    processed = cv2.threshold(processed ,55, 255, cv2.THRESH_BINARY)[1]
   # processed = cv2.adaptiveThreshold(processed, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 37, 1)[1]
   # processed = cv2.threshold(processed, valueTreshold1, 255, cv2.THRESH_BINARY_INV)[1]  
   cv2.imwrite(path, processed)
   processed = Image.open(path)
   ocr_result2 = pytesseract.image_to_string(processed)
   # ocr_result = pytesseract.image_to_string(processed, lang='eng',
   # config="--psm 10 --oem 3 -c tessedit_char_blacklist=&")
   # ocr_result = re.sub("[^0-9]","", ocr_result) 

   # print(list_value)
   return ocr_result2

   
# list_value = screenValues2(1010, 550, 60, 60, 1)
# print(list_value)
