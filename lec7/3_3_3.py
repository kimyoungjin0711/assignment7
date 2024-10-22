import RPi.GPIO as GPIO
import time

BUZZER = 12
SW1 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(SW1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

frequencies = [392, 330, 330, 392, 330, 262]

p = GPIO.PWM(BUZZER, 262)


try:
    while True:
        if GPIO.input(SW1) == 1:
            p.start(50)
            for freq in frequencies:
                p.ChangeFrequency(freq)
                time.sleep(1.0)
        else :
            time.sleep(1.0)


except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()