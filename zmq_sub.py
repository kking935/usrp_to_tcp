#!/usr/bin/env python

import zmq
import struct

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.REQ)

print "Collecting updates..."
socket.connect ("tcp://localhost:9005")

while True:
    socket.send("request")
    try:
        x=struct.unpack('f', socket.recv()[0:4])
        print(x[0])
    except:
	pass
