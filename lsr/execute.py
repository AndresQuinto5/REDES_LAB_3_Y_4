'''
Laboratorio 3 - Algoritmos de enrutamiento

Mirka Monzon 18139
Oscar De Leon 19298
Andres Quinto 19288
'''
import json

hello = 'HELLO'
echo_send = "ECHO SEND"
echo_response = "ECHO RESPONSE"
message_type= "MESSAGE"
lsp = 'LSP'

"""
Recibe una cadena similar a json y la convierte en un objeto 
Argumentos: json_string -- json-like string
"""
def json_to_object(jason_string):
    object = json.loads(jason_string)
    return object



"""
Recibe un objeto y lo convierte en una cadena similar a json
Argumentos: object -- an object
"""
def object_to_json(object):
    json_string = json.dumps(object)
    return json_string



"""
Recibe el ID en la topología y devuelve el JID en el servidor
Argumentos: names_file -- the filename of the file with the name-node associations / ID -- The ID in the topology
"""
def get_JID(names_file,ID):
	file = open(names_file, "r")
	file = file.read()
	info = eval(file)
	if(info["type"]=="names"):
		names = info["config"]
		JID = names[ID]
		return(JID)
	else:
		raise Exception('El archivo no tiene un formato válido para los nombres')



"""
Recibe el JID del servidor y devuelve el ID en la topología
Argumentos: name -- the filename of the file with the name-node associations / JID -- The JID in the server
"""
def get_ID(names_file, JID):
	file = open(names_file, "r")
	file = file.read()
	info = eval(file)
	if(info["type"]=="names"):
		names = info["config"]
		JIDS = {v: k for k, v in names.items()}
		name = JIDS[JID]
		return(name)
	else:
		raise Exception('El archivo no tiene un formato válido para los nombres')



"""
Devuelve una lista de los vecinos de un nodo dado
Argumentos: topolo -- the filename of the file with the node-node / JID -- JID -- The JID in the server
"""
def get_neighbors(topology_file, ID):
	file = open(topology_file, "r")
	file = file.read()
	info = eval(file)
	if(info["type"]=="topo"):
		names = info["config"]
		neighbors_IDs = names[ID]
		return(neighbors_IDs)
	else:
		raise Exception('El archivo no tiene un formato válido para la topologia')