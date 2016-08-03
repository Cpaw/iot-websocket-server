#!/usr/bin/env python3
from websocket import create_connection
ws = create_connection("ws://localhost:7000")

while input() == '':
    print("# Sending...")
    ws.send("Hi")

    print("# Receiving...")
    result =  ws.recv()
    print(result)

ws.close()
