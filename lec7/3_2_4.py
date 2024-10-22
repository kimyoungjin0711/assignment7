import RPi.GPIO as GPIO
import time

SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

previous = 0
current = 0
try:
    a=0
    b=0
    c=0
    d=0
    while True:
        current = GPIO.input(SW1)
        if previous == GPIO.LOW and current == GPIO.HIGH:
            a = a+1
            
            print("SW1 click %d"%a)
            
        previous = current
        time.sleep(0.1)    
    
        current = GPIO.input(SW2)
        if previous == GPIO.LOW and current == GPIO.HIGH:
            b = b+1
            
            print("SW2 click %d"%b)
            
        previous = current
        time.sleep(0.1)    

        current = GPIO.input(SW3)
        if previous == GPIO.LOW and current == GPIO.HIGH:
            c = c+1
            
            print("SW3 click %d"%c)
            
        previous = current
        time.sleep(0.1)    

        current = GPIO.input(SW4)
        if previous == GPIO.LOW and current == GPIO.HIGH:
            d = d+1
            
            print("SW4 click %d"%d)
            
        previous = current
        time.sleep(0.1)    

except KeyboardInterrupt:
    pass

GPIO.cleanup()
