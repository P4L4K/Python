import random

import pyautogui as pg
import time
time.sleep(8)
for i in range(500):
    pg.write("..")
    pg.press("enter", interval=0.0000000000000000001)  # Add a slight delay
    time.sleep(0.2) 
print("done")    
