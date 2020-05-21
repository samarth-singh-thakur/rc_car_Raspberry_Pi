import RPi.GPIO as GPIO          
from time import sleep
import time



pin1 = 21
pin2 = 20
pin3 = 16
pin4 = 26
TRIG = 27                                  #Associate pin 23 to TRIG
ECHO = 17  



GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)
GPIO.setup(pin4,GPIO.OUT)
GPIO.output(pin1,GPIO.LOW)
GPIO.output(pin2,GPIO.LOW)
GPIO.output(pin3,GPIO.LOW)
GPIO.output(pin4,GPIO.LOW)
GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in



def forward():
    print("forward")
    GPIO.output(pin1,GPIO.HIGH) 
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin4,GPIO.LOW)
    return 0



def back():
    print("back")
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.HIGH)
    return 0
    
def left():
    print("left")
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin4,GPIO.HIGH)
    return 0


def right():
    print("right")
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.HIGH)
    GPIO.output(pin3,GPIO.HIGH)
    GPIO.output(pin4,GPIO.LOW)
    return 0

def stop():
    print("stop")
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin3,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)         
    GPIO.output(pin4,GPIO.LOW)
    return 0

while True:

    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    sleep(0.1)                     #Delay of 2 seconds
    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
            pulse_start = time.time()     
    while GPIO.input(ECHO)==1:   
            pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150 
    distance = round(distance, 2) 
    print(distance)
    
    if distance>15:
        forward()
    else:
        stop()