import eel
import pyautogui

eel.init('views')
eel.start(
    'templates/index.html',
    size = pyautogui.size()
)