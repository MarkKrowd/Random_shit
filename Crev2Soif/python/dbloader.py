# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:24:32 2020

@author: RMichaud
"""


import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import pickle

def Read_database():
    with open('objs.pkl', "rb") as f:  # Python 3: open(..., 'rb')
        data = pickle.load(f)
    return data

def Save_database(data):
    with open("save.txt", "w") as fp:
        fp.write(str(data))
        fp.close()
    with open('objs.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump(data,f)
        
def Save_new(data,user):
    with open(user + "_save.txt", "w") as fp:
        fp.write(str(data))
        fp.close()
    
        
def check_user(user):
    with open("admins.txt","r") as fp:
        username = fp.readline().strip()
    fp.close()
    return user == username

hostName = "localhost"
hostPort = 8000



class MyServer(BaseHTTPRequestHandler):
	# Ceci est un dictionnaire Python, c'est pas encore du JSON
    data = Read_database()

	# Contient les headers standards pour répondre du JSON
    def _set_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

	# Nécessaire pour le POST.
    def do_OPTIONS(self):
        self.send_response(200)
        self._set_headers()

	#	GET
    def do_GET(self):
        self.data = Read_database()
        self.send_response(200)
        self._set_headers()
		# json.dumps converti le dictionnaire python en JSON
        self.wfile.write(bytes(json.dumps(self.data), "utf-8"))

	#	POST is for submitting data.
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        
        

        print("Le serveur a reçu un POST!", self.path, post_data)
        
		
        new_characters = json.loads(post_data.decode('utf8'))
        print(new_characters["properties"])
        user = new_characters["properties"]["usernaaaame"]
        
        if check_user(user):
            new_characters["properties"]["user"] = "admin"
            self.data["features"].append(new_characters)
            Save_database(self.data)
            self.send_response(201)
            self._set_headers()
            self.wfile.write(bytes(json.dumps(self.data), "utf-8"))
        else:
            Save_new(new_characters,user)
            self.send_response(301)
            self._set_headers()
            self.wfile.write(bytes(json.dumps(self.data), "utf-8"))
        


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))