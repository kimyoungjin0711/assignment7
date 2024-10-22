import RPi.GPIO as GPIO
import time

BUZZER = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

frequencies = [262, 294, 330, 349, 392, 440, 494, 523] 

p = GPIO.PWM(BUZZER, 262)
p.start(50)

try:
    while True:
        for freq in frequencies:
            p.ChangeFrequency(freq)
            time.sleep(1.0)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()