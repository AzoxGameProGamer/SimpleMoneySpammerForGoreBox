import pyautogui
import time
import keyboard

print("To make it work go to GoreBox and open tab menu, and then click on money and then put 1 there and then drop it or don't drop it and then just press the Insert and enjoy")

def teleport_and_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def main():
    while True:
        if keyboard.is_pressed('insert'):
            keyboard.press_and_release('tab')
            time.sleep(0.1)
            teleport_and_click(1715, 212)
            time.sleep(0.1)
            teleport_and_click(958, 720)
            time.sleep(0.1)
        else:
            continue

if __name__ == "__main__":
    main()