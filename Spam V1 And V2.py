import pyautogui as pg
import time
import webbrowser
from tkinter import *

def Web():
    webbrowser.open("https://bit.ly/3pMANuV")

def kk1():
    pg.keyDown('alt')
    pg.press('tab')
    #pg.press('tab')
    pg.keyUp('alt')

def start1():
    pg.press('I')
    
    pg.press('space')
    
    pg.press('s')
    pg.press('p')
    pg.press('a')
    pg.press('m')
    
    pg.press('enter')
    time.sleep(0.8)
    
def start2():
    pg.hotkey('I','space','s','p','a','m')


def start_V1_50():
    
    kk1()
    
    count = 0
    while (count < 50 ):
        count = count +1
        start1()

        pg.FAILSAFE = 0
        

def start_v1_100M():
    
    kk1()
    
    count = 0
    while (count < 10000000000000000000000 ):
        count = count +1
        start1()

        pg.FAILSAFE = 0

def start_V2_50():
    
    kk1()
    
    count = 0
    while (count < 50 ):
        count = count +1
        #print("loop")
        start2()
        
        pg.press('enter')
        time.sleep(0.5)

        pg.FAILSAFE = 0

def start_v2_100M():
    
    kk1()
    
    count = 0
    while (count < 10000000000000000000000 ):
        count = count +1
        #print("loop")m
        start2()
        
        pg.press('enter')
        time.sleep(0.5)

        pg.FAILSAFE = 0

def time1():
    time.sleep(0.5)


def about1():
    root1 = Tk()
    root1.title('About')
    root1.geometry('300x230')

    label1 = Label(master=root1,text='โปรแกรม Verson V1 และ V2' ,font=50)
    label1.pack()

    label2 = Label(master=root1,text='ผู้สร้างคือ KNHDSA TV ',font=50)
    label2.pack()

    label3 = Label(master=root1,text= 'ติดตามได้ใน Facebook และ YouTube',font=50)
    label3.pack()

    Button1 = Button(master=root1, text= 'เว็ปเจ้าของคนสร้าง' , command=Web)
    Button1.pack()

    root1.mainloop()

def knhdsa1():
    root = Tk()
    root.title('โปรแกรม Spam V1-2')
    root.geometry("300x230")

    myMenu = Menu()
    root.config(menu=myMenu)

    Menu1 = Menu()
    Menu1.add_command(label="เว็ป" , command=Web)
    Menu1.add_command(label="เกียวกับ" , command=about1)

    myMenu.add_cascade(label="Menu 1" , menu=Menu1)


    label = Label(master=root, text= 'โปรแกรม Spam Free จากคนไทย', font=30)
    label.pack()

    button = Button(master=root, text='Spam V1 50ครั้ง', font=50 , command=start_V1_50)
    button.pack()
    
    button = Button(master=root, text='Spam V1 100Mครั้ง', font=50 , command=start_v1_100M)
    button.pack()
    
    button = Button(master=root, text='Spam V2 50ครั้ง', font=50 , command=start_V2_50)
    button.pack()
    
    button = Button(master=root, text='Spam V2 100Mครั้ง', font=50 , command=start_v2_100M)
    button.pack()

    root.mainloop()

knhdsa1()

pg.FAILSAFE = 0