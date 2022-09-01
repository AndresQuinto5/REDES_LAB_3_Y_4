'''
Laboratorio 3 - Algoritmos de enrutamiento

Mirka Monzon 18139
Oscar De Leon 19298
Andres Quinto 19288
'''

from getpass import getpass
from lsr import LSR

#Main
if __name__ == '__main__':
    print("\n--- Chatea :) ---\n")
    jid = input('Ingresa tu jid: ')
    password = getpass('Ingresa tu contraseña: ')
    name = input('Ingresa tu nombre(s): ')
    topolo = input('Ingresa tu topologia: ')

    xmpp = LSR(jid, password,topolo,name)
    xmpp.connect()
    xmpp.process(forever=False)