import time
import pyautogui

def sendCommand(command, x, y):
	if(command == "click" or command == "rightClick" or command == 'attack'):
		if(command == "click"):
			pyautogui.keyDown("ctrl")
			pyautogui.click(x, y, button="left")
			pyautogui.keyUp("ctrl")
		if(command == "rightClick"):
			pyautogui.click(x, y, button="right")
		else:
			pyautogui.keyDown("shift")
			pyautogui.click(x, y, button="left")
			pyautogui.keyUp("shift")

	else:
		print("move and button")
		pyautogui.moveTo(x,y)
		pyautogui.keyDown(command)
		time.sleep(.01)
		pyautogui.keyUp(command)