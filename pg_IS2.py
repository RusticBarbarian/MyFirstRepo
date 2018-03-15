import pyautogui as q
import time

q.hotkey('ctrl','winleft','d') 
q.hotkey('winleft')
q.typewrite('chrome\n',0.3)
q.hotkey('winleft','up')
q.typewrite ('youtube.com\n',0.3)
time.sleep(4) 
q.moveTo(862, 609, 1)
q.click()

