cmake_minimum_required(VERSION 2.8.3)
project(udp_localino_ros)

find_package(catkin REQUIRED COMPONENTS

 roscpp
 rospy
 std_msgs
 message_generation

)
 add_message_files(
   FILES
   udp_msg.msg
)
generate_messages(
   DEPENDENCIES
   std_msgs 
 )


catkin_package(

CATKIN_DEPENDS message_runtime

)

