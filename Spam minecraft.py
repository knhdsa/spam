import pyautogui as pg
import time as tm

gg0_1 = input('keyboard all available (Y or N) :  ')

if gg0_1 =='Y' or gg0_1 =='y':
    tm.sleep(0.5)
    print('Oh Ok')
    tm.sleep(1)
    print(pg.KEYBOARD_KEYS)
    
else : 
    tm.sleep(0.5)
    print('Ok')

import webbrowser
import tkinter as tk

gg1 = input("Spam Key KB : ")
gg2 = int(input("quantity :  "))
gg3 = (gg2+1)
gg4 = float(input("Time Sleep : ") )
gg5 = input("Key Chat : ")

def kk1():
    pg.keyDown('alt')
    pg.press('tab')
    #pg.press('tab')
    pg.keyUp('alt')
    

def start1():
    kk1()
    for i in range(gg2):
        pg.keyDown(gg5)
        pg.keyUp(gg5)
        tm.sleep(gg4)
        pg.write(gg1)
        pg.press('enter')

start1()

pg.FAILSAFE = 0

gg0_2 = input('Open Youtube KNHDSA TV (Y OR N) : ')

if gg0_2 =='Y' or gg0_2 =='y':
    tm.sleep(0.5)
    print('OK')
    tm.sleep(1)
    webbrowser.open("https://www.youtube.com/channel/UCZC3tz_NJf9-s1jBrp-wafw")

tm.sleep(20)