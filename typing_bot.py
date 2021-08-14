import pyautogui as p
import time as t
t.sleep(2)
text = open("text.txt")
for each_line in text:
    p.typewrite(each_line)
