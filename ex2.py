import pyautogui
import time

time.sleep(6)#include <iostream>
#include <vector>
#include <queue>

with open('code.txt','r')as f:
    lines = f.readlines()
    for line in lines:
        pyautogui.write(line.lstrip())