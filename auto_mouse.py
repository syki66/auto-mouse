from tkinter import *
import time
import pyautogui
import threading
import keyboard

resolution = 100

posArray = []

delay = 1 / resolution
pyautogui.PAUSE = delay

pyautogui.FAILSAFE = False

root = Tk()
root.title("automouse v0.1.0")
root.geometry("250x500")

inputTime = Entry(root)
inputTime.pack()
inputTime.insert(0, 10)

def btnClick():
    time.sleep(1)
    initTime = inputTime.get()
    if initTime.isnumeric():
        initTime = int(initTime)
        btn['state'] = DISABLED
        for i in range(initTime * resolution):
            pos = (pyautogui.position()[0], pyautogui.position()[1])
            posArray.append(pos)

            notice['text'] = f'{round(initTime - (i * delay), 1)}s'
            root.update()
            time.sleep( delay )

        notice['text'] = "PRESS Q TO EXIT"
        root.update()

        threading.Thread(target=moveMouse).start()
    else:
        notice['text'] = "enter only numbers"
def moveMouse():
    end = False
    while(not end):
        for i in range(len(posArray)):
            pyautogui.moveTo(posArray[i])
            if keyboard.is_pressed("q"):
                end = True
    posArray.clear()
    btn['state'] = NORMAL

btn = Button(root, text="start", command=btnClick)
btn.pack()

notice = Label(root, text="write second")
notice.pack()

root.mainloop()