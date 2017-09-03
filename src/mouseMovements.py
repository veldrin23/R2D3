import pandas as pd
import pyautogui
import time
import csv

mouseLocs = []
i = 0
while i < 10000:
    if i % 1000 == 0:
        print(i)
    time.sleep(.1)
    mouseLocs.append([i, time.time(), pyautogui.position()[0], pyautogui.position()[1]])
    i += 1


print(mouseLocs)


pd.DataFrame.to_csv(pd.DataFrame(mouseLocs), 'mouselocs.csv')


