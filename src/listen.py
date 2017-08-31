import time
from pynput.keyboard import Key
from pynput.keyboard import Listener as keyboardListener
from pynput.mouse import Button
from pynput.mouse import Listener as mouseListener
from msvcrt import getch

diabloKeys = ['1', '2', '3', '4', 'q', 'click']

# keyboard
def on_press(key):
    print('{0} pressed'.format(
        key))
    return key

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# mouse
def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} {1} at {2}'.format(
        button,
        'Pressed' if pressed else 'Released',
        (x, y)))



print('asd')

while True:
    key = ord(getch())
    print(key)
    if key == 27: #ESC
        break
    elif key == 13: #Enter
        select()
    else:
        key = ord(getch())
        print(key)
