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
	file = open(names_file, "r")
	file = file.read()
	info = eval(file)
	if(info["type"]=="names"):
		names = info["config"]
		JID = names[ID]
		return(JID)
	else:
		raise Exception('ERROR; names.txt is not a valid file or has a wrong format')