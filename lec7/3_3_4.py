import RPi.GPIO as GPIO
import time

BUZZER = 12
SW1 = 5
SW2 = 6
SW3 = 13
SW4 = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


p = GPIO.PWM(BUZZER, 262)
previous1 = 0
previous2 = 0
previous3 = 0
previous4 = 0
current1 = 0
current2 = 0
current3 = 0
current4 = 0

try:
    while True:
        current = GPIO.input(SW1)
        if previous1 == GPIO.LOW and current == GPIO.HIGH:
           p.start(50)
           p.ChangeFrequency(262)
           previous1 = current1
           time.sleep(0.5)  
           p.stop()  
    
        current = GPIO.input(SW2)
        if previous2 == GPIO.LOW and current == GPIO.HIGH:
            p.start(50)
            p.ChangeFrequency(330)
            previous2 = current2
            time.sleep(0.5)    
            p.stop()  

        current = GPIO.input(SW3)
        if previous3 == GPIO.LOW and current == GPIO.HIGH:
            p.start(50)
            p.ChangeFrequency(292)
            previous3 = current3
            time.sleep(0.5)    
            p.stop()  

        current = GPIO.input(SW4)
        if previous4 == GPIO.LOW and current == GPIO.HIGH:
            p.start(50)
            p.ChangeFrequency(523)
            previous4 = current4
            time.sleep(0.5)    
            p.stop()  


except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()