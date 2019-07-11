#!/usr/bin/env python

import sys
import zmq

f = open("power_zmq", "w")
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.REQ)

print "Collecting updates..."
socket.connect ("tcp://localhost:9005")

while True:
    socket.send("request")
    f.write(socket.recv())

f.close()
