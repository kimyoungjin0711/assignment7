import RPi.GPIO as GPIO
import time

BUZZER = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

frequencies = [392, 330, 330, 392, 330, 262]

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