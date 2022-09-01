'''
Laboratorio 3 - Algoritmos de enrutamiento

Mirka Monzon 18139
Oscar De Leon 19298
Andres Quinto 19288
'''

from Client import Client
from aioconsole import ainput
import networkx as nx
import yaml 
from optparse import OptionParser
import getpass


# Se carga la configuracion de topologia y nombres
def cargarConfiguracion():

    lectorTopologia = open("topology.txt", "r", encoding="utf8")
    lectorNombres = open("names.txt", "r", encoding="utf8")

    stringTopologia = lectorTopologia.read()
    stringNombres = lectorNombres.read()

    yamlTopologia = yaml.load(stringTopologia, Loader=yaml.FullLoader)
    yamlNombres = yaml.load(stringNombres, Loader=yaml.FullLoader)
    return yamlTopologia, yamlNombres


# Se obtienen los nodos 
def obtenerNodos(topologia, nombres, usuario):
    for key, value in nombres["config"].items():
        if usuario == value:
            return key, topologia["config"][key]


# Se realiza el grafico 
def obtenerGrafico(topologia, nombres, usuario):
    graph = {}
    origen = None

    for key, value in topologia['config'].items():
        graph.key = {}
        for nodo in value:
            graph[key][nodo] = float('inf')
            if nombres['config'][nodo] == usuario:
                origen = nodo
    
    return graph, origen

# Se realiza la prueba del grafico
def pruebaGrafo(topologia, nombres):
    G = nx.DiGraph()
    G.add_nodes_from(G.nodes(data=True))
    G.add_edges_from(G.edges(data=True))
    for key, value in nombres["config"].items():
        G.add_node(key, jid=value)
        
    for key, value in topologia["config"].items():
        for i in value:
            G.add_edge(key, i, weight=1)
    
    return G


# Main
async def main(xmpp: Client):
    run = True
    while run:
        print("""
        Bienvenido!

        0. Mensaje
        1. Salir
        
        """)
        opcion = await ainput("Ingrese una opcion: ")
        if opcion == '0':
            destinatario = await ainput("Ingrese el usuario receptor:  ")
            activo = True
            while activo:
                mensaje = await ainput("Ingrese su mensaje o atras para regresar:  ")
                if (mensaje != 'atras') and len(mensaje) > 0:
                    if xmpp.algoritmo == '1':
                        mensaje = "1|" + str(xmpp.jid) + "|" + str(destinatario) + "|" + str(xmpp.graph.number_of_nodes()) + "||" + str(xmpp.nodo) + "|" + str(mensaje)
                        shortest_neighbor_node = xmpp.dvr.caminoCorto(destinatario)
                        if shortest_neighbor_node:
                            if shortest_neighbor_node[1] in xmpp.dvr.obtenerVecinos:

                                xmpp.send_message(
                                    mto=xmpp.nombres[shortest_neighbor_node[1]],
                                    mbody=mensaje,
                                    mtype='chat' 
                                )
                            else:
                                pass
                        else:
                            pass
                    else:
                        xmpp.send_message(
                            mto=destinatario,
                            mbody=mensaje,
                            mtype='chat' 
                        )
                elif mensaje == 'atras':
                    activo = False
                else:
                    pass
        elif opcion == '1':
            run = False
            xmpp.disconnect()
        else:
            pass


if __name__ == "__main__":

    optp = OptionParser()
    optp.add_option("-j", "--jid", dest="jid",
                    help="JID a utilizar")
    optp.add_option("-p", "--password", dest="password",
                    help="contrasenia a utilizar")
    optp.add_option("-a", "--algoritmo", dest="algoritmo",
                    help="algoritmo a utilizar")
    
    opts, args = optp.parse_args()

    topo, names = cargarConfiguracion()
    if opts.jid is None:
        opts.jid = input("Escriba su JID: ")
    if opts.password is None:
        opts.password = getpass.getpass("Escriba su contrasenia: ")
    if opts.algoritmo is None:
        print("""Algoritmos disponibles:
        
        1. Distance Vector Routing
        
        """)
        opts.algoritmo = input("Escriba el numero de algoritmo a utilizar: ")

    graph_dict, source = obtenerGrafico(topo, names, user=opts.jid)

    nodo, nodes = obtenerNodos(topo, names, opts.jid)

    graph = pruebaGrafo(topo, names)

    xmpp = Client(opts.jid, opts.password, opts.algoritmo, nodo, nodes, names["config"], graph, graph_dict, source)
    xmpp.connect() 
    xmpp.loop.run_until_complete(xmpp.connected_event.wait())
    xmpp.loop.create_task(main(xmpp))
    xmpp.process(forever=False)

