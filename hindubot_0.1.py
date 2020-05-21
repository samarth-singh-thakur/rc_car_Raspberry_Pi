import RPi.GPIO as GPIO          
from time import sleep

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
    print("forward")
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin4,GPIO.LOW)


def back():
    print("back")
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin4,GPIO.HIGH)
    
def right():
    print("right")
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.HIGH)

def left():
    print("left")
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin4,GPIO.LOW)

def stop():
    
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin4,GPIO.LOW)
    
while True:
    x = input()
    if x == 'w':
        forward()
    if x == 's':
        back()
    if x == 'a':
        right()
    if x == 'd':
        left()
    if x == 'q':
        stop()
        
    sleep(1)
    stop()
    
        
    
    
    
    