import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
lightSensorPin = 15
motorPin = 18
motorPin2 = 16
GPIO.setup(motorPin, GPIO.OUT)
GPIO.output(motorPin, GPIO.LOW)
GPIO.setup(motorPin2, GPIO.OUT)
GPIO.output(motorPin2, GPIO.LOW)

while True:
    GPIO.setup(lightSensorPin, GPIO.OUT)
    GPIO.output(lightSensorPin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(lightSensorPin, GPIO.IN)
    
    curTime = time.time()
    timeDiff = 0
    
    while (GPIO.input(lightSensorPin) == GPIO.LOW):
        timeDiff = time.time() - curTime

    #print(timeDiff)
    
    if (timeDiff < 0.12):
        #print("in sunlight")
        GPIO.output(motorPin, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(motorPin, GPIO.LOW)
        break
    
    time.sleep(1)