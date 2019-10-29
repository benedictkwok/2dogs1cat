import pyautogui
import time
print('Press Contrl-C to quit')
try:
    while True:
        x, y = pyautogui.position()
        positionStr='X: ' +str(x).rjust(4) + ' Y: '+str(y).rjust(4)
        print(positionStr)
        time.sleep(120)
        new_x, new_y = pyautogui.position()

        if x==new_x:
            pyautogui.click(500,100)
            pyautogui.typewrite('1')
            time.sleep(1)

except KeyboardInterrupt:
    print('\nBye!')
