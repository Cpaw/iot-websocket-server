#!/usr/bin/env python3
from websocket import create_connection
from IPython import embed
from IPython.terminal.embed import InteractiveShellEmbed
import sys

if len(sys.argv) < 2:
    print(sys.argv[0] + " <Address>:<Port>")
    sys.exit()

ws = create_connection("ws://%s" % sys.argv[1])
str = ' '
while str != '':
    str = input()
    print("# Sending...")
    ws.send(str)

    print("# Receiving...")
    result =  ws.recv()
    print(result)
    # embed()

ws.close()
