import pyautogui as q
import time 

q.click(1114, 37, 1)
q.typewrite('nfl.com\n', .1)
q.moveTo(1098, 298, 1)
q.scroll(-2000)
time.sleep(1) 
q.click(1098, 298, 1)
time.sleep(2)
q.scroll(-1000)
q.moveTo(1155, 422, 1)
q.click(1155, 422, 1) 

