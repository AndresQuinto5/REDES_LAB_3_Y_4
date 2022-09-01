import asyncio
from atexit import register
from http.client import METHOD_NOT_ALLOWED
from unittest.mock import call
import slixmpp
import networkx as nx
import ast
from datetime import datetime

class Client(slixmpp.ClientXMPP):
    def __init__(self, usuario, contrasenia, algoritmo, nodo, nodos, nombres, graph, graph_directorio, fuente):
        super().__init__(usuario, contrasenia)
        self.recibido = set()
        self.algoritmo = algoritmo
        self.nombres = nombres
        self.graph = graph
        
        # falta vector routing !!!!!!

        #self.dvr = #pendiente de routing vectorial

        self.nodo = nodo
        self.nodos = nodos
        self.schedule(name="echo", callback=self.echo_mensaje, seconds=5, repeat=True)
        self.schedule(name="update", callback=self.actualizar_mensaje, seconds=10, repeat=True)

        self.evento_conectado = asyncio.Event()
        self.presencia_recibida = asyncio.Event()

        self.add_event_handler('session_start', self.iniciar)
        self.add_event_handler('message', self.mensaje)

        self.register_plugin('xep_0045')
        self.register_plugin('xep_0199')
        self.register_plugin('xep_0030')
        


    async def iniciar(self, evento):
        self.send_presence()
        await self.get_roster()
        self.evento_conectado.set()

    async def mensaje(self, texto):
        if texto['type'] in ('nornmal','chat'):
            await self.contestar_mensaje(texto['body'])
        
    async def contestar_mensaje(self, texto):
        mensaje = texto.split('|')
        if mensaje[0] == '1':
            if self.algoritmo == '1':
                if mensaje[2] == self.usuario:
                    print("Mensaaje entrante --> " + mensaje[6])
                else:
                    nodoVecinoMasCercano = 0 #pendiente
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

                self.graph.agregarNodos(nodos)
                self.graph.agregarPeso(aristas)

                #pendiente update graph

                datosVecinos = self.graph.nodos().data()
                datosEdges = self.graph.edges.data('weight')
                

                #Pendiente parte vecinos



        elif mensaje[0] == '3':
            if mensaje[6] == '':
                ahora = datetime.now()
                tiempo = datetime.timestamp(ahora)
                mensaje = texto+str(tiempo)
                self.send_message

