#!/usr/bin/env python

import rospy
import durip.msg



import zmq
import struct


class ZMQfeed:
        def __init__(self):
                # Socket to talk to server
                self.context = zmq.Context()
                self.socket = self.context.socket(zmq.REQ)

                self.socket.connect ("tcp://localhost:9005")

                self.rssiVal = 0


        def run(self):
		try:
                        self.socket.send("request")
                        tcp_data=self.socket.recv()
                        self.rssiVal=struct.unpack('f', tcp_data[0:4])[0]
		except struct.error:
			pass

        def get_data(self):
                return self.rssiVal

        def __del__(self):
                self.socket.close()
                self.context.term()








rospy.init_node('uhdRX')

rssi_pub = rospy.Publisher("rssi", durip.msg.rssiMsg, queue_size = 1)

zmq = ZMQfeed()



def rosPub(event):
	rssiVal = zmq.get_data() 
	pubMsg = durip.msg.rssiMsg(timestamp=rospy.Time.now().secs, rssi=rssiVal)
        rssi_pub.publish(pubMsg)




rospy.Timer(rospy.Duration(0.01), rosPub)


while True:
	zmq.run()
