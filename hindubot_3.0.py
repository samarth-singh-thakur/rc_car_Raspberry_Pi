from pynput.keyboard import Key, Listener
import RPi.GPIO as GPIO    

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
    print('f')

    


def back():

    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.HIGH)
    print('s')
    
    
def left():
    
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.HIGH)
    print('a')

     

def right():

    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin4,GPIO.LOW)
    print("d")
    
    
    

def stop():
    
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)         
    GPIO.output(pin4,GPIO.LOW)

def on_press(key):






    if key.char == 'w':
        forward()
    if key.char == 's':
        back()
    if key.char == 'a':
        left()
    if key.char == 'd':
        right()

def on_release(key):

    stop()
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

