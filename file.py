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
win.title("LED Toggler");
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
    elif value1 == 2:
        led.off()
        led_red.on()
        led_white.off()
    elif value1 == 3:
        led.off()
        led_red.off()
        led_white.on()
    else :
        led.off()
        led_red.off()
        led_white.off()
        

def close():
    win.destroy()
    GPIO.cleanup()
    
    
ledbutton1 = Radiobutton(win, text = "turn the green led on", font = Font, variable = value, value = 1, command = ledtoggle, bg = 'bisque2', height = 1, width = 24)
ledbutton1.grid(row = 0, column = 1)

ledbutton2 = Radiobutton(win, text = "turn the red led on", font = Font, variable = value, value = 2, command = ledtoggle, bg = 'bisque2', height = 1, width = 24)
ledbutton2.grid(row = 1, column = 1)

ledbutton3 = Radiobutton(win, text = "turn the white red led on", font = Font, variable = value, value = 3, command = ledtoggle, bg = 'bisque2', height = 1, width = 24)
ledbutton3.grid(row = 2, column = 1)

closebutton = Radiobutton(win, text = "EXIT", font = Font,command = close, bg = 'bisque2', height = 1, width = 24)
closebutton.grid(row = 3, column = 1)

