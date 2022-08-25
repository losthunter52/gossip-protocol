import socket, threading

#---------------------------------------------------------------------------
# Active Module Class
#---------------------------------------------------------------------------

class ActiveSender (threading.Thread):
    # init method
    def __init__(self, object, DESTINY_HOST):
        # initializes the communication sender module
        threading.Thread.__init__(self)
        self.object = object
        self.DESTINY_HOST = DESTINY_HOST
        self.DESTINY_PORT = 61666

    # send method
    def send(self):
        # sends stored information to a pre-defined destination
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((self.DESTINY_HOST, self.DESTINY_PORT))
            sock.sendall(bytes(self.object,encoding="utf-8"))
        finally:
            sock.close()
        
    # run method
    def run(self):
        # start the ActiveSender thread
        self.send()