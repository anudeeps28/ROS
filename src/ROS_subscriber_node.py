# subscribing to a topic

# #!/user/bin/env
import queue
import rospy
impoort std_msgs.msg 
import String
from package_name import Position

def callback(data):
    rospy.loginfo("RECEIVED DATA %s", data.data)
    # if taking message from another file
        # rospy.loginfo("%s x, %f y", data.message, data.x, data.y)

# defining the function that we use in main
def listener(): 
    rospy.init_node('subscriber_node', anonymous = True)
    rospy.Subscriber('talking_topic', String, callback) # arguments = topic name, type of message, callback function (function that we will be calling whenever we recieve message on this)
        # here also in place of string, change to position if you are taking message from another file message
    rospy.spin() # it will let us to run the node until we continously shut it down
    


# writing the main function
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

# then go in CmakeLists and add a function catkin_install_python (PROGRAMA scripts/subscriber_node.py
# DESTINATION $(CATKIN_PACKAGE_BIN_DESTINATION)
# ) and save this
# then do catkin_make 
# then do source devel bash/setup.bash

# then go to a new terminal, do catkin_make and source devel/setup.bash
# run publisher = rosrun name_of_package publisher_node.py

# run roscore in the first terminal (the subscriber one)
# then do rosrun name_of_package subscriber_node.py
    # this will start the subscribing node
    # this will print new messages


# in a new terminal: rostopic list
    # to see the list of all the topics that are published until now
    # our newly created talking_topic will also be present there
# rostopic echo /talking_topic: you will get the message published every second