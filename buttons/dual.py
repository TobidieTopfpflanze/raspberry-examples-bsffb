import RPi.GPIO as GPIO
 
button1 = 37
button2 = 38
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
 

print("B1: " + str(GPIO.input(button1)))
print("B2: " + str(GPIO.input(button2)))

while True:
    if GPIO.input(button1) == 1:
        print("Hallo von button 1")
        break; 

    if GPIO.input(button2) == 1:
        print("Hallo von button 2")
        break; 
