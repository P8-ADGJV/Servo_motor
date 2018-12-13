import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
#GPIO.setwarnings(False)

pwm=GPIO.PWM(17,50)
pwm.start(5)

while True:
	angle = input("Entrez l'angle souhaite (Entre 0 et 100 %):\n")
	pwm.ChangeDutyCycle(angle)
	time.sleep(1)

except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()