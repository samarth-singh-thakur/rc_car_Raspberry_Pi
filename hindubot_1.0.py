import RPi.GPIO as GPIO          
from time import sleep
import time
import keyboard
import curses

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

pin1 = 21
pin2 = 20
pin3 = 16
pin4 = 26




GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)
GPIO.setup(pin4,GPIO.OUT)
GPIO.output(pin1,GPIO.LOW)
GPIO.output(pin2,GPIO.LOW)
GPIO.output(pin3,GPIO.LOW)
GPIO.output(pin4,GPIO.LOW)


def forward():
    while True:
        try: 
           if keyboard.is_pressed('w'):
                print("forward")
                GPIO.output(pin1,GPIO.HIGH) 
                GPIO.output(pin2,GPIO.LOW)
                GPIO.output(pin3,GPIO.HIGH)
                GPIO.output(pin4,GPIO.LOW)
        except:
            print("A")
            GPIO.output(pin1,GPIO.HIGH) 
            GPIO.output(pin2,GPIO.LOW)
            GPIO.output(pin3,GPIO.HIGH)
            GPIO.output(pin4,GPIO.LOW)
            break


def back():
    print("back")
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.HIGH)
    
def left():
    print("left")
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.HIGH)


def right():
    print("right")
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin4,GPIO.LOW)
     

def stop():
    
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)         
    GPIO.output(pin4,GPIO.LOW)
def dance():
    t1 = time.time()
    while(True):
        
        right()
        sleep(0.2)
        forward()
        sleep(0.2)
        left()
        sleep(0.2)
        forward()
        sleep(0.2)
        t2 = time.time()
        if (int(t2-t1) == 5):
            break

    
try:           
    while True:

        char = screen.getch()

        if char == ord('w'):
            forward()
            
            
        if char == ord('s'):
            back()
            
            
        if char == ord('a'):
            right()
            
            
        if char == ord('d'):
            left()
            
            
        if char == ord('q'):
            stop()
        if char == ord('e'):
            dance()

        sleep(0.2)
        stop()

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()


    
    
    