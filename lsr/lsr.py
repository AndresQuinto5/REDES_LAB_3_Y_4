'''
Laboratorio 3 - Algoritmos de enrutamiento

Mirka Monzon 18139
Oscar De Leon 19298
Andres Quinto 19288
'''
import slixmpp

class LSR(slixmpp.ClientXMPP):
    def __init__(self, jid, password,topolo,name):
        slixmpp.ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)
        
        self.topolo = topolo
        self.name = name
        self.network = []
        self.echo_sent = None
        self.LSP = {
            'type': lsp,
            'from': self.boundjid.bare,
            'sequence': 1,
            'neighbours':{}
        }
        self.id = get_ID(self.name, jid)
        self.neighbours_IDS = get_neighbors(self.topoLO, self.id)
        self.neighbours = []
        self.neighbours_JID()

