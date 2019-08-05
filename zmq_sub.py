#!/usr/bin/env python

import zmq
import struct

import rospy
import durip.msg


# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect ("tcp://localhost:9005")
rospy.loginfo("Connected")

rospy.init_node('uhdRX', disable_signals=True) #enable signals before integrating with main ROS code

rssi_pub = rospy.Publisher("rssi", durip.msg.rssiMsg, queue_size = 1)

rssiVal = 0


def rosPub(event):
	pubMsg = durip.msg.rssiMsg(timestamp=rospy.Time.now().secs, rssi=rssiVal)
        rssi_pub.publish(pubMsg)


rospy.Timer(rospy.Duration(0.01), rosPub)

while True:
	try:
       		socket.send("request")
		tcp_data=socket.recv()
		rssiVal=struct.unpack('f', tcp_data[0:4])[0]
	except KeyboardInterrupt:
		break
	except:
		pass
socket.close()
context.term()

