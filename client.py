#!/usr/bin/env python3
from websocket import create_connection
from IPython import embed
from IPython.terminal.embed import InteractiveShellEmbed

ws = create_connection("ws://172.16.42.34:7000")
str = ' '
while str != '':
    str = input()
    print("# Sending...")
    ws.send(str)

    print("# Receiving...")
    result =  ws.recv()
    print(result)
    embed()

ws.close()
