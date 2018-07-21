#!/usr/bin/env python

'''

@Author:Balasubramanyam Evani
Manipal University Jaipur

Script publishes the Anchor-Tag Distances, Tested with Localino v2.0

'''

## Importing Required Libraries
import socket
from udp_localino_ros.msg import udp_msg
import rospy

UDP_IP= ""
UDP_PORT=10000 ## defining the UDP_PORT

def process(data,pub):
    localino_msg = udp_msg() 		## Creating a msg object
    res = data.split(",") 		## data read to be split with delimited space " " 
    id_num = int(res[0]) % 2000		## The anchor tags had id's like 2000, 2001, 2002 ...., hence taking mod 2000 for anchor id, can change it
    dist = float(res[2])		## secong argument represents the distance in 'm'

    localino_msg.header.stamp = rospy.Time.now()	## Creating a Header
    localino_msg.header.frame_id = "localino"
    localino_msg.Anchor_Number = id_num
    localino_msg.AT_dist = dist

    pub.publish(localino_msg)				## Publishing the msg


## Main Function

if __name__ == "__main__":

    rospy.init_node("Localino_Node")			## Node initialization
    pub = rospy.Publisher("localino_distances", udp_msg , queue_size = 1) 	## publisher initialization
    rospy.loginfo("Starting Localino node")		## log info stating the starting up of node
    sock = socket.socket(socket.AF_INET ,  socket.SOCK_DGRAM)	## socket connection
    sock.bind((UDP_IP,UDP_PORT))		
    while True:
        data, addr = sock.recvfrom(1024)		## receiving at baud rate 1024
        process(data,pub)				## process the data received
