import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
#GPIO.setwarnings(False)

while True:
    angle = input("Entrez l'angle souhaite (Entre 0 et 100 %):\n")

    pwm=GPIO.PWM(17,50)
    pwm.start(5)

    pwm.ChangeDutyCycle(angle)
    time.sleep(1)
    GPIO.cleanup()
