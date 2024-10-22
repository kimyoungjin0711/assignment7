import RPi.GPIO as GPIO
import time

SW1 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

previous = 0 
current = 0

try:
    a = 0
    while True:
        current = GPIO.input(SW1)
        if previous == GPIO.LOW and current == GPIO.HIGH:
            a = a+1
            
            print("click %d"%a)
            
        previous = current
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
