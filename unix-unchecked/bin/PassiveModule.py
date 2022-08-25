import ast, socket, threading
from bin.ActiveModule import ActiveSender
from threading import Thread

#---------------------------------------------------------------------------
# Passive Module Class
#---------------------------------------------------------------------------

class PassiveReceptor (threading.Thread):
    # init method
    def __init__(self, HOST, neighborhood, database):
        # initializes the communication receiver module
        threading.Thread.__init__(self)
        self.database = database
        self.HOST = HOST
        self.PORT = 61666
        self.neighborhood = neighborhood

    # connection method
    def connection(self, conn):
        # thread-isolated communicator (concurrent execution)
        while True:
            data = conn.recv(1024)
            if not data: break
            self.decoder(data)
        conn.close()

    # decoder method
    def decoder(self, data):
        # check received communication
        segment = data.decode("utf-8")
        data = ast.literal_eval(segment)
        if self.database.isNews(data) == 'Yes':
            self.database.addJson(data)
            self.dissiminate(segment)

    # dissiminate method
    def dissiminate(self, segment):
        # disseminate information to neighborhood
        for neighbor in self.neighborhood:
            send = ActiveSender(segment, neighbor)
            send.start()
            send.join()

    # run method
    def run(self):
        # start the PassiveReceiver master thread
        print("P. M. Actived")
        pm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        params = (self.HOST, self.PORT)
        pm_socket.bind(params)
        pm_socket.listen(1)
        while True:
            conn, attr = pm_socket.accept()
            connect = Thread(target=self.connection, args=(conn,))
            connect.start()
        pm_socket.close()