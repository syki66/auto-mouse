import pyautogui
import time

posArray = []
inputTime = 200
mouseSpeed = 0.05

print("10초동안 마우스 입력받습니다.")

for i in range(inputTime):
    pos = (pyautogui.position()[0], pyautogui.position()[1])
    posArray.append(pos)
    
    time.sleep(mouseSpeed)
    
    print( round((200 - i) * mouseSpeed, 1), "s")

print("입력받은값 무한반복 시작.. \n 중단을 원할시 마우스를 왼쪽 상단 끝으로 보내세요.")

while(True):
    for i in range(len(posArray)):
        pyautogui.moveTo(posArray[i])
