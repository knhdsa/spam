def Youtube_open():
    webbrowser.open("https://www.youtube.com/channel/UCZC3tz_NJf9-s1jBrp-wafw")

import pyautogui as pg
import time as tm
import webbrowser
import tkinter as tk

gg1 = input("Spam Key KB : ")
gg2 = int(input("quantity :  "))
gg3 = (gg2+1)
gg4 = float(input("Time Sleep : ") )

def kk1():
    pg.keyDown('alt')
    pg.press('tab')
    #pg.press('tab')
    pg.keyUp('alt')

def start1():
    kk1()
    for i in range(gg2):
        tm.sleep(gg4)
        pg.write(gg1)
        pg.press('enter')


def knhdsa1():
    window = tk.Tk()
    window.title('โปรแกรม Spam V3')
    window.minsize(width=300, height=300)


    title_label = tk.Label(master=window, text='โปรแกรม free 100%', font=100)
    title_label.pack()

    start_button = tk.Button(master=window, text='เริ่มการสแปม', font=100 , command=start1)
    start_button.pack()
    
    window.mainloop()

def start_knhdsa():
    knhdsa1()
    knhdsa2()

def knhdsa2():
    window = tk.Tk()
    window.title('เปิดอีกรอบ')
    window.minsize(width=300, height=300)

    title_label = tk.Label(master=window, text= '', font=100)
    title_label.pack()

    start_button = tk.Button(master=window, text='เปิดโปรแกรมอีกรอบ', font=100, command= start_knhdsa)
    start_button.pack()
    
    window.mainloop()

start_knhdsa()

pg.FAILSAFE = 0