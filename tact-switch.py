import _webiopi.GPIO

GPIO = _webiopi.GPIO

DIGITAL_INPIN = 25

GPIO.setFunction(DIGITAL_INPIN, GPIO.IN)

while True:
    bButtonState = GPIO.digitalRead(DIGITAL_INPIN)
    if bButtonState:
        while bButtonState:
            bButtonState = GPIO.digitalRead(DIGITAL_INPIN)
        print("clicked")
