from gfxhat import lcd
from random import randrange
from gfxhat import backlight
import time

def clearlcd():
    lcd.clear()
    lcd.show()

def verticalline(x):  #I want to make it simple for user to get a vertical line by entering only one number, So I only chose one parameter.
    clearlcd()       #The purpose of intergrating the commands of 'lcd.clear()' and 'lcd.show()' is the same as choosing one parameter.
    y=0
    while y<=63:
        lcd.set_pixel(x,y,1)
        y+=1
    lcd.show()

def horizontalline(y):
    clearlcd()
    for x in range(0,128):
        lcd.set_pixel(x,y,1)
    lcd.show()


def staircase(x, y, w, h):
    clearlcd()
    while x+w<=127 and y+h<=63:
          for x in range(x,x+w):
              lcd.set_pixel(x,y,1)
          for y in range(y, y+h):
              lcd.set_pixel(x,y,1)
    lcd.show()


def randompixel():
    clearlcd()
    while True:
        x1 = randrange(0, 127)
        y1 = randrange(0, 63)
        lcd.set_pixel(x1,y1,1)
        time.sleep(0.5)
        lcd.show()
    #Use Ctrl+c to stop loop

def clearBacklight():
    backlight.set_all(0,0,0)
    backlight.show()








