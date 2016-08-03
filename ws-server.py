#!/usr/bin/env python3
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import sys
import webiopi
import json

menus = [
    {
        "name": "Orange",
        "price": 120,
        "value": 5,
    },
    {
        "name": "Cider",
        "price": 100,
        "value": 4,
    },
    {
        "name": "RedBull",
        "price": 200,
        "value": 15,
    },
]

webiopi.setDebug()

PIN_L1 = 6
PIN_L2 = 13
PIN_R1 = 19
PIN_R2 = 26

g_mode = 0
g_percentage = 50

GPIO = webiopi.GPIO
GPIO.setFunction(PIN_L1, GPIO.PWM)
GPIO.setFunction(PIN_L2, GPIO.PWM)
GPIO.setFunction(PIN_R1, GPIO.PWM)
GPIO.setFunction(PIN_R2, GPIO.PWM)

def MotorDrive(iIn1Pin, iIn2Pin, percentage):
    if 100 < percentage:
        percentage = 100
    if -100 > percentage:
        percentage = -100
    if 10 > percentage and -10 < percentage:
        GPIO.pwmWrite(iIn1Pin, 0.0)
        GPIO.pwmWrite(iIn2Pin, 0.0)
    elif 0 < percentage:
        GPIO.pwmWrite(iIn1Pin, percentage * 0.01)
        GPIO.pwmWrite(iIn2Pin, 0.0)
    else:
        GPIO.pwmWrite(iIn1Pin, 0.0)
        GPIO.pwmWrite(iIn2Pin, -percentage * 0.01)

@webiopi.macro
def ChangeDriveMode(mode):
    if mode == "0":
        webiopi.debug("ChangeDriveMode : Stop")
        MotorDrive(PIN_L1, PIN_L2, 0);
        MotorDrive(PIN_R1, PIN_R2, 0);
    elif mode == "1":
        webiopi.debug("ChangeDriveMode : Forward")
        MotorDrive(PIN_L1, PIN_L2, g_percentage);
        MotorDrive(PIN_R1, PIN_R2, g_percentage);
    elif mode == "2":
        webiopi.debug("ChangeDriveMode : Backward")
        MotorDrive(PIN_L1, PIN_L2, -g_percentage);
        MotorDrive(PIN_R1, PIN_R2, -g_percentage);
    elif mode == "3":
        webiopi.debug("ChangeDriveMode : CW")
        MotorDrive(PIN_L1, PIN_L2, g_percentage);
        MotorDrive(PIN_R1, PIN_R2, -g_percentage);
    elif mode == "4":
        webiopi.debug("ChangeDriveMode : CCW")
        MotorDrive(PIN_L1, PIN_L2, -g_percentage);
        MotorDrive(PIN_R1, PIN_R2, g_percentage);
    global g_mode
    g_mode = mode

@webiopi.macro
def ChangeVoltageLevel(level):
    webiopi.debug("ChangeVoltageLevel : %s" % (level))
    global g_percentage
    g_percentage = 10 * int(level)
    ChangeDriveMode(g_mode)

class Server(WebSocket):
    def handleMessage(self):
        print(self.data)
        str = self.data.strip()
        if str == 'stop':
            ChangeDriveMode('0')
        elif str == 'forward':
            ChangeDriveMode('1')
        elif str == 'back':
            ChangeDriveMode('2')
        elif str == 'right':
            ChangeDriveMode('3')
        elif str == 'left':
            ChangeDriveMode('4')
        elif str == 'list':
            self.sendMessage(json.dumps(menus))
            return
        else:
            self.sendMessage('Command not found: ' + str)
            return
        self.sendMessage('Return: ' + self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

ChangeDriveMode("0")
ChangeVoltageLevel("5")

if 2 <= len(sys.argv):
    port = int(sys.argv[1])
else:
    port = 7000

print(port)
server = SimpleWebSocketServer('', port, Server)
server.serveforever()
