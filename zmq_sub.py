#!/usr/bin/env python

import zmq
import struct

import rospy
import durip.msg


# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.REQ)

print "Collecting updates..."
socket.connect ("tcp://localhost:9005")
print("Connected")


r = rospy.rate(100)
rssi_pub = rospy.publisher("rssi", durip.msg.rssiMsg)

while True:
        socket.send("request")
        try:
                x=struct.unpack('f', socket.recv()[0:4])[0]
                pubMsg = durip.msg.rssiMsg(timestamp=rospy.Time.now().secs, rssi=x)
                rssi_pub.publish(pubMsg)
        except:
                pass

        r.sleep()




