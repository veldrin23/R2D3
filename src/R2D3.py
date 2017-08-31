from PIL import ImageGrab
import time
from findGameWindow import *
from processImage import *
from sendCommand import *
import sys
import pyautogui
import random


gameName = sys.argv[0]


last_time = time.time()


d3Window = getWindowSizes("Diablo III")
# print(d3Window)
# win32gui.SetForegroundWindow(d3Window[0][3])
box = (d3Window[0][1][0], d3Window[0][1][1],
       d3Window[0][1][0] + d3Window[0][2][0],
       d3Window[0][1][1] + d3Window[0][2][1])

center = ((2 * d3Window[0][1][0] + d3Window[0][2][0])/2, (d3Window[0][1][1] * 2 +  d3Window[0][2][1])/2)

while True:
    screen = np.array(ImageGrab.grab(bbox=box))
    new_screen = mag_thresh(screen)
    print("Loop took {} seconds".format(time.time() - last_time))

    last_time = time.time()
    cv2.imshow("window", new_screen)

    if(cv2.waitKey(25) & 0xFF == ord('q')):
       cv2.destroyAllWindows()
       break



    if(random.uniform(0,1) < .075):
      sendCommand("attack", x = center[0] + random.uniform(-50,50), y = center[1] + random.uniform(-50,50))

    pyautogui.moveTo(center)

    
