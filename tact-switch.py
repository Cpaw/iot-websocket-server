import webiopi
import time

GPIO = webiopi.GPIO

LEDPIN = 24
DIGITAL_INPIN = 25
DEBOUNCE_DELAY = 0.5

g_bButtonState_prev = False
g_bLedState = False
g_dSec_prev = time.time()

GPIO.setFunction(LEDPIN, GPIO.OUT)
GPIO.setFunction(DIGITAL_INPIN, GPIO.IN)
GPIO.digitalWrite(LEDPIN, g_bLedState)

while True:
    bButtonState = GPIO.digitalRead(DIGITAL_INPIN)
    if False == g_bButtonState_prev and True == bButtonState:
        dSec = time.time()
        if DEBOUNCE_DELAY < dSec - g_dSec_prev:
            g_bLedState = not g_bLedState
            GPIO.digitalWrite(LEDPIN, g_bLedState)
        g_dSec_prev = dSec
    g_bButtonState_prev = bButtonState
