import os, threading, time, json
from .ActiveModule import ActiveSender
from .Data import Database
from .PassiveModule import PassiveReceptor

#---------------------------------------------------------------------------
# Control Painel Class
#---------------------------------------------------------------------------

class ControlPainel(threading.Thread):
    # init method
    def __init__(self, HOST, neighborhood):
        # initializes the control painel module
        threading.Thread.__init__(self)
        self.HOST = HOST
        self.neighborhood = neighborhood
        self.database = Database()

    # menu method
    def menu(self):
        # control the program
        running = True
        while running == True:
            os.system('clear')
            print("------------------------------------------------------")
            print('        Simplified P2P Model - Gossip Protocol        ')
            print("------------------------------------------------------")
            print('1 - Send Message')
            print('2 - Seed Database')
            print('3 - List Database')
            print('0 - Exit')
            print("------------------------------------------------------")
            option = input('Type a option: ')

            if option == '1':
                self.send()

            if option == '2':
                self.seed()

            if option == '3':
                self.print()

            if option == '0':
                os.system('clear')
                running = False
                print("Bye Bye - By losthunter52")

    # seed method
    def seed(self):
        # send all database to net
        os.system('clear')
        print('loading...')
        database = self.database.getJson()
        for dictionary in database:
            object = json.dumps(dictionary)
            for neighbor in self.neighborhood:
                send = ActiveSender(object, neighbor)
                send.start()
                send.join()

    # send method
    def send(self):
        # send data to net
        os.system('clear')
        message = input('Type a message: ')
        os.system('clear')
        print('loading..')
        dictionary = {"HOST" : self.HOST, 
                      "MESSAGE" : message, 
                      "TIME" : time.ctime()} 
        object = json.dumps(dictionary)
        for neighbor in self.neighborhood:
            send = ActiveSender(object, neighbor)
            send.start()
            send.join()

    # print method
    def print(self):
        # print local database
        os.system('clear')
        print("------------------------------------------------------")
        print("                       DATABASE                       ")
        print("------------------------------------------------------")
        self.database.printData()
        print("------------------------------------------------------")
        input("              Press ENTER to continue...              ")

    # run method
    def run(self):
        # start the menu thread
        pm = PassiveReceptor(self.HOST, self.neighborhood, self.database)
        pm.start()
        self.menu()
