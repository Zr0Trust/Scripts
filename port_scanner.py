#!/bin/python3

#This script was created from using/learning from The Cyber Mentor's "Python for beginners - full course" which can be found on youtube. 

import sys
import socket
from datetime import datetime

#Define your target
if len(sys.argv) == 2: 
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else: 
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	
#Add Banner
print("-" * 50)
print("scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85): #Alter ports as needed
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Gather IPv4 address and port
		socket.setdefaulttimeout(1) #timeout on port after 1 second
		result = s.connect_ex((target,port)) #connect on target and port
		if result == 0: #if port is open it returns 0
			print(f"Port {port} is open")
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()	
	
except socket.error:
	print("Could not connect to the server")
	sys.exit()
