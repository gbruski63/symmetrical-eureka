from RPi import GPIO #default copied from https://github.com/modmypi/Rotary-Encoder/blob/master/rotary_encoder.py
from time import sleep #imports 

clk = 27
dt = 22 #these 3 declarations set up the gpio pins which will be used, clk and dt for the rotary encoder, and the list is the gpio for the pins from lowest to highest 'power'
mygpios = [12,25,18,20,21]
indexmultiplier = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #setting up r. encoder
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0 #default value for r.encoder. One rotation is 40 (clockwise) or -40 (C.C.)
clkLastState = GPIO.input(clk) #default position (pos=0) for r.encoder

try:

        while True:
                clkState = GPIO.input(clk)
                dtState = GPIO.input(dt) #assigning current states of
                if clkState != clkLastState: #determining rotation
                        if dtState != clkState:
                                counter -= 1
                        else: #editing the counter variable based on rotation
                                counter += 1
                        print(counter)
                        
                gpioindex = 0
                for p in mygpios: #checking if the rotation of the knob is enough to change the state of the gpio pin of each LED
                        if counter >= (gpioindex * indexmultiplier):
                                GPIO.setup(mygpios[gpioindex], GPIO.OUT)
                                GPIO.setup(mygpios[gpioindex], GPIO.HIGH) #turns on led
                        elif counter < (gpioindex * indexmultiplier):
                                GPIO.setup(mygpios[gpioindex], GPIO.LOW) #turns off led
                                
                clkLastState = clkState #updates the state of the clk internal contact of the r.encoder
                sleep(0.01)
finally:
        GPIO.cleanup()
