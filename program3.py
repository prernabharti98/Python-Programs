# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 16:45:33 2018

@author: Hp
"""

import pyautogui, time
time.sleep(10)
pyautogui.click()
distance=200
while distance>0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance=distance-5
    pyautogui.dragRel(0, distance, duration=0.2)
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance=distance-5
    pyautogui.dragRel(0, -distance, duration=0.2)