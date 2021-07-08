import pyautogui
from time import sleep

number_of_loops = int(input("Number of loops wished : "))
time_to_sleep = int(input("Craft time of your macro : "))
print("Leaving 5s time to put the ff window on top")
sleep(5)
print("Starting !")
button = pyautogui.center(pyautogui.locateOnScreen('fabricate.png'))
for i in range(0, number_of_loops):
    pyautogui.click(button)
    pyautogui.click(button)
    sleep(3)
    pyautogui.keyDown('ctrl')
    sleep(0.1)
    pyautogui.keyDown('&')
    sleep(0.1)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('&')
    sleep(time_to_sleep)
    print("Item :", i+1, " Crafted")
print("Macro Done !")
