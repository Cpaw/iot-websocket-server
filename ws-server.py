from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class Server(WebSocket):

    def handleMessage(self):
        print(self.data)
        self.sendMessage('return: ' + self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('', 7000, Server)
server.serveforever()
