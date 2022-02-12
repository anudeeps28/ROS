# creating a publisher in ROS using python

# go inside the package that you want to work on,
# then make a new folder called scripts
# and inside these make a new file subscriber, publisher etc.

#!/user/bin/env
import queue
import rospy
impoort std_msgs.msg 
import String
from package_name import Position

# defining the function that we use in main
def talk_to_me(): 
    pub = rospy.Publisher('talking_topic', String , queue_size = 10) #  name of the topic which we are going to publish; talking_topic = name of the topic published, String is the type, queue size = no. which will be kept in line before deletingt
    # in place of string, write position if you are calling messages from position
    # initialize the node
    rospy.init_node('publisher_node', anonymous = True) # publisher_node = name of the node, True = if we create 2 nodes of same, they will have different names
    rate = rospy.Rate(1) #tells ros how long function will sleep before it wakes up again, value is in hertz (the freqency with which ros will send signals)
    while not rospy.is_shutdown():
        msg = "Hello Anudeep - %s" % rospy.get_time()
            # if you already have a message file, just use this
            # msg = Position()
            # msg.message = "My Position is:"
            # msg.x = 2.0
            # msg.y = 1.5
        pub.publish(msg) # publishing message
        rate.sleep() # sleep function called
        rospy.loginfo # logging the message 

# writing the main function
if __name__ == '__main__':
    try:
        talk_to_me()
    except rospy.ROSInterruptException:
        pass

# then go in CmakeLists and add a function catkin_install_python (PROGRAMA scripts/publisher_node.py
# DESTINATION $(CATKIN_PACKAGE_BIN_DESTINATION)
# ) and save this
# then do catkin_make 
# then do source devel bash/setup.bash
# run roscore
# then do rosrun name_of_package publisher_node.py
    # this will start the publishing node


# in a new terminal: rostopic list
    # to see the list of all the topics that are published until now
    # our newly created talking_topic will also be present there
# rostopic echo /talking_topic: you will get the message published every second