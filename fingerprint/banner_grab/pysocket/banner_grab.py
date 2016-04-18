#!/usr/bin/python

import sys
import socket
import select

if len(sys.argv) != 4:
	print 'Usage: ', sys.argv[0], ' [Target-IP] [First Port] [Last Port]'
	print 'Example: ', sys.argv[0], ' 10.0.0.5 1 100'
	print 'Example will grab banners for TCP ports 1 through 100 on 10.0.0.5'
	sys.exit()

ip = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

for port in range(start, end):
	try:
		bangrab = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		bangrab.connect((ip, port))
		ready = select.select([bangrab], [], [], 1)
		
		if ready[0]:
			print 'TCP port ', str(port), ' - ', bangrab.recv(4096).strip('\n')
			bangrab.close()
		
	except:
		pass