# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:33:10 2019

@author: Utilisateur
Application Web

http:/192.168.10.15:8888/index.py
"""

import http.server


PORT = 8888
server_address = ("", PORT)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
print("Serveur actif sur le port :", PORT)

httpd = server(server_address, handler)
httpd.serve_forever()
