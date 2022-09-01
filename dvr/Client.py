<<<<<<< Updated upstream
'''
Laboratorio 3 - Algoritmos de enrutamiento

Mirka Monzon 18139
Oscar De Leon 19298
Andres Quinto 19288
'''

=======
from email import message_from_binary_file
from dvRouting import DVR as DVR
>>>>>>> Stashed changes
import asyncio
from atexit import register
from http.client import METHOD_NOT_ALLOWED
from unittest.mock import call
import slixmpp
import networkx as nx
import ast
from datetime import datetime


# Inicializacion de clase Cliente
class Client(slixmpp.ClientXMPP):
    def __init__(self, jid, contrasenia, algoritmo, nodo, nodos, nombres, graph, graph_directorio, origen):
        super().__init__(jid, contrasenia)
        self.recibido = set()
        self.algoritmo = algoritmo
        self.nombres = nombres
        self.graph = graph
        
        self.dvr = DVR(graph, graph_directorio, origen)

        self.nodo = nodo
        self.nodos = nodos
        self.schedule(name="echo", callback=self.echoMensaje, seconds=5, repeat=True)
        self.schedule(name="update", callback=self.actualizarMensaje, seconds=10, repeat=True)

        self.evento_conectado = asyncio.Event()
        self.presencia_recibida = asyncio.Event()

        self.add_event_handler('session_start', self.iniciar)
        self.add_event_handler('message', self.mensaje)

        self.register_plugin('xep_0045')
        self.register_plugin('xep_0199')
        self.register_plugin('xep_0030')
        

    # Inicializacion 
    async def iniciar(self, evento):
        self.send_presence()
        await self.get_roster()
        self.evento_conectado.set()


    # Mensaje 
    async def mensaje(self, texto):
        if texto['type'] in ('nornmal','chat'):
            await self.contestar_mensaje(texto['body'])
        

    # Se realiza el proceso de contestar mensaje
    async def contestarMensaje(self, texto):
        mensaje = texto.split('|')
        if mensaje[0] == '1':
            if self.algoritmo == '1':
                if mensaje[2] == self.jid:
                    print("Mensaaje entrante --> " + mensaje[6])
                else:
                    nodoVecinoMasCercano = self.dvr.caminoCorto(mensaje[2])
                    if nodoVecinoMasCercano:
                        if nodoVecinoMasCercano[1] in self.dvr.vecinos:
                            strMensaje = "!".join(mensaje)
                            self.send_message(mto=mensaje[2],mbody=strMensaje,mtype='chat')
                        else:
                            pass
                    else:
                        pass

        elif mensaje[0] == '2':
            if self.algoritmo == '1':
                esquemaRecibido = mensaje[6]
                dividido = esquemaRecibido.split('-')
                aristas = ast.literal_eval(dividido[1])
                nodos = ast.literal_eval(dividido[0])

                self.graph.add_nodes_from(nodos)
                self.graph.add_weighted_edges_from(aristas)

                self.dvr.actualizacion(nx.to_dict_of_dicts(self.graph))

                datosVecinos = self.graph.nodos().data()
                datosEdges = self.graph.edges.data('weight')

                strNodos = str(datosVecinos) + "-" + str(datosEdges)

                for i in self.dvr.vecinos:
                    cambioMensaje = "2|" + str(self.jid) + "|" + str(self.nombres[i]) + "|" + str(self.graph.number_of_nodes()) + "||" + str(self.nodo) + strNodos
                    self.send_message(mto=self.dvr.nombres['config'][i], mbody=cambioMensaje, mtype='chat')

        elif mensaje[0] == '3':
            if mensaje[6] == '':
                ahora = datetime.now()
                tiempo = datetime.timestamp(ahora)
                mensaje = texto+str(tiempo)
                self.send_message(mto=mensaje[1], mbody=mensaje, mtype='chat')
            
            else:
                diferencia = float(mensaje[6]) - float(mensaje[4])
                self.graph[self.nodo][mensaje[5]]['weight'] = diferencia

        else:
            pass

    # Echo mensaje
    def echoMensaje(self):
        for i in self.nodos:
            ahora = datetime.now()
            tiempo = datetime.timestamp(ahora)
            mensaje = "3|" + str(self.jid) + "|" + str(self.nombres[i]) + "||"+ str(tiempo) +"|" + str(i) + "|"
            self.send_message(mto=self.nombres[i], mbody=mensaje, mtype='chat')

    # Se realiza actualizacion del mensaje
    def actualizarMensaje(self):
        if self.algoritmo == "1":
            datosVecinos = self.graph.nodes().data()
            datosEdges = self.graph.edges.data('weight')
            strNodos = str(datosVecinos) + "-" + str(datosEdges)
            for i in self.dvr.vecinos:
                nuevoMensaje = "2|" + str(self.jid) + "|" + str(self.nombres[i]) + "|" + str(self.graph.number_of_nodes()) + "||" + str(self.nodo) + "|" + strNodos
                self.send_message(mto=self.dvr.nombres[i], mbody=nuevoMensaje, mtype='chat')

