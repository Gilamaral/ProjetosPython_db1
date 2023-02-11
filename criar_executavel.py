import pyautogui as pt
import time as t

pt.hotkey('winleft', 'r')
t.sleep(3)
pt.write('cmd')
pt.press('enter')
t.sleep(3)
pt.write('auto-py-to-exe')
pt.press('enter')



