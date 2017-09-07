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
diabloKeys = ['1', '2', '3', '4', 'q', 'left', 'right']
gameName = "Blizzard App"
last_time = time.time()


# d3Window = getWindowSizes("Diablo III")
d3Window = getWindowSizes("Blizzard App")

# win32gui.SetForegroundWindow(d3Window[0][3])
box = (d3Window[0][1][0], d3Window[0][1][1],
       d3Window[0][1][0] + d3Window[0][2][0],
       d3Window[0][1][1] + d3Window[0][2][1])

center = ((box[0] + box[2])/2, (box[1] + box[3])/2)

keysPressed = []
clicks = []

k_counter = 0
m_counter = 0


def save_screenshot(gameName, x, y, key, box):

    center = ((box[0] + box[2])/2, (box[1] + box[3])/2)
    timeStamp = str(int(time.time()))

    rel_x = (x - center[0]) / (box[2] - box[0])
    rel_y = (y - center[1]) / (box[3] - box[1])

    screen = np.array(ImageGrab.grab(bbox=box))
    scipy.misc.imsave("../screens/" + gameName + "_" + str(float(rel_x)) + "_" + str(float(rel_y)) + "_" + str(key) +
                      "_" + str(int(timeStamp)) + ".jpg",
                      screen)
    print("A")



def on_press(key):
    key_press = key.char
    x, y = pyautogui.position()
    if key_press in diabloKeys:
        print(key)
        save_screenshot(gameName, x, y, key, box)


def on_click(x, y, button, pressed):
    if d3Window[0][1][0] <= x <= d3Window[0][1][0] + d3Window[0][2][0] and \
            d3Window[0][1][1] <= y <= d3Window[0][1][1] + d3Window[0][2][1] and pressed:
        if button == "Button.left":
            key = 'left'
        else:
            key = 'right'
        save_screenshot(gameName, x, y, key, box)


k_listener = keyboardListener(on_press=on_press)
m_listener = mouseListener(on_click=on_click)

for i in range(3):
    print(3-i)
    time.sleep(.5)
print("Starting to listen....")


m_listener.start()
k_listener.start()

time.sleep(10)

m_listener.stop()
k_listener.stop()
print("stopped")
