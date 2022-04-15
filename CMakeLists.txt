# CMakeLists.txt
#...
find_package(catkin REQUIRED COMPONENTS
rospy
std_msgs
message_generation
)
#...
add_message_files(
FILES
CustomMessage.msg
)
#...
catkin_package(
# INCLUDE_DIRS include
# LIBRARIES lab_1_pkg
CATKIN_DEPENDS rospy std_msgs message_runtime
# DEPENDS system_lib
)
#...
generate_messages(
DEPENDENCIES
std_msgs
)