import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
led = 26 
GPIO.setup(26,GPIO.OUT)
state = 0
period  = 1.0 
while True: 
    GPIO.output(led,state)
    state = not(state):
    state = 1 
    time.sleep(period)

