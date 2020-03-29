import pyautogui
import time

posArray = []

for i in range(1000):
    pos = (pyautogui.position()[0], pyautogui.position()[1])
    posArray.append(pos)
    
    print(pos)
    
while(True):
    for i in range(len(posArray)):
        pyautogui.moveTo(posArray[i])
