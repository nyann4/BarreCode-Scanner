import pyautogui 
from PIL import Image  
import pytesseract  
import cv2
import numpy as np
from pathlib import Path

def screenValues(A, B, C, D, E):
   #Selectionne le chemin 
   root_path = Path(".").resolve()

   down = B
   i=0

   tmp_dir = root_path / "ALLRESULT"
   try:
      tmp_dir.mkdir(parents=True)
   except:
      pass
   while i != E:
      pprice = str(tmp_dir / "thresholdimage.png")
      img = takeScreen(A, down, C, D)
    #   img.save(r''+str(root_path)+'\screenshot'+str(i)+'.png')
      threshold(img, pprice, 85)
      down += 40
      i += 1

def takeScreen(posX, posY, pixelX, pixelY):
    screen = pyautogui.screenshot(region=(posX, posY, pixelX, pixelY))
    return screen

def readScreen(screen):
    print(pytesseract.image_to_string(screen, config='digits'))

def filterImage(screen):
    cv2img = np.array(img)
    cv2.imshow('original', cv2img)
    return screen

def threshold(processed, path, valueTreshold1):
   processed.save(path)
   processed = cv2.imread(path)
   processed = cv2.cvtColor(processed, cv2.COLOR_RGB2GRAY)
#    processed = cv2.threshold(processed, valueTreshold1, 255, cv2.THRESH_OTSU)[1]  
#    processed = cv2.threshold(processed, valueTreshold1, 255, cv2.THRESH_BINARY_INV)[1]  
   cv2.imwrite(path, processed)
   processed = Image.open(path)
   ocr_result = pytesseract.image_to_string(processed)