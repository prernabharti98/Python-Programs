# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:07:59 2018

@author: Hp
"""

import pyperclip
numbers=''
for i in range(200):
    numbers=numbers + str(i) + '\n'

pyperclip.copy(numbers)