# adopted from https://stackoverflow.com/a/152454

import win32con
import win32gui

def isRealWindow(hWnd):
    '''Return True iff given window is a real Windows application window.'''
    if not win32gui.IsWindowVisible(hWnd):
        return False
    if win32gui.GetParent(hWnd) != 0:
        return False
    hasNoOwner = win32gui.GetWindow(hWnd, win32con.GW_OWNER) == 0
    lExStyle = win32gui.GetWindowLong(hWnd, win32con.GWL_EXSTYLE)
    if (((lExStyle & win32con.WS_EX_TOOLWINDOW) == 0 and hasNoOwner)
      or ((lExStyle & win32con.WS_EX_APPWINDOW != 0) and not hasNoOwner)):
        if win32gui.GetWindowText(hWnd):
            return True
    return False


def getWindowSizes(appName):
    '''
    Return a list of tuples (handler, (width, height)) for each real window.
    '''

    def callback(hWnd, windows):
        if not isRealWindow(hWnd):
            return
        rect = win32gui.GetWindowRect(hWnd)
        name = win32gui.GetWindowText(hWnd)
        placement = win32gui.GetWindowPlacement(hWnd)
        windows.append((name, (placement[4][0], placement[4][1]), (rect[2] - rect[0], rect[3] - rect[1]), hWnd))
    windows = []
    win32gui.EnumWindows(callback, windows)

    return [d for d in windows if(d[0] == appName)]

