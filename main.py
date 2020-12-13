from pymouse import PyMouse
import PyHook3
import pythoncom

KEY_START = "F8"
KEY_STOP = "F7"


def startMockMouseClick():
    print("开始 mock")
    x, y = m.position()
    m.press(x, y, button=2)


def stopMockMouseClick():
    print("停止 mock")
    x, y = m.position()
    m.release(x, y, button=2)


def onKeyboardEvent(event):
    if event.Key == KEY_START:
        startMockMouseClick()
    elif event.Key == KEY_STOP:
        stopMockMouseClick()
    return True

def main():
    hm = PyHook3.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()


if __name__ == '__main__':
    m = PyMouse()
    main()
