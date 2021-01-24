#pip install pyautogui 
import pyautogui
import time
pyautogui.FAILSAFE = False
while True:
   time.sleep(180)
   for i in range(0,50):
      pyautogui.moveTo(0, i * 5)
   for i in range(0,2):
      pyautogui.press('shift')