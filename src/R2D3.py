from PIL import ImageGrab
from src.findGameWindow import *
from src.processImage import *
from src.sendCommand import *
import sys
import scipy.misc
from pynput.keyboard import Listener as keyboardListener
from pynput.mouse import Listener as mouseListener
import pyautogui


# gameName = sys.argv[0]
diabloKeys = ['1', '2', '3', '4', 'q', 'click']
gameName = "Blizzard App"
last_time = time.time()


# d3Window = getWindowSizes("Diablo III")
d3Window = getWindowSizes("Blizzard App")

# win32gui.SetForegroundWindow(d3Window[0][3])
box = (d3Window[0][1][0], d3Window[0][1][1],
       d3Window[0][1][0] + d3Window[0][2][0],
       d3Window[0][1][1] + d3Window[0][2][1])

center = ((2 * d3Window[0][1][0] + d3Window[0][2][0])/2, (d3Window[0][1][1] * 2 + d3Window[0][2][1])/2)


keysPressed = []
clicks = []

k_counter = 0
m_counter = 0


def save_screenshot(gameName):
    timeStamp = str(int(time.time()))
    screen = np.array(ImageGrab.grab(bbox=box))
    scipy.misc.imsave("../screens/" + gameName + timeStamp + ".jpg", screen)



def on_press(key):
    key_press = key.char
    x, y = pyautogui.position()
    if key_press in diabloKeys:

        save_screenshot(gameName)
        keysPressed.append({x, y, key_press})
        if (int(time.time()) % 2) == 0:
            print("fok")
            with open("../" + gameName + "_log.txt", 'wb') as f:
                for k in keysPressed:
                    print(k)
                    f.write(k)
                    f.flush()
                f.close()

def on_click(x, y, button, pressed):
    if d3Window[0][1][0] <= x <= d3Window[0][1][0] + d3Window[0][2][0] and \
            d3Window[0][1][1] <= y <= d3Window[0][1][1] + d3Window[0][2][1] and pressed:
        # print(button)
        save_screenshot(gameName)


k_listener = keyboardListener(on_press=on_press)
m_listener = mouseListener(on_click=on_click)

for i in range(3):
    print(5-i)
    time.sleep(.5)
print("Starting to listen....")


m_listener.start()
k_listener.start()

time.sleep(15)

m_listener.stop()
k_listener.stop()
print("stopped")
