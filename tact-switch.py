import _webiopi.GPIO

GPIO = _webiopi.GPIO

DIGITAL_INPIN = 25

g_bButtonState_prev = False
g_bLedState = False

GPIO.setFunction(DIGITAL_INPIN, GPIO.IN)

while True:
    bButtonState = GPIO.digitalRead(DIGITAL_INPIN)
    if False == g_bButtonState_prev and True == bButtonState:
        g_bLedState = not g_bLedState
        print(g_bLedState)
    g_bButtonState_prev = bButtonState
