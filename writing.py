# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:23:57 2018

@author: Hp
"""

import time, pyautogui
time.sleep(5)
x, y=pyautogui.position()
pyautogui.click(x,y)
pyautogui.typewrite('Hello World!', 0.50)