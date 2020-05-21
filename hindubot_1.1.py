import RPi.GPIO as GPIO          
from time import sleep
import time
# import curses
import curses
# import msvcrthi
import tty
import sys
import termios
orig_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
mov = 0

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

    GPIO.output(pin1,GPIO.HIGH) 
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin4,GPIO.LOW)

    stop()


def back():

    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.HIGH)
    stop()
    
def left():
    
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.HIGH)
    stop()  

def right():

    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin4,GPIO.LOW)
    
    stop()
    

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
    # while True:

    #     char = screen.getch()

    #     if char == ord('w'):
    #         forward()
    #     if char == ord('s'):
    #         back()
    #     if char == ord('a'):
    #         right()
    #     if char == ord('d'):
    #         left()
    #     if char == ord('q'):
    #         stop()
    #     if char == ord('e'):
    #         dance()
    while mov != chr(27): # ESC
        mov=sys.stdin.read(1)[0]
        # print("You pressed", x)
        if(mov == 'w'):
            forward()

        elif(mov == 's'):
            back()

        elif(mov == 'd'):
            right()

        elif(mov == 'a'):
            left()

        elif(mov == 'q'):
            stop()



finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)  


    
    
    