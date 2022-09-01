'''
Laboratorio 3 - Algoritmos de enrutamiento

Mirka Monzon 18139
Oscar De Leon 19298
Andres Quinto 19288
'''

from cgitb import reset
import genericpath
from select import select
import networkx as nx

class DVR():
    def __init__(self, graph, graph_directorio, origen, nombres):

        self.graph = graph
        self.graph_directorio = graph_directorio
        self.fuente = origen
        self.distancia, self.predecesor = self.bellmanFord(graph_directorio, origen)
        self.nombres = nombres
        self.vecinos = self.obtenerVecinos(graph_directorio, origen)


    def inicializacion(self, graph_directorio, origen):

        a = {}
        b = {}

        for i in graph_directorio:
            a[i] = float('Inf')
            b[i] = None

        a[origen] = 0
        return a, b


    def relajacion(self, nodo, vecino, graph_directorio, a, b):

        if a[vecino] > a[nodo] + graph_directorio[nodo][vecino]:
            a[vecino] = a[nodo] + graph_directorio[nodo][vecino]
            b[vecino] = nodo
        

    def obtenerVecinos(self, graph_directorio, origen):

        return list(graph_directorio[origen].keys())


    def bellmanFord(self, graph_directorio, origen):

        a, b = self.inicializacion(graph_directorio, origen)
        for i in range(len(graph_directorio) - 1):
            for j in graph_directorio:
                for k in graph_directorio[j]:
                    self.relajacion(j, k, graph_directorio, a, b)


    def actualizacion(self, graph_directorio):

        nueva_grafica = {}

        for i in graph_directorio: #nodos
            nueva_grafica[i] = {}
            for j in graph_directorio[i]: #nodo vecino
                nueva_grafica[i][j] = graph_directorio[i][j]['weight']
        self.graph_directorio = nueva_grafica
        self.distancia, self.predecesor = self.bellmanFord(nueva_grafica, self.origen)
        self.vecinos = self.obtenerVecinos(nueva_grafica, self.fuente)
    

    def caminoCorto(self, objetivo):
        for i in self.nombres:
            if self.nombres[i] == objetivo:
                resultado = nx.bellman_ford_path(self.graph, self.origen, i)
                return resultado
        return None
