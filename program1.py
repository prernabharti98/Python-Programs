# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:42:01 2018

@author: Hp
"""

import pyautogui
for i in range(10):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)