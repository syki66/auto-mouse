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
root.title("AutoMouse v0.1.0")
root.geometry("360x150")
root.resizable(False, False)

def btnClick():
    initTime = inputTime.get()
    if initTime.isnumeric():
        notice['text'] = "READY"
        root.update()
        time.sleep(2)

        initTime = int(initTime)
        btn['state'] = DISABLED
        for i in range(initTime * resolution):
            pos = (pyautogui.position()[0], pyautogui.position()[1])
            posArray.append(pos)

            notice['text'] = f'{round(initTime - (i * delay), 1)}s'
            root.update()
            time.sleep( delay )

        notice['text'] = "PRESS \"Q\" TO EXIT"
        root.update()

        threading.Thread(target=moveMouse).start()
    else:
        notice['text'] = "Enter only numbers"

def moveMouse():
    end = False
    while(not end):
        for i in range(len(posArray)):
            pyautogui.moveTo(posArray[i])
            if keyboard.is_pressed("q"):
                end = True
    posArray.clear()
    btn['state'] = NORMAL

inputTime = Entry(root, width=4, font=('Arial', 45, 'bold'), justify='center')
inputTime.insert(0, 10)

btn = Button(root, text="Start", command=btnClick, font=('Arial', 30, 'bold'))

notice = Label(root, text="Enter seconds")

notice.pack(side="bottom", fill="both", padx=10, pady=10)
inputTime.pack(side="left", padx=10, pady=10)
btn.pack(side="right", padx=10, pady=10)

root.mainloop()
