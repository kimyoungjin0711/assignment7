import RPi.GPIO as GPIO
import time

SW1 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)



try:
    a = 0
    while True:

        if GPIO.input(SW1) == 1:
            a = a+1
            
            print("click %d"%a)
            
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
