##Documentation
# name : Yohjit Chopra
# Roll No. 2110994798
# Task 5.2C
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


win = Tk()
win.title("LED Toggler")
win.geometry("380x200")
win.configure(background = "pink")
Font = tkinter.font.Font(family='Aerial', size = 16, weight = "bold")


led = LED(14)
led_red = LED(15)
led_white = LED(18)

value = IntVar()


def ledtoggle():
    value1 = value.get()
    if value1 == 1:
        led.on()
        led_red.off()
        led_white.off()
        ledbutton1["text"]="GREEN: ON"
        ledbutton2["text"]="RED"
        ledbutton3["text"]="YELLOW"
    elif value1 == 2:
        led.off()
        led_red.on()
        led_white.off()
        ledbutton2["text"]="RED: ON"
        ledbutton1["text"]="GREEN"
        ledbutton3["text"]="YELLOW"
    elif value1 == 3:
        led.off()
        led_red.off()
        led_white.on()
        ledbutton3["text"]="YELLOW: ON"
        ledbutton2["text"]="RED"
        ledbutton1["text"]="GREEN"
    else :
        led.off()
        led_red.off()
        led_white.off()
        

def close():
    win.destroy()
    GPIO.cleanup()
    

    
title_text = tkinter.Label(win, text = "Choose the color of LED you want to switch on", justify="center", bg = "pink", padx = 30)
#title_text.place(x = 50 , y = 0 )
title_text.grid(row = 1, column = 1)

ledbutton1 = Radiobutton(win, text = "GREEN",indicatoron = 0, font = Font, variable = value, value = 1, command = ledtoggle, bg = 'green', height = 1, width = 12, border = 2)
ledbutton1.grid(row = 2, column = 1 )

ledbutton2 = Radiobutton(win, text = "RED",indicatoron = 0, font = Font, variable = value, value = 2, command = ledtoggle, bg = 'red', height = 1, width = 12, border = 2)
#ledbutton2.place(x = 20, y = 60 )
ledbutton2.grid(row = 3, column = 1 )

ledbutton3 = Radiobutton(win, text = "YELLOW",indicatoron = 0, font = Font, variable = value, value = 3, command = ledtoggle, bg = 'yellow', height = 1, width = 12, border = 2)
#ledbutton3.place(x = 280, y = 60 )
ledbutton3.grid(row = 4, column = 1 )

closebutton = Radiobutton(win, text = "EXIT",indicatoron = 0, font = Font,command = close, bg = 'black', height = 1, width = 5, border = 4, cursor = "pirate")
# closebutton.place(x = 175, y = 90 )
closebutton.grid(row = 5, column = 1)
