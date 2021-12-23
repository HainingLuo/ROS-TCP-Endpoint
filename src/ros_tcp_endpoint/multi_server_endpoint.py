#!/usr/bin/env python

import rospy

from ros_tcp_endpoint import TcpServer


def main():
    ros_node_name = "server_endpoint"
    rospy.init_node(ros_node_name, anonymous=True)

    # Set ROS IP
    tcp_ip = rospy.get_param("~tcp_ip", "") # get private params of the node
    tcp_server = TcpServer(ros_node_name, tcp_ip=tcp_ip) # ros_node_name is not used

    # Start the Server Endpoint
    tcp_server.start()
    rospy.spin()


if __name__ == "__main__":
    main()
