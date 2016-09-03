import _webiopi.GPIO
GPIO = _webiopi.GPIO

# GPIO, status, current-status
data = [[num, 0, False] for num in [17, 27, 22]]

for n in data:
    print(n[0], n[1], n[2])
    GPIO.setFunction(n[0], GPIO.IN)

while True:
    for n in data:
        n[2] = GPIO.digitalRead(n[0])
        if n[1] == 0 and n[2] == True:
            n[1] = 1
        elif n[1] == 1 and n[2] == False:
            n[1] = 2
        elif n[1] == 2:
            n[1] = 0
            print("%d clicked" % n[0])
