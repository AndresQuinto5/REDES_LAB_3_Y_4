'''
Laboratorio 3 - Algoritmos de enrutamiento

Mirka Monzon 18139
Oscar De Leon 19298
Andres Quinto 19288
'''
# https://es.wikipedia.org/wiki/Inundaci%C3%B3n_de_red
from getpass import getpass
from Client import *

#DEFINITION OF THE MAIN CLASS

if __name__ == '__main__':

    jid = input("Type your jid: ")
    password = getpass("Type your password: ")
    print("anything else from flooding means listening")
    routing = input("Routing type: ")
    
    listening = False
    if routing != "flooding":
        listening = True


    names_file = input("Please type the name of the names file: ")
    topology_file = input("Please type the name of the topology file: ")

    try:
        recipient = ''
        message = ''

        if(not listening):
            recipient = input("Write the reciever JID: ") 
            message = input("Write a message! : ")

        xmpp = Client(jid, password, recipient, message, routing, listening, names_file, topology_file)
        #U CAN CHECK THE PLUGINS HERE: https://xmpp.org/extensions/
        xmpp.register_plugin('xep_0030') # Service Discovery
        xmpp.register_plugin('xep_0199') # XMPP Ping
        xmpp.register_plugin('xep_0045') # Mulit-User Chat (MUC)
        xmpp.register_plugin('xep_0096') # Jabber Search
        xmpp.register_plugin('xep_0077') ### Band Registration
        xmpp.connect()
        xmpp.process(forever=False)
        
    except KeyboardInterrupt as e:
        print('\nThat was the flooding alg\n')