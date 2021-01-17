import pyautogui
import mss
import numpy as np
import cv2
import time

game = {"top": 180, "left": 0, "width": 800, "height": 400}
kernel_open = np.ones((4,4), dtype=np.uint8)
kernel_dilate = np.ones((4,4), dtype=np.uint8)

pyautogui.press('space') # start game 
 
while True:
    with mss.mss() as sct:

        img = np.array(sct.grab(game))
        dino_box = img[50:400, 20:220]

        gray = cv2.cvtColor(dino_box, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_open)
 
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_DILATE, kernel_dilate)
        
        proc_midpoint = thresh.shape[1]//2
        
        proc = np.sum(thresh[:,-1])/thresh.shape[1]     
                     
        if proc < 444:                                                                
            pyautogui.press('space')
            time.sleep(0.15)
            pyautogui.press('down')
            
      
            
        
        