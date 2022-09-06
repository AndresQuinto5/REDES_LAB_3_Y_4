'''
Laboratorio 3 - Algoritmos de enrutamiento

Mirka Monzon 18139
Oscar De Leon 19298
Andres Quinto 19288
'''

from getpass import getpass
from .lsr import *
from .lsr import LSRClient

#main
def main3():
    print("\n--- Welcome to the Chat! ---\n")
    jid = input('Type your jid: ')
    password = getpass('Type your password: ')
    name_file = input('Type your names file: ')
    topo_file = input('Type your topology file: ')

    xmpp = LSRClient(jid, password,topo_file,name_file)
    xmpp.connect()
    xmpp.process(forever=False)
