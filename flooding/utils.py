'''
Laboratorio 3 - Algoritmos de enrutamiento

Mirka Monzon 18139
Oscar De Leon 19298
Andres Quinto 19288
'''

#THIS FILE IS ONLY FOR UTILITIES LIKE MENU AND FUNCTIONS    

import json
import time

last_id = None

# Reads the id on the topology file and returns the JID on alumchat for the given ID

# uses the names.txt file to check the node - name association
# uses de id of the topology file 
def get_JID(names_file,ID):
	file = open(names_file, "r")   #IMPORTANT: this is the names file
	file = file.read()
	info = eval(file)
	if(info["type"]=="names"):
		names = info["config"]
		JID = names[ID]
		return(JID)
	else:
		raise Exception('ERROR; names.txt is not a valid file or has a wrong format')

# returns the id on topology.txt for the given JID

def get_ID(names_file, JID):
	file = open(names_file, "r")    #IMPORTANT: this is the names file
	file = file.read()
	info = eval(file)
	if(info["type"]=="names"):
		names = info["config"]
		JIDS = {v: k for k, v in names.items()}
		name = JIDS[JID]
		return(name)
	else:
		raise Exception('ERROR; names.txt is not a valid file or has a wrong format')

# returns a list of the adjacent nodes to the given node - neighbors

def get_neighbors(topology_file, names_file, JID):
	ID = get_ID(names_file, JID) #IMPORTANT: this is the id of the node FILE
	file = open(topology_file, "r") #IMPORTANT: this is the topology file
	file = file.read()
	info = eval(file)
	if(info["type"]=="topo"):
		names = info["config"]
		neighbors_IDs = names[ID]
		neighbors_JIDs = [get_JID(names_file,i) for i in neighbors_IDs]
		return(neighbors_JIDs)
	else:
		raise Exception('ERROR; the topolofy file has a wrong format')
	return  



#CALCULATE THE ROUTE BASED ON THE GIVEN PARAMETERS
# returns a calculated route for the given parameters
# uses : a message to send, the sender, the names file, the jason id

def calculate(message, sender, names_file, topology_file):
	start_time = time.time()
	info = eval(message)
	info["Jumps"] = info["Jumps"] + 1 #IMPORTANT: THIS IS THE NUMBER OF JUMPS
	nodes = get_neighbors(topology_file, names_file, sender)
	info["List_of_Nodes"] = [info["List_of_Nodes"], nodes] #IMPORTANT: this is a list of NODES ADJACENTs 
	info["Distance"] = info["Distance"] - start_time + time.time() #IMPORTANT: the time is in seconds, this is the distance
	return (nodes, json.dumps(info))